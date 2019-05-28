from .models import Student,Teacher,Course,Score
from app import app,db
from flask import render_template,flash,redirect,url_for,request,abort
from .forms import AddTeacherForm,AddStudentForm,AddCourseForm,AddScoreForm,EditTeacherForm,EditStudentForm,EditCourseForm,EditScoreForm
from flask_mail import Mail,Message
from threading import Thread
from app import mail
@app.route('/edit_course',methods=["GET","POST"])
def edit_course():
    course_id = request.args.get("id")
    if course_id is None:
        abort(404)
    c = Course.query.filter_by(id=course_id).first()
    if c is None:
        abort(404)
    form = EditCourseForm()
    form.teacher.choices=[(t.id,t.name) for t in Teacher.query.all()]

    if form.validate_on_submit():
        c.name = form.name.data
        c.teacher_id = form.teacher.data
        db.session.add(c)
        db.session.commit()
        return redirect(url_for(".courses"))

    form.name.data = c.name
    form.teacher.data = c.teacher_id
    return render_template("edit_course.html",form=form,course_active="active")

@app.route('/delete_course')
def delete_course():
    course_id = request.args.get("id")
    if id is None:
        abort(404)
    c = Course.query.filter_by(id = course_id).first()
    if c is None:
        abort(404)
    db.session.delete(c)
    db.session.commit()
    return redirect(url_for(".courses"))

@app.route('/courses')
def courses():
    cc = Course.query.order_by(Course.id.desc()).all()
    return render_template('course.html',cc=cc,course_active="active")

@app.route('/add_course',methods=['GET','POST'])
def add_course():
    form = AddCourseForm()
    form.teacher.choices=[(t.id,t.name) for t in Teacher.query.all()]
    if form.validate_on_submit():
        c = Course()
        c.name=form.name.data
        c.teacher=form.teacher.data
        db.session.add(c)
        db.session.commit()

        return redirect(url_for('.courses'))

    return render_template('add_course.html',form=form,course_active="active")

@app.route('/edit_score',methods=["GET","POST"])
def edit_score():
    score_id = request.args.get("id")
    if score_id is None:
        abort(404)
    s = Score.query.filter_by(id=score_id).first()
    if s is None:
        abort(404)
    form = EditScoreForm()
    form.student.choices = [(s.id,s.name) for s in Student.query.all()]
    form.course.choices = [(c.id,c.name) for c in Course.query.all()]

    if form.validate_on_submit():
        s.score = form.score.data
        s.student_id = form.student.data
        s.course_id = form.course.data

        db.session.add(s)
        db.session.commit()
        return redirect(url_for(".scores"))

    form.score.data = s.score
    return render_template("edit_score.html",form=form,score_active="active")

@app.route('/delete_score')
def delete_score():
    score_id = request.args.get("id")
    if id is None:
        abort(404)
    s = Score.query.filter_by(id=score_id).first()
    if s is None:
        abort(404)
    db.session.delete(s)
    db.session.commit()
    return redirect(url_for('.scores'))

@app.route('/scores')
def scores():
    sc = Score.query.order_by(Score.id.desc()).all()
    return render_template('score.html',sc=sc,score_active="active")

@app.route('/add_score',methods=['GET','POST'])
def add_score():
    form=AddScoreForm()
    form.student.choices=[(s.id,s.name)for s in Student.query.all()]
    form.course.choices=[(c.id,c.name)for c in Course.query.all()]
    if form.validate_on_submit():
        s=Score()
        s.score = form.score.data
        s.course_id = form.course.data
        s.student_id=form.student.data
        print(s.score,s.student_id,s.course_id)
        db.session.add(s)
        db.session.commit()
        print("ok")
        return redirect(url_for('.scores'))

    return render_template('add_score.html',form=form,score_active="active")

@app.route('/edit_student',methods=["GET","POST"])
def edit_student():
    student_id=request.args.get("id")
    if student_id is None:
        abort(404)
    s=Student.query.filter_by(id=student_id).first()
    if s is None:
        abort(404)
    form =EditStudentForm()
    form.teacher.choices = [(t.id,t.name) for t in Teacher.query.all()]

    if form.validate_on_submit():
        s.name = form.name.data
        s.email = form.email.data
        s.teacher_id = form.teacher.data
        if form.sex.data == 1:
            s.sex = True
        else:
            s.sex = False
        db.session.add(s)
        db.session.commit()
        return redirect(url_for(".students"))
    form.teacher.data = s.teacher_id
    form.name.data =s.name
    if s.sex:
        form.sex.data=1
    else:
        form.sex.data=2
    form.email.data=s.email
    return render_template("edit_student.html",form=form,student_active="active")

@app.route('/delete_student')
def delete_student():
    student_id = request.args.get("id")
    if id is None:
        abort(404)
    s = Student.query.filter_by(id=student_id).first()
    if s is None:
        abort(404)
    db.session.delete(s)
    db.session.commit()
    return redirect(url_for(".students"))

@app.route('/students')
def students():
    ss = Student.query.order_by(Student.id.desc()).all()
    return render_template('student.html',ss=ss,student_active="active")

@app.route('/add_student',methods=['GET','POST'])
def add_student():
    form=AddStudentForm()
    form.teacher.choices=[(t.id,t.name)for t in Teacher.query.all()]
    if form.validate_on_submit():
        s=Student()
        s.name = form.name.data
        s.email = form.email.data
        s.teacher_id=form.teacher.data
        if form.sex.data == 1:
            s.sex=True
        else:
            s.sex = False
        db.session.add(s)
        db.session.commit()
        return redirect(url_for('.students'))

    return render_template('add_student.html',form=form,student_active="active")

@app.route('/edit_teacher',methods=["GET","POST"])
def edit_teacher():
    teacher_id = request.args.get("id")
    if teacher_id is None:
        abort(404)
    t = Teacher.query.filter_by(id=teacher_id).first()
    if t is None:
        abort(404)
    form = EditTeacherForm()

    if form.validate_on_submit():
        t.name = form.name.data
        t.email = form.email.data
        if form.sex.data == 1:
            t.sex = True
        else:
            t.sex = False
        db.session.add(t)
        db.session.commit()
        return redirect(url_for(".teachers"))

    form.name.data = t.name
    if t.sex:
        form.sex.data = 1
    else:
        form.sex.data = 2
    form.email.data = t.email
    return render_template("edit_teacher.html",form=form,teacher_active="active")

@app.route('/delete_teacher')
def delete_teacher():
    teacher_id = request.args.get("id")
    if id is None:
        abort(404)
    t = Teacher.query.filter_by(id=teacher_id).first()
    if t is None:
        abort(404)
    db.session.delete(t)
    db.session.commit()
    return redirect(url_for(".teachers"))

@app.route('/teachers')
def teachers():
    ts = Teacher.query.order_by(Teacher.id.desc()).all()
    return render_template('manager.html', ts=ts , teacher_active="active")

@app.route('/add_teacher', methods=['GET','POST'])
def add_teacher():
    form = AddTeacherForm()
    if form.validate_on_submit():
        t = Teacher()
        if form.sex.data == 1:
            t.sex = True
        else:
            t.sex = False
        t.name = form.name.data
        t.email = form.email.data
        db.session.add(t)
        db.session.commit()
        return redirect(url_for('.teachers'))
    return render_template('add_teacher.html',form=form,teacher_active="active")

mail = Mail(app)
def send_fun(app,msg):
    with app.app_context():
        mail.send(msg)

def send_mail(subject, sender, recvers, body, html) :
    msg = Message(subject, sender = sender, recipients = recvers)
    msg.body = body
    msg.html = html

    thread = Thread(target=send_fun, args=[app, msg])
    thread.start()

@app.route('/student_email')
def student_email():
    student_id = request.args.get("id")
    if id is None:
        abort(404)
    s = Student.query.get(student_id)
    if s is None:
        abort(404)
    sc= s.scores
    return render_template('student_score.html',scores=sc)
    html = render_template('student_score.html',scores=sc,sender='成绩')
    send_mail('学生成绩', '604363281@qq.com',
              ['s.email'],html)
    return 'ok'