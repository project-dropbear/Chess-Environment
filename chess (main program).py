from listMoves import whatPiece
from listMoves import listMoves
from checkValid import castle
from checkValid import checkmate
from checkValid import check
from checkValid import move
from checkValid import checkValid
##Setting up chessboard
alphabet = 'abcdefgh'
numbers = '12345678'

cb = [
['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR'],
['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'wP'],
['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bP', 'bR']]

##cb = [
##['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
##['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
##['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
##['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
##['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
##['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
##['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
##['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ']]

player = 'w'
previousPlayer = 'Black'
turn = True
log = []
numMoves = 0

while True:
##Choosing player
  if player == 'w':
    opponent = 'b'
    name = 'White'
    unit = 1
  else:
    opponent = 'w'
    name = 'Black'
    unit = -1
  k = (9-unit)%9
##Interface
  print("==============================================\n"+"                "+name+"'s turn\n==============================================\n")
  for letter in alphabet[::unit]:
    print("    " + letter, end = "")
  print('\n')
  count = k
  for row in cb[::-unit]:
    print(str(count)+'  ['+"] [".join(row[::unit])+']  ' +str(count))
    print()
    count -= unit
  for letter in alphabet[::unit]:
      print("    " + letter, end = "")
  print()
##Checking check and checkmate
  if check(player,opponent,cb) == True:
    print('Check!')
  if checkmate(player,opponent,cb) == True:
    print('CHECKMATE!\n' +previousPlayer,'wins!')
    break
##Choosing initial position
  while True:
    p1 = input("\nFrom? ")
    if len(p1)<2 or p1[0] not in alphabet or p1[1] not in numbers:
      print("Invalid move. Try again!")
      continue
    elif whatPiece(p1,cb)[0] == opponent or whatPiece(p1,cb)[0] == " ":
      print("Not your piece")
      continue
  ##Listing possible moves
    moves = listMoves(p1,player,log,cb,False)
    possibleMoves = []
    for p2 in moves:
      if checkValid(p1,p2,player,opponent,cb)== True:
        possibleMoves.append(p2)
    if possibleMoves == []:
      print("No possible moves")
      continue
    else:
      print('[' +', '.join(sorted(possibleMoves))+']')
  ##Choosing final position
    p2 = input("To? ")
  ##Checking chosen move is valid
    if p2 in possibleMoves:
      log.append(str(numMoves+1)+(whatPiece(p1,cb)+p1+p2))
      if p2[:6] == 'castle':
        castle(player,p1,p2,cb,(9+unit)%9)
      else:
        move(p1,p2,cb)
  ##Promotion
        while whatPiece(p2,cb)[1] == 'P' and int(p2[1]) == k:
            promotion = input("Promote to? \n Queen | Rook | Bishop | Knight\n")
            if promotion.lower() in ('queen','rook','bishop','knight'):
              piece = {'queen':'Q','rook':'R','bishop':'B','knight':'N'}
              cb[numbers.index(p2[1])][alphabet.index(p2[0])] = player + piece[promotion.lower()]
              break
            else:
              print("Try Again...")
              continue
  ##Changing player
      if player == 'w':
        player = 'b'
      else:
        player = 'w'
      previousPlayer = name
      numMoves += 1
      break
  ##Printing errors excluding an invalid input
    else:
      print("Invalid move. Try again!")
      continue
