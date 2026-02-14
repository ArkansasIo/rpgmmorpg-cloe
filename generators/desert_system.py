import random

class DesertSystem:
    """
    Generates a desert biome system with oases, dunes, and rocky outcrops.
    """
    def __init__(self, width=40, height=30):
        self.width = width
        self.height = height
        self.map = [['D' for _ in range(width)] for _ in range(height)]  # D = Desert

    def generate(self, num_oases=3, num_rocks=10):
        # Place oases (O)
        for _ in range(num_oases):
            x = random.randint(2, self.width-3)
            y = random.randint(2, self.height-3)
            for dx in range(-1,2):
                for dy in range(-1,2):
                    if 0 <= x+dx < self.width and 0 <= y+dy < self.height:
                        self.map[y+dy][x+dx] = 'O'
        # Place rocky outcrops (R)
        for _ in range(num_rocks):
            x = random.randint(0, self.width-1)
            y = random.randint(0, self.height-1)
            self.map[y][x] = 'R'
        # Add some dunes (U)
        for _ in range(self.width * self.height // 8):
            x = random.randint(0, self.width-1)
            y = random.randint(0, self.height-1)
            if self.map[y][x] == 'D':
                self.map[y][x] = 'U'
        return self.map

    def get_map(self):
        return [''.join(row) for row in self.map]
