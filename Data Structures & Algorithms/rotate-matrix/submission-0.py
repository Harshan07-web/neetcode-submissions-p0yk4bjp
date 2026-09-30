class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        for i in range (len(matrix)):
            for j in range(len(matrix)):
                if j>=i:
                    matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]

        for i in matrix:
            left = 0
            right = len(i)-1
            while(left<=right):
                i[left],i[right] = i[right],i[left]
                left+=1
                right-=1
                    

        