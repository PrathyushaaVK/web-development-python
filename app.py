from flask import Flask, render_template, jsonify

app = Flask(__name__)

jobsDict = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'San Francisco, USA',
    'mode': 'Hybrid',
    'salary': '$94,000'
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'San Francisco, USA',
    'mode': 'On-site',
    'salary': '$120,000'
  },
  {
    'id': 3,
    'title': 'Frontend Engineer',
    'location': 'San Antonio, USA',
    'mode': 'Remote',
    'salary': '$80,000'
  },
  {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'Los Angeles, USA',
    'mode': 'Hybrid',
    'salary': '$100,000'
  },
  {
    'id': 5,
    'title': 'Full Stack Engineer',
    'location': 'San Antonio, USA',
    'mode': 'On-site',  
    'salary': '$150,000'
  }
]

@app.route("/")
def home():
  return render_template("home.html", jobs=jobsDict, companyName="Shaw Inc.")

@app.route("/api/jobs")
def job_list():
  return jsonify(jobsDict)
  
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
