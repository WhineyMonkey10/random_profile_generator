def initalise_server():

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
    
    
    print(f"{colorama.Fore.CYAN}Local server {colorama.Fore.GREEN}OPENED{colorama.Fore.CYAN} and bound to the port:  {PORT}. Copy paste this link into your browser: http://localhost:{PORT}/src/localserver/website/{colorama.Fore.RESET}")
    http.serve_forever()
    input("Press enter to close the server.")