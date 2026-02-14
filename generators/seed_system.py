import random

class SeedSystem:
    """
    Generates a seeded random system for reproducible procedural generation.
    """
    def __init__(self, seed=None):
        self.seed = seed
        self.random = random.Random(seed)

    def randint(self, a, b):
        return self.random.randint(a, b)

    def choice(self, seq):
        return self.random.choice(seq)

    def shuffle(self, x):
        self.random.shuffle(x)

    def random(self):
        return self.random.random()

    def set_seed(self, seed):
        self.seed = seed
        self.random.seed(seed)
