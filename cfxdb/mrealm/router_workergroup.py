##############################################################################
#
#                        Crossbar.io FX
#     Copyright (C) Crossbar.io Technologies GmbH. All rights reserved.
#
##############################################################################

import pprint

from cfxdb.common import ConfigurationElement
from cfxdb.gen.mrealm.WorkerGroupStatus import WorkerGroupStatus

STATUS_BY_CODE = {
    WorkerGroupStatus.NONE: 'NONE',
    WorkerGroupStatus.STOPPED: 'STOPPED',
    WorkerGroupStatus.STARTING: 'STARTING',
    WorkerGroupStatus.RUNNING: 'RUNNING',
    WorkerGroupStatus.PAUSED: 'PAUSED',
    WorkerGroupStatus.STOPPING: 'STOPPING',
    WorkerGroupStatus.ERROR: 'ERROR',
    WorkerGroupStatus.DEGRADED: 'DEGRADED',
}

STATUS_BY_NAME = {
    'NONE': WorkerGroupStatus.NONE,
    'STOPPED': WorkerGroupStatus.STOPPED,
    'STARTING': WorkerGroupStatus.STARTING,
    'RUNNING': WorkerGroupStatus.RUNNING,
    'PAUSED': WorkerGroupStatus.PAUSED,
    'STOPPING': WorkerGroupStatus.STOPPING,
    'ERROR': WorkerGroupStatus.ERROR,
    'DEGRADED': WorkerGroupStatus.DEGRADED,
}

STATUS_STOPPED = WorkerGroupStatus.STOPPED
STATUS_STARTING = WorkerGroupStatus.STARTING
STATUS_RUNNING = WorkerGroupStatus.RUNNING
STATUS_PAUSED = WorkerGroupStatus.PAUSED
STATUS_STOPPING = WorkerGroupStatus.STOPPING
STATUS_ERROR = WorkerGroupStatus.ERROR
STATUS_DEGRADED = WorkerGroupStatus.DEGRADED


class RouterWorkerGroup(ConfigurationElement):
    """
    Router worker group database configuration object.
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

        :param oid: Object ID of router worker group.
        :type oid: uuid.UUID

        :param label: Optional user label of router worker group.
        :type label: str

        :param description: Optional user description of router worker group.
        :type description: str

        :param tags: Optional list of user tags on router worker group.
        :type tags: list[str]

        :param _unknown: Any unparsed/unprocessed data attributes
        :type _unknown: None or dict
        """
        ConfigurationElement.__init__(self,
                                      oid=oid,
                                      label=label,
                                      description=description,
                                      tags=tags,
                                      _unknown=_unknown)
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
        return pprint.pformat(self.marshal())

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
            'name': self.name,
            'status': STATUS_BY_CODE[self.status] if self.status else None,
            'changed': self.changed,
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
        data = obj._unknown or {}

        # future attributes (yet unknown) are not only ignored, but passed through!
        _unknown = dict()
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

        obj = RouterWorkerGroup(oid=obj.oid,
                                label=obj.label,
                                description=obj.description,
                                tags=obj.tags,
                                name=name,
                                status=status,
                                changed=changed,
                                _unknown=_unknown)

        return obj
