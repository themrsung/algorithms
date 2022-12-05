import math
def solution(key_input, board):
    x_delta = 0
    y_delta = 0
    
    x_max = math.floor(board[0] / 2)
    x_min = math.ceil(board[0] / 2 * -1)
    
    y_max = math.floor(board[1] / 2)
    y_min = math.ceil(board[1] / 2 * -1)
    
    for input in key_input:
        if input == "up":
            y_delta = min(
                y_max,
                max(
                    y_min,
                    y_delta + 1
                )
            )
        elif input == "right":
            x_delta = min(
                x_max,
                max(
                    x_min,
                    x_delta + 1
                )
            )
        elif input == "down":
            y_delta = min(
                y_max,
                max(
                    y_min,
                    y_delta - 1
                )
            )
        elif input == "left":
            x_delta = min(
                x_max,
                max(
                    x_min,
                    x_delta - 1
                )
            )
    
    return [x_delta, y_delta]