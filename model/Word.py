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


class E(Base):
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


class F(Base):
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


class G(Base):
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


class H(Base):
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


class I(Base):
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


class J(Base):
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


class K(Base):
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


class L(Base):
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


class M(Base):
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


class N(Base):
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


class O(Base):
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


class P(Base):
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


class Q(Base):
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


class R(Base):
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


class S(Base):
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


class T(Base):
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


class U(Base):
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


class V(Base):
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


class W(Base):
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


class X(Base):
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


class Y(Base):
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


class Z(Base):
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
