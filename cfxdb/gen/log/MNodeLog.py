# automatically generated by the FlatBuffers compiler, do not modify

# namespace: log

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

# Heartbeat log record of managed nodes. Primary key: (timestamp, node_id).
class MNodeLog(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = MNodeLog()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsMNodeLog(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # MNodeLog
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Primary key: Unix time in ns when this log record was received (from CFC node clock).
    # MNodeLog
    def Timestamp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # Primary key: CF node ID.
    # MNodeLog
    def NodeId(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # MNodeLog
    def NodeIdAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint8Flags, o)
        return 0

    # MNodeLog
    def NodeIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # MNodeLog
    def NodeIdIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        return o == 0

    # Heartbeat period in seconds encompassed by this record.
    # MNodeLog
    def Period(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # Management realm ID.
    # MNodeLog
    def MrealmId(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # MNodeLog
    def MrealmIdAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint8Flags, o)
        return 0

    # MNodeLog
    def MrealmIdLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # MNodeLog
    def MrealmIdIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        return o == 0

    # Current state of CF node.
    # MNodeLog
    def State(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

    # WAMP session ID of the CF node uplink management session to this CFC instance.
    # MNodeLog
    def Session(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # Unix time in ns. This timestamp is from the original received event payload (from CF node clock).
    # MNodeLog
    def Sent(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # Sequence number as sent in the log record by the CF node (started at 0 for CF start and incremented by one on each heartbeat).
    # MNodeLog
    def Seq(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # Number of controllers running in the CF node (this is always 1).
    # MNodeLog
    def Controllers(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint16Flags, o + self._tab.Pos)
        return 0

    # Number of router workers currently running in the CF node.
    # MNodeLog
    def Routers(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint16Flags, o + self._tab.Pos)
        return 0

    # Number of container workers currently running in the CF node.
    # MNodeLog
    def Containers(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint16Flags, o + self._tab.Pos)
        return 0

    # Number of guest workers currently running in the CF node.
    # MNodeLog
    def Guests(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint16Flags, o + self._tab.Pos)
        return 0

    # Number of proxy workers currently running in the CF node.
    # MNodeLog
    def Proxies(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint16Flags, o + self._tab.Pos)
        return 0

    # Number of XBR market maker workers currently running in the CF node.
    # MNodeLog
    def Marketmakers(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint16Flags, o + self._tab.Pos)
        return 0

    # Number of hostmonitor workers currently running in the CF node (this is usually either 0 or 1).
    # MNodeLog
    def Hostmonitors(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(32))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint16Flags, o + self._tab.Pos)
        return 0

    # CF node system statistics.
    # MNodeLog
    def CpuCtxSwitches(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(34))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # MNodeLog
    def CpuFreq(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(36))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # MNodeLog
    def CpuGuest(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(38))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # MNodeLog
    def CpuGuestNice(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(40))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # MNodeLog
    def CpuIdle(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(42))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # MNodeLog
    def CpuInterrupts(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(44))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # MNodeLog
    def CpuIowait(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(46))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # MNodeLog
    def CpuIrq(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(48))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # MNodeLog
    def CpuNice(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(50))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # MNodeLog
    def CpuSoftInterrupts(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(52))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # MNodeLog
    def CpuSoftirq(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(54))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # MNodeLog
    def CpuSteal(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(56))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # MNodeLog
    def CpuSystem(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(58))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # MNodeLog
    def CpuUser(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(60))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # MNodeLog
    def DiskBusyTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(62))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # MNodeLog
    def DiskReadBytes(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(64))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # MNodeLog
    def DiskReadCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(66))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # MNodeLog
    def DiskReadMergedCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(68))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # MNodeLog
    def DiskReadTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(70))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # MNodeLog
    def DiskWriteBytes(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(72))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # MNodeLog
    def DiskWriteCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(74))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # MNodeLog
    def DiskWriteMergedCount(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(76))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # MNodeLog
    def DiskWriteTime(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(78))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # MNodeLog
    def MemoryActive(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(80))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # MNodeLog
    def MemoryAvailable(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(82))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # MNodeLog
    def MemoryBuffers(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(84))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # MNodeLog
    def MemoryCached(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(86))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # MNodeLog
    def MemoryFree(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(88))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # MNodeLog
    def MemoryInactive(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(90))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # MNodeLog
    def MemoryPercent(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(92))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # MNodeLog
    def MemoryShared(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(94))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # MNodeLog
    def MemorySlab(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(96))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # MNodeLog
    def MemoryTotal(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(98))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # MNodeLog
    def MemoryUsed(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(100))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # MNodeLog
    def NetworkBytesRecv(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(102))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # MNodeLog
    def NetworkBytesSent(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(104))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # MNodeLog
    def NetworkConnectionAfInet(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(106))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # MNodeLog
    def NetworkConnectionAfInet6(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(108))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # MNodeLog
    def NetworkConnectionAfUnix(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(110))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # MNodeLog
    def NetworkDropin(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(112))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # MNodeLog
    def NetworkDropout(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(114))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # MNodeLog
    def NetworkErrin(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(116))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # MNodeLog
    def NetworkErrout(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(118))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # MNodeLog
    def NetworkPacketsRecv(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(120))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # MNodeLog
    def NetworkPacketsSent(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(122))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

def Start(builder): builder.StartObject(60)
def MNodeLogStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddTimestamp(builder, timestamp): builder.PrependUint64Slot(0, timestamp, 0)
def MNodeLogAddTimestamp(builder, timestamp):
    """This method is deprecated. Please switch to AddTimestamp."""
    return AddTimestamp(builder, timestamp)
def AddNodeId(builder, nodeId): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(nodeId), 0)
def MNodeLogAddNodeId(builder, nodeId):
    """This method is deprecated. Please switch to AddNodeId."""
    return AddNodeId(builder, nodeId)
def StartNodeIdVector(builder, numElems): return builder.StartVector(1, numElems, 1)
def MNodeLogStartNodeIdVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartNodeIdVector(builder, numElems)
def AddPeriod(builder, period): builder.PrependUint32Slot(2, period, 0)
def MNodeLogAddPeriod(builder, period):
    """This method is deprecated. Please switch to AddPeriod."""
    return AddPeriod(builder, period)
def AddMrealmId(builder, mrealmId): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(mrealmId), 0)
def MNodeLogAddMrealmId(builder, mrealmId):
    """This method is deprecated. Please switch to AddMrealmId."""
    return AddMrealmId(builder, mrealmId)
def StartMrealmIdVector(builder, numElems): return builder.StartVector(1, numElems, 1)
def MNodeLogStartMrealmIdVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartMrealmIdVector(builder, numElems)
def AddState(builder, state): builder.PrependUint8Slot(4, state, 0)
def MNodeLogAddState(builder, state):
    """This method is deprecated. Please switch to AddState."""
    return AddState(builder, state)
def AddSession(builder, session): builder.PrependUint64Slot(5, session, 0)
def MNodeLogAddSession(builder, session):
    """This method is deprecated. Please switch to AddSession."""
    return AddSession(builder, session)
def AddSent(builder, sent): builder.PrependUint64Slot(6, sent, 0)
def MNodeLogAddSent(builder, sent):
    """This method is deprecated. Please switch to AddSent."""
    return AddSent(builder, sent)
def AddSeq(builder, seq): builder.PrependUint64Slot(7, seq, 0)
def MNodeLogAddSeq(builder, seq):
    """This method is deprecated. Please switch to AddSeq."""
    return AddSeq(builder, seq)
def AddControllers(builder, controllers): builder.PrependUint16Slot(8, controllers, 0)
def MNodeLogAddControllers(builder, controllers):
    """This method is deprecated. Please switch to AddControllers."""
    return AddControllers(builder, controllers)
def AddRouters(builder, routers): builder.PrependUint16Slot(9, routers, 0)
def MNodeLogAddRouters(builder, routers):
    """This method is deprecated. Please switch to AddRouters."""
    return AddRouters(builder, routers)
def AddContainers(builder, containers): builder.PrependUint16Slot(10, containers, 0)
def MNodeLogAddContainers(builder, containers):
    """This method is deprecated. Please switch to AddContainers."""
    return AddContainers(builder, containers)
def AddGuests(builder, guests): builder.PrependUint16Slot(11, guests, 0)
def MNodeLogAddGuests(builder, guests):
    """This method is deprecated. Please switch to AddGuests."""
    return AddGuests(builder, guests)
def AddProxies(builder, proxies): builder.PrependUint16Slot(12, proxies, 0)
def MNodeLogAddProxies(builder, proxies):
    """This method is deprecated. Please switch to AddProxies."""
    return AddProxies(builder, proxies)
def AddMarketmakers(builder, marketmakers): builder.PrependUint16Slot(13, marketmakers, 0)
def MNodeLogAddMarketmakers(builder, marketmakers):
    """This method is deprecated. Please switch to AddMarketmakers."""
    return AddMarketmakers(builder, marketmakers)
def AddHostmonitors(builder, hostmonitors): builder.PrependUint16Slot(14, hostmonitors, 0)
def MNodeLogAddHostmonitors(builder, hostmonitors):
    """This method is deprecated. Please switch to AddHostmonitors."""
    return AddHostmonitors(builder, hostmonitors)
def AddCpuCtxSwitches(builder, cpuCtxSwitches): builder.PrependUint64Slot(15, cpuCtxSwitches, 0)
def MNodeLogAddCpuCtxSwitches(builder, cpuCtxSwitches):
    """This method is deprecated. Please switch to AddCpuCtxSwitches."""
    return AddCpuCtxSwitches(builder, cpuCtxSwitches)
def AddCpuFreq(builder, cpuFreq): builder.PrependFloat32Slot(16, cpuFreq, 0.0)
def MNodeLogAddCpuFreq(builder, cpuFreq):
    """This method is deprecated. Please switch to AddCpuFreq."""
    return AddCpuFreq(builder, cpuFreq)
def AddCpuGuest(builder, cpuGuest): builder.PrependFloat32Slot(17, cpuGuest, 0.0)
def MNodeLogAddCpuGuest(builder, cpuGuest):
    """This method is deprecated. Please switch to AddCpuGuest."""
    return AddCpuGuest(builder, cpuGuest)
def AddCpuGuestNice(builder, cpuGuestNice): builder.PrependFloat32Slot(18, cpuGuestNice, 0.0)
def MNodeLogAddCpuGuestNice(builder, cpuGuestNice):
    """This method is deprecated. Please switch to AddCpuGuestNice."""
    return AddCpuGuestNice(builder, cpuGuestNice)
def AddCpuIdle(builder, cpuIdle): builder.PrependFloat32Slot(19, cpuIdle, 0.0)
def MNodeLogAddCpuIdle(builder, cpuIdle):
    """This method is deprecated. Please switch to AddCpuIdle."""
    return AddCpuIdle(builder, cpuIdle)
def AddCpuInterrupts(builder, cpuInterrupts): builder.PrependUint64Slot(20, cpuInterrupts, 0)
def MNodeLogAddCpuInterrupts(builder, cpuInterrupts):
    """This method is deprecated. Please switch to AddCpuInterrupts."""
    return AddCpuInterrupts(builder, cpuInterrupts)
def AddCpuIowait(builder, cpuIowait): builder.PrependFloat32Slot(21, cpuIowait, 0.0)
def MNodeLogAddCpuIowait(builder, cpuIowait):
    """This method is deprecated. Please switch to AddCpuIowait."""
    return AddCpuIowait(builder, cpuIowait)
def AddCpuIrq(builder, cpuIrq): builder.PrependFloat32Slot(22, cpuIrq, 0.0)
def MNodeLogAddCpuIrq(builder, cpuIrq):
    """This method is deprecated. Please switch to AddCpuIrq."""
    return AddCpuIrq(builder, cpuIrq)
def AddCpuNice(builder, cpuNice): builder.PrependFloat32Slot(23, cpuNice, 0.0)
def MNodeLogAddCpuNice(builder, cpuNice):
    """This method is deprecated. Please switch to AddCpuNice."""
    return AddCpuNice(builder, cpuNice)
def AddCpuSoftInterrupts(builder, cpuSoftInterrupts): builder.PrependUint64Slot(24, cpuSoftInterrupts, 0)
def MNodeLogAddCpuSoftInterrupts(builder, cpuSoftInterrupts):
    """This method is deprecated. Please switch to AddCpuSoftInterrupts."""
    return AddCpuSoftInterrupts(builder, cpuSoftInterrupts)
def AddCpuSoftirq(builder, cpuSoftirq): builder.PrependFloat32Slot(25, cpuSoftirq, 0.0)
def MNodeLogAddCpuSoftirq(builder, cpuSoftirq):
    """This method is deprecated. Please switch to AddCpuSoftirq."""
    return AddCpuSoftirq(builder, cpuSoftirq)
def AddCpuSteal(builder, cpuSteal): builder.PrependFloat32Slot(26, cpuSteal, 0.0)
def MNodeLogAddCpuSteal(builder, cpuSteal):
    """This method is deprecated. Please switch to AddCpuSteal."""
    return AddCpuSteal(builder, cpuSteal)
def AddCpuSystem(builder, cpuSystem): builder.PrependFloat32Slot(27, cpuSystem, 0.0)
def MNodeLogAddCpuSystem(builder, cpuSystem):
    """This method is deprecated. Please switch to AddCpuSystem."""
    return AddCpuSystem(builder, cpuSystem)
def AddCpuUser(builder, cpuUser): builder.PrependFloat32Slot(28, cpuUser, 0.0)
def MNodeLogAddCpuUser(builder, cpuUser):
    """This method is deprecated. Please switch to AddCpuUser."""
    return AddCpuUser(builder, cpuUser)
def AddDiskBusyTime(builder, diskBusyTime): builder.PrependUint64Slot(29, diskBusyTime, 0)
def MNodeLogAddDiskBusyTime(builder, diskBusyTime):
    """This method is deprecated. Please switch to AddDiskBusyTime."""
    return AddDiskBusyTime(builder, diskBusyTime)
def AddDiskReadBytes(builder, diskReadBytes): builder.PrependUint64Slot(30, diskReadBytes, 0)
def MNodeLogAddDiskReadBytes(builder, diskReadBytes):
    """This method is deprecated. Please switch to AddDiskReadBytes."""
    return AddDiskReadBytes(builder, diskReadBytes)
def AddDiskReadCount(builder, diskReadCount): builder.PrependUint64Slot(31, diskReadCount, 0)
def MNodeLogAddDiskReadCount(builder, diskReadCount):
    """This method is deprecated. Please switch to AddDiskReadCount."""
    return AddDiskReadCount(builder, diskReadCount)
def AddDiskReadMergedCount(builder, diskReadMergedCount): builder.PrependUint64Slot(32, diskReadMergedCount, 0)
def MNodeLogAddDiskReadMergedCount(builder, diskReadMergedCount):
    """This method is deprecated. Please switch to AddDiskReadMergedCount."""
    return AddDiskReadMergedCount(builder, diskReadMergedCount)
def AddDiskReadTime(builder, diskReadTime): builder.PrependUint64Slot(33, diskReadTime, 0)
def MNodeLogAddDiskReadTime(builder, diskReadTime):
    """This method is deprecated. Please switch to AddDiskReadTime."""
    return AddDiskReadTime(builder, diskReadTime)
def AddDiskWriteBytes(builder, diskWriteBytes): builder.PrependUint64Slot(34, diskWriteBytes, 0)
def MNodeLogAddDiskWriteBytes(builder, diskWriteBytes):
    """This method is deprecated. Please switch to AddDiskWriteBytes."""
    return AddDiskWriteBytes(builder, diskWriteBytes)
def AddDiskWriteCount(builder, diskWriteCount): builder.PrependUint64Slot(35, diskWriteCount, 0)
def MNodeLogAddDiskWriteCount(builder, diskWriteCount):
    """This method is deprecated. Please switch to AddDiskWriteCount."""
    return AddDiskWriteCount(builder, diskWriteCount)
def AddDiskWriteMergedCount(builder, diskWriteMergedCount): builder.PrependUint64Slot(36, diskWriteMergedCount, 0)
def MNodeLogAddDiskWriteMergedCount(builder, diskWriteMergedCount):
    """This method is deprecated. Please switch to AddDiskWriteMergedCount."""
    return AddDiskWriteMergedCount(builder, diskWriteMergedCount)
def AddDiskWriteTime(builder, diskWriteTime): builder.PrependUint64Slot(37, diskWriteTime, 0)
def MNodeLogAddDiskWriteTime(builder, diskWriteTime):
    """This method is deprecated. Please switch to AddDiskWriteTime."""
    return AddDiskWriteTime(builder, diskWriteTime)
def AddMemoryActive(builder, memoryActive): builder.PrependUint64Slot(38, memoryActive, 0)
def MNodeLogAddMemoryActive(builder, memoryActive):
    """This method is deprecated. Please switch to AddMemoryActive."""
    return AddMemoryActive(builder, memoryActive)
def AddMemoryAvailable(builder, memoryAvailable): builder.PrependUint64Slot(39, memoryAvailable, 0)
def MNodeLogAddMemoryAvailable(builder, memoryAvailable):
    """This method is deprecated. Please switch to AddMemoryAvailable."""
    return AddMemoryAvailable(builder, memoryAvailable)
def AddMemoryBuffers(builder, memoryBuffers): builder.PrependUint64Slot(40, memoryBuffers, 0)
def MNodeLogAddMemoryBuffers(builder, memoryBuffers):
    """This method is deprecated. Please switch to AddMemoryBuffers."""
    return AddMemoryBuffers(builder, memoryBuffers)
def AddMemoryCached(builder, memoryCached): builder.PrependUint64Slot(41, memoryCached, 0)
def MNodeLogAddMemoryCached(builder, memoryCached):
    """This method is deprecated. Please switch to AddMemoryCached."""
    return AddMemoryCached(builder, memoryCached)
def AddMemoryFree(builder, memoryFree): builder.PrependUint64Slot(42, memoryFree, 0)
def MNodeLogAddMemoryFree(builder, memoryFree):
    """This method is deprecated. Please switch to AddMemoryFree."""
    return AddMemoryFree(builder, memoryFree)
def AddMemoryInactive(builder, memoryInactive): builder.PrependUint64Slot(43, memoryInactive, 0)
def MNodeLogAddMemoryInactive(builder, memoryInactive):
    """This method is deprecated. Please switch to AddMemoryInactive."""
    return AddMemoryInactive(builder, memoryInactive)
def AddMemoryPercent(builder, memoryPercent): builder.PrependFloat32Slot(44, memoryPercent, 0.0)
def MNodeLogAddMemoryPercent(builder, memoryPercent):
    """This method is deprecated. Please switch to AddMemoryPercent."""
    return AddMemoryPercent(builder, memoryPercent)
def AddMemoryShared(builder, memoryShared): builder.PrependUint64Slot(45, memoryShared, 0)
def MNodeLogAddMemoryShared(builder, memoryShared):
    """This method is deprecated. Please switch to AddMemoryShared."""
    return AddMemoryShared(builder, memoryShared)
def AddMemorySlab(builder, memorySlab): builder.PrependUint64Slot(46, memorySlab, 0)
def MNodeLogAddMemorySlab(builder, memorySlab):
    """This method is deprecated. Please switch to AddMemorySlab."""
    return AddMemorySlab(builder, memorySlab)
def AddMemoryTotal(builder, memoryTotal): builder.PrependUint64Slot(47, memoryTotal, 0)
def MNodeLogAddMemoryTotal(builder, memoryTotal):
    """This method is deprecated. Please switch to AddMemoryTotal."""
    return AddMemoryTotal(builder, memoryTotal)
def AddMemoryUsed(builder, memoryUsed): builder.PrependUint64Slot(48, memoryUsed, 0)
def MNodeLogAddMemoryUsed(builder, memoryUsed):
    """This method is deprecated. Please switch to AddMemoryUsed."""
    return AddMemoryUsed(builder, memoryUsed)
def AddNetworkBytesRecv(builder, networkBytesRecv): builder.PrependUint64Slot(49, networkBytesRecv, 0)
def MNodeLogAddNetworkBytesRecv(builder, networkBytesRecv):
    """This method is deprecated. Please switch to AddNetworkBytesRecv."""
    return AddNetworkBytesRecv(builder, networkBytesRecv)
def AddNetworkBytesSent(builder, networkBytesSent): builder.PrependUint64Slot(50, networkBytesSent, 0)
def MNodeLogAddNetworkBytesSent(builder, networkBytesSent):
    """This method is deprecated. Please switch to AddNetworkBytesSent."""
    return AddNetworkBytesSent(builder, networkBytesSent)
def AddNetworkConnectionAfInet(builder, networkConnectionAfInet): builder.PrependUint32Slot(51, networkConnectionAfInet, 0)
def MNodeLogAddNetworkConnectionAfInet(builder, networkConnectionAfInet):
    """This method is deprecated. Please switch to AddNetworkConnectionAfInet."""
    return AddNetworkConnectionAfInet(builder, networkConnectionAfInet)
def AddNetworkConnectionAfInet6(builder, networkConnectionAfInet6): builder.PrependUint32Slot(52, networkConnectionAfInet6, 0)
def MNodeLogAddNetworkConnectionAfInet6(builder, networkConnectionAfInet6):
    """This method is deprecated. Please switch to AddNetworkConnectionAfInet6."""
    return AddNetworkConnectionAfInet6(builder, networkConnectionAfInet6)
def AddNetworkConnectionAfUnix(builder, networkConnectionAfUnix): builder.PrependUint32Slot(53, networkConnectionAfUnix, 0)
def MNodeLogAddNetworkConnectionAfUnix(builder, networkConnectionAfUnix):
    """This method is deprecated. Please switch to AddNetworkConnectionAfUnix."""
    return AddNetworkConnectionAfUnix(builder, networkConnectionAfUnix)
def AddNetworkDropin(builder, networkDropin): builder.PrependUint32Slot(54, networkDropin, 0)
def MNodeLogAddNetworkDropin(builder, networkDropin):
    """This method is deprecated. Please switch to AddNetworkDropin."""
    return AddNetworkDropin(builder, networkDropin)
def AddNetworkDropout(builder, networkDropout): builder.PrependUint32Slot(55, networkDropout, 0)
def MNodeLogAddNetworkDropout(builder, networkDropout):
    """This method is deprecated. Please switch to AddNetworkDropout."""
    return AddNetworkDropout(builder, networkDropout)
def AddNetworkErrin(builder, networkErrin): builder.PrependUint32Slot(56, networkErrin, 0)
def MNodeLogAddNetworkErrin(builder, networkErrin):
    """This method is deprecated. Please switch to AddNetworkErrin."""
    return AddNetworkErrin(builder, networkErrin)
def AddNetworkErrout(builder, networkErrout): builder.PrependUint32Slot(57, networkErrout, 0)
def MNodeLogAddNetworkErrout(builder, networkErrout):
    """This method is deprecated. Please switch to AddNetworkErrout."""
    return AddNetworkErrout(builder, networkErrout)
def AddNetworkPacketsRecv(builder, networkPacketsRecv): builder.PrependUint64Slot(58, networkPacketsRecv, 0)
def MNodeLogAddNetworkPacketsRecv(builder, networkPacketsRecv):
    """This method is deprecated. Please switch to AddNetworkPacketsRecv."""
    return AddNetworkPacketsRecv(builder, networkPacketsRecv)
def AddNetworkPacketsSent(builder, networkPacketsSent): builder.PrependUint64Slot(59, networkPacketsSent, 0)
def MNodeLogAddNetworkPacketsSent(builder, networkPacketsSent):
    """This method is deprecated. Please switch to AddNetworkPacketsSent."""
    return AddNetworkPacketsSent(builder, networkPacketsSent)
def End(builder): return builder.EndObject()
def MNodeLogEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)