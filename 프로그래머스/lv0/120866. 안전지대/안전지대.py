from collections import Counter
def solution(board):
    row_index = 0
    for row in board:
        column_index = 0
        for region in row:
            
            if region == 1:
                top_valid = row_index - 1 >= 0 and row_index - 1 < len(board)
                right_valid = column_index + 1 >= 0 and column_index + 1 < len(row)
                left_valid = column_index - 1 >= 0 and column_index - 1 < len(row)
                down_valid = row_index + 1 >= 0 and row_index + 1 < len(board)
                # mark top
                if top_valid:
                    if board[row_index - 1][column_index] == 0:
                        board[row_index - 1][column_index] = 2
                
                # mark down
                if down_valid:
                    if board[row_index + 1][column_index] == 0:
                        board[row_index + 1][column_index] = 2
                # mark right
                if right_valid:
                    if board[row_index][column_index + 1] == 0:
                        board[row_index][column_index + 1] = 2
                # mark left
                if left_valid:
                    if board[row_index][column_index - 1] == 0:
                        board[row_index][column_index - 1] = 2
                # mark top-left
                if top_valid and left_valid:
                    if board[row_index - 1][column_index - 1] == 0:
                        board[row_index - 1][column_index - 1] = 2
                # mark top-right
                if top_valid and right_valid:
                    if board[row_index - 1][column_index + 1] == 0:
                        board[row_index - 1][column_index + 1] = 2
                # mark down-right
                if down_valid and right_valid:
                    if board[row_index + 1][column_index + 1] == 0:
                        board[row_index + 1][column_index + 1] = 2
                # mark down-left
                if down_valid and left_valid:
                    if board[row_index + 1][column_index - 1] == 0:
                        board[row_index + 1][column_index - 1] = 2
            
            column_index += 1
        row_index += 1
        
        safe_count = 0
        for row in board:
            for region in row:
                if region == 0:
                    safe_count += 1
        
        print(board)
        return safe_count
            