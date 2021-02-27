from listMoves import listMoves
from listMoves import whatPiece
alphabet = 'abcdefgh'
numbers = '12345678'
def move(p1,p2,cb):
  cb[numbers.index(p2[1])][alphabet.index(p2[0])] = whatPiece(p1,cb)
  cb[numbers.index(p1[1])][alphabet.index(p1[0])] = "  "
  return cb
def castle(player,p1,p2,cb,k):
  k = str(k)
  if (p2[-1] == 'R' and player == 'b') or (p2[-1] == 'L' and player == 'w'):
    move('a'+k,'d'+k,cb)
    move('e'+k,'c'+k,cb)
  if (p2[-1] == 'R' and player == 'w') or (p2[-1] == 'L' and player == 'b'):
    move('e'+k,'g'+k,cb)
    move('h'+k,'f'+k,cb)
  return cb
def check(player,opponent,cb):
  for letter in alphabet:
    for number in numbers:
      position = letter + number
      if whatPiece(position,cb)[0] == opponent:
        for square in listMoves(position,opponent,[],cb,True):
          if whatPiece(square,cb) == (player+'K'):
            return True
  return False
def checkmate(player,opponent,cb):
  for letter in alphabet:
    for number in numbers:
      position = letter + number
      if whatPiece(position,cb)[0] == player:
        moves = listMoves(position,player,[],cb,True)
        possibleMoves = []
        for final in moves:
          if checkValid(position,final,player,opponent,cb) == True:
              return False
  return True
##Check if move is valid
def checkValid(p1,p2,player,opponent,cb):
  kValues = {'w':1,'b':8}
  k = kValues[player]
  piece = whatPiece(p1,cb)
  newcb = [row[:] for row in cb]
  if p2[:6] == 'castle':
    castle(player,p1,p2,newcb,k)
  else:
    move(p1,p2,newcb)
  if check(player,opponent,newcb) == False:
    return True
  return False
