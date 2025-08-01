# automatically generated by the FlatBuffers compiler, do not modify

# namespace: NestedUnion

import flatbuffers
from flatbuffers.compat import import_numpy
from typing import Any
from flatbuffers.table import Table
from typing import Optional
np = import_numpy()

class NestedUnionTest(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset: int = 0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = NestedUnionTest()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsNestedUnionTest(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # NestedUnionTest
    def Init(self, buf: bytes, pos: int):
        self._tab = flatbuffers.table.Table(buf, pos)

    # NestedUnionTest
    def Name(self) -> Optional[str]:
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # NestedUnionTest
    def DataType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, o + self._tab.Pos)
        return 0

    # NestedUnionTest
    def Data(self) -> Optional[flatbuffers.table.Table]:
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            obj = Table(bytearray(), 0)
            self._tab.Union(obj, o)
            return obj
        return None

    # NestedUnionTest
    def Id(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int16Flags, o + self._tab.Pos)
        return 0

def NestedUnionTestStart(builder: flatbuffers.Builder):
    builder.StartObject(4)

def Start(builder: flatbuffers.Builder):
    NestedUnionTestStart(builder)

def NestedUnionTestAddName(builder: flatbuffers.Builder, name: int):
    builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(name), 0)

def AddName(builder: flatbuffers.Builder, name: int):
    NestedUnionTestAddName(builder, name)

def NestedUnionTestAddDataType(builder: flatbuffers.Builder, dataType: int):
    builder.PrependUint8Slot(1, dataType, 0)

def AddDataType(builder: flatbuffers.Builder, dataType: int):
    NestedUnionTestAddDataType(builder, dataType)

def NestedUnionTestAddData(builder: flatbuffers.Builder, data: int):
    builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(data), 0)

def AddData(builder: flatbuffers.Builder, data: int):
    NestedUnionTestAddData(builder, data)

def NestedUnionTestAddId(builder: flatbuffers.Builder, id: int):
    builder.PrependInt16Slot(3, id, 0)

def AddId(builder: flatbuffers.Builder, id: int):
    NestedUnionTestAddId(builder, id)

def NestedUnionTestEnd(builder: flatbuffers.Builder) -> int:
    return builder.EndObject()

def End(builder: flatbuffers.Builder) -> int:
    return NestedUnionTestEnd(builder)

import MyGame.Example.NestedUnion.Any
import MyGame.Example.NestedUnion.TestSimpleTableWithEnum
import MyGame.Example.NestedUnion.Vec3
try:
    from typing import Union
except:
    pass

class NestedUnionTestT(object):

    # NestedUnionTestT
    def __init__(
        self,
        name = None,
        dataType = 0,
        data = None,
        id = 0,
    ):
        self.name = name  # type: Optional[str]
        self.dataType = dataType  # type: int
        self.data = data  # type: Union[None, 'MyGame.Example.NestedUnion.Vec3.Vec3T', 'MyGame.Example.NestedUnion.TestSimpleTableWithEnum.TestSimpleTableWithEnumT']
        self.id = id  # type: int

    @classmethod
    def InitFromBuf(cls, buf, pos):
        nestedUnionTest = NestedUnionTest()
        nestedUnionTest.Init(buf, pos)
        return cls.InitFromObj(nestedUnionTest)

    @classmethod
    def InitFromPackedBuf(cls, buf, pos=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, pos)
        return cls.InitFromBuf(buf, pos+n)

    @classmethod
    def InitFromObj(cls, nestedUnionTest):
        x = NestedUnionTestT()
        x._UnPack(nestedUnionTest)
        return x

    # NestedUnionTestT
    def _UnPack(self, nestedUnionTest):
        if nestedUnionTest is None:
            return
        self.name = nestedUnionTest.Name()
        if self.name is not None:
            self.name = self.name.decode('utf-8')
        self.dataType = nestedUnionTest.DataType()
        self.data = MyGame.Example.NestedUnion.Any.AnyCreator(self.dataType, nestedUnionTest.Data())
        self.id = nestedUnionTest.Id()

    # NestedUnionTestT
    def Pack(self, builder):
        if self.name is not None:
            name = builder.CreateString(self.name)
        if self.data is not None:
            data = self.data.Pack(builder)
        NestedUnionTestStart(builder)
        if self.name is not None:
            NestedUnionTestAddName(builder, name)
        NestedUnionTestAddDataType(builder, self.dataType)
        if self.data is not None:
            NestedUnionTestAddData(builder, data)
        NestedUnionTestAddId(builder, self.id)
        nestedUnionTest = NestedUnionTestEnd(builder)
        return nestedUnionTest
