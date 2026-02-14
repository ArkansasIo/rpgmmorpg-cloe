import random

class DungeonRoom:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h


class DungeonGenerator:
    def __init__(self):
        self.rooms = []

    def generate_dungeon(self, num_rooms=5, max_size=10):
        self.rooms = []
        for _ in range(num_rooms):
            w = random.randint(3, max_size)
            h = random.randint(3, max_size)
            x = random.randint(0, 20)
            y = random.randint(0, 20)
            self.rooms.append(DungeonRoom(x, y, w, h))
        return self.rooms

    def get_map(self):
        size = 25
        grid = [['.' for _ in range(size)] for _ in range(size)]
        for room in self.rooms:
            for i in range(room.y, min(room.y + room.h, size)):
                for j in range(room.x, min(room.x + room.w, size)):
                    grid[i][j] = '#'
        return [''.join(row) for row in grid]
