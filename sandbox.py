from listMoves import whatPiece
from listMoves import listMoves
from checkValid import check
from checkValid import move
from checkValid import checkValid

##Displaying chess board
cb = [
['  ', '  ', '  ', '  ', 'wK', '  ', '  ', 'wR'],
['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
['  ', '  ', '  ', '  ', 'bK', '  ', '  ', '  ']]
p1 = 'h1'
p2 = 'castleR'
moves = []
typePiece = whatPiece(p1,cb)[1]
player = 'w'
unit = 1
opponent = 'b'
k = (9+unit)%9
log =[]


k = str(k)
if (p2[-1] == 'R' and player == 'b') or (p2[-1] == 'L' and player == 'w'):
  move('a'+k,'d'+k,cb)
  move('e'+k,'c'+k,cb)
elif (p2[-1] == 'R' and player == 'w') or (p2[-1] == 'L' and player == 'b'):
  move('h'+k,'f'+k,cb)
  move('e'+k,'g'+k,cb)
for i in cb:
  print(i)
