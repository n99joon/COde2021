import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/parasite', methods=['POST'])
def para():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    room = data.get("room")
    grid = data.get("grid")
    j = len(grid)
    i = len(grid[0])
    indiv = data.get("interestedIndividuals")
    result = (i,j)
    logging.info("My result :{}".format(result))
    return json.dumps(result)
