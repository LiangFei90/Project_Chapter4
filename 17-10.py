# -*- encoding: UTF-8  -*-

from mongoengine import *
import flask


app=flask.Flask(__name__)
app.secret_key = '123456'
#
#为了解决下面这个错误！！！！！！
#The session is unavailable because no secret key was set.
#Set the secret_key on the application to something unique and secret.
#

#用ORM操作数据库
connect('test')
class User(Document):
    username=StringField()
    psw=StringField()


@app.route('/')
def index():
    if 'username' in flask.session:
        return 'Hello：'+flask.session['username']+' <p><a href="/logout">Logout</a></p>'
    else:
        return '<a href="/login">Login</a> <a href="/signup">Sigup</a>'

@app.route('/signup',methods=['GET','POST'])
def signup():
    if flask.request.method=='GET':
        return flask.render_template('signup.html')
    else:
        name='name' in flask.request.form and flask.request.form['name']
        password='password' in flask.request.form and flask.request.form['password']
        if name and password:
            res=User.objects(username=name).first()
            if res.username==name:
                return 'Username Had Logined'
            else:
                us=User(username=name,psw=password)
                us.save()
                flask.session['username']=name
                return flask.redirect(flask.url_for('index'))
        else:
            return flask.redirect(flask.url_for('signup'))
@app.route('/login',methods=['GET','POST'])
def login():
    if flask.request.method=='GET':
        return flask.render_template('login.html')
    else:
        name='name' in flask.request.form and flask.request.form['name']
        password='password' in flask.request.form and flask.request.form['password']
        if name and password:
            res=User.objects(username=name).first()
            if res.username and res.psw==password:
                flask.session['username']=name
                return flask.redirect(flask.url_for('index'))
            else:
                return 'Login Error'
        else:
            return 'Please input all args'
@app.route('/logout')
def logout():
    flask.session.pop('username',None)
    return flask.redirect(flask.url_for('index'))

if  __name__=='__main__':
    app.run()

