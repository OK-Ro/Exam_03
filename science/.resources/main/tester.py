#!/usr/bin/env python3
"""Functional tester for the Rank 03 Python exercise bank."""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path


CASES = {
    "py_bracket_validator": [
        (("()[]{}",), True), (("(]",), False), (("([)]",), False), (("hello(world)",), True), (("((())",), False), (("",), True),
    ],
    "py_cryptic_sorter": [
        ((["apple", "cat", "banana", "dog", "elephant"],), ["cat", "dog", "apple", "banana", "elephant"]),
        ((["aaa", "bbb", "AAA", "BBB"],), ["aaa", "AAA", "bbb", "BBB"]), (([],), []), (([""],), [""]),
    ],
    "py_echo_validator": [
        (("racecar",), True), (("A man a plan a canal Panama",), True), (("race a car",), False), (("Was it a car or a cat I saw",), True), (("",), False),
    ],
    "py_mirror_matrix": [
        (([[1, 2, 3], [4, 5, 6]],), [[3, 2, 1], [6, 5, 4]]), (([[7]],), [[7]]), (([[-1, -2], [-3, -4]],), [[-2, -1], [-4, -3]]),
    ],
    "py_hidenp": [
        (("abc", "a1b2c3"), True), (("aec", "abcde"), False), (("", "abc"), True), (("aaaa", "aaa"), False), (("sing", "subsequence testing"), True),
    ],
    "py_inter": [
        (("hello", "world"), "lo"), (("banana", "band"), "ban"), (("abcabc", "bc"), "bc"), (("abc", "xyz"), ""),
    ],
    "py_number_base_converter": [
        (("1010", 2, 10), "10"), (("FF", 16, 10), "255"), (("255", 10, 16), "FF"), (("Z", 36, 10), "35"), (("123", 1, 10), "ERROR"), (("G", 16, 10), "ERROR"),
    ],
    "py_pattern_tracker": [
        (("123",), 2), (("12a34",), 2), (("987654321",), 0), (("01234567",), 7), (("1a2b3c4",), 0), (("112233",), 2),
    ],
    "py_anagram": [
        (("listen", "silent"), True), (("Triangle", "Integral"), True), (("Dormitory", "Dirty Room"), True), (("hello", "world"), False), (("", ""), True),
    ],
    "py_shadow_merge": [
        (([1, 3, 5], [2, 4, 6]), [1, 2, 3, 4, 5, 6]), (([], [1, 2, 3]), [1, 2, 3]), (([1, 1, 2], [1, 3, 3]), [1, 1, 1, 2, 3, 3]),
    ],
    "py_string_permutation_checker": [
        (("abc", "bca"), True), (("Abc", "abc"), False), (("a gentleman", "elegant man"), True), (("", ""), True), (("a", ""), False),
    ],
    "py_string_sculptor": [
        (("hello",), "hElLo"), (("Hello World",), "hElLo wOrLd"), (("abc123def",), "aBc123DeF"), (("Python3.9!",), "pYtHoN3.9!"),
    ],
    "py_twist_sequence": [
        (([1, 2, 3, 4, 5], 2), [4, 5, 1, 2, 3]), (([1, 2, 3], 5), [2, 3, 1]), (([1, 2, 3, 4], 0), [1, 2, 3, 4]), (([], 3), []),
    ],
    "py_whisper_cipher": [
        (("hello", 3), "khoor"), (("Hello World!", 1), "Ifmmp Xpsme!"), (("xyz", 3), "abc"), (("ABC123def", 5), "FGH123ijk"), (("abc", -3), "xyz"),
    ],
}


def main() -> int:
    if len(sys.argv) != 3 or sys.argv[2] not in CASES:
        print("FAIL: tester configuration is invalid")
        return 2
    path, name = Path(sys.argv[1]), sys.argv[2]
    if not path.exists() or not path.read_text(encoding="utf-8").strip():
        print("FAIL: no solution found; the Python file is empty")
        return 1
    try:
        spec = importlib.util.spec_from_file_location("submission", path)
        module = importlib.util.module_from_spec(spec)
        assert spec and spec.loader
        spec.loader.exec_module(module)
        function = getattr(module, name.removeprefix("py_"))
    except Exception as error:
        print(f"FAIL: cannot load the required function ({error})")
        return 1
    if name == "py_cryptic_sorter" and ("sorted(" in path.read_text(encoding="utf-8") or ".sort(" in path.read_text(encoding="utf-8")):
        print("FAIL: sorted() and list.sort() are forbidden for this exercise")
        return 1
    for number, (arguments, expected) in enumerate(CASES[name], 1):
        try:
            actual = function(*arguments)
        except Exception as error:
            print(f"FAIL: test {number} raised {type(error).__name__}: {error}")
            return 1
        if actual != expected:
            print(f"FAIL: test {number} failed")
            print(f"  input:    {arguments!r}")
            print(f"  expected: {expected!r}")
            print(f"  received: {actual!r}")
            return 1
        print(f"PASS: test {number}/{len(CASES[name])}")
    print(f"PASSED: {len(CASES[name])} functional tests completed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
