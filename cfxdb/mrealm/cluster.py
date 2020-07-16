##############################################################################
#
#                        Crossbar.io FX
#     Copyright (C) Crossbar.io Technologies GmbH. All rights reserved.
#
##############################################################################

import pprint

from cfxdb.common import ConfigurationElement
from cfxdb.gen.mrealm.ClusterStatus import ClusterStatus

STATUS_BY_CODE = {
    ClusterStatus.NONE: 'NONE',
    ClusterStatus.STOPPED: 'STOPPED',
    ClusterStatus.STARTING: 'STARTING',
    ClusterStatus.RUNNING: 'RUNNING',
    ClusterStatus.PAUSED: 'PAUSED',
    ClusterStatus.STOPPING: 'STOPPING',
    ClusterStatus.ERROR: 'ERROR',
    ClusterStatus.DEGRADED: 'DEGRADED',
}

STATUS_BY_NAME = {
    'NONE': ClusterStatus.NONE,
    'STOPPED': ClusterStatus.STOPPED,
    'STARTING': ClusterStatus.STARTING,
    'RUNNING': ClusterStatus.RUNNING,
    'PAUSED': ClusterStatus.PAUSED,
    'STOPPING': ClusterStatus.STOPPING,
    'ERROR': ClusterStatus.ERROR,
    'DEGRADED': ClusterStatus.DEGRADED,
}

STATUS_STOPPED = ClusterStatus.STOPPED
STATUS_STARTING = ClusterStatus.STARTING
STATUS_RUNNING = ClusterStatus.RUNNING
STATUS_PAUSED = ClusterStatus.PAUSED
STATUS_STOPPING = ClusterStatus.STOPPING
STATUS_ERROR = ClusterStatus.ERROR
STATUS_DEGRADED = ClusterStatus.DEGRADED


class Cluster(ConfigurationElement):
    """
    CFC Cluster database configuration object.
    """
    def __init__(self,
                 oid=None,
                 label=None,
                 description=None,
                 tags=None,
                 name=None,
                 status=None,
                 changed=None,
                 _unknown=None):
        """

        :param oid: Object ID of node
        :type oid: uuid.UUID

        :param label: Optional user label of node
        :type label: str

        :param description: Optional user description of node
        :type description: str

        :param tags: Optional list of user tags on node
        :type tags: list[str]

        :param _unknown: Any unparsed/unprocessed data attributes
        :type _unknown: None or dict
        """
        ConfigurationElement.__init__(self, oid=oid, label=label, description=description, tags=tags)
        self.name = name
        self.status = status
        self.changed = changed

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if not ConfigurationElement.__eq__(self, other):
            return False
        if other.name != self.name:
            return False
        if other.status != self.status:
            return False
        if other.changed != self.changed:
            return False
        return True

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return '\n{}\n'.format(pprint.pformat(self.marshal()))

    def marshal(self):
        """
        Marshal this object to a generic host language object.

        :return: dict
        """
        assert self.name is None or type(self.name) == str
        assert self.status is None or type(self.status) == int
        assert self.changed is None or type(self.changed) == int

        obj = ConfigurationElement.marshal(self)

        obj.update({
            u'name': self.name,
            u'status': STATUS_BY_CODE[self.status],
            u'changed': self.changed,
        })

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
            if k not in ['name', 'status', 'changed']:
                _unknown[k] = data[k]

        name = data.get('name', None)
        assert name is None or (type(name) == str)

        status = data.get('status', None)
        assert status is None or (type(status) == str)
        status = STATUS_BY_NAME.get(status, None)

        changed = data.get('changed', None)
        assert changed is None or (type(changed) == int)

        obj = Cluster(oid=obj.oid,
                      label=obj.label,
                      description=obj.description,
                      tags=obj.tags,
                      name=name,
                      status=status,
                      changed=changed,
                      _unknown=_unknown)

        return obj
