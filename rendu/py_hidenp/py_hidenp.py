def hidenp(small: str, big: str) -> bool:
    chars = iter(big)
    return all(char in chars for char in small)