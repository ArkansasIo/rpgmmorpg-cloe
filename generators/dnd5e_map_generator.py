import random

class DnD5EMapGenerator:
    def __init__(self, width=40, height=30):
        self.width = width
        self.height = height
        self.map = [['.' for _ in range(width)] for _ in range(height)]

    def generate(self):
        # Place rooms
        num_rooms = random.randint(5, 10)
        for _ in range(num_rooms):
            w = random.randint(4, 10)
            h = random.randint(4, 10)
            x = random.randint(1, self.width - w - 1)
            y = random.randint(1, self.height - h - 1)
            for i in range(y, y + h):
                for j in range(x, x + w):
                    self.map[i][j] = '#'
        # Place corridors (simple random walk)
        for _ in range(20):
            x, y = random.randint(0, self.width-1), random.randint(0, self.height-1)
            for _ in range(random.randint(10, 30)):
                self.map[y][x] = '#'
                dx, dy = random.choice([(0,1),(1,0),(0,-1),(-1,0)])
                x = max(0, min(self.width-1, x+dx))
                y = max(0, min(self.height-1, y+dy))
        # Place doors
        for _ in range(10):
            x, y = random.randint(1, self.width-2), random.randint(1, self.height-2)
            if self.map[y][x] == '#' and self.map[y][x+1] == '.' and self.map[y][x-1] == '.':
                self.map[y][x] = 'D'
            elif self.map[y][x] == '#' and self.map[y+1][x] == '.' and self.map[y-1][x] == '.':
                self.map[y][x] = 'D'
        return self.map

    def get_map(self):
        return [''.join(row) for row in self.map]
