#  -*- encoging : UTF-8 -*-
import flask
html_txt='''
<!DOCTYPE html>
<html>
    <body>
        <h2>收到GET请求</h2>
        <form method='post'>
         <input type='text' name='name' placeholder='请输入你的姓名' />
         <input type='submit' value='发送POST请求'>
        </form>
    </body>
</html>
'''

app=flask.Flask(__name__)
@app.route('/hello',methods=['GET','POST'])
def hello():
    if  flask.request.method=='GET':
        return html_txt
    else:
        name='name' in flask.request.form and flask.request.form['name']
        if name:
            return 'You are '+name
        else:
            return 'You didn\'t input name'

if __name__=='__main__':
    app.run(debug=True)
    
           
