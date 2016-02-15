from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)

class FireGet(Form):
    name = StringField('name', validators=[DataRequired()])
    #age = StringField('age', validators=[DataRequired()])
    #height = StringField('height', validators=[DataRequired()])

class FirePut(Form):
    title = StringField('title', validators=[DataRequired()])
    year = StringField('year', validators=[DataRequired()])
    rating = StringField('rating', validators=[DataRequired()])
