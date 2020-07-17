##############################################################################
#
#                        Crossbar.io FX
#     Copyright (C) Crossbar.io Technologies GmbH. All rights reserved.
#
##############################################################################

import pprint
import uuid

import six


class ClusterNodeMembership(object):
    def __init__(self, cluster_oid=None, node_oid=None, _unknown=None):
        self.cluster_oid = cluster_oid
        self.node_oid = node_oid
        self._unknown = _unknown

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if other.cluster_oid != self.cluster_oid:
            return False
        if other.node_oid != self.node_oid:
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
            'cluster_oid': str(self.cluster_oid),
            'node_oid': str(self.node_oid),
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
            if k not in ['cluster_oid', 'node_oid']:
                _unknown[k] = data[k]

        cluster_oid = None
        if 'cluster_oid' in data:
            assert type(data['cluster_oid']) == six.text_type
            cluster_oid = uuid.UUID(data['cluster_oid'])

        node_oid = None
        if 'node_oid' in data:
            assert type(data['node_oid']) == six.text_type
            node_oid = uuid.UUID(data['node_oid'])

        obj = ClusterNodeMembership(cluster_oid=cluster_oid, node_oid=node_oid, _unknown=_unknown)

        return obj
