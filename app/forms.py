from flask_wtf import FlaskForm
from wtforms import IntegerField, FloatField, StringField
from wtforms.validators import DataRequired


class gen_dist_form(FlaskForm):
    x1 = IntegerField('x1:', validators=[DataRequired()])
    x2 = IntegerField('x2:', validators=[DataRequired()])
    y1 = IntegerField('y1:', validators=[DataRequired()])
    y2 = IntegerField('y2:', validators=[DataRequired()])


class gen_email_form(FlaskForm):
    email_input = StringField('email_input:', validators=[DataRequired()])


class gen_bmi_form(FlaskForm):
    f = IntegerField('Feet:', validators=[DataRequired()])
    i = IntegerField('Inches:', validators=[DataRequired()])
    p = IntegerField('Pounds:', validators=[DataRequired()])


class gen_retire_form(FlaskForm):
    age = IntegerField('Current age:', validators=[DataRequired()])
    salary = FloatField('Annual salary:', validators=[DataRequired()])
    percent = FloatField('Percent saved:', validators=[DataRequired()])
    goal = FloatField('Savings goal:', validators=[DataRequired()])


class gen_tip_form(FlaskForm):
    tip = FloatField('Tip Amount:', validators=[DataRequired()])
    guest = IntegerField('Number of Guest:', validators=[DataRequired()])
