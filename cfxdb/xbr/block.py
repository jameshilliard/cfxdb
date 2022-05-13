##############################################################################
#
#                        Crossbar.io Database
#     Copyright (c) Crossbar.io Technologies GmbH. Licensed under MIT.
#
##############################################################################

import pprint

import flatbuffers
from cfxdb import pack_uint256, unpack_uint256
from cfxdb.gen.xbr import Block as BlockGen
from zlmdb import datetime64, table, MapBytes32FlatBuffers


class _BlockGen(BlockGen.Block):
    """
    Expand methods on the class code generated by flatc.

    FIXME: come up with a PR for fla_CatalogGentc to generated this stuff automatically.
    """
    @classmethod
    def GetRootAsBlock(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = _BlockGen()
        x.Init(buf, n + offset)
        return x

    def BlockNumberAsBytes(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            _off = self._tab.Vector(o)
            _len = self._tab.VectorLen(o)
            return memoryview(self._tab.Bytes)[_off:_off + _len]
        return None

    def BlockHashAsBytes(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            _off = self._tab.Vector(o)
            _len = self._tab.VectorLen(o)
            return memoryview(self._tab.Bytes)[_off:_off + _len]
        return None


class Block(object):
    """
    Blockchain blocks. This table stores information about the series of Ethereum blocks that make up the blockchain.
    """
    def __init__(self, from_fbs=None):
        self._from_fbs = from_fbs

        # uint64
        self._timestamp = None

        # [uint8] (uint256)
        self._block_number = None

        # [uint8]
        self._block_hash = None

        # uint32
        self._cnt_events = None

    def marshal(self) -> dict:
        obj = {
            'timestamp': int(self.timestamp) if self.timestamp else None,
            'block_number': pack_uint256(self.block_number) if self.block_number else 0,
            'block_hash': bytes(self.block_hash) if self.block_hash else None,
            'cnt_events': self.cnt_events,
        }
        return obj

    def __str__(self):
        return '\n{}\n'.format(pprint.pformat(self.marshal()))

    @property
    def timestamp(self) -> datetime64:
        """
        Timestamp when record was inserted (Unix epoch time in ns).
        """
        if self._timestamp is None and self._from_fbs:
            self._timestamp = datetime64(self._from_fbs.Timestamp())
        return self._timestamp

    @timestamp.setter
    def timestamp(self, value: datetime64):
        assert value is None or isinstance(value, datetime64)
        self._timestamp = value

    @property
    def block_hash(self) -> bytes:
        """
        Block hash.
        """
        if self._block_hash is None and self._from_fbs:
            if self._from_fbs.BlockHashLength():
                self._block_hash = self._from_fbs.BlockHashAsBytes()
        return self._block_hash

    @block_hash.setter
    def block_hash(self, value: bytes):
        assert value is None or type(value) == bytes
        self._block_hash = value

    @property
    def block_number(self) -> int:
        """
        Primary key: block number.
        """
        if self._block_number is None and self._from_fbs:
            if self._from_fbs.BlockNumberLength():
                _block_number = self._from_fbs.BlockNumberAsBytes()
                self._block_number = unpack_uint256(bytes(_block_number))
            else:
                self._block_number = 0
        return self._block_number

    @block_number.setter
    def block_number(self, value: int):
        assert value is None or type(value) == int
        self._block_number = value

    @property
    def cnt_events(self) -> int:
        """
        Number of XBR blockchain log events found in the block.
        """
        if self._cnt_events is None and self._from_fbs:
            self._cnt_events = self._from_fbs.CntEvents()
        return self._cnt_events or 0

    @cnt_events.setter
    def cnt_events(self, value: int):
        assert value is None or type(value) == int
        self._cnt_events = value

    @staticmethod
    def cast(buf):
        return Block(_BlockGen.GetRootAsBlock(buf, 0))

    def build(self, builder):

        block_number = self.block_number
        if block_number:
            block_number = builder.CreateString(pack_uint256(block_number))

        block_hash = self.block_hash
        if block_hash:
            block_hash = builder.CreateString(block_hash)

        BlockGen.BlockStart(builder)

        if self.timestamp:
            BlockGen.BlockAddTimestamp(builder, int(self.timestamp))

        if block_number:
            BlockGen.BlockAddBlockNumber(builder, block_number)

        if block_hash:
            BlockGen.BlockAddBlockHash(builder, block_hash)

        if self.cnt_events:
            BlockGen.BlockAddCntEvents(builder, self.cnt_events)

        final = BlockGen.BlockEnd(builder)

        return final


@table('a4a0553e-24fa-4280-9959-5805f034d861', build=Block.build, cast=Block.cast)
class Blocks(MapBytes32FlatBuffers):
    """
    Blockchain blocks processed.

    Map :class:`zlmdb.MapBytes32FlatBuffers` from ``block_number`` to :class:`cfxdb.xbr.Block`
    """
