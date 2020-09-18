from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, FileField
from wtforms.fields.html5 import DateField, EmailField, IntegerField
from wtforms.validators import data_required


class add_patient(FlaskForm):
    imag= FileField(label='Upload your image')
    fn=StringField('First name ', validators=[data_required()], render_kw={'placeholder':'First name'})
    ln=StringField('Last name ', render_kw={'placeholder': 'Last name'})
    dob=DateField('D.O.B ', format='%Y-%m-%d' , validators=[data_required()])
    gen=SelectField('Gender ', choices=[('none', 'Select'), ('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    add1= StringField('Address', render_kw={'placeholder' : 'House no./Street no.'})
    add2 = StringField('Address', render_kw={'placeholder': 'city'})
    add3= StringField('Address', render_kw={'placeholder' : 'State'})
    add4= StringField('Address', render_kw={'placeholder' : 'Pincode'})
    mob=IntegerField('Phone no', render_kw={'placeholder': 'XXXXXXXXXX'}, validators=[ data_required()])
    email=EmailField('Email(if any)', render_kw={'placeholder': 'xyz@admin.com'})
    # valid=validate_email(email=email)
    # email=valid.email
    submit=SubmitField('Submit')

class delete(FlaskForm):
    dlt = SubmitField(label='Delete')
