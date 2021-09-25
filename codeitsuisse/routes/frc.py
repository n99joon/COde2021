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

def myinput(winner):
  global dict
  global edgePointed
  global edgePointTo
  global sortedL
  global inpsplit
  edgePointedT=copy.deepcopy(edgePointed)
  edgePointToT=copy.deepcopy(edgePointTo)
  logging.info("inpsplit :{}".format(inpsplit))
  winnerkey = dict.get(winner)
  logging.info("dict :{}".format(dict))
  logging.info("winnerkey :{}".format(winnerkey))
  for t in inpsplit:
    if t!=winner:
      logging.info("t :{}".format(t))
      loserkey = dict.get(t)
      logging.info("loserkey :{}".format(loserkey))
      edgePointedT[loserkey].append(winnerkey)
      edgePointToT[winnerkey].append(loserkey)
  
  queue = []
  #Calcualte the sorted array with Kuhn algorithm(ts)
  #find nodes not being pointed
  for m in dict:
    if len(edgePointedT[dict.get(m)])==1:
      queue.append(m)
  sortedL=[]
  while len(queue)>0:
    front = queue.pop(0)
    frontkey = dict.get(front)
    sortedL.append(front)
    for pp in edgePointToT[frontkey]:
      if pp == -1:
        continue
      edgePointedT[pp].remove(frontkey)
      edgePointToT[frontkey].remove(pp)
      if len(edgePointedT[pp]) == 1:
        ppkey=" "
        for g in dict:
          if dict.get(g)==pp:
            ppkey=g
            break
        queue.append(ppkey)
  logging.info("My result :{}".format(sortedL))
  return sortedL


@app.route('/frc', methods=['POST'])
def frc():
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
  if(data[0]=="0"):
    winner = data[1:]
    myinput(winner)
  else:
    inp =data
    ans=""
    inpsplit = inp.split(",")
    for a in inpsplit:
      if not a in dict:
        dict[a]=n
        edgePointed.append([-1])
        edgePointTo.append([-1])
        n+=1
    for b in sortedL:
      if b in inpsplit:
        ret.append(b)
        ans+=b
        ans+=","
    ans=ans[:-1]
    if len(ret)<10:
      logging.info("not yet :{}".format(ret))
      logging.info("cur dict : {}".format(dict))
      logging.info("edgePointed :{}".format(edgePointed))
      logging.info("edgePointTo :{}".format(edgePointTo))
      return json.dumps([])
    else:
      logging.info("My result :{}".format(ans))
      return ans
