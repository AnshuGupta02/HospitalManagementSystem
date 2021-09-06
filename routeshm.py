from apphm import app, db
from flask import render_template, flash, get_flashed_messages, redirect, url_for, request
import formhm
from datetime import datetime, date
from modelshm import Manage
#from email_validator import validate_email
import os

@app.context_processor  # to make available Permission class with all its constants to all the tamplates,
# to avoid add a template argumrnt in every render_template()
def inject_permissions():
    return dict(images=set(os.listdir("static//images")))

@app.route('/')
@app.route('/records')
def home():
    form = formhm.add_patient()
    dat = datetime.now().date()
    datas=Manage.query.all()
    return render_template('home.html', page='RECORDS', datas=datas, date=dat, form=form,
                           alert_type=request.args.get("alert_type"))


@app.route('/register', methods=['GET', 'POST'])
def add():
    alert_type=None
    form=formhm.add_patient()
    dat = datetime.now().date()
    if form.validate_on_submit():
        print(int((date.today() - form.dob.data).days))
        data=Manage(fn=form.fn.data, ln=form.ln.data,date=dat, dob=form.dob.data, age=int((date.today() -
                                                                                           form.dob.data).days/365.2425), gen=form.gen.data, add1= form.add1.data, add2= form.add2.data , add3= form.add3.data , add4= form.add4.data , mob=form.mob.data, email=form.email.data)
        db.session.add(data)
        db.session.commit()
        if request.files["imag"].filename:
            request.files["imag"].save(f"static\\images\\{data.id}")
        alert_type = "success"
        flash('Your Data has been Added')
        return redirect(url_for('home', alert_type=alert_type))
    elif request.method == "POST":
        flash("Please Enter a 10 digit Phone number.")
        alert_type="warning"
    return render_template('add.html', page='REGISTER', form=form, date=dat, alert_type=alert_type)


@app.route('/edit/<int:data_id>', methods=['GET', 'POST'])
def edit(data_id):
    alert_type=None
    data=Manage.query.get(data_id)
    form=formhm.add_patient()
    if data:
        if form.validate_on_submit():
            data.fn=form.fn.data
            data.ln=form.ln.data
            data.dob= form.dob.data
            data.age= int((date.today() - form.dob.data).days/365.2425)
            data.gen=form.gen.data
            data.add1= form.add1.data
            data.add2 = form.add2.data
            data.add3 = form.add3.data
            data.add4 = form.add4.data
            data.mob= form.mob.data
            data.email= form.email.data
            db.session.commit()
            if request.files["imag"].filename:
                request.files["imag"].save(f"static\\images\\{data.id}")
            flash('Record updated')
            alert_type = "success"
            return redirect(url_for('home', alert_type=alert_type))
        elif request.method == "POST":
            flash("Please Enter a 10 digit Phone number.")
            alert_type = "warning"
        form.fn.data=data.fn
        form.ln.data= data.ln
        form.dob.data = data.dob
        form.gen.data = data.gen
        form.add1.data= data.add1
        form.add2.data = data.add2
        form.add3.data = data.add3
        form.add4.data = data.add4
        form.mob.data = data.mob
        form.email.data = data.email
        return render_template('edit.html', form=form, data_id=data_id, page='EDIT RECORD', date=datetime.now().date(

        ), alert_type=alert_type)
    else:
        alert_type="danger"
        flash('Record not found')
    return redirect(url_for('home', alert_type=alert_type))

@app.route('/delete/<int:data_id>', methods=['GET', 'POST'])
def delete(data_id):
    data = Manage.query.get(data_id)
    form = formhm.delete()
    if data:
        if form.validate_on_submit():
            db.session.delete(data)
            db.session.commit()
            flash('Data has been deleted')
            alert_type="success"
            try:
                os.remove(f"static\\images\\{data.id}")
            except:
                pass
            return redirect(url_for('home', alert_type=alert_type))
        return render_template('delete.html', page='DELETE RECORD', form=form, data_id=data_id)
    else:
        flash('Record not found')
        alert_type="danger"
    return redirect(url_for('home', alert_type=alert_type))

def search():
    pass
