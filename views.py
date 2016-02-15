from firebase import firebase
from flask import Flask
from .forms import FirePut

app = Flask(__name__)
firebase = firebase.FirebaseApplication('<path to your firebase app>', None)

@app.route('/')
def index():
    return "<h1>Hello, World!</h1>"

@app.router('/testing')
def testing():
    return "<h1>This is another testing page</h1>"

count = 0

@app.route('/api/put', methods=['GET', 'POST'])
def fireput():
    form = FirePut()
    global count
    count += 1
    putData = {'Title':form.title.data, 'Year':form.year.data, 'Rating':form.rating.data)
    firebase.put('/films','film' + str(count),putData)
    result = firebase.get('/films','film' + str(count))
    return '<h3>' + str(result) + '</h3>'

if __name__ == '__main__'
    app.run(debug=True)


