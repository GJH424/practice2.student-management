from flask import Flask, render_template, jsonify, request
import pymysql

app = Flask(__name__)
db = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='ai_college_web', charset="utf8")
cursor = db.cursor()

@app.route("/", methods=["GET"])
def hello():
	return "Hello World"

@app.route("/page", methods=["GET"])
def mainPage():
    return render_template('index.html')

#GET API(db 불러오기)
@app.route("/practice2", methods=["GET"])
def get_info():
    cursor.execute("select * from practice2")
    students = cursor.fetchall()
    # print(students)
    # ((1, '홍길동', 20))
    info = []
    for s in students:
        info.append({
            'id':s[0],
            'name':s[1],
            'age':s[2]
        })
    return jsonify(info)

#POST API(학생 저장)
@app.route("/practice2", methods=["POST"])
def save_info():
    student_name = request.form['name']
    student_age = request.form['age']
    cursor.execute(f"insert into practice2 (name, age) values ('{student_name}', {student_age})")
    db.commit()
    return "POST API"

#PUT API(학생 수정)
@app.route("/practice2", methods=["PUT"])
def put_info():
    student_id = request.form['id']
    student_name = request.form['name']
    student_age = request.form['age']
    cursor.execute(f"update practice2 set name='{student_name}', age={student_age} where id = {student_id}")
    db.commit()
    return "PUT API"

#DELETE API(학생 삭제)
@app.route("/practice2", methods=["DELETE"])
def del_info():
    student_id = request.args.get('id')
    cursor.execute(f"delete from practice2 where id={student_id}")
    db.commit()
    return "DELETE API"

if __name__ == "__main__":
    app.run(debug=True)