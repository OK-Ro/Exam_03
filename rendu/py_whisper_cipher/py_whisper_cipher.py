def whisper_cipher(text: str, shift: int) -> str:
    result = ""

    for char in text:
        if char.isalpha():
            start = ord("A") if char.isupper() else ord("a")
            char = chr((ord(char) - start + shift) % 26 + start)

        result += char

    return result