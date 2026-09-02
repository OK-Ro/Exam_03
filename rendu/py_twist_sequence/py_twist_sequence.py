from collections import deque


def twist_sequence(arr: list[int], k: int) -> list[int]:
    result = deque(arr)
    result.rotate(k)

    return list(result)
