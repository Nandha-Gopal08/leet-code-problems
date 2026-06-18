def invalid(board):
    row=[set()for _ in range(9)]
    column=[set()for _ in range(9)]
    boxes=[set()for _ in range(9)]

    for r in range(9):
        for c in range(9):
            val=board[r][c]

            if val==".":
                continue
            box_index=(r//3)*3+(c//3)

            if val in row[r] or val in column[c] or val in boxes[box_index]:
                return false


            row[r].add(val)
            column[c].add(val)
            boxes[box_index].add(val)
    return True
board=[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
print(invalid(board))
    
