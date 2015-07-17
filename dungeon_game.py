import random

CELLS = [(0,0), (0,1), (0,2),
	(1,0), (1,1), (1,2),
	(2,0), (2,1), (2,2)]

def get_locations():
  #monster = random location
  # door = random location
  # start = random location
  # if monster, door, or start are same, pick something else
  # return monster, door, start
  n = 0
  start_locs = ()
  cellscpy = CELLS[:]
  a_cell = ()
  while n < 3:
    a_cell = random.choice( cellscpy )
    cellscpy.remove( a_cell )
    start_locs.append( a_cell )
    n += 1
  return start_locs
  
def move_player( player, move ):
  # get player's current loc
  # if move is LEFT, y -1
  # if move is RIGHT y +1
  # if move is UP x - 1
  # if move is DOWN x + 1
  x, y = player
  if move in get_moves( player ):
    if move == 'LEFT':
      y = y - 1
    elif move == 'RIGHT':
      y = y + 1
    elif move == 'UP':
      x = x - 1
    elif move == 'DOWN':
      x = x + 1
    player = x, y
  else:
    print('Not a valid move.')
  return player


def get_moves( player ):
  MOVES = ['LEFT', 'RIGHT', 'UP', 'DOWN']
  # if player's y is 0, remove LEFT
  # if player's x is 0, remove UP
  # if player's y is 2, remove RIGHT
  # if player's x is 2, remove DOWN
  x, y = player
  if x == 0:
    MOVES.remove('UP')
  elif x == 2:
    MOVES.remove('DOWN')
  elif y == 0:
    MOVES.remove('LEFT')
  elif y == 2:
    MOVES.remove('RIGHT')
  return MOVES

monster, door, start = get_locations()
player = start

while True:
  print("Welcome to the dungeon!")
  print("You're currently in room {}".format( player ) ) # fill with player pos
  print("You can move {}". format( get_moves( player ) ) ) # fill with available moves
  print("Enter QUIT to quit")

  move = input("> ")
  move = move.upper()

  if move == 'QUIT':
    break
  else:
    move_player( player )
    if player == door:
      print('Winner!')
      break
    if player == monster:
      print('You were eaten :(')
      break
  # if it's a good move, change player pos
  # if a bad move, alert player but do not change pos
  # if new player position is the door they win
  # if new player position is the monster they lose
  # otherwise continue
