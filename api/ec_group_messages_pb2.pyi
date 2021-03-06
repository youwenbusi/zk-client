# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int


class HexPointBaseGroup1Affine(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    x_coord = ... # type: typing___Text
    y_coord = ... # type: typing___Text

    def __init__(self,
        *,
        x_coord : typing___Optional[typing___Text] = None,
        y_coord : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: builtin___bytes) -> HexPointBaseGroup1Affine: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"x_coord",u"y_coord"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"x_coord",b"x_coord",u"y_coord",b"y_coord"]) -> None: ...

class HexPointBaseGroup2Affine(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    x_c1_coord = ... # type: typing___Text
    x_c0_coord = ... # type: typing___Text
    y_c1_coord = ... # type: typing___Text
    y_c0_coord = ... # type: typing___Text

    def __init__(self,
        *,
        x_c1_coord : typing___Optional[typing___Text] = None,
        x_c0_coord : typing___Optional[typing___Text] = None,
        y_c1_coord : typing___Optional[typing___Text] = None,
        y_c0_coord : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: builtin___bytes) -> HexPointBaseGroup2Affine: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"x_c0_coord",u"x_c1_coord",u"y_c0_coord",u"y_c1_coord"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"x_c0_coord",b"x_c0_coord",u"x_c1_coord",b"x_c1_coord",u"y_c0_coord",b"y_c0_coord",u"y_c1_coord",b"y_c1_coord"]) -> None: ...
