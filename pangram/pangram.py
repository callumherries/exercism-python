def is_pangram(_string: str) -> bool:
    lower = _string.lower()
    chars = list(lower)
    alphabet = map(chr, range(ord('a'), ord('z') + 1))
    return all(map(lambda x: x in chars, alphabet))



