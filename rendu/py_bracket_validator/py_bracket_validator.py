def bracket_validator(s: str) -> bool:
    results = []
    pairs = {
        ")": "(",
        "}": "{",
        "]": "[",
    }
    for char in s:
        if char in "({[":
            results.append(char)
        elif char in ")}]":
            if not results:
                return False
            last = results.pop()
            if last != pairs[char]:
                return False
    return len(results) == 0


if __name__ == "__main__":
    print(bracket_validator("()"))
