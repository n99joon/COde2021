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
sortedL =['Cecila Cribb', 'Isreal Isenhour', 'Rossana Rackers', 'Sharyl Shepler','Jannet Jacquemin','Dorathy Detweiler', 'Patrina Ptak', 'Ozell Ostrem', 'Bernie Bondy', 'Bernadine Brackin', 'Tanesha Telfer', 'Alysia Alejandro', 'Lucy Lippold', 'Olympia Oliphant', 'Lindsey Lamb', 'Dion Dionne', 'Mari Maus', 'Fletcher Felty', 'Teddy Twist',  'Cleveland Crofts', 'Quincy Quiroz', 'Carlo Chute', 'Kimberley Kincade', 'Douglas Delima','Lavonna Latson', 'Enriqueta Ealy', 'Gilberto Gethers', 'Clemencia Carcamo', 'Spring Sawin', 'Jewel Jaeger', 'Randy Rohlfing', 'Johanne Jeffress', 'Judith Juntunen', 'Lorita Loeffler', 'Joseph Jarosz','Lucas Lucht', 'Nelson Noss', 'Francisco Finchum', 'Yu Yeates', 'Robbyn Ryland', 'Livia Luse', 'Brady Borda', 'Leslie Lubinsky', 'Deidre Draves', 'Elbert Ehrman', 'Armida Abarca', 'Ernesto Eno', 'Annalee Angert', 'Donald Drennen', 'Orval Olsson', 'Anibal Abler', 'Demetrius Dixion','Dominque Deshon',  'Regenia Rathburn','Thanh Tammaro', 'Derek Duclos', 'Florine Faison', 'Britt Bisceglia', 'Terry Tietz', 'Lauretta Lippard', 'Hilario Heatherly', 'Leana Lynde',  'Burl Byas', 'Danae Depuy', 'Trudy Toone', 'Cortez Carranco', 'Lisha Levesque']
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
