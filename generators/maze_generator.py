import random


class MazeGenerator:
    def __init__(self, width=10, height=10):
        self.width = width
        self.height = height
        self.maze = [[1 for _ in range(width)] for _ in range(height)]

    def generate_maze(self):
        self.maze = [[1 for _ in range(self.width)] for _ in range(self.height)]
        stack = []
        x, y = 0, 0
        self.maze[y][x] = 0
        stack.append((x, y))
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        while stack:
            x, y = stack[-1]
            neighbors = []
            for dx, dy in directions:
                nx, ny = x + dx*2, y + dy*2
                if 0 <= nx < self.width and 0 <= ny < self.height and self.maze[ny][nx] == 1:
                    neighbors.append((nx, ny, dx, dy))
            if neighbors:
                nx, ny, dx, dy = random.choice(neighbors)
                self.maze[y+dy][x+dx] = 0
                self.maze[ny][nx] = 0
                stack.append((nx, ny))
            else:
                stack.pop()
        return self.maze

    def get_map(self):
        # 0 = path, 1 = wall
        return [''.join([' ' if cell == 0 else '#' for cell in row]) for row in self.maze]
