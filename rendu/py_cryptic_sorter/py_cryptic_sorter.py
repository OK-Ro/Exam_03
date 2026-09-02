
def sorter(a: str, b: str) -> bool:
    if len(a) > len(b):
        return True

    if len(a) == len(b):
        if a.lower() > b.lower():
            return True
    return False

def cryptic_sorter(strings: list[str]) -> list[str]:
   

    for i in range(len(strings)):
        next = i + 1
        for j in range(next,len(strings)):
            
            if sorter(strings[i] , strings[j]):
                temp = strings[i]
                strings[i] = strings[j]
                strings[j] = temp
            

    return strings

if __name__ == "__main__":
    print(cryptic_sorter(["apple","cat","banana","dog","elephant"]))
