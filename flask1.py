from flask import Flask,render_template
app=Flask(__name__)
from scrapper import get_courses

@app.route('/')
def index():
    courses=get_courses(1)
    return render_template('index.html',courses=courses)

if __name__=="__main__":
    app.run(debug=True, port=5001)
