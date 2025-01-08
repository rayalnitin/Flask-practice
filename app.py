from flask import Flask , render_template , jsonify

Jobs =[
    {
        'id': 1,
        'title':'Software Developer',
        'location':'Banglore , India',
        'salary':'Rs 12,00,000'
    },
    {
        'id': 2,
        'title':'Frontend engineer',
        'location':'Noida , India',
        'salary':'Rs 7,00,000'
    },
    {
        'id': 3,
        'title':'Backend Developer',
        'location':'Remote',
        'salary':'Rs 9,00,000'
    },
    {
        'id': 4,
        'title':'Data Scientist',
        'location':'New Delhi , India',
    },
]

app = Flask(__name__)  #object of the class Flask
@app.route("/")
def hw():
    return render_template('home.html' , jobs = Jobs)

@app.route("/jobs")
def listjobs():
    return jsonify(Jobs)

if __name__ == "__main__":
    app.run(host='0.0.0.0' , debug=True)
