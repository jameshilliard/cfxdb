# automatically generated by the FlatBuffers compiler, do not modify

# namespace: mrealm

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ClusterNodeMembership(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ClusterNodeMembership()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsClusterNodeMembership(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # ClusterNodeMembership
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # OID of web cluster to which to the node is added. A cluster can have zero or more nodes added.
    # ClusterNodeMembership
    def ClusterOid(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = o + self._tab.Pos
            from ..oid_t import oid_t
            obj = oid_t()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # OID of the node to add to the cluster. A node can be added to more than one cluster.
    # ClusterNodeMembership
    def NodeOid(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = o + self._tab.Pos
            from ..oid_t import oid_t
            obj = oid_t()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # The desired (maximum) parallelism (in terms of CPU usage, given as number of workers) that the node should receive if it is active (not a standby node) in this cluster.
    # ClusterNodeMembership
    def Parallel(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint16Flags, o + self._tab.Pos)
        return 0

    # Wheather this node acts as a standby node that only takes over work when an active node fails.
    # ClusterNodeMembership
    def Standby(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

def Start(builder): builder.StartObject(4)
def ClusterNodeMembershipStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddClusterOid(builder, clusterOid): builder.PrependStructSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(clusterOid), 0)
def ClusterNodeMembershipAddClusterOid(builder, clusterOid):
    """This method is deprecated. Please switch to AddClusterOid."""
    return AddClusterOid(builder, clusterOid)
def AddNodeOid(builder, nodeOid): builder.PrependStructSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(nodeOid), 0)
def ClusterNodeMembershipAddNodeOid(builder, nodeOid):
    """This method is deprecated. Please switch to AddNodeOid."""
    return AddNodeOid(builder, nodeOid)
def AddParallel(builder, parallel): builder.PrependUint16Slot(2, parallel, 0)
def ClusterNodeMembershipAddParallel(builder, parallel):
    """This method is deprecated. Please switch to AddParallel."""
    return AddParallel(builder, parallel)
def AddStandby(builder, standby): builder.PrependBoolSlot(3, standby, 0)
def ClusterNodeMembershipAddStandby(builder, standby):
    """This method is deprecated. Please switch to AddStandby."""
    return AddStandby(builder, standby)
def End(builder): return builder.EndObject()
def ClusterNodeMembershipEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)