from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World! Update 1 today 7 april"

if __name__ == "__main__":
    application.run()
