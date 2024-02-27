from wtforms import Form, StringField, EmailField, IntegerField
# Aquí de los validadores importamos el dato obligatorio y el email
from wtforms import validators#, DataRequired, Email}

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
    
class UserForm2(Form):
    id=IntegerField('id',[
        validators.number_range(min=1, max=20, message='valor no valido')
    ])   
    nombre = StringField('nombre', [
        validators.DataRequired(message='El campo es requerido'),
        validators.Length(min=4, max=10, message='Ingresa un nombre válido')
    ])
    apaterno = StringField('apaterno', [
        validators.DataRequired(message='El campo es requerido'),
        validators.Length(min=4, max=30, message='Ingresa un apellido válido')
    ])   
    email = StringField('email', [
        validators.DataRequired(message='El campo es requerido'),
        validators.Email(message='Ingresa un email válido')
    ])
