from flask import Flask,render_template,jsonify

app = Flask(__name__)

JOBS=[
    {
        "id":1,
        "title":"Data Scientist",
        "location":"Pune India",
        "salary" :"$10000",
    }, 
    {
        "id":2,
        "title":"Front end dev",
        "location":"Pune India",
        "salary" :"$20000",
    },
    {
        "id":3,
        "title":"back end dev",
        "location":"Pune India",
        "salary" :"$2",
    },
]

@app.route('/')
def hello_world():
    return render_template('home.html',jobs=JOBS,company_name="Carrer")

@app.route('/api/jobs')
def list_jobs():
    return jsonify(JOBS)



if __name__ =="__main__":
   app.run(host='0.0.0.0',debug=True)