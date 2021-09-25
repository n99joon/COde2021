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
sortedL = ['Annamarie Ahern', 'Gaston Glotfelty', 'Emily Eckles', 'Boris Batts', 'Armida Abarca', 'Danae Depuy', 'Anibal Abler', 'Hollis Hohlt', 'Chase Colone', 'Demetrius Dixion', 'Alayna Alberson', 'Vida Veal', 'Cecila Cribb', 'Chantel Corn', 'Lavonna Latson', 'Winfred Wilton', 'Judi Jacquez', 'Ozell Ostrem', 'Marcellus Mallow', 'Synthia Sylvestre', 'Corine Cottrill', 'Gary Ginsburg', 'Douglas Delima', 'Fletcher Felty', 'Judith Juntunen', 'Autumn Acuff', 'Brady Borda', 'Donald Drennen', 'Gilberto Gethers', 'Justa Jeffery', 'Quincy Quiroz', 'Dominque Deshon', 'Lindsey Lamb', 'Florine Faison', 'Livia Luse', 'Yu Yeates', 'Leslie Lubinsky', 'Annalee Angert', 'Lamont Lasch', 'Regenia Rathburn', 'Darren Dudley', 'Sonny Stratford', 'Alanna Ayoub', 'Lola Leyendecker', 'Duane Darrell', 'Stepanie Strang', 'Arron Ammerman', 'Rebekah Regnier', 'Milford Mcqueen', 'Fabian Fogel', 'Valerie Vera', 'Yuette Yurick', 'Kasandra Kroll', 'Napoleon Negrete', 'Derek Duclos', 'Trinity Trueblood', 'Pamula Parrinello', 'Lorita Loeffler', 'Justin Jack', 'Bernadine Brackin', 'Kali Krupp', 'Eva Epping', 'Thanh Tammaro', 'Alex Appleton', 'Shirly Sosebee', 'Bernie Bondy', 'Erwin Ewen', 'Olympia Oliphant']
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
