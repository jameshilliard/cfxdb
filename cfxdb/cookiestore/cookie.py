##############################################################################
#
#                        Crossbar.io Database
#     Copyright (c) Crossbar.io Technologies GmbH. Licensed under MIT.
#
##############################################################################

import uuid
import pprint
from typing import Optional, Dict, Any

import cbor2
import flatbuffers
import numpy as np

from zlmdb import table, MapUuidFlatBuffers, MapStringUuid
from cfxdb.gen.cookiestore import Cookie as CookieGen


class _CookieGen(CookieGen.Cookie):
    @classmethod
    def GetRootAsCookie(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = _CookieGen()
        x.Init(buf, n + offset)
        return x

    def OidAsBytes(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            _off = self._tab.Vector(o)
            _len = self._tab.VectorLen(o)
            return memoryview(self._tab.Bytes)[_off:_off + _len]
        return None

    def AuthenticatedOnNodeAsBytes(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            _off = self._tab.Vector(o)
            _len = self._tab.VectorLen(o)
            return memoryview(self._tab.Bytes)[_off:_off + _len]
        return None

    def AuthExtraAsBytes(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            _off = self._tab.Vector(o)
            _len = self._tab.VectorLen(o)
            return memoryview(self._tab.Bytes)[_off:_off + _len]
        return None


class Cookie(object):
    """
    Persistent cookies, as used in WAMP-Cookie authentication by router and proxy workers.
    """
    def __init__(self, from_fbs=None):
        self._from_fbs = from_fbs

        # [uint8] (uuid)
        self._oid = None

        # uint64 (timestamp)
        self._created = None

        # uint64
        self._max_age = None

        # string
        self._name = None

        # string
        self._value = None

        # uint64 (timestamp)
        self._authenticated = None

        # [uint8] (uuid)
        self._authenticated_on_node = None

        # uint64
        self._authenticated_session = None

        # uint64 (timestamp)
        self._authenticated_joined_at = None

        # string
        self._authenticated_authmethod = None

        # string
        self._authid = None

        # string
        self._authrole = None

        # string
        self._authrealm = None

        # [uint8] (cbor)
        self._authextra = None

    def marshal(self) -> dict:
        obj = {
            'oid': self.oid.bytes if self.oid else None,
            'created': int(self.created) if self.created else None,
            'max_age': self.max_age,
            'name': self.name,
            'value': self.value,
            'authenticated': int(self.authenticated) if self.authenticated else None,
            'authenticated_on_node': self.authenticated_on_node.bytes if self.authenticated_on_node else None,
            'authenticated_session': self.authenticated_session,
            'authenticated_joined_at':
            int(self.authenticated_joined_at) if self.authenticated_joined_at else None,
            'authenticated_authmethod': self.authenticated_authmethod,
            'authid': self.authid,
            'authrole': self.authrole,
            'authrealm': self.authrealm,
            # 'authextra': cbor2.dumps(self.authextra) if self.authextra else None,
            'authextra': self.authextra,
        }
        return obj

    def __str__(self):
        return '\n{}\n'.format(pprint.pformat(self.marshal()))

    @property
    def oid(self) -> uuid.UUID:
        """
        Database ID of this cookie record.
        """
        if self._oid is None and self._from_fbs:
            if self._from_fbs.OidLength():
                _oid = self._from_fbs.OidAsBytes()
                self._oid = uuid.UUID(bytes=bytes(_oid))
        return self._oid

    @oid.setter
    def oid(self, value: uuid.UUID):
        assert value is None or isinstance(value, uuid.UUID)
        self._oid = value

    @property
    def created(self) -> np.datetime64:
        """
        Timestamp when the cookie was created. Epoch time in ns.
        """
        if self._created is None and self._from_fbs:
            self._created = np.datetime64(self._from_fbs.Created(), 'ns')
        return self._created

    @created.setter
    def created(self, value: np.datetime64):
        assert value is None or isinstance(value, np.datetime64)
        self._created = value

    @property
    def max_age(self) -> int:
        """
        WAMP session ID of the caller that originally placed this offer.
        """
        if self._max_age is None and self._from_fbs:
            self._max_age = self._from_fbs.MaxAge()
        return self._max_age

    @max_age.setter
    def max_age(self, value: int):
        assert value is None or type(value) == int
        self._max_age = value

    @property
    def name(self) -> str:
        """
        Cookie name, as set in HTTP header, e.g. ``"cbtid"``.
        """
        if self._name is None and self._from_fbs:
            _name = self._from_fbs.Name()
            if _name:
                self._name = _name.decode('utf8')
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    @property
    def value(self) -> str:
        """
        Cookie value, as set in HTTP header, e.g. ``"gn2ri8fuAYQse50/L6N7jnt2"``.
        """
        if self._value is None and self._from_fbs:
            _value = self._from_fbs.Value()
            if _value:
                self._value = _value.decode('utf8')
        return self._value

    @value.setter
    def value(self, value: str):
        self._value = value

    @property
    def authenticated(self) -> np.datetime64:
        """
        Timestamp when the cookie was authenticated (if any). Epoch time in ns.
        """
        if self._authenticated is None and self._from_fbs:
            self._authenticated = np.datetime64(self._from_fbs.Authenticated(), 'ns')
        return self._authenticated

    @authenticated.setter
    def authenticated(self, value: np.datetime64):
        assert value is None or isinstance(value, np.datetime64)
        self._authenticated = value

    @property
    def authenticated_on_node(self) -> uuid.UUID:
        """
        Database ID of this cookie record.
        """
        if self._authenticated_on_node is None and self._from_fbs:
            if self._from_fbs.AuthenticatedOnNodeLength():
                _authenticated_on_node = self._from_fbs.AuthenticatedOnNodeAsBytes()
                self._authenticated_on_node = uuid.UUID(bytes=bytes(_authenticated_on_node))
        return self._authenticated_on_node

    @authenticated_on_node.setter
    def authenticated_on_node(self, value: uuid.UUID):
        assert value is None or isinstance(value, uuid.UUID)
        self._authenticated_on_node = value

    @property
    def authenticated_session(self) -> int:
        """
        The WAMP session ID of the original authenticating session.
        """
        if self._authenticated_session is None and self._from_fbs:
            self._authenticated_session = self._from_fbs.AuthenticatedSession()
        return self._authenticated_session

    @authenticated_session.setter
    def authenticated_session(self, value: int):
        assert value is None or type(value) == int
        self._authenticated_session = value

    @property
    def authenticated_joined_at(self) -> np.datetime64:
        """
        Timestamp when the original authenticating session was welcome by the router. Epoch time in ns.
        """
        if self._authenticated_joined_at is None and self._from_fbs:
            self._authenticated_joined_at = np.datetime64(self._from_fbs.AuthenticatedJoinedAt(), 'ns')
        return self._authenticated_joined_at

    @authenticated_joined_at.setter
    def authenticated_joined_at(self, value: np.datetime64):
        assert value is None or isinstance(value, np.datetime64)
        self._authenticated_joined_at = value

    @property
    def authenticated_authmethod(self) -> str:
        """
        The (original) WAMP authentication method, after which the client was authenticated before setting this cookie.
        """
        if self._authenticated_authmethod is None and self._from_fbs:
            _authenticated_authmethod = self._from_fbs.AuthenticatedAuthmethod()
            if _authenticated_authmethod:
                self._authenticated_authmethod = _authenticated_authmethod.decode('utf8')
        return self._authenticated_authmethod

    @authenticated_authmethod.setter
    def authenticated_authmethod(self, value: str):
        self._authenticated_authmethod = value

    @property
    def authid(self) -> str:
        """
        The WAMP authid a cookie-authenticating session is to be assigned.
        """
        if self._authid is None and self._from_fbs:
            _authid = self._from_fbs.Authid()
            if _authid:
                self._authid = _authid.decode('utf8')
        return self._authid

    @authid.setter
    def authid(self, value: str):
        self._authid = value

    @property
    def authrole(self) -> str:
        """
        The WAMP authrole a cookie-authenticating session is to join under.
        """
        if self._authrole is None and self._from_fbs:
            _authrole = self._from_fbs.Authrole()
            if _authrole:
                self._authrole = _authrole.decode('utf8')
        return self._authrole

    @authrole.setter
    def authrole(self, value: str):
        self._authrole = value

    @property
    def authrealm(self) -> str:
        """
        The WAMP realm a cookie-authenticating session is to join.
        """
        if self._authrealm is None and self._from_fbs:
            _authrealm = self._from_fbs.Authrealm()
            if _authrealm:
                self._authrealm = _authrealm.decode('utf8')
        return self._authrealm

    @authrealm.setter
    def authrealm(self, value: str):
        self._authrealm = value

    @property
    def authextra(self) -> dict:
        """
        The WAMP authentication extra data to be returned to the client performing cookie-based authentication.
        """
        if self._authextra is None and self._from_fbs:
            _authextra = self._from_fbs.AuthExtraAsBytes()
            if _authextra:
                self._authextra = cbor2.loads(_authextra)
            else:
                self._authextra = {}
        return self._authextra

    @authextra.setter
    def authextra(self, value: Optional[Dict[str, Any]]):
        assert value is None or type(value) == dict
        self._authextra = value

    @staticmethod
    def cast(buf) -> 'Cookie':
        return Cookie(_CookieGen.GetRootAsCookie(buf, 0))

    def build(self, builder):

        oid = self.oid.bytes if self.oid else None
        if oid:
            oid = builder.CreateString(oid)

        name = self.name
        if name:
            name = builder.CreateString(name)

        value = self.value
        if value:
            value = builder.CreateString(value)

        authenticated_on_node = self.authenticated_on_node.bytes if self.authenticated_on_node else None
        if authenticated_on_node:
            authenticated_on_node = builder.CreateString(authenticated_on_node)

        authenticated_authmethod = self.authenticated_authmethod
        if authenticated_authmethod:
            authenticated_authmethod = builder.CreateString(authenticated_authmethod)

        authid = self.authid
        if authid:
            authid = builder.CreateString(authid)

        authrole = self.authrole
        if authrole:
            authrole = builder.CreateString(authrole)

        authrealm = self.authrealm
        if authrealm:
            authrealm = builder.CreateString(authrealm)

        authextra = self.authextra
        if authextra:
            authextra = builder.CreateString(cbor2.dumps(authextra))

        CookieGen.CookieStart(builder)

        if oid:
            CookieGen.CookieAddOid(builder, oid)

        if self.created:
            CookieGen.CookieAddCreated(builder, int(self.created))

        if self.max_age:
            CookieGen.CookieAddMaxAge(builder, self.max_age)

        if name:
            CookieGen.CookieAddName(builder, name)

        if value:
            CookieGen.CookieAddValue(builder, value)

        if self.authenticated:
            CookieGen.CookieAddAuthenticated(builder, int(self.authenticated))

        if authenticated_on_node:
            CookieGen.CookieAddAuthenticatedOnNode(builder, authenticated_on_node)

        if self.authenticated_session:
            CookieGen.CookieAddAuthenticatedSession(builder, self.authenticated_session)

        if self.authenticated_joined_at:
            CookieGen.CookieAddAuthenticatedJoinedAt(builder, int(self.authenticated_joined_at))

        if authenticated_authmethod:
            CookieGen.CookieAddAuthenticatedAuthmethod(builder, authenticated_authmethod)

        if authid:
            CookieGen.CookieAddAuthid(builder, authid)

        if authrole:
            CookieGen.CookieAddAuthrole(builder, authrole)

        if authrealm:
            CookieGen.CookieAddAuthrealm(builder, authrealm)

        if authextra:
            CookieGen.CookieAddAuthextra(builder, authextra)

        final = CookieGen.CookieEnd(builder)

        return final


@table('62f8c8c9-c50b-4686-bafe-38b221c64a0c', build=Cookie.build, cast=Cookie.cast)
class Cookies(MapUuidFlatBuffers):
    """
    Persisted cookies table.

    Map :class:`zlmdb.MapUuidFlatBuffers` from ``cookie_oid`` to :class:`cfxdb.cookiestore.Cookie`
    """


@table('65e1d8c1-fa8b-459d-ae43-cb320d28cc97')
class CookiesByValue(MapStringUuid):
    """
    Index: cookie_value -> cookie_oid
    """
