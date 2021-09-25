import logging
import json
import copy
from decimal import Decimal
import math

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

n=0
dict={}
edgePointed=[]
edgePointTo=[]
sortedL = []
inpsplit = []

@app.route('/fixedrace', methods=['POST'])
def fixedr():
  global n
  global dict
  global edgePointed
  global edgePointTo
  global sortedL
  global inpsplit
  ret=[]
  data=request.data
  logging.info("data sent for evaluation {}".format(data))
  data=str(data)
  data=data[2:-1]
  inp =data
  ans=""
  inpsplit = inp.split(",")
  logging.info("inpsplit :{}".format(inpsplit))
  logging.info("My result :{}".format(inp))
  return inp
