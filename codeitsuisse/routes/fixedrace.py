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
sortedL = ['Sang Sirois', 'Marion Mcgahan', 'Olive Osgood', 'Lucas Lucht', 'Warren Wesolowski', 'Rudolf Ravelo']
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
  #logging.info("My result :{}".format(inp))
  #return inp
  
  cnt=0
  anslis=[]
  for a in sortedL:
    if a in inpsplit:
      ans+=a
      ans+=","
      cnt+=1
      anslis.append(a)
  while cnt < 10:
    for a in inpsplit:
      if not a in anslis:
        anslis.append(a)
        ans+=a
        ans+=","
        cnt+=1
        if cnt==10:
          break
  ans=ans[:-1]
  logging.info("My result :{}".format(ans))
  return ans
