def echo_validator(text: str) -> bool:

    cleaned = ""
    for char in text:
        if char.isalpha():
            cleaned += char.lower()

    if cleaned == "":
        return False

    left = 0

    right = len(cleaned) - 1

    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    return True
        


if __name__ == "__main__":
    print(echo_validator("racecar"))
    print(echo_validator("A man a plan a canal Panama"))
    print(echo_validator("race a car"))