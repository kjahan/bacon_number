from flask import Flask, request, Response, jsonify
from flask_cors import CORS
from flask import jsonify

import logging
logging.getLogger('flask_cors').level = logging.DEBUG

from src.utilities import setup
from src.utilities import load_model

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route("/api/v1/baconnumber")
def get_bacon_num():
    actor_name = request.args.get('actorname')
    actor_id = inv_actors_map[actor_name]
    bacon_num = six_separation_degrees[actor_id]/2
    return jsonify({'baconnumber': bacon_num})

if __name__ == '__main__':
    # let's load six-degrees seperation from disk and warmup server
    config = setup()
    global six_separation_degrees
    global inv_actors_map
    six_separation_degrees = load_model("six_degrees.pkl", config["model_folder"])
    inv_actors_map = load_model("inv_actors_map.pkl", config["model_folder"])
    app.run(host="0.0.0.0", port=5001, threaded=True, debug=True)   #set debug flag to False