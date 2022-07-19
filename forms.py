from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from wtforms.fields.simple import SubmitField


class RegisterForm(Form):
    username = StringField('Username', [validators.DataRequired(), validators.Length(min=4, max=30)])
    email = StringField('Email', [validators.DataRequired(), validators.Length(min=5, max=50)])
    password = PasswordField("Password", [validators.DataRequired(), validators.EqualTo('confirm', message='Passwords do not match')])
    confirm = PasswordField('Confirm Password')
    submit = SubmitField("Log in")


class LoginForm(Form):
    username = StringField('Username', [validators.DataRequired(), validators.Length(min=4, max=30)])
    password = PasswordField("Password", [validators.DataRequired(), validators.Length(min=5, max=50)])
    submit = SubmitField("Log in")


class ContactUsForm(Form):
    message = TextAreaField('Message', [validators.DataRequired()])
    submit_info = SubmitField("Send")