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


class A(Base):
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


class B(Base):
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


class C(Base):
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


class D(Base):
    def _get_val(self):  # serializing json
        return ({'id': self.id,
                 'word': self.word,
                 'type': self.type,
                 'meaning_zg': self.meaning_zg,
                 'meaning_uni': self.meaning_uni,
                 'remark': self.remark
                 })


class E(Base):
    def _get_val(self):  # serializing json
        return ({'id': self.id,
                 'word': self.word,
                 'type': self.type,
                 'meaning_zg': self.meaning_zg,
                 'meaning_uni': self.meaning_uni,
                 'remark': self.remark
                 })


class F(Base):
    def _get_val(self):  # serializing json
        return ({'id': self.id,
                 'word': self.word,
                 'type': self.type,
                 'meaning_zg': self.meaning_zg,
                 'meaning_uni': self.meaning_uni,
                 'remark': self.remark
                 })


class G(Base):
    def _get_val(self):  # serializing json
        return ({'id': self.id,
                 'word': self.word,
                 'type': self.type,
                 'meaning_zg': self.meaning_zg,
                 'meaning_uni': self.meaning_uni,
                 'remark': self.remark
                 })


class H(Base):
    def _get_val(self):  # serializing json
        return ({'id': self.id,
                 'word': self.word,
                 'type': self.type,
                 'meaning_zg': self.meaning_zg,
                 'meaning_uni': self.meaning_uni,
                 'remark': self.remark
                 })


class I(Base):
    def _get_val(self):  # serializing json
        return ({'id': self.id,
                 'word': self.word,
                 'type': self.type,
                 'meaning_zg': self.meaning_zg,
                 'meaning_uni': self.meaning_uni,
                 'remark': self.remark
                 })


class J(Base):
    def _get_val(self):  # serializing json
        return ({'id': self.id,
                 'word': self.word,
                 'type': self.type,
                 'meaning_zg': self.meaning_zg,
                 'meaning_uni': self.meaning_uni,
                 'remark': self.remark
                 })


class K(Base):
    def _get_val(self):  # serializing json
        return ({'id': self.id,
                 'word': self.word,
                 'type': self.type,
                 'meaning_zg': self.meaning_zg,
                 'meaning_uni': self.meaning_uni,
                 'remark': self.remark
                 })


class L(Base):
    def _get_val(self):  # serializing json
        return ({'id': self.id,
                 'word': self.word,
                 'type': self.type,
                 'meaning_zg': self.meaning_zg,
                 'meaning_uni': self.meaning_uni,
                 'remark': self.remark
                 })


class M(Base):
    def _get_val(self):  # serializing json
        return ({'id': self.id,
                 'word': self.word,
                 'type': self.type,
                 'meaning_zg': self.meaning_zg,
                 'meaning_uni': self.meaning_uni,
                 'remark': self.remark
                 })


class N(Base):
    def _get_val(self):  # serializing json
        return ({'id': self.id,
                 'word': self.word,
                 'type': self.type,
                 'meaning_zg': self.meaning_zg,
                 'meaning_uni': self.meaning_uni,
                 'remark': self.remark
                 })


class O(Base):
    def _get_val(self):  # serializing json
        return ({'id': self.id,
                 'word': self.word,
                 'type': self.type,
                 'meaning_zg': self.meaning_zg,
                 'meaning_uni': self.meaning_uni,
                 'remark': self.remark
                 })


class P(Base):
    def _get_val(self):  # serializing json
        return ({'id': self.id,
                 'word': self.word,
                 'type': self.type,
                 'meaning_zg': self.meaning_zg,
                 'meaning_uni': self.meaning_uni,
                 'remark': self.remark
                 })


class Q(Base):
    def _get_val(self):  # serializing json
        return ({'id': self.id,
                 'word': self.word,
                 'type': self.type,
                 'meaning_zg': self.meaning_zg,
                 'meaning_uni': self.meaning_uni,
                 'remark': self.remark
                 })


class R(Base):
    def _get_val(self):  # serializing json
        return ({'id': self.id,
                 'word': self.word,
                 'type': self.type,
                 'meaning_zg': self.meaning_zg,
                 'meaning_uni': self.meaning_uni,
                 'remark': self.remark
                 })


class S(Base):
    def _get_val(self):  # serializing json
        return ({'id': self.id,
                 'word': self.word,
                 'type': self.type,
                 'meaning_zg': self.meaning_zg,
                 'meaning_uni': self.meaning_uni,
                 'remark': self.remark
                 })


class T(Base):
    def _get_val(self):  # serializing json
        return ({'id': self.id,
                 'word': self.word,
                 'type': self.type,
                 'meaning_zg': self.meaning_zg,
                 'meaning_uni': self.meaning_uni,
                 'remark': self.remark
                 })


class U(Base):
    def _get_val(self):  # serializing json
        return ({'id': self.id,
                 'word': self.word,
                 'type': self.type,
                 'meaning_zg': self.meaning_zg,
                 'meaning_uni': self.meaning_uni,
                 'remark': self.remark
                 })


class V(Base):
    def _get_val(self):  # serializing json
        return ({'id': self.id,
                 'word': self.word,
                 'type': self.type,
                 'meaning_zg': self.meaning_zg,
                 'meaning_uni': self.meaning_uni,
                 'remark': self.remark
                 })


class W(Base):
    def _get_val(self):  # serializing json
        return ({'id': self.id,
                 'word': self.word,
                 'type': self.type,
                 'meaning_zg': self.meaning_zg,
                 'meaning_uni': self.meaning_uni,
                 'remark': self.remark
                 })


class X(Base):
    def _get_val(self):  # serializing json
        return ({'id': self.id,
                 'word': self.word,
                 'type': self.type,
                 'meaning_zg': self.meaning_zg,
                 'meaning_uni': self.meaning_uni,
                 'remark': self.remark
                 })


class Y(Base):
    def _get_val(self):  # serializing json
        return ({'id': self.id,
                 'word': self.word,
                 'type': self.type,
                 'meaning_zg': self.meaning_zg,
                 'meaning_uni': self.meaning_uni,
                 'remark': self.remark
                 })


class Z(Base):
    def _get_val(self):  # serializing json
        return ({'id': self.id,
                 'word': self.word,
                 'type': self.type,
                 'meaning_zg': self.meaning_zg,
                 'meaning_uni': self.meaning_uni,
                 'remark': self.remark
                 })
