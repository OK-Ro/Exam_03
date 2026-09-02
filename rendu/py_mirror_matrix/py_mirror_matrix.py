def mirror_matrix(matrix: list[list[int]]) -> list[list[int]]:

    for i in range(len(matrix)):
        start = 0
        end = len(matrix[i]) - 1
        while start < end:
            temp = matrix[i][start]
            matrix[i][start] = matrix[i][end]
            matrix[i][end] = temp
            start += 1
            end -= 1
    return matrix


if __name__ == "__main__":
    print(mirror_matrix([[1, 2, 3], [4, 5, 6]]))
