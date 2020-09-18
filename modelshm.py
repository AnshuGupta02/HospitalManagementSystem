from apphm import db

class manage(db.Model):
    id=db.Column( db.Integer, primary_key=True)
    date=db.Column('Date', db.DATE)
    fn=db.Column('First name', db.String, nullable=False)
    ln=db.Column('Last name', db.String)
    dob= db.Column('D.O.B', db.DATE)
    age=db.Column('Age', db.Integer)
    gen=db.Column('Gender', db.String)
    add1=db.Column('Address1', db.String)
    add2 = db.Column('Address2', db.String)
    add3 = db.Column('Address3', db.String)
    add4 = db.Column('Address4', db.String)
    mob=db.Column('Phone', db.Integer)
    email=db.Column('email', db.String)
    imag=db.Column('Image')

    def __repr__(self):
        return f'registered on {self.date}, Name={self.fn} {self.ln}, dob={self.dob}, age={self.age}, gender={self.gen}, add={self.add1} {self.add2} {self.add3} {self.add4}, phone={self.mob} email={self.email}, {self.imag} '