from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.fields.html5 import DateField, EmailField, IntegerField
from wtforms.validators import data_required, ValidationError, Email


class add_patient(FlaskForm):
    fn=StringField('First name ', validators=[data_required()], render_kw={'placeholder':'First name'})
    ln=StringField('Last name ', render_kw={'placeholder': 'Last name'})
    dob=DateField('D.O.B ', format='%Y-%m-%d' , validators=[data_required()])
    gen=SelectField('Gender ', choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    add1= StringField('Address', render_kw={'placeholder' : 'House no./Street no.'})
    add2 = StringField('Address', render_kw={'placeholder': 'city'})
    add3= StringField('Address', render_kw={'placeholder' : 'State'})
    add4= StringField('Address', render_kw={'placeholder' : 'Pincode'})
    mob=IntegerField('Phone no', render_kw={'placeholder': 'XXXXXXXXXX'}, validators=[ data_required()])
    email=EmailField('Email(if any)', render_kw={'placeholder': 'xyz@admin.com'}, validators=[Email()])
    submit=SubmitField('Submit')

    def validate_mob(self, field):
        if len(str(field.data)) != 10:
            raise ValidationError("Please enter a 10 digit number.")

class delete(FlaskForm):
    dlt = SubmitField(label='Delete')
