from flask import Flask , render_template , jsonify

app = Flask(__name__)
JOBS = [
    {
        'id' : 1,
        'title' : 'Data Analyst' ,
        'location': 'Kolkata , India',
        'Salary': 'Rs. 1,00,000'
    },
    {
        'id' : 2,
        'title' : 'Data scientist' ,
        'location': 'Bangalore , India',
        'Salary': 'Rs. 15,00,000'
    },
    {
        'id' : 3,
        'title' : 'ML Engineer' ,
        'location': 'Mumbai , India',
        'Salary': 'Rs. 16,00,000'
    },
    {
        'id' : 4,
        'title' : 'Frontend Engineer' ,
        'location': 'Delhi , India',
        'Salary': 'Rs. 1,00,000'
    }

]

@app.route("/")

def hellow_world():
    return render_template('home.html' , 
                           jobs = JOBS , comapany_name = 'Arko')

@app.route("/api/job")

def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(host = "0.0.0.0" , debug=True)
