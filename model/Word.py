import sqlalchemy as sa
import json

from model import Base


class User(Base):
    # id = sa.Column(sa.String(255), primary_key=True)
    name = sa.Column(sa.String(255))
    email = sa.Column(sa.String(255))
    # gender = sa.Column(sa.types.Enum("boy", "girl"))
    profile = sa.Column(sa.String(255))
    nric_no = sa.Column(sa.String(255))
    pass_code = sa.Column(sa.String(255))
    address = sa.Column(sa.String(255))
    zipcode = sa.Column(sa.String(255))
    is_verified = sa.Column(sa.Boolean())

    def _get_val(self):  # serializing json
        return ({'id': self.id,
                 'name': self.name,
                 'email': self.email,
                 'profile': self.profile,
                 'nric_no': self.nric_no,
                 'pass_code': self.pass_code,
                 'address': self.address,
                 'zipcode': self.zipcode,
                 'is_verified': self.is_verified
                 })
