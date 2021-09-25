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
  logging.info("data sent for evaluation {}".format(data))
  ans=[]
  return ans
