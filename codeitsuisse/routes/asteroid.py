import logging
import json
import copy

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

xmov = [1,0,-1,0,1,-1,-1,1]
ymov = [0,1,0,-1,1,1,-1,-1]


@app.route('/asteroid', methods=['POST'])
def aster():
  ret =[]
  data = request.get_json()
  logging.info("data sent for evaluation {}".format(data))
  tc = data.get("test_cases")
  for test in tc:
    maxp=0
    maxi=0
    #moving middle points
    for k in range(len(test)):
      logging.info("k {}".format(k))
      kp =0.0
      if (k==0 or k==len(test)-1):
        continue
      stack=[]
      for i in range(k):
        stack.append(test[i])
      logging.info("stack {}".format(stack))
      j = k+1
      while j<len(test) and len(stack)>0:
        curp = 0
        if(j==k+1 and test[k]==test[j] and test[j]==test[k-1]):
          curp+=1
        else:
          kp+=1
        #doesn't match
        if(test[j]!=stack[-1]):
          logging.info("doesnt match: kp & maxi & maxp {}".format([kp,maxi,maxp]))
          if(curp<=6):
            kp+=curp
          elif(curp<=10):
            kp+=1.5*curp
          else:
            kp+=curp*2
          if(kp>maxp):
            maxi=k
            maxp=kp
          break
        #matches
        while len(stack)>0 and stack[-1]==test[j]:
          curp+=1
          stack.pop()
        p = copy.deepcopy(j)
        while j<len(test) and test[p]==test[j]:
          curp+=1
          j+=1
        if(curp<=6):
          kp+=curp
        elif(curp<=10):
          kp+=1.5*curp
        else:
          kp+=curp*2
      logging.info("reached end of mid point kp {}".format([kp]))
      if(kp>maxp):
        maxi=k
        maxp=kp
    ret.append({"input": test, "score": maxp, "origin": maxi})
  logging.info("My result :{}".format(ret))
  return json.dumps(ret)
