# -*-encoding=utf-8 -*-
import flask
html_txt="""
<!DOCTYPE html>
<html>
    <body>
       <h2>收到GET请求</h2>
       <a href='/get_info'>获取cookie信息</a>
    </body>
</html>
"""
app=flask.Flask('__name__')

@app.route('/set_info/<name>')
def set_cks(name):
    name=name if name else 'anonymous'
    resp=flask.make_response(html_txt)
    resp.set_cookie('name',name)
    return resp
@app.route('/get_info')
def get_cks():
    name=name in flask.request.cookies.get('name')
    return '获取的Cookies的信息是'+name
if __name__=='__main__':
    app.run()
