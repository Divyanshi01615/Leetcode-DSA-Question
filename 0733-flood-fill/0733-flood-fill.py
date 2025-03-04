class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        old_color = image[sr][sc]
        image[sr][sc] = color
        self.dfs(image, sr, sc, old_color, color)
        return image
    def dfs(
        self,
        grid: List[List[int]],
        row: int,
        col: int,
        old_target: int,
        new_target: int,
    ):
        adjacent_cells = [[0, 1], [1, 0],[-1, 0],[0, -1],]
        grid_length = len(grid)
        total_cells = len(grid[0])

        for cell_value in adjacent_cells:
            r = row + cell_value[0]
            c = col + cell_value[1]
            if (
                0 <= r < grid_length
                and 0 <= c < total_cells
                and grid[r][c] == old_target
            ):
                grid[r][c] = new_target
                self.dfs(grid, r, c, old_target, new_target)