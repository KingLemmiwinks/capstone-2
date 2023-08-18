# Add 4 metadata columns to ALL EDITABLE MODELS
# createdBy, createdDate, modifiedBy, modifiedDate

from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

bcrypt = Bcrypt()
db = SQLAlchemy()


class User(db.Model):
    """User in the system."""

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    phone_number = db.Column(db.String, nullable=False)
    userHousehold = db.relationship('userHouseholds')

    # start_register
    @classmethod
    def register(cls, username, pwd):
        """Register user w/hashed password & return user."""

        hashed = bcrypt.generate_password_hash(pwd)
        # turn bytestring into normal (unicode utf8) string
        hashed_utf8 = hashed.decode("utf8")

        # return instance of user w/username and hashed pwd
        return cls(username=username, password=hashed_utf8)
    # end_register

    # start_authenticate
    @classmethod
    def authenticate(cls, username, pwd):
        """Validate that user exists & password is correct.

        Return user if valid; else return False.
        """

        u = User.query.filter_by(username=username).first()

        if u and bcrypt.check_password_hash(u.password, pwd):
            # return user instance
            return u
        else:
            return False
    # end_authenticate

class Household(db.Model):
    """Mapping user household to app."""

    __tablename__ = 'households'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    street_address = db.Column(db.String)
    city = db.Column(db.String)
    state = db.Column(db.String)
    zip = db.Column(db.Integer)
    photo = db.Column(db.String, nullable=True)
    notes = db.Column(db.Text, nullable=True)

class UserHousehold(db.Model):
    """User's Household"""

    __tablename__ = 'userHouseholds'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userID = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='cascade'))
    householdID = db.Column(db.Integer, db.ForeignKey('households.id', ondelete='cascade'))
    household = db.relationship('households')

class SellerExpertise(db.Model):
    """Seller's Expertise"""

    __tablename__ = 'sellerExpertise'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    hasExpertise = db.Column(db.Boolean)
    isLandlord = db.Column(db.Boolean)
    isRealEstateLicensee = db.Column(db.Boolean)
    notes = db.Column(db.Text, nullable=True)
    householdID = db.Column(db.Integer, db.ForeignKey('households.id', ondelete='cascade'))

class OwnershipOccupancy(db.Model):
    """Ownership and Occupancy"""

    __tablename__ = 'ownershipOccupancy'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    mostRecentOccupation = db.Column(db.DateTime)
    isOccupiedBySeller = db.Column(db.Boolean)
    sellerOccupancyHistory = db.Column(db.Text, nullable=True)
    hasHadPets = db.Column(db.Boolean)
    purchaseDate = db.Column(db.DateTime)
    notes = db.Column(db.Text, nullable=True)
    householdID = db.Column(db.Integer, db.ForeignKey('households.id', ondelete='cascade'))
    roleTypeID = db.Column(db.Integer, db.ForeignKey('roleTypes.id', ondelete='cascade'))

class RoleType(db.Model):
    """Role Type"""

    __tablename__ = 'roleTypes'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    roleTypeName = db.Column(db.String)

class Associations(db.Model):
    """Associations"""

    __tablename__ = 'associations'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fees = db.Column(db.Float, nullable=True)
    initiationFees = db.Column(db.Float, nullable=True)
    communityMaintenance = db.Column(db.String, nullable=True)
    notes = db.Column(db.Text, nullable=True)
    householdID = db.Column(db.Integer, db.ForeignKey('households.id', ondelete='cascade'))
    associationTypeID = db.Column(db.Integer, db.ForeignKey('associationTypes.id', ondelete='cascade'))
    frequencyTypeID = db.Column(db.Integer, db.ForeignKey('frequencyTypes.id', ondelete='cascade'), nullable=True)

class AssociationType(db.Model):
    """Association Type"""

    __tablename__ = 'associationTypes'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    associationTypeName = db.Column(db.String)

class FrequencyType(db.Model):
    """Frequency Type"""

    __tablename__ = 'frequencyTypes'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    frequencyTypeName = db.Column(db.String)

class Roof(db.Model):
    """Roof"""

    __tablename__ = 'roof'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    installationDate = db.Column(db.DateTime, nullable=True)
    invoicePhoto = db.Column(db.String, nullable=True)
    hasBeenReplaced = db.Column(db.Boolean)
    hadExistingMaterialRemoved = db.Column(db.Boolean)
    hasPreexistingLeaks = db.Column(db.Boolean)
    hasRainwaterProblems = db.Column(db.Boolean)
    notes = db.Column(db.Text, nullable=True)
    householdID = db.Column(db.Integer, db.ForeignKey('households.id', ondelete='cascade'))

class Basement(db.Model):
    """Basement"""

    __tablename__ = 'basements'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    hasSumpPump = db.Column(db.Boolean)
    pumpCount = db.Column(db.Integer, nullable=True)
    hasBeenUsed = db.Column(db.Boolean)
    hasWaterDamage = db.Column(db.Boolean)
    hasRepairs = db.Column(db.Boolean)
    hasDownspoutConnection = db.Column(db.Boolean)
    notes = db.Column(db.Text, nullable=True)
    householdID = db.Column(db.Integer, db.ForeignKey('households.id', ondelete='cascade'))

def connect_db(app):
    """Connect this database to provided Flask app."""

    db.app = app
    db.init_app(app)