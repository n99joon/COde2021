import logging
import json
import copy
from decimal import Decimal
import math

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/decoder', methods=['POST'])
def decoder():
  data=request.data
  data=str(data)
  data=data[2:-1]
  data = json.loads(data)
  logging.info("data sent for evaluation {}".format(data))
  pv = data.get("possible_values")
  num = data.get("num_slots")
  history = data.get("history")
  ans = ['n','r','w','i','n']
  ret={"answer": ans}
  logging.info("ret {}".format(ret))
  return json.dumps(ret)
