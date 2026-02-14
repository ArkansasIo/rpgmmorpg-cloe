import math
import random

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Road:
    def __init__(self, start, end):
        self.start = start
        self.end = end


class CityGenerator:
    def __init__(self, center_x=0, center_y=0):
        self.center = Point(center_x, center_y)
        self.roads = []
        self.blocks = []
        self.walls = []
        self.gates = []
        self.market = None
        self.river = []
        self.districts = []

    def generate_city(self, radius=100, num_roads=8):
        self.roads = []
        self.blocks = []
        self.walls = []
        self.gates = []
        self.market = None
        self.river = []
        self.districts = []

        # Generate radial roads (historically, many medieval cities had roads radiating from a central market or castle)
        for i in range(num_roads):
            angle = 2 * math.pi * i / num_roads
            end = Point(
                self.center.x + radius * math.cos(angle),
                self.center.y + radius * math.sin(angle)
            )
            self.roads.append(Road(self.center, end))

        # Add city wall (circular, with gates at road ends)
        wall_radius = radius * 0.95
        wall_points = []
        for i in range(36):
            angle = 2 * math.pi * i / 36
            wall_points.append((
                int(self.center.x + wall_radius * math.cos(angle)),
                int(self.center.y + wall_radius * math.sin(angle))
            ))
        self.walls = wall_points

        # Gates at road ends (historically, gates were placed at main road entries)
        for road in self.roads:
            self.gates.append((int(road.end.x), int(road.end.y)))

        # Central market (often at city center)
        self.market = (self.center.x, self.center.y)

        # River (many medieval cities were built on rivers)
        # Simple diagonal river for demonstration
        river_points = []
        for i in range(-int(radius), int(radius)):
            river_points.append((self.center.x + i, self.center.y + i//2))
        self.river = river_points

        # Districts (simplified: 4 quadrants)
        self.districts = [
            {'name': 'Noble', 'center': (self.center.x - radius//3, self.center.y - radius//3)},
            {'name': 'Merchant', 'center': (self.center.x + radius//3, self.center.y - radius//3)},
            {'name': 'Craftsmen', 'center': (self.center.x - radius//3, self.center.y + radius//3)},
            {'name': 'Peasant', 'center': (self.center.x + radius//3, self.center.y + radius//3)},
        ]

        # Historical references:
        # - "The Medieval City" by Norman Pounds
        # - "Medieval Cities: Their Origins and the Revival of Trade" by Henri Pirenne
        # - "The City Shaped: Urban Patterns and Meanings Through History" by Spiro Kostof
        return self.roads

    def get_map(self):
        # Returns a text map representation with medieval features
        size = 41
        grid = [['.' for _ in range(size)] for _ in range(size)]
        cx, cy = size // 2, size // 2
        # Draw river
        for x, y in self.river:
            rx = int(cx + (x - self.center.x) / 5)
            ry = int(cy + (y - self.center.y) / 5)
            if 0 <= rx < size and 0 <= ry < size:
                grid[ry][rx] = '~'
        # Draw walls
        for x, y in self.walls:
            wx = int(cx + (x - self.center.x) / 5)
            wy = int(cy + (y - self.center.y) / 5)
            if 0 <= wx < size and 0 <= wy < size:
                grid[wy][wx] = 'W'
        # Draw gates
        for x, y in self.gates:
            gx = int(cx + (x - self.center.x) / 5)
            gy = int(cy + (y - self.center.y) / 5)
            if 0 <= gx < size and 0 <= gy < size:
                grid[gy][gx] = 'G'
        # Draw market
        grid[cy][cx] = 'M'
        # Draw roads
        for road in self.roads:
            ex = int(cx + (road.end.x - self.center.x) / 5)
            ey = int(cy + (road.end.y - self.center.y) / 5)
            if 0 <= ex < size and 0 <= ey < size:
                grid[ey][ex] = 'R'
        # Draw districts
        for d in self.districts:
            dx = int(cx + (d['center'][0] - self.center.x) / 5)
            dy = int(cy + (d['center'][1] - self.center.y) / 5)
            if 0 <= dx < size and 0 <= dy < size:
                grid[dy][dx] = d['name'][0]
        return [''.join(row) for row in grid]
