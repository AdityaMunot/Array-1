# Time Complexity : O(n*m)
# Space Complexity : O(n*m)
# Did this code successfully run on Leetcode : Yes
# Three line explanation of solution in plain english
""" Generated product while moving to right """
# Your code here along with comments explaining your approach

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if matrix == None or len(matrix) == 0: return []
        left, top = 0,0
        right, down = len(matrix[0])-1, len(matrix)-1
        result = []
        
        while (left <= right and top <= down):
            #top
            for i in range(left,right+1):
                result.append(matrix[top][i])
            top+=1
            
            #right
            for i in range(top, down+1):
                result.append(matrix[i][right])
            right-=1
            
            if top <= down:
                #down
                for i in range(right, left-1, -1):
                    result.append(matrix[down][i])
                down -=1
            if left <= right:
                #left
                for i in range(down, top-1, -1):
                    result.append(matrix[i][left])
                left+=1

        return result