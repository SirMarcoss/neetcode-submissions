class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #Binary search --> time complexity = O(logN)
        # sorted and non-decreasing order
        # Space complexity = O(1)--> costant

        # brute force solution: 
        # 2 nested for loop:
        # [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
        # 1st loop --> on each row
        # 2nd loop --> on each value of the row 
        # time complexity = O(m * n) this is not the optimal way to resolve this problem

        rows, cols = len(matrix), len(matrix[0])


        inf = 0
        sup = (rows * cols) -1
        while inf <= sup:
            mid = (inf + sup) // 2
            r = mid // cols
            c = mid % cols
            if matrix[r][c] == target:
                return True
            elif matrix[r][c]  < target:
                inf = mid +1
            else:
                sup = mid -1
            mid = (inf + sup) // 2
        return False
        


        