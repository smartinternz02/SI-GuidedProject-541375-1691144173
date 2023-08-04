from flask import Flask, render_template, request
import ibm_db

app = Flask(__name__)

conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=b1bc1829-6f45-4cd4-bef4-10cf081900bf.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=32304;PROTOCOL=TCPIP;USERNAME=xmt76987;PASSWORD=5g9oiV5ie93PDx3n;SECURITY=ssl;SSLSERVERCERTIFICATE=DigiCertGlobalRootCA.crt","","")
print(ibm_db.active(conn))
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/login",methods =["GET" , "POST"])
def login():
    if request.method == "POST" :
        uname = request.form['username']
        pword = request.form['password']
        print(uname, pword)
        sql= 'SELECT * FROM REGISTER_FDP WHERE USERNAME=? AND PASSWORD=?'
        stmt = ibm_db.prepare(conn, sql)
        ibm_db.bind_param(stmt, 1, uname)
        ibm_db.bind_param(stmt, 2, pword)
        ibm_db.execute(stmt)
        out= ibm_db.fetch_assoc(stmt)
        print(out)
        if out==False:
            msg= "Invalid Credentials, "
            return render_template("login.html", Login_message=msg)
        else:
            role = out['ROLL']
            if role ==0:
                return render_template("studentprofile.html")
            elif role ==1:
                return render_template("facultyprofile.html")
            elif role ==2:
                return render_template("profile.html")


    
    return render_template("login.html")
    
if __name__ == "__main__" : 
    app.run(debug=True)