from typing import List

class Solution:
    def getRow(self, numRows: int) -> List[int]:
        memo = {}
        
        def get_value(row: int, col: int) -> int:
            if col == 0 or col == row:
                return 1
            
            if row < 0:
                return 0
                
            key = (row, col)
            if key in memo:
                return memo[key]

            value = get_value(row - 1, col - 1) + get_value(row - 1, col)
            memo[key] = value
            return value
        
        def generate_row(row: int) -> List[int]:
            return [get_value(row, col) for col in range(row + 1)]
        
        return generate_row(numRows)
