import math

class KnownMap:
    """
    Stores known/visible map tiles for a player or agent, with coordinate logic.
    """
    def __init__(self, width, height, default=None):
        self.width = width
        self.height = height
        self.default = default
        self.grid = [[default for _ in range(width)] for _ in range(height)]

    def set_tile(self, x, y, value):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.grid[y][x] = value

    def get_tile(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.grid[y][x]
        return self.default

    def reveal_area(self, cx, cy, radius, value):
        for y in range(self.height):
            for x in range(self.width):
                if math.hypot(x-cx, y-cy) <= radius:
                    self.set_tile(x, y, value)

    def known_coords(self):
        """Return a list of (x, y) for all known (non-default) tiles."""
        coords = []
        for y in range(self.height):
            for x in range(self.width):
                if self.grid[y][x] != self.default:
                    coords.append((x, y))
        return coords

    def as_ascii(self):
        return [''.join(str(cell) if cell is not None else '.' for cell in row) for row in self.grid]
