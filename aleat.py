#!/usr/bin/python3

import webapp
import random

class ServURLAleat(webapp.webApp):
    def process(self, parsedRequest):
        rndi = str(random.randint(0, 1000000))

        return ("200 OK", "<html><head><h1>X-Serv-14.6-ServURLAleat</h1></head>"
                "<body><p>Hola. Dame otra <a href=" + rndi +
                ">https://"+rndi+"</a></p></body></html>")

if __name__ == "__main__":
    testWebApp = ServURLAleat("localhost", 1234)
