from flask_wtf import FlaskForm
from wtforms import StringField
from flask_wtf.file import FileAllowed, FileField, FileRequired
from wtforms.validators import DataRequired

class UploadForm(FlaskForm):
    file = FileField('image', validators=[
    	DataRequired(),
    	FileAllowed(['jpg','png','Images Only!'])
    ])
    