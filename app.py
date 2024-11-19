import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error as mse ,r2_score as r

# Step 2: Create or load your dataset
sal=pd.read_csv("D:/vs ml/envi/app/Salary_dataset.csv")
x=sal[["YearsExperience"]]
y=sal["Salary"]

xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.2,random_state=42)

model=LinearRegression().fit(xtrain,ytrain)
ypred=model.predict(xtest)
#print(mse(ypred,ytest))
#print(r(ypred,ytest))
from flask import Flask , render_template , request

app=Flask(__name__)
@app.route("/")
def login():
    return render_template("login.html")
@app.route("/read")
def read():
    return render_template("redirect.html")

@app.route("/get",methods=['POST','GET'])
def get():
    age=None
    if request.method=='POST':
        age=request.form["experience"]
    elif request.method=="GET" :
        age=request.args.get("experience")
    if age:
        n=pd.DataFrame({"YearsExperience":[age]})
        ans=model.predict(n)
        yp=round(float(ans),0)
        return render_template("index.html",salary=yp)
    else:
        return "enter some value"
if __name__=='__main__':
    app.run(debug=True)
    

