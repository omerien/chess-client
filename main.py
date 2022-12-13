import requests
from getpass import getpass

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
