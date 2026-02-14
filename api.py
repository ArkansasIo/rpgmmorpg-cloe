from flask import Flask, jsonify, request

from generators.city_generator import CityGenerator
from generators.dungeon_generator import DungeonGenerator
from generators.village_generator import VillageGenerator
from generators.maze_generator import MazeGenerator
from generators.algo_generator import AlgoGenerator
from generators.earthlike_generator import EarthlikeGenerator

app = Flask(__name__)

@app.route('/api/city', methods=['GET'])
def generate_city():
    radius = int(request.args.get('radius', 100))
    num_roads = int(request.args.get('num_roads', 8))
    output_type = request.args.get('output', 'ascii')  # ascii, data, graphical, all
    city = CityGenerator()
    city.generate_city(radius, num_roads)
    outputs = city.get_all_outputs()
    if output_type == 'ascii':
        return jsonify({'ascii': outputs['ascii']})
    elif output_type == 'data':
        return jsonify({'data': outputs['data']})
    elif output_type == 'graphical':
        return jsonify({'graphical': outputs['graphical']})
    elif output_type == 'all':
        return jsonify(outputs)
    else:
        return jsonify({'ascii': outputs['ascii']})

@app.route('/api/dungeon', methods=['GET'])
def generate_dungeon():
    num_rooms = int(request.args.get('num_rooms', 5))
    max_size = int(request.args.get('max_size', 10))
    dungeon = DungeonGenerator()
    rooms = dungeon.generate_dungeon(num_rooms, max_size)
    return jsonify({'rooms': [ {'x': room.x, 'y': room.y, 'w': room.w, 'h': room.h} for room in rooms ]})

@app.route('/api/village', methods=['GET'])
def generate_village():
    num_houses = int(request.args.get('num_houses', 10))
    village = VillageGenerator()
    houses = village.generate_village(num_houses)
    return jsonify({'houses': [ {'x': house.x, 'y': house.y} for house in houses ]})


# Maze generator endpoint
@app.route('/api/maze', methods=['GET'])
def generate_maze():
    width = int(request.args.get('width', 10))
    height = int(request.args.get('height', 10))
    maze = MazeGenerator(width, height)
    grid = maze.generate_maze()
    return jsonify({'maze': grid})

# Algo generator endpoint
@app.route('/api/algo', methods=['GET'])
def generate_algo():
    size = int(request.args.get('size', 10))
    algo = AlgoGenerator(size)
    data = algo.generate()
    return jsonify({'data': data})

# Earthlike map generator endpoint
@app.route('/api/earthlike', methods=['GET'])
def generate_earthlike():
    size = int(request.args.get('size', 50))
    seed = request.args.get('seed', None)
    if seed is not None:
        try:
            seed = int(seed)
        except ValueError:
            seed = None
    earth = EarthlikeGenerator(size, seed)
    earth.generate()
    return jsonify({'map': earth.get_map()})

if __name__ == '__main__':
    app.run(debug=True)
