from flask import Flask,render_template,request
from decn import decrypt_file
app=Flask(__name__,template_folder='template')
from aesn import encrypt_file
@app.errorhandler(404)
def page_not_found(error):
    return render_template('main.html'), 404
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/home2') 
def home2():
    return render_template('main.html')
@app.route('/success', methods=['GET', 'POST']) 
def success():
    name=request.form.get('name')
    print(encrypt_file(name,'0101010101010101',None,16))
    return render_template("main.html"  ,name= name)
@app.route('/down', methods=['GET', 'POST']) 
def down():
    name1=request.form.get('dname')
    print(decrypt_file('0101010101010101',name1,None,16))
    return render_template("main.html"  ,name= name1)
if __name__ == '__main__':
    app.run(debug = True)