from flask import Flask,render_template
from service_manager import MetroService

app = Flask(__name__)
metro = MetroService()

@app.route("/")
def index():
    stations = metro.get_all()
    return render_template("index.html", stations=metro.get_all())

if __name__ == "__main__":
    app.run(debug=True)