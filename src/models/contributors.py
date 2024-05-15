import enum
import json
import logging
from datetime import datetime, timezone

from flask_migrate import Migrate
from src import app, db

logger = logging.getLogger("Models")
logger.setLevel(logging.INFO)

migrate = Migrate(app, db)


class PledgeType(enum.Enum):
    ONE_TIME = "ONE_TIME"
    REGULAR_CONTRIBUTION = "REGULAR_CONTRIBUTION"


class PledgeStatus(enum.Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"


class Contributors(db.Model):
    __tablename__ = 'contributors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    class_section = db.Column(db.String(100), nullable=False, unique=True)
    year = db.Column(db.String(100), nullable=False, unique=True)
    phone = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now(timezone.utc))
    bank_details = db.relationship('ContributorBankDetails', backref='contributors', lazy=True)
    pledge_details = db.relationship('ContributorPledgeDetails', backref='contributors', lazy=True)
    inactivity = db.relationship('ContributorInactivity', backref='contributors', lazy=True)

    def __repr__(self):
        return f"Contributor('{self.id}', '{self.name}')"


class ContributorBankDetails(db.Model):
    __tablename__ = 'contributor_bank_details'
    id = db.Column(db.Integer, primary_key=True)
    contributor_id = db.Column(db.Integer, db.ForeignKey(Contributors.id), nullable=True)
    bank_name = db.Column(db.String(100), nullable=False, unique=True)
    bank_account_number = db.Column(db.String(100), nullable=False, unique=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now(timezone.utc))

    def __repr__(self):
        return f"Contributor('{self.id}', '{self.name}')"


class ContributorPledgeDetails(db.Model):
    __tablename__ = 'contributor_pledge_details'
    id = db.Column(db.Integer, primary_key=True)
    contributor_id = db.Column(db.Integer, db.ForeignKey(Contributors.id), nullable=True)
    pledge_date = db.Column(db.DateTime, nullable=False)
    pledge_amount = db.Column(db.Integer, nullable=False)
    pledge_status = db.Column(db.Enum(PledgeStatus), nullable=False, default=PledgeStatus.ACTIVE)
    pledge_type = db.Column(db.Enum(PledgeType), nullable=False, default=PledgeType.REGULAR_CONTRIBUTION)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now(timezone.utc))

    def __repr__(self):
        return f"Contributor('{self.id}', '{self.name}')"


class ContributorInactivity(db.Model):
    __tablename__ = 'contributor_inactivity'
    id = db.Column(db.Integer, primary_key=True)
    contributor_id = db.Column(db.Integer, db.ForeignKey(Contributors.id), nullable=True)
    inactivity_start = db.Column(db.DateTime, nullable=False)
    inactivity_end = db.Column(db.DateTime, nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now(timezone.utc))

    def __repr__(self):
        return f"Contributor('{self.id}', '{self.name}')"