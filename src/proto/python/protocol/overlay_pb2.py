

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import common_pb2 as common__pb2
import chain_pb2 as chain__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='overlay.proto',
  package='protocol',
  syntax='proto3',
  serialized_pb=_b('\n\roverlay.proto\x12\x08protocol\x1a\x0c\x63ommon.proto\x1a\x0b\x63hain.proto\"\xa3\x01\n\x05Hello\x12\x12\n\nnetwork_id\x18\x01 \x01(\x03\x12\x16\n\x0eledger_version\x18\x02 \x01(\x03\x12\x17\n\x0foverlay_version\x18\x03 \x01(\x03\x12\x14\n\x0c\x62umo_version\x18\x04 \x01(\t\x12\x16\n\x0elistening_port\x18\x05 \x01(\x03\x12\x14\n\x0cnode_address\x18\x06 \x01(\t\x12\x11\n\tnode_rand\x18\x07 \x01(\t\"L\n\rHelloResponse\x12\'\n\nerror_code\x18\x01 \x01(\x0e\x32\x13.protocol.ERRORCODE\x12\x12\n\nerror_desc\x18\x02 \x01(\t\"}\n\x04Peer\x12\n\n\x02ip\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\x03\x12\x14\n\x0cnum_failures\x18\x03 \x01(\x03\x12\x19\n\x11next_attempt_time\x18\x04 \x01(\x03\x12\x13\n\x0b\x61\x63tive_time\x18\x05 \x01(\x03\x12\x15\n\rconnection_id\x18\x06 \x01(\x03\"&\n\x05Peers\x12\x1d\n\x05peers\x18\x01 \x03(\x0b\x32\x0e.protocol.Peer\";\n\nGetLedgers\x12\r\n\x05\x62\x65gin\x18\x01 \x01(\x03\x12\x0b\n\x03\x65nd\x18\x02 \x01(\x03\x12\x11\n\ttimestamp\x18\x03 \x01(\x03\"\xdf\x01\n\x07Ledgers\x12(\n\x06values\x18\x01 \x03(\x0b\x32\x18.protocol.ConsensusValue\x12-\n\tsync_code\x18\x02 \x01(\x0e\x32\x1a.protocol.Ledgers.SyncCode\x12\x0f\n\x07max_seq\x18\x03 \x01(\x03\x12\r\n\x05proof\x18\x04 \x01(\x0c\"[\n\x08SyncCode\x12\x06\n\x02OK\x10\x00\x12\x0f\n\x0bOUT_OF_SYNC\x10\x01\x12\x12\n\x0eOUT_OF_LEDGERS\x10\x02\x12\x08\n\x04\x42USY\x10\x03\x12\n\n\x06REFUSE\x10\x04\x12\x0c\n\x08INTERNAL\x10\x05\"&\n\x08\x44ontHave\x12\x0c\n\x04type\x18\x01 \x01(\x03\x12\x0c\n\x04hash\x18\x02 \x01(\x0c\"v\n\x13LedgerUpgradeNotify\x12\r\n\x05nonce\x18\x01 \x01(\x03\x12(\n\x07upgrade\x18\x02 \x01(\x0b\x32\x17.protocol.LedgerUpgrade\x12&\n\tsignature\x18\x03 \x01(\x0b\x32\x13.protocol.Signature\"\x1a\n\tEntryList\x12\r\n\x05\x65ntry\x18\x01 \x03(\x0c\"M\n\nChainHello\x12,\n\x08\x61pi_list\x18\x01 \x03(\x0e\x32\x1a.protocol.ChainMessageType\x12\x11\n\ttimestamp\x18\x02 \x01(\x03\"z\n\x0b\x43hainStatus\x12\x11\n\tself_addr\x18\x01 \x01(\t\x12\x16\n\x0eledger_version\x18\x02 \x01(\x03\x12\x17\n\x0fmonitor_version\x18\x03 \x01(\x03\x12\x14\n\x0c\x62umo_version\x18\x04 \x01(\t\x12\x11\n\ttimestamp\x18\x05 \x01(\x03\"O\n\x10\x43hainPeerMessage\x12\x15\n\rsrc_peer_addr\x18\x01 \x01(\t\x12\x16\n\x0e\x64\x65s_peer_addrs\x18\x02 \x03(\t\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x0c\"#\n\x10\x43hainSubscribeTx\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x03(\t\"7\n\rChainResponse\x12\x12\n\nerror_code\x18\x01 \x01(\x05\x12\x12\n\nerror_desc\x18\x02 \x01(\t\"\xd5\x02\n\rChainTxStatus\x12\x30\n\x06status\x18\x01 \x01(\x0e\x32 .protocol.ChainTxStatus.TxStatus\x12\x0f\n\x07tx_hash\x18\x02 \x01(\t\x12\x16\n\x0esource_address\x18\x03 \x01(\t\x12\x1a\n\x12source_account_seq\x18\x04 \x01(\x03\x12\x12\n\nledger_seq\x18\x05 \x01(\x03\x12\x17\n\x0fnew_account_seq\x18\x06 \x01(\x03\x12\'\n\nerror_code\x18\x07 \x01(\x0e\x32\x13.protocol.ERRORCODE\x12\x12\n\nerror_desc\x18\x08 \x01(\t\x12\x11\n\ttimestamp\x18\t \x01(\x03\"P\n\x08TxStatus\x12\r\n\tUNDEFINED\x10\x00\x12\r\n\tCONFIRMED\x10\x01\x12\x0b\n\x07PENDING\x10\x02\x12\x0c\n\x08\x43OMPLETE\x10\x03\x12\x0b\n\x07\x46\x41ILURE\x10\x04*\x83\x02\n\x14OVERLAY_MESSAGE_TYPE\x12\x18\n\x14OVERLAY_MSGTYPE_NONE\x10\x00\x12\x18\n\x14OVERLAY_MSGTYPE_PING\x10\x01\x12\x19\n\x15OVERLAY_MSGTYPE_HELLO\x10\x02\x12\x19\n\x15OVERLAY_MSGTYPE_PEERS\x10\x03\x12\x1f\n\x1bOVERLAY_MSGTYPE_TRANSACTION\x10\x04\x12\x1b\n\x17OVERLAY_MSGTYPE_LEDGERS\x10\x05\x12\x18\n\x14OVERLAY_MSGTYPE_PBFT\x10\x06\x12)\n%OVERLAY_MSGTYPE_LEDGER_UPGRADE_NOTIFY\x10\x07*\xfa\x01\n\x10\x43hainMessageType\x12\x13\n\x0f\x43HAIN_TYPE_NONE\x10\x00\x12\x0f\n\x0b\x43HAIN_HELLO\x10\n\x12\x13\n\x0f\x43HAIN_TX_STATUS\x10\x0b\x12\x15\n\x11\x43HAIN_PEER_ONLINE\x10\x0c\x12\x16\n\x12\x43HAIN_PEER_OFFLINE\x10\r\x12\x16\n\x12\x43HAIN_PEER_MESSAGE\x10\x0e\x12\x1b\n\x17\x43HAIN_SUBMITTRANSACTION\x10\x0f\x12\x17\n\x13\x43HAIN_LEDGER_HEADER\x10\x10\x12\x16\n\x12\x43HAIN_SUBSCRIBE_TX\x10\x11\x12\x16\n\x12\x43HAIN_TX_ENV_STORE\x10\x12\x42\"\n io.rexx.sdk.core.extend.protobufb\x06proto3')
  ,
  dependencies=[common__pb2.DESCRIPTOR,chain__pb2.DESCRIPTOR,])

_OVERLAY_MESSAGE_TYPE = _descriptor.EnumDescriptor(
  name='OVERLAY_MESSAGE_TYPE',
  full_name='protocol.OVERLAY_MESSAGE_TYPE',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OVERLAY_MSGTYPE_NONE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OVERLAY_MSGTYPE_PING', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OVERLAY_MSGTYPE_HELLO', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OVERLAY_MSGTYPE_PEERS', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OVERLAY_MSGTYPE_TRANSACTION', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OVERLAY_MSGTYPE_LEDGERS', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OVERLAY_MSGTYPE_PBFT', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OVERLAY_MSGTYPE_LEDGER_UPGRADE_NOTIFY', index=7, number=7,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1663,
  serialized_end=1922,
)
_sym_db.RegisterEnumDescriptor(_OVERLAY_MESSAGE_TYPE)

OVERLAY_MESSAGE_TYPE = enum_type_wrapper.EnumTypeWrapper(_OVERLAY_MESSAGE_TYPE)
_CHAINMESSAGETYPE = _descriptor.EnumDescriptor(
  name='ChainMessageType',
  full_name='protocol.ChainMessageType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CHAIN_TYPE_NONE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHAIN_HELLO', index=1, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHAIN_TX_STATUS', index=2, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHAIN_PEER_ONLINE', index=3, number=12,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHAIN_PEER_OFFLINE', index=4, number=13,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHAIN_PEER_MESSAGE', index=5, number=14,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHAIN_SUBMITTRANSACTION', index=6, number=15,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHAIN_LEDGER_HEADER', index=7, number=16,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHAIN_SUBSCRIBE_TX', index=8, number=17,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHAIN_TX_ENV_STORE', index=9, number=18,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1925,
  serialized_end=2175,
)
_sym_db.RegisterEnumDescriptor(_CHAINMESSAGETYPE)

ChainMessageType = enum_type_wrapper.EnumTypeWrapper(_CHAINMESSAGETYPE)
OVERLAY_MSGTYPE_NONE = 0
OVERLAY_MSGTYPE_PING = 1
OVERLAY_MSGTYPE_HELLO = 2
OVERLAY_MSGTYPE_PEERS = 3
OVERLAY_MSGTYPE_TRANSACTION = 4
OVERLAY_MSGTYPE_LEDGERS = 5
OVERLAY_MSGTYPE_PBFT = 6
OVERLAY_MSGTYPE_LEDGER_UPGRADE_NOTIFY = 7
CHAIN_TYPE_NONE = 0
CHAIN_HELLO = 10
CHAIN_TX_STATUS = 11
CHAIN_PEER_ONLINE = 12
CHAIN_PEER_OFFLINE = 13
CHAIN_PEER_MESSAGE = 14
CHAIN_SUBMITTRANSACTION = 15
CHAIN_LEDGER_HEADER = 16
CHAIN_SUBSCRIBE_TX = 17
CHAIN_TX_ENV_STORE = 18


_LEDGERS_SYNCCODE = _descriptor.EnumDescriptor(
  name='SyncCode',
  full_name='protocol.Ledgers.SyncCode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OK', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OUT_OF_SYNC', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OUT_OF_LEDGERS', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BUSY', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REFUSE', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INTERNAL', index=5, number=5,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=659,
  serialized_end=750,
)
_sym_db.RegisterEnumDescriptor(_LEDGERS_SYNCCODE)

_CHAINTXSTATUS_TXSTATUS = _descriptor.EnumDescriptor(
  name='TxStatus',
  full_name='protocol.ChainTxStatus.TxStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNDEFINED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONFIRMED', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PENDING', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COMPLETE', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILURE', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1580,
  serialized_end=1660,
)
_sym_db.RegisterEnumDescriptor(_CHAINTXSTATUS_TXSTATUS)


_HELLO = _descriptor.Descriptor(
  name='Hello',
  full_name='protocol.Hello',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='network_id', full_name='protocol.Hello.network_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ledger_version', full_name='protocol.Hello.ledger_version', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='overlay_version', full_name='protocol.Hello.overlay_version', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rexx_version', full_name='protocol.Hello.rexx_version', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='listening_port', full_name='protocol.Hello.listening_port', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='node_address', full_name='protocol.Hello.node_address', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='node_rand', full_name='protocol.Hello.node_rand', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=55,
  serialized_end=218,
)


_HELLORESPONSE = _descriptor.Descriptor(
  name='HelloResponse',
  full_name='protocol.HelloResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='error_code', full_name='protocol.HelloResponse.error_code', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error_desc', full_name='protocol.HelloResponse.error_desc', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=220,
  serialized_end=296,
)


_PEER = _descriptor.Descriptor(
  name='Peer',
  full_name='protocol.Peer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ip', full_name='protocol.Peer.ip', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='port', full_name='protocol.Peer.port', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_failures', full_name='protocol.Peer.num_failures', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='next_attempt_time', full_name='protocol.Peer.next_attempt_time', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='active_time', full_name='protocol.Peer.active_time', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='connection_id', full_name='protocol.Peer.connection_id', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=298,
  serialized_end=423,
)


_PEERS = _descriptor.Descriptor(
  name='Peers',
  full_name='protocol.Peers',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='peers', full_name='protocol.Peers.peers', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=425,
  serialized_end=463,
)


_GETLEDGERS = _descriptor.Descriptor(
  name='GetLedgers',
  full_name='protocol.GetLedgers',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='begin', full_name='protocol.GetLedgers.begin', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end', full_name='protocol.GetLedgers.end', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='protocol.GetLedgers.timestamp', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=465,
  serialized_end=524,
)


_LEDGERS = _descriptor.Descriptor(
  name='Ledgers',
  full_name='protocol.Ledgers',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='values', full_name='protocol.Ledgers.values', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sync_code', full_name='protocol.Ledgers.sync_code', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_seq', full_name='protocol.Ledgers.max_seq', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='proof', full_name='protocol.Ledgers.proof', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _LEDGERS_SYNCCODE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=527,
  serialized_end=750,
)


_DONTHAVE = _descriptor.Descriptor(
  name='DontHave',
  full_name='protocol.DontHave',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='protocol.DontHave.type', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hash', full_name='protocol.DontHave.hash', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=752,
  serialized_end=790,
)


_LEDGERUPGRADENOTIFY = _descriptor.Descriptor(
  name='LedgerUpgradeNotify',
  full_name='protocol.LedgerUpgradeNotify',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nonce', full_name='protocol.LedgerUpgradeNotify.nonce', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='upgrade', full_name='protocol.LedgerUpgradeNotify.upgrade', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='signature', full_name='protocol.LedgerUpgradeNotify.signature', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=792,
  serialized_end=910,
)


_ENTRYLIST = _descriptor.Descriptor(
  name='EntryList',
  full_name='protocol.EntryList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='entry', full_name='protocol.EntryList.entry', index=0,
      number=1, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=912,
  serialized_end=938,
)


_CHAINHELLO = _descriptor.Descriptor(
  name='ChainHello',
  full_name='protocol.ChainHello',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='api_list', full_name='protocol.ChainHello.api_list', index=0,
      number=1, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='protocol.ChainHello.timestamp', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=940,
  serialized_end=1017,
)


_CHAINSTATUS = _descriptor.Descriptor(
  name='ChainStatus',
  full_name='protocol.ChainStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='self_addr', full_name='protocol.ChainStatus.self_addr', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ledger_version', full_name='protocol.ChainStatus.ledger_version', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='monitor_version', full_name='protocol.ChainStatus.monitor_version', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rexx_version', full_name='protocol.ChainStatus.rexx_version', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='protocol.ChainStatus.timestamp', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1019,
  serialized_end=1141,
)


_CHAINPEERMESSAGE = _descriptor.Descriptor(
  name='ChainPeerMessage',
  full_name='protocol.ChainPeerMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='src_peer_addr', full_name='protocol.ChainPeerMessage.src_peer_addr', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='des_peer_addrs', full_name='protocol.ChainPeerMessage.des_peer_addrs', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='protocol.ChainPeerMessage.data', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1143,
  serialized_end=1222,
)


_CHAINSUBSCRIBETX = _descriptor.Descriptor(
  name='ChainSubscribeTx',
  full_name='protocol.ChainSubscribeTx',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='protocol.ChainSubscribeTx.address', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1224,
  serialized_end=1259,
)


_CHAINRESPONSE = _descriptor.Descriptor(
  name='ChainResponse',
  full_name='protocol.ChainResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='error_code', full_name='protocol.ChainResponse.error_code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error_desc', full_name='protocol.ChainResponse.error_desc', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1261,
  serialized_end=1316,
)


_CHAINTXSTATUS = _descriptor.Descriptor(
  name='ChainTxStatus',
  full_name='protocol.ChainTxStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='protocol.ChainTxStatus.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tx_hash', full_name='protocol.ChainTxStatus.tx_hash', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='source_address', full_name='protocol.ChainTxStatus.source_address', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='source_account_seq', full_name='protocol.ChainTxStatus.source_account_seq', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ledger_seq', full_name='protocol.ChainTxStatus.ledger_seq', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='new_account_seq', full_name='protocol.ChainTxStatus.new_account_seq', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error_code', full_name='protocol.ChainTxStatus.error_code', index=6,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error_desc', full_name='protocol.ChainTxStatus.error_desc', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='protocol.ChainTxStatus.timestamp', index=8,
      number=9, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CHAINTXSTATUS_TXSTATUS,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1319,
  serialized_end=1660,
)

_HELLORESPONSE.fields_by_name['error_code'].enum_type = common__pb2._ERRORCODE
_PEERS.fields_by_name['peers'].message_type = _PEER
_LEDGERS.fields_by_name['values'].message_type = chain__pb2._CONSENSUSVALUE
_LEDGERS.fields_by_name['sync_code'].enum_type = _LEDGERS_SYNCCODE
_LEDGERS_SYNCCODE.containing_type = _LEDGERS
_LEDGERUPGRADENOTIFY.fields_by_name['upgrade'].message_type = common__pb2._LEDGERUPGRADE
_LEDGERUPGRADENOTIFY.fields_by_name['signature'].message_type = common__pb2._SIGNATURE
_CHAINHELLO.fields_by_name['api_list'].enum_type = _CHAINMESSAGETYPE
_CHAINTXSTATUS.fields_by_name['status'].enum_type = _CHAINTXSTATUS_TXSTATUS
_CHAINTXSTATUS.fields_by_name['error_code'].enum_type = common__pb2._ERRORCODE
_CHAINTXSTATUS_TXSTATUS.containing_type = _CHAINTXSTATUS
DESCRIPTOR.message_types_by_name['Hello'] = _HELLO
DESCRIPTOR.message_types_by_name['HelloResponse'] = _HELLORESPONSE
DESCRIPTOR.message_types_by_name['Peer'] = _PEER
DESCRIPTOR.message_types_by_name['Peers'] = _PEERS
DESCRIPTOR.message_types_by_name['GetLedgers'] = _GETLEDGERS
DESCRIPTOR.message_types_by_name['Ledgers'] = _LEDGERS
DESCRIPTOR.message_types_by_name['DontHave'] = _DONTHAVE
DESCRIPTOR.message_types_by_name['LedgerUpgradeNotify'] = _LEDGERUPGRADENOTIFY
DESCRIPTOR.message_types_by_name['EntryList'] = _ENTRYLIST
DESCRIPTOR.message_types_by_name['ChainHello'] = _CHAINHELLO
DESCRIPTOR.message_types_by_name['ChainStatus'] = _CHAINSTATUS
DESCRIPTOR.message_types_by_name['ChainPeerMessage'] = _CHAINPEERMESSAGE
DESCRIPTOR.message_types_by_name['ChainSubscribeTx'] = _CHAINSUBSCRIBETX
DESCRIPTOR.message_types_by_name['ChainResponse'] = _CHAINRESPONSE
DESCRIPTOR.message_types_by_name['ChainTxStatus'] = _CHAINTXSTATUS
DESCRIPTOR.enum_types_by_name['OVERLAY_MESSAGE_TYPE'] = _OVERLAY_MESSAGE_TYPE
DESCRIPTOR.enum_types_by_name['ChainMessageType'] = _CHAINMESSAGETYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Hello = _reflection.GeneratedProtocolMessageType('Hello', (_message.Message,), dict(
  DESCRIPTOR = _HELLO,
  __module__ = 'overlay_pb2'
  # @@protoc_insertion_point(class_scope:protocol.Hello)
  ))
_sym_db.RegisterMessage(Hello)

HelloResponse = _reflection.GeneratedProtocolMessageType('HelloResponse', (_message.Message,), dict(
  DESCRIPTOR = _HELLORESPONSE,
  __module__ = 'overlay_pb2'
  # @@protoc_insertion_point(class_scope:protocol.HelloResponse)
  ))
_sym_db.RegisterMessage(HelloResponse)

Peer = _reflection.GeneratedProtocolMessageType('Peer', (_message.Message,), dict(
  DESCRIPTOR = _PEER,
  __module__ = 'overlay_pb2'
  # @@protoc_insertion_point(class_scope:protocol.Peer)
  ))
_sym_db.RegisterMessage(Peer)

Peers = _reflection.GeneratedProtocolMessageType('Peers', (_message.Message,), dict(
  DESCRIPTOR = _PEERS,
  __module__ = 'overlay_pb2'
  # @@protoc_insertion_point(class_scope:protocol.Peers)
  ))
_sym_db.RegisterMessage(Peers)

GetLedgers = _reflection.GeneratedProtocolMessageType('GetLedgers', (_message.Message,), dict(
  DESCRIPTOR = _GETLEDGERS,
  __module__ = 'overlay_pb2'
  # @@protoc_insertion_point(class_scope:protocol.GetLedgers)
  ))
_sym_db.RegisterMessage(GetLedgers)

Ledgers = _reflection.GeneratedProtocolMessageType('Ledgers', (_message.Message,), dict(
  DESCRIPTOR = _LEDGERS,
  __module__ = 'overlay_pb2'
  # @@protoc_insertion_point(class_scope:protocol.Ledgers)
  ))
_sym_db.RegisterMessage(Ledgers)

DontHave = _reflection.GeneratedProtocolMessageType('DontHave', (_message.Message,), dict(
  DESCRIPTOR = _DONTHAVE,
  __module__ = 'overlay_pb2'
  # @@protoc_insertion_point(class_scope:protocol.DontHave)
  ))
_sym_db.RegisterMessage(DontHave)

LedgerUpgradeNotify = _reflection.GeneratedProtocolMessageType('LedgerUpgradeNotify', (_message.Message,), dict(
  DESCRIPTOR = _LEDGERUPGRADENOTIFY,
  __module__ = 'overlay_pb2'
  # @@protoc_insertion_point(class_scope:protocol.LedgerUpgradeNotify)
  ))
_sym_db.RegisterMessage(LedgerUpgradeNotify)

EntryList = _reflection.GeneratedProtocolMessageType('EntryList', (_message.Message,), dict(
  DESCRIPTOR = _ENTRYLIST,
  __module__ = 'overlay_pb2'
  # @@protoc_insertion_point(class_scope:protocol.EntryList)
  ))
_sym_db.RegisterMessage(EntryList)

ChainHello = _reflection.GeneratedProtocolMessageType('ChainHello', (_message.Message,), dict(
  DESCRIPTOR = _CHAINHELLO,
  __module__ = 'overlay_pb2'
  # @@protoc_insertion_point(class_scope:protocol.ChainHello)
  ))
_sym_db.RegisterMessage(ChainHello)

ChainStatus = _reflection.GeneratedProtocolMessageType('ChainStatus', (_message.Message,), dict(
  DESCRIPTOR = _CHAINSTATUS,
  __module__ = 'overlay_pb2'
  # @@protoc_insertion_point(class_scope:protocol.ChainStatus)
  ))
_sym_db.RegisterMessage(ChainStatus)

ChainPeerMessage = _reflection.GeneratedProtocolMessageType('ChainPeerMessage', (_message.Message,), dict(
  DESCRIPTOR = _CHAINPEERMESSAGE,
  __module__ = 'overlay_pb2'
  # @@protoc_insertion_point(class_scope:protocol.ChainPeerMessage)
  ))
_sym_db.RegisterMessage(ChainPeerMessage)

ChainSubscribeTx = _reflection.GeneratedProtocolMessageType('ChainSubscribeTx', (_message.Message,), dict(
  DESCRIPTOR = _CHAINSUBSCRIBETX,
  __module__ = 'overlay_pb2'
  # @@protoc_insertion_point(class_scope:protocol.ChainSubscribeTx)
  ))
_sym_db.RegisterMessage(ChainSubscribeTx)

ChainResponse = _reflection.GeneratedProtocolMessageType('ChainResponse', (_message.Message,), dict(
  DESCRIPTOR = _CHAINRESPONSE,
  __module__ = 'overlay_pb2'
  # @@protoc_insertion_point(class_scope:protocol.ChainResponse)
  ))
_sym_db.RegisterMessage(ChainResponse)

ChainTxStatus = _reflection.GeneratedProtocolMessageType('ChainTxStatus', (_message.Message,), dict(
  DESCRIPTOR = _CHAINTXSTATUS,
  __module__ = 'overlay_pb2'
  # @@protoc_insertion_point(class_scope:protocol.ChainTxStatus)
  ))
_sym_db.RegisterMessage(ChainTxStatus)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n io.rexx.sdk.core.extend.protobuf'))
# @@protoc_insertion_point(module_scope)
