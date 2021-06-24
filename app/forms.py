from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, HiddenField
from wtforms.fields.html5 import EmailField
from wtforms.validators import ValidationError, DataRequired, Email
from .models import User

class SignUpForm(FlaskForm):
    """ Create a form for creating a new user """

    # Create form fields for user inputs, hidden inputs, and a submission option
    name = StringField('Name', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    key = HiddenField(validators=[DataRequired()])
    submit = SubmitField('Submit')

    def validate_email(self, email):
        """ Ensure provided email not already in use """

        # Search database for any users with provided email
        found_user = User.query.filter_by(
            email = email.data
        ).first()

        # Raise validation error if any user found
        if found_user:
            raise ValidationError()