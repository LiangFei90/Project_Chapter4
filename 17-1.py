import flask
app=flask.Flask(__name__)
@app.route('/')
def hello():
    return 'Hello'
if __name__=='__main__':
    app.run()
