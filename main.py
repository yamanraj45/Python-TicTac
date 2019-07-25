board = ["-","-","-",
         "-","-","-",
         "-","-","-"]



game_is_running = True
current_player = "X"
winner = None



def display_board():
  print(board[0] + "|" + board[1] + "|" + board[2])
  print(board[3] + "|" + board[4] + "|" + board[5])
  print(board[6] + "|" + board[7] + "|" + board[8])




def handle_turn(player):
  position = input("Enter the position from 1-9:  ")
  position = int(position) - 1
  board[position] = player
  display_board()


display_board()


def play_game():
  display_board

  while game_is_running:
    handle_turn(current_player)
    check_if_game_over()
    flip_player()
  if winner =="x" or winner == "O":
      print(winner+ " wom")
  elif winner==None:
      print("Game is draw")

def check_if_game_over():
  check_if_win()
  check_if_draw()

def check_if_win():
  global winner
  row_winner = check_row()
  column_winner = check_column()
  diagonal_winner = check_diagonal()

  if row_winner:
      winner = row_winner
  elif column_winner:
      winner = column_winner
  elif diagonal_winner:
    winner = diagonal_winner
  else:
      winner = None

def check_row():
    global game_is_running
    row1 = board[0]==board[1]==board[2] !="-"
    row2 = board[3]==board[4]==board[5] !="-"
    row3 = board[6]==board[7]==board[8] !="-"
    if row1 or row2 or row3:
        
        game_is_running = False
    if row1:
        return board[0]
    if row2:
        return board[3]
    if row3:
        return board[6]
    return

def check_column():
    global game_is_running
    column1 = board[0]==board[3]==board[6] !="-"
    column2 = board[1]==board[4]==board[7] !="-"
    column3 = board[2]==board[5]==board[8] !="-"
    if column1 or column2 or column3:
        game_is_running = False
    if column1:
        return board[0]
    elif column2:
        return board[1]
    elif column3:
        return board[2]
    
    return

def check_diagonal():
    global game_is_running
    diagonal1 = board[0]==board[4]==board[8] !="-"
    diagonal2 = board[6]==board[4]==board[2] !="-"
    if diagonal1 or diagonal2:
        game_is_running = False
    if diagonal1:
        return board[0]
    elif diagonal2:
        return board[2]
    return



def check_if_draw():
    if "-" not in board:
        game_is_running = False
    return



def flip_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return
    

play_game()

