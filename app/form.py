from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import InputRequired, Regexp, Length
from wtforms.widgets import TextArea
from flask_wtf.file import FileField, FileRequired, FileAllowed
from werkzeug.utils import secure_filename

class PropertyForm(FlaskForm):
    Title = StringField("Property Title", validators=[InputRequired(), Length(max=100,message=("Exceeded character count (100)"))])
    NumOfBed = StringField("No. of Rooms", validators=[InputRequired(), Regexp("^[0-9]+$",message=("Please only enter digits (0-9)"))])
    NumOfBath = StringField("No. of Bathrooms", validators=[InputRequired(),Regexp("^[0-9]+$",message=("Please only enter digits (0-9)"))])
    Location = StringField("Location",validators=[InputRequired(),Length(max=100,message=("Exceeded character count (100)"))])
    Price = StringField("Price", validators=[InputRequired(),Regexp("^[0-9]+$",message=("Please only enter digits (0-9)"))])
    Type = SelectField("Property Type", choices=[('House','House'),('Property','Property')], validators=[InputRequired()])
    Description = TextAreaField("Description", validators=[InputRequired(),Length(max=255,message=("Exceeded character count (100)"))])
    Photo = FileField(validators=[FileRequired(), FileAllowed(['jpg','png','jpeg'],'Images only!')])