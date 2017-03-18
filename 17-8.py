#  -*- encoding:UTF-8 -*-
import flask

app=flask.Flask(__name__)

@app.route('/test')
def test():
    return flask.render_template('index.html')

if __name__=='__main__':
    app.run()
