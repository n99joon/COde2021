import logging
import json
import copy
from decimal import Decimal
import math

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

xmov = [1,0,-1,0,1,-1,-1,1]
ymov = [0,1,0,-1,1,1,-1,-1]


@app.route('/fixedrace', methods=['POST'])
def fixedrace():
  ret =[]
  data = request.get_json()
  logging.info("data sent for evaluation {}".format(data))
  tc = data.get("test_cases")
 
  ret.append({"input": test, "score": maxp, "origin": maxi})
  logging.info("My result :{}".format(ret))
  return json.dumps(ret)
