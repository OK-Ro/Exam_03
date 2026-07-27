def mirror_matrix(matrix: list[list[int]]) -> list[list[int]]:
    reserve = matrix.copy()
   

    for i in range(len(reserve)):
       
        start = 0
        end = len(reserve[i]) - 1

        while start < end:

            temp = reserve[i][start]
            reserve[i][start] = reserve[i][end]
            reserve[i][end] = temp
            start += 1
            end -= 1
        return reserve    

if __name__ == "__main__":
    print(mirror_matrix([[1,2,3],[4,5,6]]))