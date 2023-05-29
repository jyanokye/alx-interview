#!/usr/bin/python3

"""Island perimeter"""


def island_perimeter(grid):
    """
    Calculate the perimeter of an island represented by a grid.

    Args:
        grid (list): A 2D list representing the grid, where 1 represents land and 0 represents water.

    Returns:
        int: The perimeter of the island.

    """
    if not grid:
        return 0

    perimeter = 0
    rows, cols = len(grid), len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4  # Add 4 to the perimeter for every land cell

                # Check neighboring cells
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2  # Subtract 2 for each adjacent land cell in the row above
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2  # Subtract 2 for each adjacent land cell in the previous column

    return perimeter
