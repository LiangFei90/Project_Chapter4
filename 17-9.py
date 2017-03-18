#  -*-  encoding:UTF-8   -*-
import  flask
import  os

UPLOAD_FOLDER = 'static/Uploads'
app=flask.Flask(__name__)

@app.route('/upload',methods=['GET','POST'])
def upload():
    if flask.request.method=='GET':
        return flask.render_template('upload.html')

    else:
        f=flask.request.files['file']
        fname=f.filename
        f.save(os.path.join(UPLOAD_FOLDER, fname))
        if f:
            f.save(f.filename)
            return f.filename
        else:
            return 'Error'
        
if __name__=='__main__':
    app.run(debug=True)
    
