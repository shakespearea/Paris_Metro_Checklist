from flask import Flask,render_template, request
from service_manager import MetroService

app = Flask(__name__)
metro = MetroService()

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        metro.toggle_visited(request.form['station'])
    return render_template("index.html", stations=metro.get_lines(), visited=metro.visited_States)

if __name__ == "__main__":
    app.run(debug=True)