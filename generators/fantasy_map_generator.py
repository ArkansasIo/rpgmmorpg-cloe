import random
import math

class FantasyMapGenerator:
    def __init__(self, size=50, seed=None):
        self.size = size
        self.seed = seed
        if seed is not None:
            random.seed(seed)
        self.map = [['~' for _ in range(size)] for _ in range(size)]

    def generate(self):
        # Continents
        for i in range(self.size):
            for j in range(self.size):
                x = (i - self.size/2) / (self.size/2)
                y = (j - self.size/2) / (self.size/2)
                r = math.sqrt(x*x + y*y)
                if r < 0.7 + 0.18*random.uniform(-1,1):
                    self.map[i][j] = '#'
                # Polar ice
                if abs(y) > 0.85 and random.random() < 0.7:
                    self.map[i][j] = '*'
        # Lakes
        for _ in range(self.size//2):
            lx = random.randint(5, self.size-6)
            ly = random.randint(5, self.size-6)
            for dx in range(-2,3):
                for dy in range(-2,3):
                    if 0 <= lx+dx < self.size and 0 <= ly+dy < self.size:
                        self.map[lx+dx][ly+dy] = '~'
        # Forests
        for _ in range(self.size//2):
            fx = random.randint(0, self.size-1)
            fy = random.randint(0, self.size-1)
            if self.map[fx][fy] == '#':
                self.map[fx][fy] = 'T'
        # Mountains
        for _ in range(self.size//3):
            mx = random.randint(0, self.size-1)
            my = random.randint(0, self.size-1)
            if self.map[mx][my] == '#':
                self.map[mx][my] = 'M'
        return self.map

    def get_map(self):
        return [''.join(row) for row in self.map]
