import codecs
from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
   return codecs.open("Hello.html", 'r', "utf-8").read()

if __name__ == "__main__":
   application.run()