import webbrowser
import socket
print("your ip adress is {0}".format(socket.gethostbyname(socket.gethostname())))

url ="http://localhost:7065/login.html"
webbrowser.open_new_tab(url)#launches the homepage
import webserver7065 #runs the webserver


