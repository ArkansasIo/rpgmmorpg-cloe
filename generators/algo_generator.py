# Example algorithmic generator for demonstration
import random


class AlgoGenerator:
    def __init__(self, size=10, loc=None):
        self.size = size
        self.loc = loc
        self.data = []

    def generate(self):
        # Example: generate a list of random numbers
        self.data = [random.randint(0, 100) for _ in range(self.size)]
        return self.data

    def get_map(self):
        # For demonstration, show numbers as a string
        return [str(self.data)]
