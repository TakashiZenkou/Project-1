from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import InputRequired, Regexp
from wtforms.widgets import TextArea
from flask_wtf.file import FileField, FileRequired, FileAllowed
from werkzeug.utils import secure_filename

class PropertyForm(FlaskForm):
    Title = StringField("Property Title", validators=[InputRequired()])
    NumOfBed = StringField("No. of Rooms", validators=[InputRequired()])
    NumOfBath = StringField("No. of Bathrooms", validators=[InputRequired()])
    Location = StringField("Location",validators=[InputRequired()])
    Price = StringField("Price", validators=[InputRequired()])
    Type = SelectField("Property Type", choices=[('House','House'),('Property','Property')], validators=[InputRequired()])
    Description = TextAreaField("Description", render_kw={"rows": 3, "cols": 4}, validators=[InputRequired()])
    Photo = FileField(validators=[FileRequired(), FileAllowed(['jpg','png'],'Images only!')])