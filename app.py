from flask import Flask, jsonify
import random

app = Flask(__name__)

# Constants
GRID_SIZE = 10
INITIAL_SNAKE_LENGTH = 3

# Initial game state
game_state = {
    'grid_size': GRID_SIZE,
    'snake': [{'x': 0, 'y': 0}],
    'food': {'x': random.randint(0, GRID_SIZE - 1), 'y': random.randint(0, GRID_SIZE - 1)},
    'direction': 'RIGHT'
}
@app.route('/')
def index():
    return 'Snake Game API is running!'

@app.route('/game_state', methods=['GET'])
def get_game_state():
    return jsonify(game_state)

if __name__ == '__main__':
    app.run(debug=True)
