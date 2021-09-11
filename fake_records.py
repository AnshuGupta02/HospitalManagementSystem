from faker import Faker
from modelshm import Manage
from datetime import date, datetime
from random import choice
from apphm import db


def fake_patients(n=100):
    db.session.rollback()
    f = Faker()
    for _ in range(n):
        dob = f.date_of_birth()
        age = int((date.today() - dob).days/365.2425)
        p = Manage(
            date=datetime(*map(int, f.date().split("-"))),
            fn = f.first_name(),
            ln = f.last_name(),
            dob = dob,
            age = age,
            gen = choice(["Male", "Female", "Other"]),
            add1 = f.street_address(),
            add2 = f.city(),
            add3 = f.state(),
            add4 = f.postcode(),
            mob = int(f.numerify("9#########")),
            email = f.email()
        )
        db.session.add(p)
    db.session.commit()
