###########################################################################################
## CLASS : CPSC-449-section-1
## ASSIGNMENT: 1 (HTTP Client and Server with FOAAS and PurgoMalum)
## GROUP: Section 01 (Wednesday) - Group 6
## STUDENTS INFORMATION FROM Group 6::
    # Nidhi Shah- 
    # Priyanka Kadam 
    # Robert Nguyen 

##########################################################################################
########### imporitng require modules #################################
from http.server import BaseHTTPRequestHandler
import redact
import socketserver
#########################################################################

#set the port value
PORT = 8000

####################################################################
#Created a requestHandler to handle a http request.
class requestHandler(BaseHTTPRequestHandler):
    """ The request will be hadled using GET """
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        # Getting data from a fooasConnection function of a redact.
        # self.path contains a request path.
        filterresponse = redact.fooasConnection(self.path)
        # Getting the message and subtitle from a redact
        message = filterresponse['message']
        subtitle = filterresponse['subtitle']

         #Created a app string for dynamic HTML to display result on a web which matches with the FOAAS.

        appString =(f'<!DOCTYPE html> <html> <head> <title>{message} {subtitle}</title>'
                    f'<meta charset="utf-8">'
                    f'<meta property="og:title" content="{message}{subtitle}">'
                    f'<meta property="og:description" content="{message}{subtitle}"> <meta name="twitter:card" content="summary" /> '
                    f'<meta name="twitter:site" content="@foaas" /> <meta name="twitter:title" content="FOAAS: Fuck Off As A Service" />'
                    f' <meta name="twitter:description" content="{message}{subtitle}" />  <meta name="viewport" content="width=device-width, initial-scale=1"> '
                    f'<link href="//netdna.bootstrapcdn.com/twitter-bootstrap/2.3.2/css/bootstrap-combined.min.css" rel="stylesheet"></head>'
                    f'<body style="margin-top:40px;"> <div class="container"> <div id="view-10"> <div class="hero-unit">'
                    f'<h1>{message}</h1>'
                    f'<p><em>{subtitle}</em></p> </div> </div>'
                    f'<p style="text-align: center"><a href="https://foaas.com/%22%3Efoaas.com">foaas.com</a></p> </div> </body> </html>' )

        #Giving a response as appstring to the client
        self.wfile.write(appString.encode())

#########################################################################
#Socketserver.TCPServer has a PORT, the request sent to the client a
with socketserver.TCPServer(("", PORT), requestHandler) as httpd:
    print("serving at port", PORT)
    #It will handle a request until the server gets shutdown.
    httpd.serve_forever()
     #It cleans up and closes the server.
    httpd.socket.close()
