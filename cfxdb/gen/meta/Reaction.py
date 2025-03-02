# automatically generated by the FlatBuffers compiler, do not modify

# namespace: meta

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class Reaction(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Reaction()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsReaction(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # Reaction
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Table of the object holding the attribute.
    # Reaction
    def TableOid(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # Reaction
    def TableOidAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint8Flags, o)
        return 0

    # Reaction
    def TableOidLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Reaction
    def TableOidIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        return o == 0

    # Object (within the table) holding the attribute
    # Reaction
    def ObjectOid(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # Reaction
    def ObjectOidAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint8Flags, o)
        return 0

    # Reaction
    def ObjectOidLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Reaction
    def ObjectOidIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        return o == 0

    # Object (within the table) holding the attribute
    # Reaction
    def VoterOid(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # Reaction
    def VoterOidAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint8Flags, o)
        return 0

    # Reaction
    def VoterOidLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Reaction
    def VoterOidIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        return o == 0

    # Reaction name (or URI in general).
    # Reaction
    def Reaction(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # Timestamp when the reaction was recorded or last modifified.
    # Reaction
    def Reacted(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint64Flags, o + self._tab.Pos)
        return 0

    # CBOR-serialized, object-valued extra data stored along with this reaction.
    # Reaction
    def Extra(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # Reaction
    def ExtraAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint8Flags, o)
        return 0

    # Reaction
    def ExtraLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Reaction
    def ExtraIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        return o == 0

def Start(builder): builder.StartObject(6)
def ReactionStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddTableOid(builder, tableOid): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(tableOid), 0)
def ReactionAddTableOid(builder, tableOid):
    """This method is deprecated. Please switch to AddTableOid."""
    return AddTableOid(builder, tableOid)
def StartTableOidVector(builder, numElems): return builder.StartVector(1, numElems, 1)
def ReactionStartTableOidVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartTableOidVector(builder, numElems)
def AddObjectOid(builder, objectOid): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(objectOid), 0)
def ReactionAddObjectOid(builder, objectOid):
    """This method is deprecated. Please switch to AddObjectOid."""
    return AddObjectOid(builder, objectOid)
def StartObjectOidVector(builder, numElems): return builder.StartVector(1, numElems, 1)
def ReactionStartObjectOidVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartObjectOidVector(builder, numElems)
def AddVoterOid(builder, voterOid): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(voterOid), 0)
def ReactionAddVoterOid(builder, voterOid):
    """This method is deprecated. Please switch to AddVoterOid."""
    return AddVoterOid(builder, voterOid)
def StartVoterOidVector(builder, numElems): return builder.StartVector(1, numElems, 1)
def ReactionStartVoterOidVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartVoterOidVector(builder, numElems)
def AddReaction(builder, reaction): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(reaction), 0)
def ReactionAddReaction(builder, reaction):
    """This method is deprecated. Please switch to AddReaction."""
    return AddReaction(builder, reaction)
def AddReacted(builder, reacted): builder.PrependUint64Slot(4, reacted, 0)
def ReactionAddReacted(builder, reacted):
    """This method is deprecated. Please switch to AddReacted."""
    return AddReacted(builder, reacted)
def AddExtra(builder, extra): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(extra), 0)
def ReactionAddExtra(builder, extra):
    """This method is deprecated. Please switch to AddExtra."""
    return AddExtra(builder, extra)
def StartExtraVector(builder, numElems): return builder.StartVector(1, numElems, 1)
def ReactionStartExtraVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartExtraVector(builder, numElems)
def End(builder): return builder.EndObject()
def ReactionEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)