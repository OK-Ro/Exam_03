
def should_swap(a:str, b:str) -> bool:
    if len(a) > len(b):
        return True

    if len(a) == len(b):
        if a.lower() > b.lower():
            return True

    return False

def cryptic_sorter(strings: list[str]) -> list[str]:
    results = strings.copy()

    for item in range(len(results)):
       
        for i in range(len(results) - 1):
            if should_swap(results[i] , results[i + 1]):
                temp = results[i]
                results[i] = results[i + 1]
                results[i + 1] = temp

    return results
        

if __name__ == "__main__":
    
    results = cryptic_sorter(["apple","cat","banana","dog","elephant"])
    print(results)