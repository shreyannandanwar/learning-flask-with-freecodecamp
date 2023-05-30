from flask import Flask,render_template
from flask import jsonify

app = Flask(__name__)

id_data = [
  {
    'id': 1,
    'title': 'Info contact of part 1',
    'location': 'San Fansisco',
    'salary': '1,00,000'
  },
  {
    'id': 2,
    'title': 'Info contact of part 2',
    'location': 'Sans',
    'salary': '2,00,000'
  },  {
    'id': 3,
    'title': 'Info contact of part 3',
    'location': 'San Fansisco',
    'salary': '1,00,000'
  },]

@app.route("/")
def hello_world():
  return render_template("about.html", jobs = id_data)

@app.route("/jobs")
def list_job():
  return jsonify(id_data)

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)


