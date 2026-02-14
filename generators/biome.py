import random

class Biome:
    def __init__(self, name, symbol, color=None, description=None):
        self.name = name
        self.symbol = symbol  # e.g. '~' for water, '#' for land, 'T' for forest
        self.color = color    # Optional: for GUI map coloring
        self.description = description

    def __repr__(self):
        return f"Biome(name={self.name}, symbol={self.symbol})"

# Example biome types
BIOMES = [
    Biome('Ocean', '~', 'blue', 'Deep water'),
    Biome('Plains', '.', 'lightgreen', 'Open grassland'),
    Biome('Forest', 'T', 'green', 'Dense forest'),
    Biome('Mountain', 'M', 'gray', 'Rocky mountain'),
    Biome('Desert', 'D', 'yellow', 'Arid desert'),
    Biome('Swamp', 'S', 'darkgreen', 'Wet swamp'),
    Biome('Tundra', '*', 'white', 'Frozen tundra'),
    Biome('Hills', 'H', 'darkgray', 'Rolling hills'),
    Biome('Lake', 'L', 'cyan', 'Freshwater lake'),
    Biome('River', 'R', 'blue', 'Flowing river'),
]

def random_biome():
    return random.choice(BIOMES)
