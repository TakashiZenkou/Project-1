from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Email
from wtforms.widgets import TextArea
from flask_wtf.file import FileField, FileRequired, FileAllowed
from werkzeug.utils import secure_filename

class PropertyForm(FlaskForm):
    Title = StringField("Property Title", validators=[DataRequired()])
    NumOfBed = StringField("No. of Rooms", validators=[DataRequired()])
    NumOfBath = StringField("No. of Bathrooms", validators=[DataRequired()])
    Location = StringField("Location",validators=[DataRequired()])
    Price = StringField("Price", validators=[DataRequired()])
    Type = SelectField("Property Type", choices=[('House','House'),('Property','Property')], validators=[DataRequired()])
    Description = TextAreaField("Description", validators=[DataRequired()])
    Photo = FileField(validators=[FileRequired(), FileAllowed(['jpg','png'],'Images only!')])