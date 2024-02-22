from wtforms import Form, StringField, EmailField, IntegerField
# Aquí de los validadores importamos el dato obligatorio y el email
from wtforms import validators#, DataRequired, Email

class UserForm(Form):
    nombre = StringField('nombre',[
        validators.DataRequired(message = 'El campo es requerido'),
        validators.length(min = 4, max = 10, message = 'Ingresa un nombre valido')
    ])
    email = EmailField('email', [
        validators.Email(message = 'Ingresa un correo valido')
    ])
    aPaterno = StringField('aPaterno',[
        validators.DataRequired(message = 'El campo es requerido'),
        validators.length(min = 4, max = 10, message = 'Ingresa un apellido paterno valido')
    ])
    aMaterno = StringField('aMaterno',[
        validators.DataRequired(message = 'El campo es requerido'),
        validators.length(min = 4, max = 10, message = 'Ingresa un apellido materno valido')
    ])
    edad = IntegerField('edad',[
        validators.DataRequired(message = 'El campo es requerido'),
        validators.number_range(message = 'Ingresa una edad valida')
    ])
