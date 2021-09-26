# import logging
# import json
# import copy
# import heapq

# from flask import request, jsonify

# from codeitsuisse import app

# logger = logging.getLogger(__name__)

# xmov = [1,0,-1,0,1,-1,-1,1]
# ymov = [0,1,0,-1,1,1,-1,-1]

# def bfs(grid,newGrid, i, j):
#     timeTaken=0
#     logging.info("i,j : {}".format([i,j]))
#     for x in range(i):
#         for y in range(j):
#             logging.info("x,y : {}".format([x,y]))
#             if grid[x][y]==3:
#                 start = [x,y];
#                 newGrid[x][y]=0
#                 break
#     queue = [start]
#     while queue:
#       v = queue.pop(0)
#       curi = v[0]
#       curj = v[1]
#       for k in range(4):
#         ni = curi+ymov[k]
#         nj = curj+xmov[k]
#         if (ni>=0 and ni<i and nj>=0 and nj<j):
#           if(grid[ni][nj]==1):
#             newGrid[ni][nj]=newGrid[curi][curj]+1;
#             timeTaken=max(newGrid[ni][nj],timeTaken)
#             grid[ni][nj]=3;
#             queue.append([ni,nj])
#     newGrid[start[0]][start[1]]=-1
#     return [newGrid,grid,timeTaken]
    
# def bfsthree(gridT,newgridT, i, j):
#     timeTaken=0
#     logging.info("i,j : {}".format([i,j]))
#     for x in range(i):
#         for y in range(j):
#             logging.info("x,y : {}".format([x,y]))
#             if gridT[x][y]==3:
#                 start = [x,y];
#                 newgridT[x][y]=0
#                 break
#     logging.info("start {}".format(start))
#     logging.info("gridT {}".format(gridT))
#     logging.info("newgridT {}".format(newgridT))
#     queue = [start]
#     while queue:
#       v = queue.pop(0)
#       curi = v[0]
#       curj = v[1]
#       for k in range(8):
#         ni = curi+ymov[k]
#         nj = curj+xmov[k]
#         if (ni>=0 and ni<i and nj>=0 and nj<j):
#           if(gridT[ni][nj]==1):
#             newgridT[ni][nj]=newgridT[curi][curj]+1;
#             timeTaken=max(newgridT[ni][nj],timeTaken)
#             gridT[ni][nj]=3;
#             queue.append([ni,nj])
#     newgridT[start[0]][start[1]]=-1
#     return [gridT,timeTaken]    
            
# def bfsfour(gridF, i, j):
#     enerTaken=0
#     logging.info("i,j : {}".format([i,j]))
#     for x in range(i):
#         for y in range(j):
#             logging.info("x,y : {}".format([x,y]))
#             if gridF[x][y]==3:
#                 start = [x,y];
#                 #newgridF[x][y]=0
#                 break
#     logging.info("start {}".format(start))
#     logging.info("gridF {}".format(gridF))
#     #logging.info("newgridF {}".format(newgridF))
#     start.insert(0,0)
#     heap=[]
#     heapq.heappush(heap,(start,0))
#     cntr = 0
#     while heap:
#       cntr = cntr+1
#       v = heapq.heappop(heap)
#       logging.info("v is {}".format(v))
#       energy = v[0][0]
#       curi = v[0][1]
#       curj = v[0][2]
#       for k in range(4):
#         ni = curi+ymov[k]
#         nj = curj+xmov[k]
#         if (ni>=0 and ni<i and nj>=0 and nj<j):
#           if(gridF[ni][nj]==1):
#             enerTaken=max(enerTaken,energy)
#             gridF[ni][nj]=3;
#             curcnt = copy.deepcopy(cntr)
#             nel = [energy,ni,nj]
#             heapq.heappush(heap,(nel, curcnt))
#           elif(gridF[ni][nj]!=3):
#             gridF[ni][nj]=3;
#             curcnt = copy.deepcopy(cntr)
#             nel = [energy+1,ni,nj]
#             heapq.heappush(heap,(nel,curcnt))

    
#     return enerTaken 

# @app.route('/parasite', methods=['POST'])
# def para():
#     ret =[]
#     data = request.get_json()
#     logging.info("data sent for evaluation {}".format(data))
#     for dt in data:
#       room = dt.get("room")
#       grid = dt.get("grid")
#       i = len(grid)
#       j = len(grid[0])
#       indiv = dt.get("interestedIndividuals")
#       newGrid = [[-1 for x in range(j)] for y in range (i)]

#       gridT = copy.deepcopy(grid)
#       newgridT = [[-1 for x in range(j)] for y in range (i)]

#       gridF = copy.deepcopy(grid)
#       #newgridF = [[-1 for x in range(j)] for y in range (i)]

#       newL = bfs(grid,newGrid, i, j)
#       newGrido = newL[0]
#       infectedGrid = newL[1]
#       tt = newL[2]

#       pOne={}
#       for k in indiv:
#         idx = k.find(',')
#         ni = int(k[:idx])
#         nj = int(k[idx+1:])
#         pOne[k]=newGrido[ni][nj]
      

#       for x in range (i):
#         for y in range (j):
#           if infectedGrid[x][y]==1:
#             tt = -1
#             break

#       ThrL = bfsthree(gridT,newgridT,i,j)
#       infectedG = ThrL[0]
#       ttt = ThrL[1]
#       for x in range (i):
#         for y in range (j):
#           if infectedG[x][y]==1:
#             ttt = -1
#             break

#       tttt = bfsfour(gridF,i,j)
#       ret.append({"room": room, "p1": pOne, "p2": tt, "p3": ttt, "p4": tttt})
#       logging.info("My result :{}".format(ret))
#     return json.dumps(ret)
