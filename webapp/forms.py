from flask_wtf import Form
from wtforms import StringField, TextAreaField, SubmitField, DateTimeField, SelectField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo, URL, Email
from webapp.models import User



class SpeakerForm(Form):
    f_name = StringField('First Name:', validators=[DataRequired(), Length(max=255)])
    l_name = StringField('Last Name:', validators=[DataRequired(), Length(max=255)])
    image = StringField('Image:', validators=[DataRequired(), Length(max=500)])
    employer = StringField('Title:', validators=[DataRequired(), Length(max=255)])
    bio = TextAreaField('Bio:', validators=[DataRequired()])
    submit = SubmitField('Submit:')


class EventForm(Form):
    title = StringField('Event Title:', validators=[DataRequired(), Length(max=255)])
    time = StringField('When(YYYY-MM-DD HH:MM):', validators=[DataRequired()])
    speaker = SelectField('Speaker:', coerce=int)
    description = TextAreaField('Description:')
    submit = SubmitField('Submit')


class LoginForm(Form):
    username = StringField('Username:', validators=[DataRequired(), Length(max=255)])
    password = PasswordField('Password:', validators=[DataRequired()])
    submit = SubmitField('Submit')

    def validate(self):
        check_validate = super(LoginForm, self).validate()

        if not check_validate:
            return False


        #check username
        user = User.query.filter_by(username=self.username.data).first()
        if not user:
            self.username.errors.append('Invalid username')
            return False


        #check password
        if not user.check_password(self.password.data):
            self.password.errors.append('Invalid Password')
            return False

        return True


class RegisterForm(Form):
    name = StringField('Name:', validators=[DataRequired(), Length(max=255)])
    username = StringField('Username:', validators=[DataRequired(), Length(max=255)])
    password = PasswordField('Password:', validators=[DataRequired(), Length(min=8)])
    confirm = PasswordField('Confirm Password:', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Submit')

    def validate(self):
        check_validate = super(RegisterForm, self).validate()

        #if validators do not pass
        if not check_validate:
            return False

        user = User.query.filter_by(username=self.username.data).first()
        #check to see if user already exists
        if user:
            self.username.errors.append("User with that name already exists")
            return False

        return True

