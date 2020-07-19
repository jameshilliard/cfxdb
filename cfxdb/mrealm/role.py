##############################################################################
#
#                        Crossbar.io FX
#     Copyright (C) Crossbar.io Technologies GmbH. All rights reserved.
#
##############################################################################

import pprint
import uuid
from datetime import datetime

import six

from cfxdb.common import ConfigurationElement


class Role(ConfigurationElement):
    """
    CFC management realm database configuration object.
    """
    def __init__(self,
                 oid=None,
                 label=None,
                 description=None,
                 tags=None,
                 name=None,
                 created=None,
                 owner=None,
                 _unknown=None):
        """

        :param oid: Object ID of management realm
        :type oid: uuid.UUID

        :param label: Optional user label of management realm
        :type label: str

        :param description: Optional user description of management realm
        :type description: str

        :param tags: Optional list of user tags on management realm
        :type tags: list[str]

        :param name: Name of management realm
        :type name: str

        :param created: Timestamp when the management realm was created
        :type created: datetime.datetime

        :param owner: Owning user (object ID)
        :type owner: uuid.UUID

       :param _unknown: Any unparsed/unprocessed data attributes
        :type _unknown: None or dict
        """
        ConfigurationElement.__init__(self, oid=oid, label=label, description=description, tags=tags)
        self.name = name
        self.created = created
        self.owner = owner

        # private member with unknown/untouched data passing through
        self._unknown = _unknown

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if not ConfigurationElement.__eq__(self, other):
            return False
        if other.name != self.name:
            return False
        if other.created != self.created:
            return False
        if other.owner != self.owner:
            return False
        return True

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return pprint.pformat(self.marshal())

    def copy(self, other, overwrite=False):
        """
        Copy over other object.

        :param other: Other management realm to copy data from.
        :type other: instance of :class:`ManagementRealm`
        :return:
        """
        ConfigurationElement.copy(self, other, overwrite=overwrite)

        if (not self.name and other.name) or overwrite:
            self.name = other.name
        if (not self.created and other.created) or overwrite:
            self.created = other.created
        if (not self.owner and other.owner) or overwrite:
            self.owner = other.owner

        # _unknown is not copied!

    def marshal(self):
        """
        Marshal this object to a generic host language object.

        :return: dict
        """
        assert isinstance(self.oid, uuid.UUID)
        assert type(self.name) == six.text_type
        assert isinstance(self.created, datetime)
        assert isinstance(self.owner, uuid.UUID)

        obj = ConfigurationElement.marshal(self)

        obj.update({
            'oid': str(self.oid),
            'name': self.name,
            'created': int(self.created.timestamp() * 1000000) if self.created else None,
            'owner': str(self.owner),
        })

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

        obj = ConfigurationElement.parse(data)
        data = obj._unknown

        # future attributes (yet unknown) are not only ignored, but passed through!
        _unknown = {}
        for k in data:
            if k not in ['oid', 'name', 'owner', 'created']:
                _unknown[k] = data[k]

        name = data.get('name', None)
        assert name is None or type(name) == six.text_type

        owner = data.get('owner', None)
        assert owner is None or type(owner) == six.text_type
        if owner:
            owner = uuid.UUID(owner)

        created = data.get('created', None)
        assert created is None or type(created) == float or type(created) in six.integer_types
        if created:
            created = datetime.utcfromtimestamp(float(created) / 1000000.)

        obj = Role(oid=obj.oid,
                   label=obj.label,
                   description=obj.description,
                   tags=obj.tags,
                   name=name,
                   owner=owner,
                   created=created,
                   _unknown=_unknown)

        return obj
