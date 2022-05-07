# Import libraries
import http.server
import socketserver
import colorama
  
# Defining PORT number
PORT = 8080
  
# Creating handle
Handler = http.server.SimpleHTTPRequestHandler
  
# Creating TCPServer
http = socketserver.TCPServer(("", PORT), Handler)
  
# Getting logs
print(f"{colorama.Fore.CYAN}LocaL server {colorama.Fore.GREEN}OPENED{colorama.Fore.CYAN} and bound to the port: {PORT}")
http.serve_forever()