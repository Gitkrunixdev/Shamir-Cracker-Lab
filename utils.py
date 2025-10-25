def load_wordlist(path):
    with open(path, ""r"") as f:
        return [w.strip() for w in f.readlines()]
