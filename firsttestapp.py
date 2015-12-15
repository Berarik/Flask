from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "Warning:Incorrect way.Correct way :http://localhost:5000/hello/Student"

@app.route("/hello/Student")
def hello():
    return "Student"

if __name__ == "__main__":
    app.run()
