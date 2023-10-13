from flask import Flask
from Controllers.skills_controller import skills_controller

app = Flask(__name__)
app.register_blueprint(skills_controller)


@app.route("/")
def hello_world():
    return "Hello"


if __name__ == "__main__":
    app.run(debug=True)