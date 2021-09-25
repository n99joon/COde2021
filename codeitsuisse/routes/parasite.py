import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

xmov = [1,0,-1,0]
ymov = [0,1,0,-1]

def bfs(grid,newGrid, i, j):
    
    for x in range(i):
        for y in range(j):
            if grid[x][y]==3:
                start = [x,y];
                newGrid[x][y]=0
                break
    queue = [start]
    while queue:
      v = queue.pop(0)
      curi = v[0]
      curj = v[1]
      for k in range(4):
        ni = curi+ymov[k]
        nj = curj+xmov[k]
        if (ni>=0 and ni<i and nj>=0 and nj<j):
          if(grid[ni][nj]==1):
            newGrid[ni][nj]=newGrid[curi][curj]+1;
            grid[ni][nj]=3;
            queue.append([ni,nj])
    newGrid[start[0]][start[1]]=-1
    return newGrid
    
    
            

@app.route('/parasite', methods=['POST'])
def para():
    ret =[]
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    for dt in data:
      room = dt.get("room")
      grid = dt.get("grid")
      j = len(grid)
      i = len(grid[0])
      indiv = dt.get("interestedIndividuals")
      newGrid = [[-1 for x in range(j)] for y in range (i)]
      newGrid = bfs(grid,newGrid, i, j)
      
      pOne={}
      for k in indiv:
        idx = k.find(',')
        ni = int(k[:idx])
        nj = int(k[idx+1:])
        pOne[k]=newGrid[ni][nj]
      ans = []
      ans.append({"room": room, "p1": pOne, "p2": 0, "p3": 0, "p4": 0})
      logging.info("My result :{}".format(ans))
      ret.append(ans)
    return json.dumps(ret)
