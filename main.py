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
