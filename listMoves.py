numbers = '12345678'
alphabet = 'abcdefgh'
##Returns the piece located in a certain position
def whatPiece(p, cb):
  return cb[numbers.index(p[1])][alphabet.index(p[0])]
##Lists all possible moves of a piece given its position
def listMoves(p1,player,log,cb,control):
  moves = []
  typePiece = whatPiece(p1,cb)[1]
##These variables define how each player moves
  if player == 'w':
    unit = 1
    opponent = 'b'
  elif player == 'b':
    unit = -1
    opponent = 'w'
  k = (9+unit)%9
  side = ['','L','R']
##COMPLEX (PAWN)
  if typePiece == 'P':
    numbersIndex = numbers.index(p1[1])+unit
    alphabetIndexR = alphabet.index(p1[0])+unit
    alphabetIndexL = alphabet.index(p1[0])-unit
    if numbersIndex in range(0,8):
      if whatPiece(p1[0] + numbers[numbersIndex],cb) == "  " and control == False:
        moves.append(p1[0] + numbers[numbersIndex])
      if alphabetIndexR in range(0,8):
        if whatPiece(alphabet[alphabetIndexR] + numbers[numbersIndex],cb)[0]== opponent:
          moves.append(alphabet[alphabetIndexR] + numbers[numbersIndex])
      if alphabetIndexL in range(0,8):
        if whatPiece(alphabet[alphabetIndexL] + numbers[numbersIndex],cb)[0]== opponent:
          moves.append(alphabet[alphabetIndexL] + numbers[numbersIndex])
    if p1[1] == str(k+unit) and control == False:
      moves.append(p1[0] + numbers[k+3*unit-1])
##L-SHAPE (KNIGHT)
  if typePiece == 'N':
    oldmoves = [
    (str(alphabet.index(p1[0])-2),str(numbers.index(p1[1])+1)),
    (str(alphabet.index(p1[0])-2),str(numbers.index(p1[1])-1)),
    (str(alphabet.index(p1[0])-1),str(numbers.index(p1[1])+2)),
    (str(alphabet.index(p1[0])-1),str(numbers.index(p1[1])-2)),
    (str(alphabet.index(p1[0])+1),str(numbers.index(p1[1])+2)),
    (str(alphabet.index(p1[0])+1),str(numbers.index(p1[1])-2)),
    (str(alphabet.index(p1[0])+2),str(numbers.index(p1[1])+1)),
    (str(alphabet.index(p1[0])+2),str(numbers.index(p1[1])-1))
    ]
    for square in oldmoves:
      letter = int(square[0])
      number = int(square[1])
      if letter in range(0,8) and number in range(0,8):
        position = alphabet[letter] + numbers[number]
        if whatPiece(position,cb)[0] != player:
          moves.append(position)
        elif whatPiece(position,cb)[0] == player and control == True:
          moves.append(position)
  
          
##HORIZONTAL AND VERTICAL (ROOK AND QUEEN)
  if typePiece == 'R' or typePiece == 'Q':
    for n in range(numbers.index(p1[1])+unit,8-(k-unit),unit):
      if whatPiece(p1[0]+numbers[n],cb)[0] == ' ':
        moves.append(p1[0]+numbers[n])
      elif whatPiece(p1[0]+numbers[n],cb)[0] == player and control == True:
        moves.append(p1[0]+numbers[n])
        break
      elif whatPiece(p1[0]+numbers[n],cb)[0] == opponent:
        moves.append(p1[0]+numbers[n])
        break
      else:
        break
    for s in range(numbers.index(p1[1])-unit,(k-unit)-1,-unit):
      if whatPiece(p1[0]+numbers[s],cb)[0] == ' ':
        moves.append(p1[0]+numbers[s])
      elif whatPiece(p1[0]+numbers[s],cb)[0] == player and control == True:
        moves.append(p1[0]+numbers[s])
        break
      elif whatPiece(p1[0]+numbers[s],cb)[0] == opponent:
        moves.append(p1[0]+numbers[s])
        break
      else:
        break
    for e in range(alphabet.index(p1[0])+unit,8-(k-unit),unit):
      if whatPiece(alphabet[e]+p1[1],cb)[0] == ' ':
        moves.append(alphabet[e]+p1[1])
      elif whatPiece(alphabet[e]+p1[1],cb)[0] == player and control == True:
        moves.append(alphabet[e]+p1[1])
        break
      elif whatPiece(alphabet[e]+p1[1],cb)[0] == opponent:
        moves.append(alphabet[e]+p1[1])
        break
      else:
        break
    for w in range(alphabet.index(p1[0])-unit,(k-unit)-1,-unit):
      if whatPiece(alphabet[w]+p1[1],cb)[0] == ' ':
        moves.append(alphabet[w]+p1[1])
      elif whatPiece(alphabet[w]+p1[1],cb)[0] == player and control == True:
        moves.append(alphabet[w]+p1[1])
        break
      elif whatPiece(alphabet[w]+p1[1],cb)[0] == opponent:
        moves.append(alphabet[w]+p1[1])
        break
      else:
        break
##DIAGONAL (BISHOP AND QUEEN)
  if typePiece == 'B' or typePiece == 'Q':
    for ne in range(1,8):
      alphabetIndex = alphabet.index(p1[0])+ne*unit
      numbersIndex = numbers.index(p1[1])+ne*unit
      if alphabetIndex < 8 and alphabetIndex > -1 and numbersIndex < 8 and numbersIndex > -1:
        square = alphabet[alphabetIndex] + numbers[numbersIndex]
        if whatPiece(square,cb)[0] == ' ':
          moves.append(square)
        elif whatPiece(square,cb)[0] == player and control == True:
          moves.append(square)
          break
        elif whatPiece(square,cb)[0] == opponent:
          moves.append(square)
          break
        else:
          break
    for nw in range(1,8):
      alphabetIndex = alphabet.index(p1[0])-nw*unit
      numbersIndex = numbers.index(p1[1])-nw*unit
      if alphabetIndex < 8 and alphabetIndex > -1 and numbersIndex < 8 and numbersIndex > -1:
        square = alphabet[alphabetIndex] + numbers[numbersIndex]
        if whatPiece(square,cb)[0] == ' ':
          moves.append(square)
        elif whatPiece(square,cb)[0] == player and control == True:
          moves.append(square)
          break
        elif whatPiece(square,cb)[0] == opponent:
          moves.append(square)
          break
        else:
          break
    for se in range(1,8):
      alphabetIndex = alphabet.index(p1[0])+se*unit
      numbersIndex = numbers.index(p1[1])-se*unit
      if alphabetIndex < 8 and alphabetIndex > -1 and numbersIndex < 8 and numbersIndex > -1:
        square = alphabet[alphabetIndex] + numbers[numbersIndex]
        if whatPiece(square,cb)[0] == ' ':
          moves.append(square)
        elif whatPiece(square,cb)[0] == player and control == True:
          moves.append(square)
          break
        elif whatPiece(square,cb)[0] == opponent:
          moves.append(square)
          break
        else:
          break
    for sw in range(1,8):
      alphabetIndex = alphabet.index(p1[0])-sw*unit
      numbersIndex = numbers.index(p1[1])+sw*unit
      if alphabetIndex < 8 and alphabetIndex > -1 and numbersIndex < 8 and numbersIndex > -1:
        square = alphabet[alphabetIndex] + numbers[numbersIndex]
        if whatPiece(square,cb)[0] == ' ':
          moves.append(square)
        elif whatPiece(square,cb)[0] == player and control == True:
          moves.append(square)
          break
        elif whatPiece(square,cb)[0] == opponent:
          moves.append(square)
          break
        else:
          break
##KING        
  if typePiece == 'K':
    oldmoves = [
    (str(alphabet.index(p1[0])),str(numbers.index(p1[1])+1)),
    (str(alphabet.index(p1[0])),str(numbers.index(p1[1])-1)),
    (str(alphabet.index(p1[0])+1),str(numbers.index(p1[1])+1)),
    (str(alphabet.index(p1[0])+1),str(numbers.index(p1[1])-1)),
    (str(alphabet.index(p1[0])-1),str(numbers.index(p1[1])+1)),
    (str(alphabet.index(p1[0])-1),str(numbers.index(p1[1])-1)),
    (str(alphabet.index(p1[0])+1),str(numbers.index(p1[1]))),
    (str(alphabet.index(p1[0])-1),str(numbers.index(p1[1]))),
    ]
    for square in oldmoves:
      letter = int(square[0])
      number = int(square[1])
      if letter in range(0,8) and number in range(0,8):
        position = alphabet[letter] + numbers[number]
        if whatPiece(position,cb)[0] != player:
          moves.append(position)
        elif whatPiece(position,cb)[0] == player and control == True:
          moves.append(position)
##[SPECIAL] CASTLING
  if (typePiece == 'K' or typePiece == 'R') and control == False:
    k = str(k)
    if whatPiece('e'+k,cb) == player + 'K' and (whatPiece('a'+k,cb)==player+'R'):
      if whatPiece('b'+k,cb)== whatPiece('c'+k,cb)==whatPiece('d'+k,cb)=="  ":
        castle = True
        for script in log:
          if player+'K'+'e'+k in script or player+'R'+'a'+k in script:
            castle = False
        if castle == True:
          moves.append('castle'+side[unit])
    if whatPiece('e'+k,cb) == player + 'K' and (whatPiece('h'+k,cb)== player + 'R'):
      if whatPiece('f'+k,cb)== whatPiece('g'+k,cb)=="  ":
        castle = True
        for script in log:
          if player+'K'+'e'+k in script or player+'R'+'h'+k in script:
            castle = False
        if castle == True:
          moves.append('castle'+side[-unit])    
    if typePiece == 'R':
      count = 0
      for move in moves:
        if 'castle' in move:
          count += 1
        if count >= 2:
          if alphabet.index(p1[0])-4 < 0 and player == 'w':
            moves.remove('castleR')
          elif alphabet.index(p1[0])-4 > 0 and player == 'w':
            moves.remove('castleL')
          if alphabet.index(p1[0])-4 > 0 and player == 'b':
            moves.remove('castleR')
          elif alphabet.index(p1[0])-4 < 0 and player == 'b':
            moves.remove('castleL')
  return moves
