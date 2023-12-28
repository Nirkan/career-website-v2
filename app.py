from flask import Flask, render_template, jsonify
from database import load_jobs_from_db, load_job_from_db

app = Flask(__name__)

@app.route("/")
def Hello_NextStep():
  return render_template("home.html", 
                         jobs=jobs,
                        company_name="NextStep")


# Return as api endpoint(i.e. as json)
@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

@app.route("/job/<id>")
def show_job(id):
  job = show_job_from_id(job)
  if not job:
    return "Not Found", 404
  return render_template('jobpage.html', job=job)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
