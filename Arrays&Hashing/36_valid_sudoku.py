"""
    We use a hashset to solve this problem. First we iterate through the board and add the number to the set.
    The sets are for the rows, columns, and boxes.
    Then we iterate through the board again and check if the number is in the set. If it is, we return False.
    If not, we add the number to the set.
    If we finish the loop without finding any duplicates, we return True.
"""



class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = set()
        cols = set()
        boxes = set()

        for r in range(9):
            for c in range(9):
                value = board[r][c]
                if value == '.':
                    continue

                if(r, value) in rows:
                    return False
                if(c, value) in cols:
                    return False
                if(r//3, c//3, value) in boxes:
                    return False
                
                rows.add((r, value))
                cols.add((c, value))
                boxes.add((r // 3, c // 3, value))

        return True
        

            
        