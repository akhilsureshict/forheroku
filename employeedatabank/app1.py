from flask import Flask,render_template,request

app=Flask(__name__)

@app.route("/")
def Index():
    return render_template('home.html')

@app.route('/home/')
def home():
    return 'ss'
    #return render_template('home.html')

@app.route("/emp/")
def Employee():
    return render_template('employeedata.html')

    



if(__name__=='__main__'):
    app.run()