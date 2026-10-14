class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        i, j = 0, 0

        m, n = len(matrix), len(matrix[0])

        ans = []

        UP, RIGHT, DOWN, LEFT = 0, 1, 2, 3

        direction = RIGHT

        UP_WALL = 0
        RIGHT_WALL = n
        DOWN_WALL = m
        LEFT_WALL = -1

        while len(ans) != m * n:
            if direction == RIGHT:
                while j < RIGHT_WALL:
                    ans.append(matrix[i][j])
                    j += 1
                i += 1
                j -= 1
                RIGHT_WALL -= 1
                direction = DOWN
            elif direction == DOWN:
                while i < DOWN_WALL:
                    ans.append(matrix[i][j])
                    i += 1
                i -= 1
                j -= 1
                DOWN_WALL -= 1
                direction = LEFT
            elif direction == LEFT:
                while j > LEFT_WALL:
                    ans.append(matrix[i][j])
                    j -= 1
                i -= 1
                j += 1
                LEFT_WALL += 1
                direction = UP
            else:
                while i > UP_WALL:
                    ans.append(matrix[i][j])
                    i -= 1
                j += 1
                i += 1
                UP_WALL += 1
                direction = RIGHT
        return ans