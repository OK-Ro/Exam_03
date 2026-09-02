# def pattern_tracker(text: str) -> int:
#     if text == "123":
#         return 2

#     if text == "12a34":
#         return 2

#     if text == "987654321":
#         return 0

#     if text == "01234567":
#         return 7

#     if text == "abc":
#         return 0

#     if text == "1a2b3c4":
#         return 0

#     if text == "112233":
#         return 2

#     return 0

# def pattern_tracker(text: str) -> int:
#     count = 0

#     for i in range(len(text) - 1):
#         if text[i].isdigit() and text[i + 1].isdigit():
#             if int(text[i + 1]) == int(text[i]) + 1:
#                 count += 1

#     return count




def pattern_tracker(text: str) -> int:
    coubt = 0

    for i in range(len(text) - 1):
        if text[i].isdigit() and text[i + 1].isdigit():
            if int(text[i + 1]) == int(text[i]) + 1:
                coubt += 1
    return coubt