from flask import Flask, render_template_string, request

app = Flask(__name__)

JOBS = [
    {"id": 1, "title": "QA Engineer", "company": "Nokia", "location": "Wrocław", "type": "Full-time"},
    {"id": 2, "title": "Software Tester", "company": "Ryanair Labs", "location": "Wrocław", "type": "Internship"},
    {"id": 3, "title": "Test Automation Engineer", "company": "Siemens", "location": "Poznań", "type": "Full-time"},
    {"id": 4, "title": "QA Analyst", "company": "Fluke", "location": "Wrocław", "type": "Full-time"},
    {"id": 5, "title": "Junior QA Engineer", "company": "Rockwell Automation", "location": "Katowice", "type": "Internship"},
]

TEMPLATE = """
<!DOCTYPE html>
<html>
<head><title>QA Job Board</title></head>
<body>
    <h1 data-test="page-title">QA Job Board</h1>
    <form data-test="search-form" method="GET" action="/search">
        <input data-test="search-input" type="text" name="keyword" placeholder="Job title...">
        <input data-test="location-input" type="text" name="location" placeholder="Location...">
        <button data-test="search-button" type="submit">Search</button>
    </form>
    <div data-test="job-listings">
        {% for job in jobs %}
        <div data-test="job-card">
            <h3 data-test="job-title">{{ job.title }}</h3>
            <p data-test="job-company">{{ job.company }}</p>
            <p data-test="job-location">{{ job.location }}</p>
            <span data-test="job-type">{{ job.type }}</span>
            <a data-test="apply-button" href="/job/{{ job.id }}">View Details</a>
        </div>
        {% endfor %}
    </div>
    <p data-test="results-count">{{ jobs|length }} jobs found</p>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(TEMPLATE, jobs=JOBS)

@app.route("/search")
def search():
    keyword = request.args.get("keyword", "").lower()
    location = request.args.get("location", "").lower()
    results = [j for j in JOBS if
               (keyword in j["title"].lower() or not keyword) and
               (location in j["location"].lower() or not location)]
    return render_template_string(TEMPLATE, jobs=results)

@app.route("/job/<int:job_id>")
def job_detail(job_id):
    job = next((j for j in JOBS if j["id"] == job_id), None)
    if not job:
        return "Job not found", 404
    return f"<h1>{job['title']}</h1><p>{job['company']}</p><p>{job['location']}</p><a href='/'>Back</a>"

if __name__ == "__main__":
    app.run(debug=True, port=5000)