import hashlib
import random


def hash_generator():
    return hashlib.sha256(str(random.getrandbits(256)).encode("utf-8")).hexdigest()
