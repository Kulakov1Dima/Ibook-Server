from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
   return "<h1>ibook server ready 19.10.22</h1>"

if __name__ == "__main__":
   application.run(host='0.0.0.0')