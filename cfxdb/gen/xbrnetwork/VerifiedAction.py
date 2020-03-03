# automatically generated by the FlatBuffers compiler, do not modify

# namespace: xbrnetwork

import flatbuffers

class VerifiedAction(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsVerifiedAction(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = VerifiedAction()
        x.Init(buf, n + offset)
        return x

    # VerifiedAction
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

# /// Globally unique and static ID of action.
    # VerifiedAction
    def Oid(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # VerifiedAction
    def OidAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint8Flags, o)
        return 0

    # VerifiedAction
    def OidLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

# /// Timestamp (epoch time in ns) of initial creation of this record.
    # VerifiedAction
    def Created(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

# /// Verification type.
    # VerifiedAction
    def Vtype(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

# /// Verification type.
    # VerifiedAction
    def Vstatus(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

# /// Verification code sent.
    # VerifiedAction
    def Vcode(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

# /// ID of object of verified action.
    # VerifiedAction
    def VerifiedOid(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # VerifiedAction
    def VerifiedOidAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint8Flags, o)
        return 0

    # VerifiedAction
    def VerifiedOidLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

# /// Action data, serialized in CBOR.
    # VerifiedAction
    def VerifiedData(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # VerifiedAction
    def VerifiedDataAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint8Flags, o)
        return 0

    # VerifiedAction
    def VerifiedDataLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

def VerifiedActionStart(builder): builder.StartObject(7)
def VerifiedActionAddOid(builder, oid): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(oid), 0)
def VerifiedActionStartOidVector(builder, numElems): return builder.StartVector(1, numElems, 1)
def VerifiedActionAddCreated(builder, created): builder.PrependUint64Slot(1, created, 0)
def VerifiedActionAddVtype(builder, vtype): builder.PrependUint8Slot(2, vtype, 0)
def VerifiedActionAddVstatus(builder, vstatus): builder.PrependUint8Slot(3, vstatus, 0)
def VerifiedActionAddVcode(builder, vcode): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(vcode), 0)
def VerifiedActionAddVerifiedOid(builder, verifiedOid): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(verifiedOid), 0)
def VerifiedActionStartVerifiedOidVector(builder, numElems): return builder.StartVector(1, numElems, 1)
def VerifiedActionAddVerifiedData(builder, verifiedData): builder.PrependUOffsetTRelativeSlot(6, flatbuffers.number_types.UOffsetTFlags.py_type(verifiedData), 0)
def VerifiedActionStartVerifiedDataVector(builder, numElems): return builder.StartVector(1, numElems, 1)
def VerifiedActionEnd(builder): return builder.EndObject()
