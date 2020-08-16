##############################################################################
#
#                        Crossbar.io FX
#     Copyright (C) Crossbar.io Technologies GmbH. All rights reserved.
#
##############################################################################

from typing import Optional
import pprint
from uuid import UUID

import numpy as np


class Credential(object):
    """
    Credentials created for use with WAMP authentication.
    """
    def __init__(self,
                 oid: Optional[UUID] = None,
                 created: Optional[np.datetime64] = None,
                 authmethod: Optional[str] = None,
                 authid: Optional[str] = None,
                 realm: Optional[str] = None,
                 authconfig: Optional[dict] = None,
                 principal_oid: Optional[UUID] = None,
                 _unknown=None):
        """

        :param oid: Object ID of this credential object

        :param created: Timestamp when credential was created.

        :param authmethod: WAMP authentication method offered by the authenticating client.

        :param realm: WAMP realm requested by the authenticating client.

        :param authid: WAMP authid announced by the authenticating client.

        :param authconfig: Authentication method specific configuration.

        :param principal_oid: ID of the principal this credential resolves to upon successful authentication.
        """
        self.oid = oid
        self.created = created
        self.authmethod = authmethod
        self.realm = realm
        self.authid = authid
        self.authconfig = authconfig
        self.principal_oid = principal_oid

        # private member with unknown/untouched data passing through
        self._unknown = _unknown

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if other.oid != self.oid:
            return False
        if other.created != self.created:
            return False
        if other.authmethod != self.authmethod:
            return False
        if other.realm != self.realm:
            return False
        if other.authid != self.authid:
            return False
        if other.authconfig != self.authconfig:
            return False
        if other.principal_oid != self.principal_oid:
            return False
        return True

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return pprint.pformat(self.marshal())

    def copy(self, other, overwrite=False):
        """
        Copy over other object.

        :param other: Other credential to copy data from.
        :type other: instance of :class:`ManagementRealm`
        :return:
        """
        if (not self.oid and other.oid) or overwrite:
            self.oid = other.oid
        if (not self.created and other.created) or overwrite:
            self.created = other.created
        if (not self.authmethod and other.authmethod) or overwrite:
            self.authmethod = other.authmethod
        if (not self.realm and other.realm) or overwrite:
            self.realm = other.realm
        if (not self.authid and other.authid) or overwrite:
            self.authid = other.authid
        if (not self.authconfig and other.authconfig) or overwrite:
            self.authconfig = other.authconfig
        if (not self.principal_oid and other.principal_oid) or overwrite:
            self.principal_oid = other.principal_oid

        # _unknown is not copied!

    def marshal(self):
        """
        Marshal this object to a generic host language object.

        :return: dict
        """
        obj = {
            'oid': str(self.oid) if self.oid else None,
            'created': int(self.created) if self.created else None,
            'authmethod': self.authmethod,
            'realm': self.realm,
            'authid': self.authid,
            'authconfig': self.authconfig,
            'principal_oid': str(self.principal_oid) if self.principal_oid else None,
        }

        if self._unknown:
            # pass through all attributes unknown
            obj.update(self._unknown)

        return obj

    @staticmethod
    def parse(data):
        """
        Parse generic host language object into an object of this class.

        :param data: Generic host language object
        :type data: dict

        :return: instance of :class:`ManagementRealm`
        """
        assert type(data) == dict

        # future attributes (yet unknown) are not only ignored, but passed through!
        _unknown = {}
        for k in data:
            if k not in ['oid', 'created', 'authmethod', 'realm', 'authid', 'authconfig', 'principal_oid']:
                _unknown[k] = data[k]

        oid = data.get('oid', None)
        assert oid is None or type(oid) == str
        if oid:
            oid = UUID(oid)

        created = data.get('created', None)
        assert created is None or type(created) == int
        if created:
            created = np.datetime64(created, 'ns')

        authmethod = data.get('authmethod', None)
        assert authmethod is None or type(authmethod) == str

        realm = data.get('realm', None)
        assert realm is None or type(realm) == str

        authid = data.get('authid', None)
        assert authid is None or type(authid) == str

        authconfig = data.get('authconfig', None)
        assert authconfig is None or type(authconfig) == dict

        principal_oid = data.get('principal_oid', None)
        assert principal_oid is None or type(principal_oid) == str
        if principal_oid:
            principal_oid = UUID(principal_oid)

        obj = Credential(oid=oid,
                         created=created,
                         authmethod=authmethod,
                         realm=realm,
                         authid=authid,
                         authconfig=authconfig,
                         principal_oid=principal_oid,
                         _unknown=_unknown)

        return obj
