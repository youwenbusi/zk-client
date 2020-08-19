# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/zeth_messages.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='api/zeth_messages.proto',
  package='zeth_proto',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x17\x61pi/zeth_messages.proto\x12\nzeth_proto\"C\n\x08ZethNote\x12\x0b\n\x03\x61pk\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\x12\x0b\n\x03rho\x18\x03 \x01(\t\x12\x0e\n\x06trap_r\x18\x04 \x01(\t\"\x83\x01\n\x0eJoinsplitInput\x12\x13\n\x0bmerkle_path\x18\x01 \x03(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x01(\x03\x12\"\n\x04note\x18\x03 \x01(\x0b\x32\x14.zeth_proto.ZethNote\x12\x14\n\x0cspending_ask\x18\x04 \x01(\t\x12\x11\n\tnullifier\x18\x05 \x01(\t\"\xc1\x01\n\x0bProofInputs\x12\x10\n\x08mk_roots\x18\x01 \x03(\t\x12-\n\tjs_inputs\x18\x02 \x03(\x0b\x32\x1a.zeth_proto.JoinsplitInput\x12(\n\njs_outputs\x18\x03 \x03(\x0b\x32\x14.zeth_proto.ZethNote\x12\x14\n\x0cpub_in_value\x18\x04 \x01(\t\x12\x15\n\rpub_out_value\x18\x05 \x01(\t\x12\r\n\x05h_sig\x18\x06 \x01(\t\x12\x0b\n\x03phi\x18\x07 \x01(\tb\x06proto3')
)




_ZETHNOTE = _descriptor.Descriptor(
  name='ZethNote',
  full_name='zeth_proto.ZethNote',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='apk', full_name='zeth_proto.ZethNote.apk', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='zeth_proto.ZethNote.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rho', full_name='zeth_proto.ZethNote.rho', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='trap_r', full_name='zeth_proto.ZethNote.trap_r', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=39,
  serialized_end=106,
)


_JOINSPLITINPUT = _descriptor.Descriptor(
  name='JoinsplitInput',
  full_name='zeth_proto.JoinsplitInput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='merkle_path', full_name='zeth_proto.JoinsplitInput.merkle_path', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='address', full_name='zeth_proto.JoinsplitInput.address', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='note', full_name='zeth_proto.JoinsplitInput.note', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='spending_ask', full_name='zeth_proto.JoinsplitInput.spending_ask', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nullifier', full_name='zeth_proto.JoinsplitInput.nullifier', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=109,
  serialized_end=240,
)


_PROOFINPUTS = _descriptor.Descriptor(
  name='ProofInputs',
  full_name='zeth_proto.ProofInputs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mk_roots', full_name='zeth_proto.ProofInputs.mk_roots', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='js_inputs', full_name='zeth_proto.ProofInputs.js_inputs', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='js_outputs', full_name='zeth_proto.ProofInputs.js_outputs', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pub_in_value', full_name='zeth_proto.ProofInputs.pub_in_value', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pub_out_value', full_name='zeth_proto.ProofInputs.pub_out_value', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='h_sig', full_name='zeth_proto.ProofInputs.h_sig', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='phi', full_name='zeth_proto.ProofInputs.phi', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=243,
  serialized_end=436,
)

_JOINSPLITINPUT.fields_by_name['note'].message_type = _ZETHNOTE
_PROOFINPUTS.fields_by_name['js_inputs'].message_type = _JOINSPLITINPUT
_PROOFINPUTS.fields_by_name['js_outputs'].message_type = _ZETHNOTE
DESCRIPTOR.message_types_by_name['ZethNote'] = _ZETHNOTE
DESCRIPTOR.message_types_by_name['JoinsplitInput'] = _JOINSPLITINPUT
DESCRIPTOR.message_types_by_name['ProofInputs'] = _PROOFINPUTS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ZethNote = _reflection.GeneratedProtocolMessageType('ZethNote', (_message.Message,), {
  'DESCRIPTOR' : _ZETHNOTE,
  '__module__' : 'api.zeth_messages_pb2'
  # @@protoc_insertion_point(class_scope:zeth_proto.ZethNote)
  })
_sym_db.RegisterMessage(ZethNote)

JoinsplitInput = _reflection.GeneratedProtocolMessageType('JoinsplitInput', (_message.Message,), {
  'DESCRIPTOR' : _JOINSPLITINPUT,
  '__module__' : 'api.zeth_messages_pb2'
  # @@protoc_insertion_point(class_scope:zeth_proto.JoinsplitInput)
  })
_sym_db.RegisterMessage(JoinsplitInput)

ProofInputs = _reflection.GeneratedProtocolMessageType('ProofInputs', (_message.Message,), {
  'DESCRIPTOR' : _PROOFINPUTS,
  '__module__' : 'api.zeth_messages_pb2'
  # @@protoc_insertion_point(class_scope:zeth_proto.ProofInputs)
  })
_sym_db.RegisterMessage(ProofInputs)


# @@protoc_insertion_point(module_scope)
