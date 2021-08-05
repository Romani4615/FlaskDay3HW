from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.fields.simple import TextAreaField
from wtforms.validators import DataRequired, EqualTo, Email


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_pass = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField()
    
class CreatePostForm(FlaskForm):
    title=StringField('Title', validators=[DataRequired()])
    body=TextAreaField('Title', validators=[DataRequired()])
    submit = SubmitField()


class Comments(FlaskForm):
    comment = TextAreaField('Username', "id", 'body', 'date_created', 'user_id' )
    submit = SubmitField
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired()])
    submit = SubmitField()
