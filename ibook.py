import codecs
from authorizationServer.auth import auth as authorization 
from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
   return codecs.open("Hello.html", 'r', "utf-8").read()

@application.route("/auth", methods=["POST"])
@application.route("/authorization",methods=["POST"])
def auth():
   return authorization()

if __name__ == "__main__":
   application.run()