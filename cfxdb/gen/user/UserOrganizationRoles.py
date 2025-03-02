# automatically generated by the FlatBuffers compiler, do not modify

# namespace: user

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

# CFC user roles on an organization
class UserOrganizationRoles(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = UserOrganizationRoles()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsUserOrganizationRoles(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # UserOrganizationRoles
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # List of roles the user has on the respective organization.
    # UserOrganizationRoles
    def Roles(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Int8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # UserOrganizationRoles
    def RolesAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Int8Flags, o)
        return 0

    # UserOrganizationRoles
    def RolesLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # UserOrganizationRoles
    def RolesIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        return o == 0

def Start(builder): builder.StartObject(1)
def UserOrganizationRolesStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddRoles(builder, roles): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(roles), 0)
def UserOrganizationRolesAddRoles(builder, roles):
    """This method is deprecated. Please switch to AddRoles."""
    return AddRoles(builder, roles)
def StartRolesVector(builder, numElems): return builder.StartVector(1, numElems, 1)
def UserOrganizationRolesStartRolesVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartRolesVector(builder, numElems)
def End(builder): return builder.EndObject()
def UserOrganizationRolesEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)