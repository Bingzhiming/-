from flask_wtf import FlaskForm
from wtforms.validators import DataRequired,Length,Email
from wtforms import StringField,SubmitField,SelectField,IntegerField,FloatField

class AddTeacherForm(FlaskForm):
    name = StringField(label="姓名",validators=[DataRequired(message="姓名必须填写"),Length(1,32,message="长度必须是1-32个字符")])
    email = StringField(label="邮箱", validators=[DataRequired(message="邮箱必须填写"), Length(1, 64, message="长度必须是1-64个字符"),Email(message="必须是邮箱格式")])
    sex = SelectField(label="性别",coerce=int,choices=[(1,"男"),(2,"女")],default=(1,"男"))
    submit = SubmitField(label="提交")

class AddStudentForm(FlaskForm):
    name = StringField(label="姓名",validators=[DataRequired(message="姓名必须填写"),Length(1,32,message="长度必须是1-32个字符")])
    email = StringField(label="邮箱", validators=[DataRequired(message="邮箱必须填写"), Length(1, 64, message="长度必须是1-64个字符"),Email(message="必须是邮箱格式")])
    sex = SelectField(label="性别",coerce=int,choices=[(1,"男"),(2,"女")],default=(1,"男"))
    teacher = SelectField(label='老师',coerce=int)
    submit = SubmitField(label="提交")

class AddCourseForm(FlaskForm):
    name = StringField(label="课程名",validators=[DataRequired(message="课程名必须填写"),Length(1,32,message="长度必须是1-32个字符")])
    teacher = SelectField(label='任课老师',coerce=int)
    submit = SubmitField(label="提交")

class AddScoreForm(FlaskForm):
    course = SelectField(label="课程名",coerce=int)
    student = SelectField(label='学生',coerce=int)
    score = FloatField(label="分数",validators=[DataRequired(message="分数必须填写")])
    submit = SubmitField(label="提交")

class EditTeacherForm(FlaskForm):
    name = StringField(label="姓名",validators=[DataRequired(message="姓名必须填写"),Length(1,32,message="长度必须是1-32个字符")])
    email = StringField(label="邮箱", validators=[DataRequired(message="邮箱必须填写"), Length(1, 64, message="长度必须是1-64个字符"),Email(message="必须是邮箱格式")])
    sex = SelectField(label="性别",coerce=int,choices=[(1,"男"),(2,"女")],default=(1,"男"))
    submit = SubmitField(label="提交")

class EditStudentForm(FlaskForm):
    name = StringField(label="姓名",validators=[DataRequired(message="姓名必须填写"),Length(1,32,message="长度必须是1-32个字符")])
    email = StringField(label="邮箱", validators=[DataRequired(message="邮箱必须填写"), Length(1, 64, message="长度必须是1-64个字符"),Email(message="必须是邮箱格式")])
    sex = SelectField(label="性别",coerce=int,choices=[(1,"男"),(2,"女")],default=(1,"男"))
    teacher = SelectField(label='老师',coerce=int)
    submit = SubmitField(label="提交")

class EditCourseForm(FlaskForm):
    name = StringField(label="课程名称",validators=[DataRequired(message="课程名称必须填写"),
                                                Length(1,32,message="长度必须是1-32个字符")])
    teacher = SelectField(label="任课老师",coerce=int)
    submit = SubmitField(label="提交")

class EditScoreForm(FlaskForm):
    student = SelectField(label="学生姓名",coerce=int)
    course = SelectField(label="课程",coerce=int)
    score = FloatField(label="分数",default=0)
    submit = SubmitField(label="提交")