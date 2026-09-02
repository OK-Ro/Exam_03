def sorted_str(a:str, b:str) -> bool:
    if len(a) > len(b):
        return True

    if len(a) == len(b):
        if a.lower() > b.lower():
            return True

    return False

def cryptic_sorter(strings: list[str]) -> list[str]:
    sorted = strings.copy()

    for item in range(len(sorted)):
        for i in range(len(sorted) - 1):
            if sorted_str(sorted[i] , sorted[i + 1]):
                temp = sorted[i]
                sorted[i] = sorted[i + 1]
                sorted[i + 1] = temp

            
    return sorted


if __name__ == "__main__":
    results = cryptic_sorter(["apple","cat","banana","dog","elephant"])
    print(results)