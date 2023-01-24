# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: manager.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rmanager.proto\x12\x07manager\x1a\x1cgoogle/protobuf/struct.proto\"\xad\x01\n\nDiagnostic\x12.\n\x08severity\x18\x01 \x01(\x0e\x32\x1c.manager.Diagnostic.Severity\x12\x0f\n\x07summary\x18\x02 \x01(\t\x12\x0e\n\x06\x64\x65tail\x18\x03 \x01(\t\"N\n\x08Severity\x12\x18\n\x14SEVERITY_UNSPECIFIED\x10\x00\x12\x12\n\x0eSEVERITY_ERROR\x10\x01\x12\x14\n\x10SEVERITY_WARNING\x10\x02\"\xcd\x01\n\x08Retrieve\x1az\n\x07Request\x12\x0e\n\x06source\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65stination\x18\x02 \x01(\t\x12\'\n\x06\x66ilter\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct\x12!\n\x04\x61uth\x18\x04 \x01(\x0b\x32\x13.manager.AuthConfig\x1a\x45\n\x08Response\x12\x0f\n\x07\x64igests\x18\x01 \x03(\t\x12(\n\x0b\x64iagnostics\x18\x02 \x03(\x0b\x32\x13.manager.Diagnostic\"\xcb\x01\n\x07Publish\x1az\n\x07Request\x12\x0e\n\x06source\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65stination\x18\x02 \x01(\t\x12\'\n\ncollection\x18\x03 \x01(\x0b\x32\x13.manager.Collection\x12!\n\x04\x61uth\x18\x04 \x01(\x0b\x32\x13.manager.AuthConfig\x1a\x44\n\x08Response\x12\x0e\n\x06\x64igest\x18\x01 \x01(\t\x12(\n\x0b\x64iagnostics\x18\x02 \x03(\x0b\x32\x13.manager.Diagnostic\"^\n\nCollection\x12\x16\n\x0eschema_address\x18\x01 \x01(\t\x12\x1a\n\x12linked_collections\x18\x02 \x03(\t\x12\x1c\n\x05\x66iles\x18\x03 \x03(\x0b\x32\r.manager.File\"A\n\x04\x46ile\x12\x0c\n\x04\x66ile\x18\x01 \x01(\t\x12+\n\nattributes\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\"t\n\nAuthConfig\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\x12\x15\n\rregistry_host\x18\x03 \x01(\t\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x04 \x01(\t\x12\x15\n\rrefresh_token\x18\x05 \x01(\t2\xa8\x01\n\x11\x43ollectionManager\x12G\n\x0ePublishContent\x12\x18.manager.Publish.Request\x1a\x19.manager.Publish.Response\"\x00\x12J\n\x0fRetrieveContent\x12\x19.manager.Retrieve.Request\x1a\x1a.manager.Retrieve.Response\"\x00\x42IZGgithub.com/emporous/emporous-go/api/services/collectionmanager/v1alpha1b\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'manager_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'ZGgithub.com/emporous/emporous-go/api/services/collectionmanager/v1alpha1'
  _DIAGNOSTIC._serialized_start=57
  _DIAGNOSTIC._serialized_end=230
  _DIAGNOSTIC_SEVERITY._serialized_start=152
  _DIAGNOSTIC_SEVERITY._serialized_end=230
  _RETRIEVE._serialized_start=233
  _RETRIEVE._serialized_end=438
  _RETRIEVE_REQUEST._serialized_start=245
  _RETRIEVE_REQUEST._serialized_end=367
  _RETRIEVE_RESPONSE._serialized_start=369
  _RETRIEVE_RESPONSE._serialized_end=438
  _PUBLISH._serialized_start=441
  _PUBLISH._serialized_end=644
  _PUBLISH_REQUEST._serialized_start=452
  _PUBLISH_REQUEST._serialized_end=574
  _PUBLISH_RESPONSE._serialized_start=576
  _PUBLISH_RESPONSE._serialized_end=644
  _COLLECTION._serialized_start=646
  _COLLECTION._serialized_end=740
  _FILE._serialized_start=742
  _FILE._serialized_end=807
  _AUTHCONFIG._serialized_start=809
  _AUTHCONFIG._serialized_end=925
  _COLLECTIONMANAGER._serialized_start=928
  _COLLECTIONMANAGER._serialized_end=1096
# @@protoc_insertion_point(module_scope)
