from py4web import Field
from pydal.validators import *
from .common import db

# rooms
db.define_table('rooms',
    Field('room_number', 'string', unique=True),
    Field('number_of_beds', 'integer', default=1),
    Field('amenities', 'text', default=''),
    Field('price_per_night', 'decimal(10,2)'),
    Field('image', 'upload')
)

# customers
db.define_table('customers',
    Field('name', 'string'),
    Field('address', 'text', default=''),
    Field('phone_number', 'string', default=''),
    Field('email', 'string', unique=True)
)

# reservations
db.define_table('reservations',
    Field('room_id', 'reference rooms'),
    Field('customer_id', 'reference customers'),
    Field('start_date', 'date'),
    Field('end_date', 'date'),
    Field('notes', 'text', default=''),
    Field('total_cost', 'decimal(10,2)')
)

# setting up rules
# room
db.rooms.room_number.requires = [
    IS_NOT_EMPTY(error_message="Room number cannot be empty"),
    IS_NOT_IN_DB(db, 'rooms.room_number', error_message="This room number already exists")
]
db.rooms.number_of_beds.requires = IS_INT_IN_RANGE(1, 10, error_message="Number of beds must be between 1 and 10")
db.rooms.price_per_night.requires = IS_DECIMAL_IN_RANGE(0, 10000, error_message="Price must be between 0 and 10000")

# customers
db.customers.name.requires = IS_NOT_EMPTY(error_message="Name cannot be empty")
db.customers.email.requires = [
    IS_EMAIL(error_message="Invalid email format"),
    IS_NOT_IN_DB(db, 'customers.email', error_message="This email already exists")
]

# reservations
db.reservations.room_id.requires = IS_IN_DB(db, 'rooms.id', error_message="Room does not exist")
db.reservations.customer_id.requires = IS_IN_DB(db, 'customers.id', error_message="Customer does not exist")
db.reservations.start_date.requires = IS_DATE(error_message="Invalid start date")
db.reservations.end_date.requires = IS_DATE(error_message="Invalid end date")

# save
db.commit()