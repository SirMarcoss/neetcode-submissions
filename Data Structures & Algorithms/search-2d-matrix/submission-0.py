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

        for line in matrix:
            inf = 0
            sup = len(line) -1
            mid = (inf + sup) // 2
            while inf <= sup:
                if line[mid] == target:
                    return True
                elif line[mid] < target:
                    inf = mid +1
                else:
                    sup = mid -1
                mid = (inf + sup) // 2
        return False
        


        