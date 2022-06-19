from flask import Flask, render_template, jsonify, request
import pymysql

app = Flask(__name__)
db = pymysql.connect(host='localhost', port=3306, user='root', passwd='1234', db='web_test', charset="utf8")
cursor = db.cursor()

@app.route("/page", methods=["GET"])
def hello():
    return render_template('index.html')

@app.route("/student_score", methods=["GET"])
def get_students_grade():
    sql = "select * from student_score"
    cursor.execute(sql)
    results = cursor.fetchall()
    db.commit()
    grades = []
    for result in results:
        grades.append({
            'name': result[1],
            'kor': result[2],
            'math': result[3],
            'eng': result[4]
        })
    return jsonify(grades)

@app.route("/student_score", methods=["POST"])
def save_grade():
    server_name = request.form["name"]
    server_kor = request.form["kor"]
    server_math = request.form["math"]
    server_eng = request.form["eng"]
    sql = "insert into student_score (name, kor, math, eng) values ('%s', %s, %s, %s)" % (server_name, server_kor, server_math, server_eng)
    cursor.execute(sql)
    db.commit()
    return "OK"

@app.route("/student_score", methods=["PUT"])
def update_grade():
    server_name = request.form["name"]
    server_kor = request.form["kor"]
    server_math = request.form["math"]
    server_eng = request.form["eng"]
    sql = "update student_score set kor = %s, math = %s , eng = %s where name = '%s'" % (server_kor, server_math, server_eng, server_name)
    cursor.execute(sql)
    db.commit()
    return "OK"

@app.route("/student_score", methods=["DELETE"])
def delete_grade():
    server_name = request.args.get("name")
    sql = "delete from student_score where name = '%s' " % server_name
    cursor.execute(sql)
    db.commit()
    return "OK"



if __name__ == "__main__":
    app.run(debug=True)
