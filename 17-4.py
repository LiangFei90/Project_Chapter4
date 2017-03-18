import flask
app=flask.Flask(__name__)

@app.route('/hello/<name>')
def hello(name):
    return  'Hello,'+name+'!'
if  __name__=='__main__':
    app.run()
    
