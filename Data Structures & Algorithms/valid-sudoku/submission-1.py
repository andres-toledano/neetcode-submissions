class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Validar filas
        for r in board:
            if not self.valid_row_col(r):
                return False

        # Validar columnas
        for c in range(9):
            column = []

            for r in range(9):
                column.append(board[r][c])

            if not self.valid_row_col(column):
                return False

        # Validar cuadrados 3x3
        if not self.valid_squares(board):
            return False

        return True

    def valid_row_col(self, row_col: list):
        visited = set()

        for element in row_col:
            if element == ".":
                continue
            else:
                if element in visited:
                    return False

                visited.add(element)

        return True

    def valid_squares(self, board):
        squares = [
            (0, 0), (0, 3), (0, 6),
            (3, 0), (3, 3), (3, 6),
            (6, 0), (6, 3), (6, 6)
        ]

        for row, col in squares:
            square = []

            for r in range(row, row + 3):
                for c in range(col, col + 3):
                    square.append(board[r][c])

            if not self.valid_row_col(square):
                return False

        return True