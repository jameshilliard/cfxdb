##############################################################################
#
#                        Crossbar.io FX
#     Copyright (C) Crossbar.io Technologies GmbH. All rights reserved.
#
##############################################################################

import pprint
import uuid

import flatbuffers
import numpy as np
from autobahn.xbr import unpack_uint256, pack_uint256
from cfxdb.gen.xbrnetwork import Account as AccountGen
from zlmdb import table, MapUuidFlatBuffers, MapStringUuid, MapBytes20Uuid


class _AccountGen(AccountGen.Account):
    """
    Expand methods on the class code generated by flatc.

    FIXME: come up with a PR for flatc to generated this stuff automatically.
    """
    @classmethod
    def GetRootAsAccount(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = _AccountGen()
        x.Init(buf, n + offset)
        return x

    def OidAsBytes(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            _off = self._tab.Vector(o)
            _len = self._tab.VectorLen(o)
            return memoryview(self._tab.Bytes)[_off:_off + _len]
        return None

    def WalletAddressAsBytes(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            _off = self._tab.Vector(o)
            _len = self._tab.VectorLen(o)
            return memoryview(self._tab.Bytes)[_off:_off + _len]
        return None

    def RegisteredAsBytes(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            _off = self._tab.Vector(o)
            _len = self._tab.VectorLen(o)
            return memoryview(self._tab.Bytes)[_off:_off + _len]
        return None


class Account(object):
    """
    XBR Network members.
    """

    ACCOUNT_LEVEL_NONE = 0
    """
    Unset.
    """

    ACCOUNT_LEVEL_ACTIVE = 1
    """
    Account is active.
    """

    ACCOUNT_LEVEL_VERIFIED = 2
    """
    Account is active and verified.
    """

    ACCOUNT_LEVEL_RETIRED = 3
    """
    Account is retired.
    """

    ACCOUNT_LEVEL_PENALTY = 4
    """
    Account is subject to a temporary penalty.
    """

    ACCOUNT_LEVEL_BLOCKED = 5
    """
    Account is currently blocked and cannot current actively participate in the market.
    """

    ACCOUNT_LEVEL = list(range(6))
    """
    Valid account levels.
    """

    WALLET_TYPE_NONE = 0
    """
    Wallet type unset ("null").
    """

    WALLET_TYPE_IMPORTED = 1
    """
    Account (primary) wallet was imported (the user provided the wallet public address).
    """

    WALLET_TYPE_METAMASK = 2
    """
    Account (primary) wallet was imported (the user provided the wallet public address).
    """

    WALLET_TYPE_HOSTED = 3
    """
    Account wallet in hosted (in this database).
    """

    WALLET_TYPE = list(range(4))
    """
    Valid account wallet types.
    """

    WALLET_TYPE_TO_STRING = {
        0: 'none',
        1: 'imported',
        2: 'metamask',
        3: 'hosted',
    }
    """
    Map of ``wallet-type-code`` to ``wallet-type-name``.
    """

    WALLET_TYPE_FROM_STRING = {
        'none': 0,
        'imported': 1,
        'metamask': 2,
        'hosted': 3,
    }
    """
    Map of ``wallet-type-name`` to ``wallet-type-code``.
    """
    def __init__(self, from_fbs=None):
        self._from_fbs = from_fbs

        # Globally unique and static member ID.
        # [uint8] (uuid)
        self._oid = None

        # Timestamp (epoch time in ns) of initial creation of this record.
        # uint64 (timestamp)
        self._created = None

        # XBR Network username (must be globall unique on https://xbr.network)
        # string
        self._username = None

        # User (primary) email address.
        # string
        self._email = None

        # Timestamp (epoch time in ns) when the user email was (last) verified or 0 if unverified.
        # uint64 (timestamp)
        self._email_verified = None

        # Type of (primary) user crypto wallet in use.
        # WalletType
        self._wallet_type = None

        # Public address of user crypto wallet in use.
        # [uint8] (address)
        self._wallet_address = None

        # Block number (on the blockchain) when the member (originally) registered.
        # [uint8] (uint256)
        self._registered = None

        # EULA the member agreed to when joining the market (IPFS Multihash string).
        # string (multihash)
        self._eula = None

        # Optional member profile (IPFS Multihash string).
        # string (multihash)
        self._profile = None

        # Current member level.
        # AccountLevel
        self._level = None

    def marshal(self):
        obj = {
            'oid': self.oid.bytes if self.oid else None,
            'created': int(self.created) if self.created else None,
            'username': self.username,
            'email': self.email,
            'email_verified': int(self.email_verified) if self.email_verified is not None else None,
            'wallet_type': self.wallet_type,
            'wallet_address': bytes(self.wallet_address) if self.wallet_address else None,
            'registered': int(self.registered) if self.registered else None,
            'eula': self.eula,
            'profile': self.profile,
            'level': self.level,
        }
        return obj

    def __str__(self):
        return '\n{}\n'.format(pprint.pformat(self.marshal()))

    @property
    def oid(self) -> uuid.UUID:
        """
        Globally unique and static member ID.
        """
        if self._oid is None and self._from_fbs:
            if self._from_fbs.OidLength():
                _oid = self._from_fbs.OidAsBytes()
                self._oid = uuid.UUID(bytes=bytes(_oid))
            else:
                self._oid = uuid.UUID(bytes=b'\x00' * 20)
        return self._oid

    @oid.setter
    def oid(self, value: uuid.UUID):
        assert value is None or isinstance(value, uuid.UUID)
        self._oid = value

    @property
    def created(self) -> np.datetime64:
        """
        Timestamp (epoch time in ns) of initial creation of this record.
        """
        if self._created is None and self._from_fbs:
            self._created = np.datetime64(self._from_fbs.Created(), 'ns')
        return self._created

    @created.setter
    def created(self, value: np.datetime64):
        assert value is None or isinstance(value, np.datetime64)
        self._created = value

    @property
    def username(self) -> str:
        """
        XBR Network username (must be globally unique on https://xbr.network)
        """
        if self._username is None and self._from_fbs:
            username = self._from_fbs.Username()
            if username:
                self._username = username.decode('utf8')
        return self._username

    @username.setter
    def username(self, value: str):
        assert value is None or type(value) == str
        self._username = value

    @property
    def email(self) -> str:
        """
        User (primary) email address.
        """
        if self._email is None and self._from_fbs:
            email = self._from_fbs.Email()
            if email:
                self._email = email.decode('utf8')
        return self._email

    @email.setter
    def email(self, value: str):
        assert value is None or type(value) == str
        self._email = value

    @property
    def email_verified(self) -> np.datetime64:
        """
        Timestamp (epoch time in ns) when the user email was (last) verified or 0 if unverified.
        """
        if self._email_verified is None and self._from_fbs:
            self._email_verified = np.datetime64(self._from_fbs.EmailVerified(), 'ns')
        return self._email_verified

    @email_verified.setter
    def email_verified(self, value: np.datetime64):
        assert value is None or isinstance(value, np.datetime64)
        self._email_verified = value

    @property
    def wallet_type(self) -> int:
        """
        Type of (primary) user crypto wallet in use.
        """
        if self._wallet_type is None and self._from_fbs:
            self._wallet_type = self._from_fbs.WalletType()
        return self._wallet_type or 0

    @wallet_type.setter
    def wallet_type(self, value: int):
        assert value is None or type(value) == int
        self._wallet_type = value

    @property
    def wallet_address(self) -> bytes:
        """
        Public address of user crypto wallet in use.
        """
        if self._wallet_address is None and self._from_fbs:
            if self._from_fbs.WalletAddressLength():
                self._wallet_address = self._from_fbs.WalletAddressAsBytes()
        return self._wallet_address

    @wallet_address.setter
    def wallet_address(self, value: bytes):
        assert value is None or (type(value) == bytes and len(value) == 20)
        self._wallet_address = value

    @property
    def registered(self) -> int:
        """
        Block number (on the blockchain) when the member (originally) registered.
        """
        if self._registered is None and self._from_fbs:
            if self._from_fbs.RegisteredLength():
                _registered = self._from_fbs.RegisteredAsBytes()
                self._registered = unpack_uint256(bytes(_registered))
            else:
                self._registered = 0
        return self._registered

    @registered.setter
    def registered(self, value: int):
        assert value is None or type(value) == int
        self._registered = value

    @property
    def eula(self) -> str:
        """
        EULA the member agreed to when joining the market (IPFS Multihash string).
        """
        if self._eula is None and self._from_fbs:
            eula = self._from_fbs.Eula()
            if eula:
                self._eula = eula.decode('utf8')
        return self._eula

    @eula.setter
    def eula(self, value: str):
        assert value is None or type(value) == str
        self._eula = value

    @property
    def profile(self) -> str:
        """
        Optional member profile (IPFS Multihash string).
        """
        if self._profile is None and self._from_fbs:
            profile = self._from_fbs.Profile()
            if profile:
                self._profile = profile.decode('utf8')
        return self._profile

    @profile.setter
    def profile(self, value: str):
        assert value is None or type(value) == str
        self._profile = value

    @property
    def level(self) -> int:
        """
        Current member level.
        """
        if self._level is None and self._from_fbs:
            self._level = self._from_fbs.Level()
        return self._level

    @level.setter
    def level(self, value: int):
        assert value is None or type(value) == int
        self._level = value

    @staticmethod
    def cast(buf):
        return Account(_AccountGen.GetRootAsAccount(buf, 0))

    def build(self, builder):

        oid = self.oid.bytes if self.oid else None
        if oid:
            oid = builder.CreateString(oid)

        username = self.username
        if username:
            username = builder.CreateString(username)

        email = self.email
        if email:
            email = builder.CreateString(email)

        wallet_address = self.wallet_address
        if wallet_address:
            wallet_address = builder.CreateString(wallet_address)

        registered = self.registered
        if registered:
            registered = builder.CreateString(pack_uint256(registered))

        eula = self.eula
        if eula:
            eula = builder.CreateString(eula)

        profile = self.profile
        if profile:
            profile = builder.CreateString(profile)

        AccountGen.AccountStart(builder)

        if oid:
            AccountGen.AccountAddOid(builder, oid)

        if self.created:
            AccountGen.AccountAddCreated(builder, int(self.created))

        if username:
            AccountGen.AccountAddUsername(builder, username)

        if email:
            AccountGen.AccountAddEmail(builder, email)

        if self.email_verified:
            AccountGen.AccountAddEmailVerified(builder, int(self.email_verified))

        if self.wallet_type:
            AccountGen.AccountAddWalletType(builder, self.wallet_type)

        if wallet_address:
            AccountGen.AccountAddWalletAddress(builder, wallet_address)

        if registered:
            AccountGen.AccountAddRegistered(builder, registered)

        if eula:
            AccountGen.AccountAddEula(builder, eula)

        if profile:
            AccountGen.AccountAddProfile(builder, profile)

        if self.level:
            AccountGen.AccountAddLevel(builder, self.level)

        final = AccountGen.AccountEnd(builder)

        return final


@table('d155dff2-ac36-4c69-b1b0-254ce2eb237d', build=Account.build, cast=Account.cast)
class Accounts(MapUuidFlatBuffers):
    """
    Database table for XBR member accounts.
    """
    @staticmethod
    def parse(data):
        """

        :param data:
        :return:
        """
        oid = None
        if 'oid' in data:
            assert type(data['oid'] == bytes and len(data['oid']) == 16)
            oid = uuid.UUID(bytes=data['oid'])

        created = None
        if 'created' in data:
            assert type(data['created'] == int)
            created = np.datetime64(data['created'], 'ns')

        username = None
        if 'username' in data:
            assert type(data['username'] == str)
            username = data['username']

        email = None
        if 'email' in data:
            assert type(data['email'] == str)
            email = data['email']

        email_verified = None
        if 'email_verified' in data:
            assert type(data['email_verified'] == int)
            email_verified = np.datetime64(data['email_verified'], 'ns')

        wallet_type = None
        if 'wallet_type' in data:
            assert type(data['wallet_type'] == int)
            wallet_type = data['wallet_type']

        wallet_address = None
        if 'wallet_address' in data:
            assert type(data['wallet_address'] == bytes and len(data['wallet_address']) == 20)
            wallet_address = data['wallet_address']

        registered = None
        if 'registered' in data:
            assert type(data['registered'] == int)
            registered = data['registered']

        eula = None
        if 'eula' in data:
            assert type(data['eula'] == str)
            eula = data['eula']

        profile = None
        if 'profile' in data:
            assert type(data['profile'] == str)
            profile = data['profile']

        level = None
        if 'level' in data:
            assert type(data['level'] == int)
            level = data['level']

        obj = Account()
        obj.oid = oid
        obj.created = created
        obj.username = username
        obj.email = email
        obj.email_verified = email_verified
        obj.wallet_type = wallet_type
        obj.wallet_address = wallet_address
        obj.registered = registered
        obj.eula = eula
        obj.profile = profile
        obj.level = level

        return obj


@table('760d42a0-110e-474b-ab85-6e2396af035d')
class IndexAccountsByUsername(MapStringUuid):
    """
    Database (index) table for username-to-account mapping.
    """


@table('76706b89-8639-491e-8989-afc5a7c8a5b4')
class IndexAccountsByEmail(MapStringUuid):
    """
    Database (index) table for (user-)email-to-account mapping.
    """


@table('432ae4fa-a23e-45d7-b2a4-c9ae868df2b3')
class IndexAccountsByWallet(MapBytes20Uuid):
    """
    Database (index) table for (user-)wallet-to-account mapping.
    """
