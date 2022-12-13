import requests
from getpass import getpass

def rendertable(a1, a2, a3, a4, a5, a6, a7, a8, b1, b2, b3, b4, b5, b6, b7, b8, c1, c2, c3, c4, c5, c6, c7, c8, d1, d2, d3, d4, d5, d6, d7, d8, e1, e2, e3, e4, e5, e6, e7, e8, f1, f2, f3, f4, f5, f6, f7, f8, g1, g2, g3, g4, g5, g6, g7, g8, h1, h2, h3, h4, h5, h6, h7, h8):
  pieces = ["♔","♚", "♕", "♛", "♖", "♜", "♗", "♝", "♘", "♞", "♙", "♟"]
  
  for i in range(64):
    

server = https://example.com/
_goodlogin = False
while _goodlogin == False:
  username = input("Username: ")
  password = getpass("Password: ")
  parameters = {'username': username, 'password': password}
  url = server + "login.php"
  sessionid = requests.get(server, , params=payload)
  if sessionid.status_code == requests.codes.ok:
    sessionid = int(sessionid)
    if sessionid == 0:
      print("Wrong email or password")
    elif seesionid == 1:
      print("Undefined error")
    else:
      _goodlogin = True
  else:
    print("Server error. (code" + sessionid.status_code + ")")
while _playing:
  print("1. Join a match")
  print("2. Play with a friend")
  print("3. View stats")
  print("4. Quit the game")
  choice = input("What do you want to do ? ")
  if choice != "1" and choice != "2" and choice != "3" and choice != "4":
    # Do nothing lol
    choice = "bruh"
  elif choice == "1":
    # Join a match
  elif choice == "2":
    friend = input("What is your friend username ? ")
  elif choice == "3":
    # Fetch stats
  elif choice == "4":
    _playing = False
print("Bye!")
