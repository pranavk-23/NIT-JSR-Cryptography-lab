# yak_demo.py  -- educational/demo implementation of YAK (modular group)
# NOT for production use. Replace the small demo prime with a large RFC prime in real systems.

import hashlib
import secrets

# ---- Utility functions ----

def H(*args) -> int:
    """Hash-to-int (SHA256) of concatenated byte inputs."""
    h = hashlib.sha256()
    for a in args:
        if isinstance(a, int):
            # integer -> bytes big-endian
            a = a.to_bytes((a.bit_length() + 7) // 8 or 1, 'big')
        if isinstance(a, str):
            a = a.encode()
        h.update(a)
    return int.from_bytes(h.digest(), 'big')

def int_to_bytes(x: int) -> bytes:
    return x.to_bytes((x.bit_length() + 7) // 8 or 1, 'big')

# ---- Group parameters (demo) ----
# For demonstration we use a small safe-ish prime. Replace with a standard large prime for real use.
# Example production primes: RFC 3526 group 14 (2048-bit). See RFC 3526/5114.
p = 0xE95E4A5F737059DC60DF5991D45029409E60FC09  # small prime for demo only
g = 2

# order q (for demo we pick (p-1)/2 when p is safe prime); here approximate for correctness in demo
q = (p - 1) // 2

def mod_pow(base, exp):
    return pow(base, exp, p)

# ---- Schnorr non-interactive ZKP for knowledge of exponent x (Fiat-Shamir) ----
def schnorr_prove(g, p, q, x):
    """Return (X = g^x mod p, proof = (c, s)) proving knowledge of x."""
    X = mod_pow(g, x)
    r = secrets.randbelow(q)
    R = mod_pow(g, r)
    c = H(int_to_bytes(g), int_to_bytes(p), int_to_bytes(X), int_to_bytes(R)) % q
    s = (r + c * x) % q
    return X, (c, s)

def schnorr_verify(g, p, q, X, proof):
    c, s = proof
    # check: g^s ?= R * X^c  (where R = g^s / X^c mod p)
    left = mod_pow(g, s)
    right = (mod_pow(X, c) * 1) % p  # we'll compute R = g^s * (X^c)^{-1} if needed; but easier to compute R then c
    # recompute R = g^s * (X^c)^{-1}
    Xc = mod_pow(X, c)
    # compute inverse of Xc mod p
    try:
        inv_Xc = pow(Xc, -1, p)
    except ValueError:
        return False
    R = (left * inv_Xc) % p
    c2 = H(int_to_bytes(g), int_to_bytes(p), int_to_bytes(X), int_to_bytes(R)) % q
    return c2 == c

# ---- YAK participant class ----
class YAKParty:
    def __init__(self, name, static_priv):
        self.name = name
        self.a = static_priv  # long-term private exponent
        self.A = mod_pow(g, self.a)  # long-term public
        self.ephemeral_x = None
        self.X = None
        self.X_proof = None
        self.peer_pub = None
        self.peer_proof = None
        self.session_key = None

    def make_ephemeral(self):
        x = secrets.randbelow(q)
        self.ephemeral_x = x
        X, proof = schnorr_prove(g, p, q, x)
        self.X = X
        self.X_proof = proof
        return X, proof

    def receive_peer(self, peer_X, peer_proof, peer_static_pub):
        self.peer_pub = peer_static_pub
        self.peer_pub_point = peer_static_pub
        self.peer_X = peer_X
        self.peer_proof = peer_proof

    def verify_peer(self):
        return schnorr_verify(g, p, q, self.peer_X, self.peer_proof)

    def compute_session_key(self):
        if self.ephemeral_x is None:
            raise ValueError("Make ephemeral first")
        # K = (g^y * B)^(x + a)  where peer_X = g^y, peer_pub = B = g^b
        combined = (self.peer_X * self.peer_pub) % p  # g^y * B
        exp = (self.ephemeral_x + self.a) % q
        K = pow(combined, exp, p)
        # Derive session key bytes
        key = hashlib.sha256(int_to_bytes(K)).digest()
        self.session_key = key
        return key

# ---- Demo run (Alice <-> Bob) ----
def demo():
    # Long-term static keys (in real use these are persistent and must be large and protected)
    a = 0x1A2B3C4D5E  # Alice's static private (demo)
    b = 0x123456789A  # Bob's static private (demo)

    alice = YAKParty("Alice", a)
    bob = YAKParty("Bob", b)

    # Each creates ephemeral and sends (X, proof)
    X_a, proof_a = alice.make_ephemeral()
    X_b, proof_b = bob.make_ephemeral()

    # Exchange: Alice receives Bob's ephemeral+proof and static pub; Bob receives Alice's
    alice.receive_peer(X_b, proof_b, bob.A)
    bob.receive_peer(X_a, proof_a, alice.A)

    # Verify proofs
    ok_a = alice.verify_peer()
    ok_b = bob.verify_peer()
    print("Alice verifies Bob's proof:", ok_a)
    print("Bob verifies Alice's proof:", ok_b)
    if not (ok_a and ok_b):
        raise SystemExit("Proof verification failed")

    # Each computes session key
    k_alice = alice.compute_session_key()
    k_bob = bob.compute_session_key()
    print("Alice session key (hex):", k_alice.hex())
    print("Bob   session key (hex):", k_bob.hex())
    print("Keys equal:", k_alice == k_bob)

if __name__ == "__main__":
    demo()
