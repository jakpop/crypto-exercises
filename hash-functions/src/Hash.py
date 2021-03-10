import hashlib as hl
from timeit import default_timer as timer


class Hash:

    def __init__(self):
        pass

    def hashing(self, text: str):
        hashes = {}
        for hash_algorithm in sorted(hl.algorithms_available):
            h = hl.new(hash_algorithm)
            h.update(text.encode())
            if hash_algorithm.startswith("shake"):
                continue
            start = timer()
            hash_str = h.hexdigest()
            end = timer()
            hashes[hash_algorithm] = [hash_str, end - start]

        return hashes

    def file_hashing(self, file_path):
        h = hl.sha256()

        with open(file_path, 'rb') as file:
            while True:
                chunk = file.read(h.block_size)
                if not chunk:
                    break
                h.update(chunk)

        return h.hexdigest()
