import requests
from getpass import getpass
import platform
import os

# Getting flags
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", help="Get da log !", action="store_true")
options = ArgumentParser.parse_args()
if options.v:
  verbosemode = True
  print("Verbose mode activated!")

version = "0" # Using a example ID; I'll put a real one once I code the server
server = https://example.com/ # Same

# Checking version (python 3.10 required)
version = platform.python_version_tuple()
if version[0] < 3:
  print("Update to python 3.10 or upwards.")
  exit()
if version[0] == 3 and version[1] < 10:
  print("Update to python 3.10 or upwards.")
  exit()
if verbosemode:
  print("Python version checked!")

print("It is advised to use an high quality monospace font that supports these characters :")
print("♔ ♚ ♕ ♛ ♖ ♜ ♗ ♝ ♘ ♞ ♙ ♟")
print("A compatibility mode isn't available yet.")
sleep(2)
  
def rendertable(a1, a2, a3, a4, a5, a6, a7, a8, b1, b2, b3, b4, b5, b6, b7, b8, c1, c2, c3, c4, c5, c6, c7, c8, d1, d2, d3, d4, d5, d6, d7, d8, e1, e2, e3, e4, e5, e6, e7, e8, f1, f2, f3, f4, f5, f6, f7, f8, g1, g2, g3, g4, g5, g6, g7, g8, h1, h2, h3, h4, h5, h6, h7, h8):
  pieces = ["♔","♚", "♕", "♛", "♖", "♜", "♗", "♝", "♘", "♞", "♙", "♟"]
  inputtable = [a1, a2, a3, a4, a5, a6, a7, a8, b1, b2, b3, b4, b5, b6, b7, b8, c1, c2, c3, c4, c5, c6, c7, c8, d1, d2, d3, d4, d5, d6, d7, d8, e1, e2, e3, e4, e5, e6, e7, e8, f1, f2, f3, f4, f5, f6, f7, f8, g1, g2, g3, g4, g5, g6, g7, g8, h1, h2, h3, h4, h5, h6, h7, h8]
  outputtable = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60", "61", "62", "63", "64" "65" "64"]
  for i in range(64):
    match inputtable[i]:
      case "wking":
        outputtable[i] = pieces[0]
      case "bking":
        outputtable[i] = pieces[1]
      case "wqueen":
        outputtable[i] = pieces[2]
      case "bqueen":
        outputtable[i] = pieces[3]
      case "wrook":
        outputtable[i] = pieces[4]
      case "brook":
        outputtable[i] = pieces[5]
      case "wbishop":
        outputtable[i] = pieces[6]
      case "bbishop":
        outputtable[i] = pieces[7]
      case "wknight":
        outputtable[i] = pieces[8]
      case "bknight":
        outputtable[i] = pieces[9]
      case "wpawn":
        outputtable[i] = pieces[10]
      case "bpawn":
        outputtable[i] = pieces[11]
      case " ":
        outputtable[i] = "_"
  print("   _______________")
  print("8 |" + outputtable[8] + "|" + outputtable[16] + "|" + outputtable[24] + "|" + outputtable[32] + "|" + outputtable[40] + "|" + outputtable[48] + "|" + outputtable[56] + "|" + outputtable[64] + "|") # Ascii art from https://www.asciiart.eu/sports-and-outdoors/chess
  print("7 |" + outputtable[7] + "|" + outputtable[15] + "|" + outputtable[23] + "|" + outputtable[31] + "|" + outputtable[39] + "|" + outputtable[47] + "|" + outputtable[55] + "|" + outputtable[63] + "|") # Author unknown
  print("6 |" + outputtable[6] + "|" + outputtable[14] + "|" + outputtable[22] + "|" + outputtable[30] + "|" + outputtable[38] + "|" + outputtable[46] + "|" + outputtable[54] + "|" + outputtable[62] + "|")
  print("5 |" + outputtable[5] + "|" + outputtable[13] + "|" + outputtable[21] + "|" + outputtable[29] + "|" + outputtable[37] + "|" + outputtable[45] + "|" + outputtable[53] + "|" + outputtable[61] + "|") # I use multiple print statements for better readability
  print("4 |" + outputtable[4] + "|" + outputtable[12] + "|" + outputtable[20] + "|" + outputtable[28] + "|" + outputtable[36] + "|" + outputtable[44] + "|" + outputtable[52] + "|" + outputtable[60] + "|")
  print("3 |" + outputtable[3] + "|" + outputtable[11] + "|" + outputtable[19] + "|" + outputtable[27] + "|" + outputtable[35] + "|" + outputtable[43] + "|" + outputtable[51] + "|" + outputtable[59] + "|")
  print("2 |" + outputtable[2] + "|" + outputtable[10] + "|" + outputtable[18] + "|" + outputtable[26] + "|" + outputtable[34] + "|" + outputtable[42] + "|" + outputtable[50] + "|" + outputtable[58] + "|")
  print("1 |" + outputtable[1] + "|" + outputtable[9] + "|" + outputtable[17] + "|" + outputtable[25] + "|" + outputtable[33] + "|" + outputtable[41] + "|" + outputtable[49] + "|" + outputtable[57] + "|")
  print("   a b c d e f g h") # That's the ugliest code I've ever written. But it works


_goodlogin = False
while _goodlogin == False:
  username = input("Username: ")
  password = getpass("Password: ")
  parameters = {'username': username, 'password': password}
  url = server + "login.php"
  sessionid = requests.get(url, params=parameters)
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

print("Checking version...")
url = server + "version"
currversion = requests.get(url)
if sessionid.status_code == requests.codes.ok:
  if currversion != version:
    print("Please update chess-client to the server version : " + currversion)
    exit()
  elif verbosemode:
    print("chess-client version is checked !")
else:
  print("The server has some configuration problems, please report this error to the owner.")
  sleep(2)


while _playing:
  print("1. Join a match")
  print("2. Play with a friend")
  print("3. View stats")
  print("4. Manage your friends")
  print("4. Quit the game")
  choice = input("What do you want to do ? ")
  os.system("cls")
  match choice:
    case "1":
      # Join a match
      url = server + "matchreq.php"
      parameters = {'sessionid': sessionid, 'type': "global"}
    case "2":
      _friend = True
      while _friend:
        friend = input("What is your friend username ? (Type \"list\" to see your friend list) ")
        if friend == "ls":
          url = server + "friendls.php"
          parameters = {'sessionid': sessionid}
          friendlist = requests.get(url, params=parameters)
          if sessionid.status_code == requests.codes.ok:
            # Treating the friend list
            if verbosemode:
              print("Friend list recieved data is" + friendlist)
            friendlistarray = friendlist.split(|)
            if friendlist == "":
              print("You have no friends! But don't worry, you can still do a global match and meet new ppl!")
              _nofriends = True
            else:
              for i in len(friendlistarray):
                if i % 10 == 0:
                  suffix = "st"
                elif (i - 1) % 10 == 0:
                  suffix = "nd"
                elif (i - 2) % 10 == 0:
                  suffix = "rd"
                else:
                  suffix = "th"
                friendnumber = str(i + 1)
                print(friendnumber + suffix + ": " + friendlistarray[i])
              _nofriends = False
          else:
            print("The server has some configuration problems, please report this error to the owner.")
            sleep(2)
      if _nofriends == False:
        url = server + "matchreq.php"
        parameters = {'sessionid': sessionid, 'type': "friend", 'friend' = friend}
        matchid = requests.get(url, params=parameters)
        _matchaccepted = False
        while _matchaccepted == False:
          url = server + "matchstatus.php"
          parameters = {'sessionid': sessionid, 'matchid': matchid, 'req': "ismatchaccepted"}
          matchstatus = requests.get(url, params=parameters)
          if sessionid.status_code == requests.codes.ok:
            if matchstatus == "ACK":
              _matchaccepted = True
            elif matchstatus == "NOP":
              print("Match refused!")
              break()
            elif matchstatus == "WAIT":
              # @ : "Bro, move your ass and come play some chess!"
              # & : "But it's 2AM..."
              # @ : "And?"
              # & : "sleep(thisnight)"
              sleep(2)
          else:
            print("The server has some configuration problems, please report this error to the owner.")
            break()
        if _matchaccepted == True:
          # Match started
    case "3":
      # Fetch stats
      print("1. ELO Leaderboard")
      print("2. Your stats")
      choice = input("What do you want to do ? ")
      url = server + stats.php
      match choice:
        case "1":
          parameters = {'type': "global"}
          
        case "2":
          parameters = {'type': "personal", 'sessionid': sessionid}
      
    case "4":
      print("1. See your friend list")
      print("2. Add a friend")
      print("3. Delete a friend")
    case "5":
      _playing = False
print("Bye!")
