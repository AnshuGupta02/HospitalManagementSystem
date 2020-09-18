from apphm import app, db
from flask import render_template, flash, get_flashed_messages, redirect, url_for
import formhm
from datetime import datetime, date
from modelshm import manage
#from email_validator import validate_email
import pickle


@app.route('/')
@app.route('/records')
def home():
    form = formhm.add_patient()
    dat = datetime.now().date()
    datas=manage.query.all()
    return render_template('home.html', page='RECORDS', datas=datas, date=dat, form=form)


@app.route('/register', methods=['GET', 'POST'])
def add():
    form=formhm.add_patient()
    dat = datetime.now().date()
    if form.validate_on_submit():
        data=manage(fn=form.fn.data, ln=form.ln.data,date=dat, dob=form.dob.data, age=int((date.today() - form.dob.data).days/365.2425), gen=form.gen.data, add1= form.add1.data, add2= form.add2.data , add3= form.add3.data , add4= form.add4.data , mob=form.mob.data, email=form.email.data, imag=form.imag.data)
        db.session.add(data)
        db.session.commit()
        flash('Your Data has been Added')
        return redirect(url_for('home'))
    return render_template('add.html', page='REGISTER', form=form, date=dat)


@app.route('/edit/<int:data_id>', methods=['GET', 'POST'])
def edit(data_id):
    data=manage.query.get(data_id)
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
            data.imag= form.imag.data
            db.session.commit()
            flash('Record updated')
            return redirect(url_for('home'))
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
        form.imag.data= data.imag
        return render_template('edit.html', form=form, data_id=data_id, page='EDIT RECORD', date=datetime.now().date())
    else:
        flash('Record not found')
    return redirect(url_for('home'))

@app.route('/delete/<int:data_id>', methods=['GET', 'POST'])
def delete(data_id):
    data = manage.query.get(data_id)
    form = formhm.delete()
    if data:
        if form.validate_on_submit():
            db.session.delete(data)
            db.session.commit()
            flash('Data has been deleted')
            return redirect(url_for('home'))
        return render_template('delete.html', page='DELETE RECORD', form=form, data_id=data_id)
    else:
        flash('Record not found')
    return redirect(url_for('home'))
