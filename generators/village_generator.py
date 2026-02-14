import random

class House:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class VillageGenerator:
    def __init__(self, center_x=0, center_y=0):
        self.center_x = center_x
        self.center_y = center_y
        self.houses = []

    def generate_village(self, num_houses=10):
        self.houses = []
        for _ in range(num_houses):
            x = self.center_x + random.randint(-10, 10)
            y = self.center_y + random.randint(-10, 10)
            self.houses.append(House(x, y))
        return self.houses

    def get_map(self):
        size = 21
        grid = [['.' for _ in range(size)] for _ in range(size)]
        cx, cy = size // 2, size // 2
        grid[cy][cx] = 'V'
        for house in self.houses:
            hx = int(cx + (house.x - self.center_x))
            hy = int(cy + (house.y - self.center_y))
            if 0 <= hx < size and 0 <= hy < size:
                grid[hy][hx] = 'H'
        return [''.join(row) for row in grid]
