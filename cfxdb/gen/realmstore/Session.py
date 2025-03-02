# automatically generated by the FlatBuffers compiler, do not modify

# namespace: realmstore

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

# This table stores WAMP sessions and serves as an anchor for all usage related data.
class Session(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Session()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsSession(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # Session
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # OID of the application realm this session is/was joined on.
    # Session
    def ArealmOid(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # Session
    def ArealmOidAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint8Flags, o)
        return 0

    # Session
    def ArealmOidLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Session
    def ArealmOidIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        return o == 0

    # Unlimited time, globally unique, long-term OID of this session. The pair of WAMP session ID and join time ``(session, joined_at)`` bidirectionally maps to session ``oid``.
    # Session
    def Oid(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # Session
    def OidAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint8Flags, o)
        return 0

    # Session
    def OidLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Session
    def OidIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        return o == 0

    # The WAMP session_id of the session.
    # Session
    def Session(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # Timestamp when the session was joined by the router. Epoch time in ns.
    # Session
    def JoinedAt(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # Timestamp when the session left the router. Epoch time in ns.
    # Session
    def LeftAt(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # OID of the node of the router worker hosting this session.
    # Session
    def NodeOid(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # Session
    def NodeOidAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint8Flags, o)
        return 0

    # Session
    def NodeOidLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Session
    def NodeOidIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        return o == 0

    # Name (management realm WAMP authid) of the node of the router worker hosting this session.
    # Session
    def NodeAuthid(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # Local worker name of the router worker hosting this session.
    # Session
    def WorkerName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # Local worker PID of the router worker hosting this session.
    # Session
    def WorkerPid(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # Session transport information, the incoming frontend client connection in proxy-router setups. This is also returned as part of authextra to the client.
    # Session
    def Transport(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # Session
    def TransportAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint8Flags, o)
        return 0

    # Session
    def TransportLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Session
    def TransportIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        return o == 0

    # From proxy (in proxy-router cluster setups): OID of the node of the proxy worker hosting this session.
    # Session
    def ProxyNodeOid(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # Session
    def ProxyNodeOidAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint8Flags, o)
        return 0

    # Session
    def ProxyNodeOidLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Session
    def ProxyNodeOidIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        return o == 0

    # From proxy (in proxy-router cluster setups): Name (management realm WAMP authid) of the node of the proxy worker hosting this session.
    # Session
    def ProxyNodeAuthid(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # From proxy (in proxy-router cluster setups): Local worker name of the proxy worker hosting this session.
    # Session
    def ProxyWorkerName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # From proxy (in proxy-router cluster setups): Local worker PID of the proxy worker hosting this session.
    # Session
    def ProxyWorkerPid(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # From proxy (in proxy-router cluster setups): Session transport information, the transport from the proxy to the backend router.
    # Session
    def ProxyTransport(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # Session
    def ProxyTransportAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint8Flags, o)
        return 0

    # Session
    def ProxyTransportLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Session
    def ProxyTransportIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        return o == 0

    # The WAMP realm (name) the session is/was joined on.
    # Session
    def Realm(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # The WAMP authid the session was authenticated under.
    # Session
    def Authid(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # The WAMP authrole the session was authenticated under.
    # Session
    def Authrole(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # The WAMP authmethod uses to authenticate the session.
    # Session
    def Authmethod(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # The WAMP authprovider that was handling the session authentication.
    # Session
    def Authprovider(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(42))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # The WAMP authextra as provided to the authenticated session.
    # Session
    def Authextra(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(44))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # Session
    def AuthextraAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(44))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint8Flags, o)
        return 0

    # Session
    def AuthextraLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(44))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Session
    def AuthextraIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(44))
        return o == 0

def Start(builder): builder.StartObject(21)
def SessionStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddArealmOid(builder, arealmOid): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(arealmOid), 0)
def SessionAddArealmOid(builder, arealmOid):
    """This method is deprecated. Please switch to AddArealmOid."""
    return AddArealmOid(builder, arealmOid)
def StartArealmOidVector(builder, numElems): return builder.StartVector(1, numElems, 1)
def SessionStartArealmOidVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartArealmOidVector(builder, numElems)
def AddOid(builder, oid): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(oid), 0)
def SessionAddOid(builder, oid):
    """This method is deprecated. Please switch to AddOid."""
    return AddOid(builder, oid)
def StartOidVector(builder, numElems): return builder.StartVector(1, numElems, 1)
def SessionStartOidVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartOidVector(builder, numElems)
def AddSession(builder, session): builder.PrependUint64Slot(2, session, 0)
def SessionAddSession(builder, session):
    """This method is deprecated. Please switch to AddSession."""
    return AddSession(builder, session)
def AddJoinedAt(builder, joinedAt): builder.PrependUint64Slot(3, joinedAt, 0)
def SessionAddJoinedAt(builder, joinedAt):
    """This method is deprecated. Please switch to AddJoinedAt."""
    return AddJoinedAt(builder, joinedAt)
def AddLeftAt(builder, leftAt): builder.PrependUint64Slot(4, leftAt, 0)
def SessionAddLeftAt(builder, leftAt):
    """This method is deprecated. Please switch to AddLeftAt."""
    return AddLeftAt(builder, leftAt)
def AddNodeOid(builder, nodeOid): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(nodeOid), 0)
def SessionAddNodeOid(builder, nodeOid):
    """This method is deprecated. Please switch to AddNodeOid."""
    return AddNodeOid(builder, nodeOid)
def StartNodeOidVector(builder, numElems): return builder.StartVector(1, numElems, 1)
def SessionStartNodeOidVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartNodeOidVector(builder, numElems)
def AddNodeAuthid(builder, nodeAuthid): builder.PrependUOffsetTRelativeSlot(6, flatbuffers.number_types.UOffsetTFlags.py_type(nodeAuthid), 0)
def SessionAddNodeAuthid(builder, nodeAuthid):
    """This method is deprecated. Please switch to AddNodeAuthid."""
    return AddNodeAuthid(builder, nodeAuthid)
def AddWorkerName(builder, workerName): builder.PrependUOffsetTRelativeSlot(7, flatbuffers.number_types.UOffsetTFlags.py_type(workerName), 0)
def SessionAddWorkerName(builder, workerName):
    """This method is deprecated. Please switch to AddWorkerName."""
    return AddWorkerName(builder, workerName)
def AddWorkerPid(builder, workerPid): builder.PrependInt32Slot(8, workerPid, 0)
def SessionAddWorkerPid(builder, workerPid):
    """This method is deprecated. Please switch to AddWorkerPid."""
    return AddWorkerPid(builder, workerPid)
def AddTransport(builder, transport): builder.PrependUOffsetTRelativeSlot(9, flatbuffers.number_types.UOffsetTFlags.py_type(transport), 0)
def SessionAddTransport(builder, transport):
    """This method is deprecated. Please switch to AddTransport."""
    return AddTransport(builder, transport)
def StartTransportVector(builder, numElems): return builder.StartVector(1, numElems, 1)
def SessionStartTransportVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartTransportVector(builder, numElems)
def AddProxyNodeOid(builder, proxyNodeOid): builder.PrependUOffsetTRelativeSlot(10, flatbuffers.number_types.UOffsetTFlags.py_type(proxyNodeOid), 0)
def SessionAddProxyNodeOid(builder, proxyNodeOid):
    """This method is deprecated. Please switch to AddProxyNodeOid."""
    return AddProxyNodeOid(builder, proxyNodeOid)
def StartProxyNodeOidVector(builder, numElems): return builder.StartVector(1, numElems, 1)
def SessionStartProxyNodeOidVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartProxyNodeOidVector(builder, numElems)
def AddProxyNodeAuthid(builder, proxyNodeAuthid): builder.PrependUOffsetTRelativeSlot(11, flatbuffers.number_types.UOffsetTFlags.py_type(proxyNodeAuthid), 0)
def SessionAddProxyNodeAuthid(builder, proxyNodeAuthid):
    """This method is deprecated. Please switch to AddProxyNodeAuthid."""
    return AddProxyNodeAuthid(builder, proxyNodeAuthid)
def AddProxyWorkerName(builder, proxyWorkerName): builder.PrependUOffsetTRelativeSlot(12, flatbuffers.number_types.UOffsetTFlags.py_type(proxyWorkerName), 0)
def SessionAddProxyWorkerName(builder, proxyWorkerName):
    """This method is deprecated. Please switch to AddProxyWorkerName."""
    return AddProxyWorkerName(builder, proxyWorkerName)
def AddProxyWorkerPid(builder, proxyWorkerPid): builder.PrependInt32Slot(13, proxyWorkerPid, 0)
def SessionAddProxyWorkerPid(builder, proxyWorkerPid):
    """This method is deprecated. Please switch to AddProxyWorkerPid."""
    return AddProxyWorkerPid(builder, proxyWorkerPid)
def AddProxyTransport(builder, proxyTransport): builder.PrependUOffsetTRelativeSlot(14, flatbuffers.number_types.UOffsetTFlags.py_type(proxyTransport), 0)
def SessionAddProxyTransport(builder, proxyTransport):
    """This method is deprecated. Please switch to AddProxyTransport."""
    return AddProxyTransport(builder, proxyTransport)
def StartProxyTransportVector(builder, numElems): return builder.StartVector(1, numElems, 1)
def SessionStartProxyTransportVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartProxyTransportVector(builder, numElems)
def AddRealm(builder, realm): builder.PrependUOffsetTRelativeSlot(15, flatbuffers.number_types.UOffsetTFlags.py_type(realm), 0)
def SessionAddRealm(builder, realm):
    """This method is deprecated. Please switch to AddRealm."""
    return AddRealm(builder, realm)
def AddAuthid(builder, authid): builder.PrependUOffsetTRelativeSlot(16, flatbuffers.number_types.UOffsetTFlags.py_type(authid), 0)
def SessionAddAuthid(builder, authid):
    """This method is deprecated. Please switch to AddAuthid."""
    return AddAuthid(builder, authid)
def AddAuthrole(builder, authrole): builder.PrependUOffsetTRelativeSlot(17, flatbuffers.number_types.UOffsetTFlags.py_type(authrole), 0)
def SessionAddAuthrole(builder, authrole):
    """This method is deprecated. Please switch to AddAuthrole."""
    return AddAuthrole(builder, authrole)
def AddAuthmethod(builder, authmethod): builder.PrependUOffsetTRelativeSlot(18, flatbuffers.number_types.UOffsetTFlags.py_type(authmethod), 0)
def SessionAddAuthmethod(builder, authmethod):
    """This method is deprecated. Please switch to AddAuthmethod."""
    return AddAuthmethod(builder, authmethod)
def AddAuthprovider(builder, authprovider): builder.PrependUOffsetTRelativeSlot(19, flatbuffers.number_types.UOffsetTFlags.py_type(authprovider), 0)
def SessionAddAuthprovider(builder, authprovider):
    """This method is deprecated. Please switch to AddAuthprovider."""
    return AddAuthprovider(builder, authprovider)
def AddAuthextra(builder, authextra): builder.PrependUOffsetTRelativeSlot(20, flatbuffers.number_types.UOffsetTFlags.py_type(authextra), 0)
def SessionAddAuthextra(builder, authextra):
    """This method is deprecated. Please switch to AddAuthextra."""
    return AddAuthextra(builder, authextra)
def StartAuthextraVector(builder, numElems): return builder.StartVector(1, numElems, 1)
def SessionStartAuthextraVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartAuthextraVector(builder, numElems)
def End(builder): return builder.EndObject()
def SessionEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)