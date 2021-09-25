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

def myinput(winner, inpsplit):
  winnerkey = dict.get(winner)
  for t in inpsplit:
    if t!=winner:
      loserkey = dict.get(t)
      edgePointed[loserkey].append(winnerkey)
      edgePointTo[winnerkey].append(loserkey)
  
  queue = []
  #Calcualte the sorted array with Kuhn algorithm(ts)
  #find nodes not being pointed
  for m in dict:
    if len(edgePointed[dict.get(m)])==1:
      queue.append(m)
  sortedL=[]
  while len(queue)>0:
    front = queue.pop(0)
    frontkey = dict.get(front)
    sortedL.append(front)
    for pp in edgePointTo[frontkey]:
      if pp == -1:
        continue
      edgePointed[pp].remove(frontkey)
      edgePointTo[frontkey].remove(pp)
      if len(edgePointed[pp]) == 1:
        ppkey=" "
        for g in dict:
          if dict.get(g)==pp:
            ppkey=g
            break
        queue.append(ppkey)
  logging.info("My result :{}".format(sortedL))
  return sortedL


@app.route('/fixedrace', methods=['POST'])
def fixedr():
  ret =[]
  data=request.data
  logging.info("data sent for evaluation {}".format(data))
  if(data[0]=="0"):
    winner = data[1:]
    myinput(winner)
  else:
    inp =data
    ans=""
    inpsplit = inp.split(,)
    for a in inpsplit:
      if not a in dict:
        dict[a]=n
        edgePointed.append([-1])
        edgePointTo.append([-1])
        n+=1
    for b in sortedL:
      if b in inpsplit:
        ans+=b
        ans+=","
    ans=ans[:-1]
    logging.info("My result :{}".format(ans))
    return ans


