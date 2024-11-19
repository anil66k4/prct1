from flask import Flask, request ,render_template

app=Flask(__name__)
@app.route("/run")
def run():
      return render_template("index1.html")
@app.route("/test",methods=['GET','POST']) 
def test():
    result1=None
    if request.method=='POST':
      result1=request.form.get('a')
    elif request.method=='GET':
      result1=request.args.get('a')
          
    if result1:
      return render_template("index1.html", result=result1)
    else:
      return "enter value"
          
    
if __name__=="__main__":
      app.run(debug=True)