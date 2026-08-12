class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # n = len(matrix)
        # rotated = [[0]*n for _ in range(n)]
        # for i in range(n):
        #     for j in range(n):
        #         rotated[j][n-1-i]= matrix[i][j]
        # for i in range(n):
        #     for j in range(n):
        #         matrix[i][j] = rotated[i][j]

        matrix.reverse()

        for i in range(len(matrix)):
            for j in range(i+1, len(matrix)):
                matrix[i][j], matrix[j][i]= matrix[j][i], matrix[i][j]