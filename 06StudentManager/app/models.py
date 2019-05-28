from app import db

class Teacher(db.Model):
    __tablename__ = "teachers"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64))
    email = db.Column(db.String(64))
    sex = db.Column(db.Boolean,default=True)

    courses = db.relationship("Course",backref="teacher")
    students = db.relationship("Student",backref="teacher")

class Student(db.Model):
    __tablename__ = "students"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64))
    email = db.Column(db.String(64))
    sex = db.Column(db.Boolean,default=True)

    teacher_id = db.Column(db.Integer,db.ForeignKey("teachers.id"))

    scores = db.relationship("Score",backref="student")

class Course(db.Model):
    __tablename__ = "courses"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64))
    teacher_id = db.Column(db.Integer,db.ForeignKey("teachers.id"))

    scores = db.relationship("Score",backref="course")

class Score(db.Model):
    __tablename__ = "scores"
    id = db.Column(db.Integer,primary_key=True)
    course_id = db.Column(db.Integer,db.ForeignKey("courses.id"))
    student_id = db.Column(db.Integer,db.ForeignKey("students.id"))
    score = db.Column(db.Float,default=0)