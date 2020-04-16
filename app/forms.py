from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Nombre del Usuario', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit =SubmitField('Enviar')

    def gitprueba(self):
        pass