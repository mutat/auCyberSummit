from flask_wtf import Form
from wtforms import StringField, TextAreaField, SubmitField, DateTimeField, SelectField
from wtforms.validators import DataRequired, Length


class SpeakerForm(Form):
    f_name = StringField('First Name:', validators=[DataRequired(), Length(max=255)])
    l_name = StringField('Last Name:', validators=[DataRequired(), Length(max=255)])
    image = StringField('Image:', validators=[DataRequired(), Length(max=500)])
    employer = StringField('Employer:', validators=[DataRequired(), Length(max=255)])
    bio = TextAreaField('Bio:', validators=[DataRequired()])
    submit = SubmitField('Submit:')

class EventForm(Form):
    title = StringField('Event Title:', validators=[DataRequired(), Length(max=255)])
    time = StringField('When:', validators=[DataRequired()])
    speaker = SelectField('Speaker:', coerce=int)
    description = TextAreaField('Description:')
    submit = SubmitField('Submit')

