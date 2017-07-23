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
    is_fav = sa.Column(sa.Boolean, default=False)

    def _get_val(self):  # serializing json
        return ({'id': self.id,
                 'word': self.word,
                 'type': self.type,
                 'meaning_zg': self.meaning_zg,
                 'meaning_uni': self.meaning_uni,
                 'remark': self.remark,
                 'is_fav': self.is_fav
                 })


class A(Base):
    word = sa.Column(sa.String(255))
    type = sa.Column(sa.String(255))
    # gender = sa.Column(sa.types.Enum("boy", "girl"))
    meaning_zg = sa.Column(sa.String(255))
    meaning_uni = sa.Column(sa.String(255))
    remark = sa.Column(sa.String(255))
    is_fav = sa.Column(sa.Boolean, default=False)

    def _get_val(self):  # serializing json
        return ({'id': self.id,
                 'word': self.word,
                 'type': self.type,
                 'meaning_zg': self.meaning_zg,
                 'meaning_uni': self.meaning_uni,
                 'remark': self.remark,
                 'is_fav': self.is_fav
                 })


class B(Base):
    word = sa.Column(sa.String(255))
    type = sa.Column(sa.String(255))
    # gender = sa.Column(sa.types.Enum("boy", "girl"))
    meaning_zg = sa.Column(sa.String(255))
    meaning_uni = sa.Column(sa.String(255))
    remark = sa.Column(sa.String(255))
    is_fav = sa.Column(sa.Boolean, default=False)

    def _get_val(self):  # serializing json
        return ({'id': self.id,
                 'word': self.word,
                 'type': self.type,
                 'meaning_zg': self.meaning_zg,
                 'meaning_uni': self.meaning_uni,
                 'remark': self.remark,
                 'is_fav': self.is_fav
                 })


class C(Base):
    word = sa.Column(sa.String(255))
    type = sa.Column(sa.String(255))
    # gender = sa.Column(sa.types.Enum("boy", "girl"))
    meaning_zg = sa.Column(sa.String(255))
    meaning_uni = sa.Column(sa.String(255))
    remark = sa.Column(sa.String(255))
    is_fav = sa.Column(sa.Boolean, default=False)

    def _get_val(self):  # serializing json
        return ({'id': self.id,
                 'word': self.word,
                 'type': self.type,
                 'meaning_zg': self.meaning_zg,
                 'meaning_uni': self.meaning_uni,
                 'remark': self.remark,
                 'is_fav': self.is_fav
                 })


class D(Base):
    word = sa.Column(sa.String(255))
    type = sa.Column(sa.String(255))
    # gender = sa.Column(sa.types.Enum("boy", "girl"))
    meaning_zg = sa.Column(sa.String(255))
    meaning_uni = sa.Column(sa.String(255))
    remark = sa.Column(sa.String(255))
    is_fav = sa.Column(sa.Boolean, default=False)

    def _get_val(self):  # serializing json
        return ({'id': self.id,
                 'word': self.word,
                 'type': self.type,
                 'meaning_zg': self.meaning_zg,
                 'meaning_uni': self.meaning_uni,
                 'remark': self.remark,
                 'is_fav': self.is_fav
                 })


class E(Base):
    word = sa.Column(sa.String(255))
    type = sa.Column(sa.String(255))
    # gender = sa.Column(sa.types.Enum("boy", "girl"))
    meaning_zg = sa.Column(sa.String(255))
    meaning_uni = sa.Column(sa.String(255))
    remark = sa.Column(sa.String(255))
    is_fav = sa.Column(sa.Boolean, default=False)

    def _get_val(self):  # serializing json
        return ({'id': self.id,
                 'word': self.word,
                 'type': self.type,
                 'meaning_zg': self.meaning_zg,
                 'meaning_uni': self.meaning_uni,
                 'remark': self.remark,
                 'is_fav': self.is_fav
                 })


class F(Base):
    word = sa.Column(sa.String(255))
    type = sa.Column(sa.String(255))
    # gender = sa.Column(sa.types.Enum("boy", "girl"))
    meaning_zg = sa.Column(sa.String(255))
    meaning_uni = sa.Column(sa.String(255))
    remark = sa.Column(sa.String(255))
    is_fav = sa.Column(sa.Boolean, default=False)

    def _get_val(self):  # serializing json
        return ({'id': self.id,
                 'word': self.word,
                 'type': self.type,
                 'meaning_zg': self.meaning_zg,
                 'meaning_uni': self.meaning_uni,
                 'remark': self.remark,
                 'is_fav': self.is_fav
                 })


class G(Base):
    word = sa.Column(sa.String(255))
    type = sa.Column(sa.String(255))
    # gender = sa.Column(sa.types.Enum("boy", "girl"))
    meaning_zg = sa.Column(sa.String(255))
    meaning_uni = sa.Column(sa.String(255))
    remark = sa.Column(sa.String(255))
    is_fav = sa.Column(sa.Boolean, default=False)

    def _get_val(self):  # serializing json
        return ({'id': self.id,
                 'word': self.word,
                 'type': self.type,
                 'meaning_zg': self.meaning_zg,
                 'meaning_uni': self.meaning_uni,
                 'remark': self.remark,
                 'is_fav': self.is_fav
                 })


class H(Base):
    word = sa.Column(sa.String(255))
    type = sa.Column(sa.String(255))
    # gender = sa.Column(sa.types.Enum("boy", "girl"))
    meaning_zg = sa.Column(sa.String(255))
    meaning_uni = sa.Column(sa.String(255))
    remark = sa.Column(sa.String(255))
    is_fav = sa.Column(sa.Boolean, default=False)

    def _get_val(self):  # serializing json
        return ({'id': self.id,
                 'word': self.word,
                 'type': self.type,
                 'meaning_zg': self.meaning_zg,
                 'meaning_uni': self.meaning_uni,
                 'remark': self.remark,
                 'is_fav': self.is_fav
                 })


class I(Base):
    word = sa.Column(sa.String(255))
    type = sa.Column(sa.String(255))
    # gender = sa.Column(sa.types.Enum("boy", "girl"))
    meaning_zg = sa.Column(sa.String(255))
    meaning_uni = sa.Column(sa.String(255))
    remark = sa.Column(sa.String(255))
    is_fav = sa.Column(sa.Boolean, default=False)

    def _get_val(self):  # serializing json
        return ({'id': self.id,
                 'word': self.word,
                 'type': self.type,
                 'meaning_zg': self.meaning_zg,
                 'meaning_uni': self.meaning_uni,
                 'remark': self.remark,
                 'is_fav': self.is_fav
                 })


class J(Base):
    word = sa.Column(sa.String(255))
    type = sa.Column(sa.String(255))
    # gender = sa.Column(sa.types.Enum("boy", "girl"))
    meaning_zg = sa.Column(sa.String(255))
    meaning_uni = sa.Column(sa.String(255))
    remark = sa.Column(sa.String(255))
    is_fav = sa.Column(sa.Boolean, default=False)

    def _get_val(self):  # serializing json
        return ({'id': self.id,
                 'word': self.word,
                 'type': self.type,
                 'meaning_zg': self.meaning_zg,
                 'meaning_uni': self.meaning_uni,
                 'remark': self.remark,
                 'is_fav': self.is_fav
                 })


class K(Base):
    word = sa.Column(sa.String(255))
    type = sa.Column(sa.String(255))
    # gender = sa.Column(sa.types.Enum("boy", "girl"))
    meaning_zg = sa.Column(sa.String(255))
    meaning_uni = sa.Column(sa.String(255))
    remark = sa.Column(sa.String(255))
    is_fav = sa.Column(sa.Boolean, default=False)

    def _get_val(self):  # serializing json
        return ({'id': self.id,
                 'word': self.word,
                 'type': self.type,
                 'meaning_zg': self.meaning_zg,
                 'meaning_uni': self.meaning_uni,
                 'remark': self.remark,
                 'is_fav': self.is_fav
                 })


class L(Base):
    word = sa.Column(sa.String(255))
    type = sa.Column(sa.String(255))
    # gender = sa.Column(sa.types.Enum("boy", "girl"))
    meaning_zg = sa.Column(sa.String(255))
    meaning_uni = sa.Column(sa.String(255))
    remark = sa.Column(sa.String(255))
    is_fav = sa.Column(sa.Boolean, default=False)

    def _get_val(self):  # serializing json
        return ({'id': self.id,
                 'word': self.word,
                 'type': self.type,
                 'meaning_zg': self.meaning_zg,
                 'meaning_uni': self.meaning_uni,
                 'remark': self.remark,
                 'is_fav': self.is_fav
                 })


class M(Base):
    word = sa.Column(sa.String(255))
    type = sa.Column(sa.String(255))
    # gender = sa.Column(sa.types.Enum("boy", "girl"))
    meaning_zg = sa.Column(sa.String(255))
    meaning_uni = sa.Column(sa.String(255))
    remark = sa.Column(sa.String(255))
    is_fav = sa.Column(sa.Boolean, default=False)

    def _get_val(self):  # serializing json
        return ({'id': self.id,
                 'word': self.word,
                 'type': self.type,
                 'meaning_zg': self.meaning_zg,
                 'meaning_uni': self.meaning_uni,
                 'remark': self.remark,
                 'is_fav': self.is_fav
                 })


class N(Base):
    word = sa.Column(sa.String(255))
    type = sa.Column(sa.String(255))
    # gender = sa.Column(sa.types.Enum("boy", "girl"))
    meaning_zg = sa.Column(sa.String(255))
    meaning_uni = sa.Column(sa.String(255))
    remark = sa.Column(sa.String(255))
    is_fav = sa.Column(sa.Boolean, default=False)

    def _get_val(self):  # serializing json
        return ({'id': self.id,
                 'word': self.word,
                 'type': self.type,
                 'meaning_zg': self.meaning_zg,
                 'meaning_uni': self.meaning_uni,
                 'remark': self.remark,
                 'is_fav': self.is_fav
                 })


class O(Base):
    word = sa.Column(sa.String(255))
    type = sa.Column(sa.String(255))
    # gender = sa.Column(sa.types.Enum("boy", "girl"))
    meaning_zg = sa.Column(sa.String(255))
    meaning_uni = sa.Column(sa.String(255))
    remark = sa.Column(sa.String(255))
    is_fav = sa.Column(sa.Boolean, default=False)

    def _get_val(self):  # serializing json
        return ({'id': self.id,
                 'word': self.word,
                 'type': self.type,
                 'meaning_zg': self.meaning_zg,
                 'meaning_uni': self.meaning_uni,
                 'remark': self.remark,
                 'is_fav': self.is_fav
                 })


class P(Base):
    word = sa.Column(sa.String(255))
    type = sa.Column(sa.String(255))
    # gender = sa.Column(sa.types.Enum("boy", "girl"))
    meaning_zg = sa.Column(sa.String(255))
    meaning_uni = sa.Column(sa.String(255))
    remark = sa.Column(sa.String(255))
    is_fav = sa.Column(sa.Boolean, default=False)

    def _get_val(self):  # serializing json
        return ({'id': self.id,
                 'word': self.word,
                 'type': self.type,
                 'meaning_zg': self.meaning_zg,
                 'meaning_uni': self.meaning_uni,
                 'remark': self.remark,
                 'is_fav': self.is_fav
                 })


class Q(Base):
    word = sa.Column(sa.String(255))
    type = sa.Column(sa.String(255))
    # gender = sa.Column(sa.types.Enum("boy", "girl"))
    meaning_zg = sa.Column(sa.String(255))
    meaning_uni = sa.Column(sa.String(255))
    remark = sa.Column(sa.String(255))
    is_fav = sa.Column(sa.Boolean, default=False)

    def _get_val(self):  # serializing json
        return ({'id': self.id,
                 'word': self.word,
                 'type': self.type,
                 'meaning_zg': self.meaning_zg,
                 'meaning_uni': self.meaning_uni,
                 'remark': self.remark,
                 'is_fav': self.is_fav
                 })


class R(Base):
    word = sa.Column(sa.String(255))
    type = sa.Column(sa.String(255))
    # gender = sa.Column(sa.types.Enum("boy", "girl"))
    meaning_zg = sa.Column(sa.String(255))
    meaning_uni = sa.Column(sa.String(255))
    remark = sa.Column(sa.String(255))
    is_fav = sa.Column(sa.Boolean, default=False)

    def _get_val(self):  # serializing json
        return ({'id': self.id,
                 'word': self.word,
                 'type': self.type,
                 'meaning_zg': self.meaning_zg,
                 'meaning_uni': self.meaning_uni,
                 'remark': self.remark,
                 'is_fav': self.is_fav
                 })


class S(Base):
    word = sa.Column(sa.String(255))
    type = sa.Column(sa.String(255))
    # gender = sa.Column(sa.types.Enum("boy", "girl"))
    meaning_zg = sa.Column(sa.String(255))
    meaning_uni = sa.Column(sa.String(255))
    remark = sa.Column(sa.String(255))
    is_fav = sa.Column(sa.Boolean, default=False)

    def _get_val(self):  # serializing json
        return ({'id': self.id,
                 'word': self.word,
                 'type': self.type,
                 'meaning_zg': self.meaning_zg,
                 'meaning_uni': self.meaning_uni,
                 'remark': self.remark,
                 'is_fav': self.is_fav
                 })


class T(Base):
    word = sa.Column(sa.String(255))
    type = sa.Column(sa.String(255))
    # gender = sa.Column(sa.types.Enum("boy", "girl"))
    meaning_zg = sa.Column(sa.String(255))
    meaning_uni = sa.Column(sa.String(255))
    remark = sa.Column(sa.String(255))
    is_fav = sa.Column(sa.Boolean, default=False)

    def _get_val(self):  # serializing json
        return ({'id': self.id,
                 'word': self.word,
                 'type': self.type,
                 'meaning_zg': self.meaning_zg,
                 'meaning_uni': self.meaning_uni,
                 'remark': self.remark,
                 'is_fav': self.is_fav
                 })


class U(Base):
    word = sa.Column(sa.String(255))
    type = sa.Column(sa.String(255))
    # gender = sa.Column(sa.types.Enum("boy", "girl"))
    meaning_zg = sa.Column(sa.String(255))
    meaning_uni = sa.Column(sa.String(255))
    remark = sa.Column(sa.String(255))
    is_fav = sa.Column(sa.Boolean, default=False)

    def _get_val(self):  # serializing json
        return ({'id': self.id,
                 'word': self.word,
                 'type': self.type,
                 'meaning_zg': self.meaning_zg,
                 'meaning_uni': self.meaning_uni,
                 'remark': self.remark,
                 'is_fav': self.is_fav
                 })


class V(Base):
    word = sa.Column(sa.String(255))
    type = sa.Column(sa.String(255))
    # gender = sa.Column(sa.types.Enum("boy", "girl"))
    meaning_zg = sa.Column(sa.String(255))
    meaning_uni = sa.Column(sa.String(255))
    remark = sa.Column(sa.String(255))
    is_fav = sa.Column(sa.Boolean, default=False)

    def _get_val(self):  # serializing json
        return ({'id': self.id,
                 'word': self.word,
                 'type': self.type,
                 'meaning_zg': self.meaning_zg,
                 'meaning_uni': self.meaning_uni,
                 'remark': self.remark,
                 'is_fav': self.is_fav
                 })


class W(Base):
    word = sa.Column(sa.String(255))
    type = sa.Column(sa.String(255))
    # gender = sa.Column(sa.types.Enum("boy", "girl"))
    meaning_zg = sa.Column(sa.String(255))
    meaning_uni = sa.Column(sa.String(255))
    remark = sa.Column(sa.String(255))
    is_fav = sa.Column(sa.Boolean, default=False)

    def _get_val(self):  # serializing json
        return ({'id': self.id,
                 'word': self.word,
                 'type': self.type,
                 'meaning_zg': self.meaning_zg,
                 'meaning_uni': self.meaning_uni,
                 'remark': self.remark,
                 'is_fav': self.is_fav
                 })


class X(Base):
    word = sa.Column(sa.String(255))
    type = sa.Column(sa.String(255))
    # gender = sa.Column(sa.types.Enum("boy", "girl"))
    meaning_zg = sa.Column(sa.String(255))
    meaning_uni = sa.Column(sa.String(255))
    remark = sa.Column(sa.String(255))
    is_fav = sa.Column(sa.Boolean, default=False)

    def _get_val(self):  # serializing json
        return ({'id': self.id,
                 'word': self.word,
                 'type': self.type,
                 'meaning_zg': self.meaning_zg,
                 'meaning_uni': self.meaning_uni,
                 'remark': self.remark,
                 'is_fav': self.is_fav
                 })


class Y(Base):
    word = sa.Column(sa.String(255))
    type = sa.Column(sa.String(255))
    # gender = sa.Column(sa.types.Enum("boy", "girl"))
    meaning_zg = sa.Column(sa.String(255))
    meaning_uni = sa.Column(sa.String(255))
    remark = sa.Column(sa.String(255))
    is_fav = sa.Column(sa.Boolean, default=False)

    def _get_val(self):  # serializing json
        return ({'id': self.id,
                 'word': self.word,
                 'type': self.type,
                 'meaning_zg': self.meaning_zg,
                 'meaning_uni': self.meaning_uni,
                 'remark': self.remark,
                 'is_fav': self.is_fav
                 })


class Z(Base):
    word = sa.Column(sa.String(255))
    type = sa.Column(sa.String(255))
    # gender = sa.Column(sa.types.Enum("boy", "girl"))
    meaning_zg = sa.Column(sa.String(255))
    meaning_uni = sa.Column(sa.String(255))
    remark = sa.Column(sa.String(255))
    is_fav = sa.Column(sa.Boolean, default=False)

    def _get_val(self):  # serializing json
        return ({'id': self.id,
                 'word': self.word,
                 'type': self.type,
                 'meaning_zg': self.meaning_zg,
                 'meaning_uni': self.meaning_uni,
                 'remark': self.remark,
                 'is_fav': self.is_fav
                 })
