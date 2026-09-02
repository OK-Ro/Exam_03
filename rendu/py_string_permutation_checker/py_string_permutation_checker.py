def string_permutation_checker(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False

    for char in s1:
        if s1.count(char) != s2.count(char):
            return False

    return True