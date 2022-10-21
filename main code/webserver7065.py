from http.server import HTTPServer, CGIHTTPRequestHandler

class handler(CGIHTTPRequestHandler):
    cgi_directories = ["/cgi-bin"]



print("webserver running")
HTTPServer(("",7065),handler)
HTTPServer(("",7065),handler).serve_forever()
