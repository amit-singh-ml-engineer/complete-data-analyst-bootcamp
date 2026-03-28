### Building URL dynamically
### Variable rule
### Jinja2 template engine
'''
{{}} expression to print output in html
{%...%} conditional statement , for loop , while loop
{#...#} single line comment

'''
from flask import Flask,render_template,request,redirect,url_for
'''
it creates an instance of flask class,
which will be yor WSGI (Web Server Gateway Interface) Application

'''
##WSGI application
app=Flask(__name__)
@app.route("/")
def welcome():
    return "<html><h1>Welcome to the flask course</h1></html>"
@app.route("/index",methods=['GET'])
def index():
    return render_template('index.html')
@app.route("/about")
def about():
    return render_template('about.html')

@app.route('/submitt',methods=['GET','POST'])
def submitt():
    if request.method=='POST':
        name=request.form['name']
        return f'Hello {name}!'
    return render_template('form.html')
## Variable rule
#@app.route('/succes/<score>')
#def succes(score):
    #return "You got the marks " + score
#@app.route('/succes/<int:score>')
#def succes(score):
    #return "You got the marks "+ str(score)
@app.route('/succes/<int:score>')
def succes(score):
    res=""
    if score>=50:
        res="PASS"
    else:
        res="FAIL"
    return render_template('result.html',results=res)

@app.route('/succesres/<int:score>')
def succesres(score):
    res=""
    if score>=50:
        res="PASS"
    else:
        res="FAIL"
    exp={'Score':score,'res':res}
    return render_template('result1.html',results=exp)

@app.route("/succesif/<int:score>")
def succesif(score):

    return render_template('result.html',results=score)
@app.route('/fail/<int:score>')
def fail(score):

    return render_template('result.html',results=score)

@app.route("/submit",methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        data_science=float(request.form['datascience'])
        total_score=(science+maths+c+data_science)/4
    return redirect(url_for('succesres',score=total_score))

if __name__=="__main__":
    app.run(debug=True)
