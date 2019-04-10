from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class SearchForm(FlaskForm):
    searchQuery = StringField('Search Query', validators=[DataRequired()])
    submit = SubmitField('Search')