##############################################################################
#
#                        Crossbar.io FX
#     Copyright (C) Crossbar.io Technologies GmbH. All rights reserved.
#
##############################################################################

import uuid
import pprint


class RouterWorkerGroupClusterPlacement(object):
    """
    Information about membership of a managed node in a management realm to a "router cluster".
    A router cluster is able to run "data planes", which are groups of router workers kept in sync,
    and meshed via router-to-router links. Finally, "(application) realms" can be started in data planes.
    """
    def __init__(self,
                 oid=None,
                 worker_group_oid=None,
                 cluster_oid=None,
                 node_oid=None,
                 worker_name=None,
                 _unknown=None):
        self.oid = oid
        self.worker_group_oid = worker_group_oid
        self.cluster_oid = cluster_oid
        self.node_oid = node_oid
        self.worker_name = worker_name
        self._unknown = _unknown

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if other.oid != self.oid:
            return False
        if other.worker_group_oid != self.worker_group_oid:
            return False
        if other.cluster_oid != self.cluster_oid:
            return False
        if other.node_oid != self.node_oid:
            return False
        if other.worker_name != self.worker_name:
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
        obj = {
            'oid': str(self.oid),
            'worker_group_oid': str(self.worker_group_oid),
            'cluster_oid': str(self.cluster_oid),
            'node_oid': str(self.node_oid),
            'worker_name': self.worker_name,
        }
        return obj

    @staticmethod
    def parse(data):
        """
        Parse generic host language object into an object of this class.

        :param data: Generic host language object
        :type data: dict

        :return: instance of :class:`WebService`
        """
        assert type(data) == dict

        # future attributes (yet unknown) are not only ignored, but passed through!
        _unknown = {}
        for k in data:
            if k not in ['oid', 'worker_group_oid', 'cluster_oid', 'node_oid', 'worker_name']:
                _unknown[k] = data[k]

        oid = None
        if 'oid' in data:
            assert type(data['oid']) == str
            oid = uuid.UUID(data['oid'])

        worker_group_oid = None
        if 'worker_group_oid' in data:
            assert type(data['worker_group_oid']) == str
            worker_group_oid = uuid.UUID(data['worker_group_oid'])

        cluster_oid = None
        if 'cluster_oid' in data:
            assert type(data['cluster_oid']) == str
            cluster_oid = uuid.UUID(data['cluster_oid'])

        node_oid = None
        if 'node_oid' in data:
            assert type(data['node_oid']) == str
            node_oid = uuid.UUID(data['node_oid'])

        worker_name = None
        if 'worker_name' in data:
            assert type(data['worker_name']) == str
            worker_name = data['worker_name']

        obj = RouterWorkerGroupClusterPlacement(oid=oid,
                                                worker_group_oid=worker_group_oid,
                                                cluster_oid=cluster_oid,
                                                worker_name=worker_name,
                                                node_oid=node_oid,
                                                _unknown=_unknown)

        return obj
