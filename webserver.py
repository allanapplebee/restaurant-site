from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

def main():
    try:
        port = 8080
        server = HTTPServer(('', port), webserverHandler)
        print ("Server is running on port {}").format(port)
        server.serve_forever()
        
    except KeyboardInterrupt:


if __name__ = '__main__':
    main()