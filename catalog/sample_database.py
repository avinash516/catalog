from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from shoes_db import *

engine = create_engine('sqlite:///shoes.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

# Delete Brand if exisitng.
session.query(Brands).delete()
# Delete ModelName if exisitng.
session.query(Models).delete()
# Delete Users if exisitng.
session.query(Userdata).delete()

# Create sample users
User1 = Userdata(name="avinash",
                 email="chekuriavinash@gmail.com",
                 picture='https://lh5.googleusercontent.com/-6tCX9WOltBs'
                         '/AAAAAAAAAAI/AAAAAAAADJc/T4yOqe2XIjc/photo.jpg')
session.add(User1)
session.commit()
User2 = Userdata(name="Avinash", email="avinash.ch@apssdc.in",
                 picture='https://lh4.googleusercontent.com/-EW6n0vdHiOk'
                         '/AAAAAAAAAAI/AAAAAAAAAE4/kHbfWo9laMw/photo.jpg')
session.add(User2)
session.commit()

# Create sample Brands
Brand1 = Brands(name="13 Reasons", user_id=1)
session.add(Brand1)
session.commit()

Brand2 = Brands(name="Red Tape", user_id=1)
session.add(Brand2)
session.commit

try:
    Model1 = Models(id=101, brand_id=2,
                    user_id=1, modelnumber="123",
                    colors="Red", price="15000", description="Quality is Fine")
    session.add(Model1)
    session.commit()
except Exception as ex:
    print(ex)

try:
    Model2 = Models(id=102,
                    brand_id=3,
                    user_id=1,
                    modelnumber="1429",
                    colors="Black",
                    price="300",
                    description="Good Quality")
    session.add(Model2)
    session.commit()
except Exception as ex:
    print(ex)

print("Your database is sample database")
