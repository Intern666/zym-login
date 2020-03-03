from flask import Flask,render_template,request,flash,redirect,url_for,session
import pymysql

app = Flask(__name__)
app.secret_key="1234"


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route("/showLogin")
def showRegister():
    return render_template("login.html")

@app.route('/doUserLogin',methods=['GET','POST'])
def doUserLogin():
    if request.method == 'GET':
        email = request.args.get("email")
        pwd = request.args.get("upwd")

    else:
        email = request.form.get('email')
        pwd = request.form.get('upwd')
        session['email'] = email

    conn = pymysql.connect(
        host="localhost",
        port=3307,
        db="bbs",
        user="root",
        password="Zhwlf1998",
        charset="utf8"
    )

    cls = conn.cursor()

    sql = "select * from user where userEmail=%s and userPassword=%s"
    rows = cls.execute(sql, [email, pwd])

    conn.commit()

    conn.close()
    if rows > 0:
        return render_template("index.html")
    else:
        # 注册失败
        flash("用户名或密码错误")
        return render_template("login.html")

if __name__ == '__main__':
    app.run()
