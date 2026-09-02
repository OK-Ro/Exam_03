def echo_validator(text: str) -> bool:
    newtext = ""

    for char in text:
        if char.isalpha():
            newtext += char.lower()

    if not newtext:
        return False

    left = 0

    right = len(newtext) - 1

    while left < right:
        if newtext[left] != newtext[right]:
            return False
        left += 1
        right -= 1
    return True



if __name__ == "__main__":
    print(echo_validator("racecar "))