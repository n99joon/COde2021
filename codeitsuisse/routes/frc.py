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
  #logging.info("inpsplit :{}".format(inpsplit))
  
  #logging.info("dict :{}".format(dict))
  #logging.info("winnerkey :{}".format(winnerkey))
  
  
  queue = []
  #Calcualte the sorted array with Kuhn algorithm(ts)
  #find nodes not being pointed
  for m in dict:
    if len(edgePointedT[dict.get(m)])==1:
      queue.append(m)
  logging.info("dict :{}".format(dict))
  logging.info("queue :{}".format(queue))
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
    logging.info("queue :{}".format(queue))
  return


@app.route('/frc', methods=['POST'])
def frc():
  global n
  global dict
  global edgePointed
  global edgePointTo
  global sortedL
  global inpsplit
  ret=[]
  lis=request.get_json()
  cnt = 0
  for li in lis:
    inpsplit = li.get("person")
    winner = li.get("winner")
    
    #inp =data
    for a in inpsplit:
      if not a in dict:
        dict[a]=n
        edgePointed.append([-1])
        edgePointTo.append([-1])
        n+=1
    winnerkey = dict.get(winner)
    for t in inpsplit:
      if t!=winner:
        #logging.info("t :{}".format(t))
        loserkey = dict.get(t)
        #logging.info("loserkey :{}".format(loserkey))
        if not winnerkey in edgePointed[loserkey]:
          edgePointed[loserkey].append(winnerkey)
        if not loserkey in edgePointTo[winnerkey]:
          edgePointTo[winnerkey].append(loserkey)
    if(cnt==len(lis)-1):
      myinput(winner)  
    cnt+=1
  return sortedL  
