import sqlalchemy as sa
import json

from model import Base


class Word(Base):
    # id = sa.Column(sa.String(255), primary_key=True)
    word = sa.Column(sa.String(255))
    type = sa.Column(sa.String(255))
    # gender = sa.Column(sa.types.Enum("boy", "girl"))
    meaning_zg = sa.Column(sa.String(255))
    meaning_uni = sa.Column(sa.String(255))
    remark = sa.Column(sa.String(255))

    def _get_val(self):  # serializing json
        return ({'id': self.id,
                 'word': self.word,
                 'type': self.type,
                 'meaning_zg': self.meaning_zg,
                 'meaning_uni': self.meaning_uni,
                 'remark': self.remark
                 })