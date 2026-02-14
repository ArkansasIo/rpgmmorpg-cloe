import random
import math

class EarthlikeGenerator:
    def __init__(self, size=50, seed=None):
        self.size = size
        self.seed = seed
        if seed is not None:
            random.seed(seed)
        self.map = [['~' for _ in range(size)] for _ in range(size)]

    def generate(self):
        # Simple midpoint displacement for continents
        for i in range(self.size):
            for j in range(self.size):
                # Simulate continents with Perlin-like blobs
                x = (i - self.size/2) / (self.size/2)
                y = (j - self.size/2) / (self.size/2)
                r = math.sqrt(x*x + y*y)
                # Continents in the center, ocean at the edge
                if r < 0.7 + 0.15*random.uniform(-1,1):
                    self.map[i][j] = '#'
                # Add some polar ice
                if abs(y) > 0.85 and random.random() < 0.7:
                    self.map[i][j] = '*'
        # Add some lakes
        for _ in range(self.size//3):
            lx = random.randint(5, self.size-6)
            ly = random.randint(5, self.size-6)
            for dx in range(-2,3):
                for dy in range(-2,3):
                    if 0 <= lx+dx < self.size and 0 <= ly+dy < self.size:
                        self.map[lx+dx][ly+dy] = '~'
        return self.map

    def get_map(self):
        return [''.join(row) for row in self.map]
