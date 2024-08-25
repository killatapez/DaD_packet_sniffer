# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: Lobby.proto
# Protobuf Python Version: 5.27.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    3,
    '',
    'Lobby.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import pb2._Character_pb2 as __Character__pb2
import pb2._Item_pb2 as __Item__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bLobby.proto\x12\tDC.Packet\x1a\x10_Character.proto\x1a\x0b_Item.proto\"!\n\x1fSC2S_CHARACTER_SELECT_ENTER_REQ\"1\n\x1fSS2C_CHARACTER_SELECT_ENTER_RES\x12\x0e\n\x06result\x18\x01 \x01(\r\"\x1f\n\x1dSC2S_LOBBY_CHARACTER_INFO_REQ\"f\n\x1dSS2C_LOBBY_CHARACTER_INFO_RES\x12\x0e\n\x06result\x18\x01 \x01(\r\x12\x35\n\x11\x63haracterDataBase\x18\x02 \x01(\x0b\x32\x1a.DC.Packet.SCHARACTER_INFO\"\x19\n\x17SC2S_OPEN_LOBBY_MAP_REQ\"\x19\n\x17SS2C_OPEN_LOBBY_MAP_RES\".\n\x1cSC2S_LOBBY_REGION_SELECT_REQ\x12\x0e\n\x06region\x18\x01 \x01(\r\">\n\x1cSS2C_LOBBY_REGION_SELECT_RES\x12\x0e\n\x06result\x18\x01 \x01(\r\x12\x0e\n\x06region\x18\x02 \x01(\r\" \n\x1eSC2S_LOBBY_ENTER_FROM_GAME_REQ\"0\n\x1eSS2C_LOBBY_ENTER_FROM_GAME_RES\x12\x0e\n\x06result\x18\x01 \x01(\r\"8\n\x1fSC2S_LOBBY_GAME_TYPE_SELECT_REQ\x12\x15\n\rgameTypeIndex\x18\x01 \x01(\r\"H\n\x1fSS2C_LOBBY_GAME_TYPE_SELECT_RES\x12\x0e\n\x06result\x18\x01 \x01(\r\x12\x15\n\rgameTypeIndex\x18\x02 \x01(\r\"E\n\x16SACCOUNT_CURRENCY_INFO\x12\x14\n\x0c\x63urrencyType\x18\x01 \x01(\r\x12\x15\n\rcurrencyValue\x18\x02 \x01(\r\"}\n$SS2C_LOBBY_ACCOUNT_CURRENCY_LIST_NOT\x12\x38\n\rcurrencyInfos\x18\x01 \x03(\x0b\x32!.DC.Packet.SACCOUNT_CURRENCY_INFO\x12\x1b\n\x13\x62uyRedstoneShardUrl\x18\x02 \x01(\t\"a\n$SS2C_LOBBY_CHARACTER_LOBBY_EMOTE_NOT\x12\x39\n\x0elobbyEmoteList\x18\x01 \x03(\x0b\x32!.DC.Packet.SCUSTOMIZE_LOBBY_EMOTE\"\\\n\x13SREPORT_PUNISH_INFO\x12.\n\x08nickname\x18\x01 \x01(\x0b\x32\x1c.DC.Packet.SACCOUNT_NICKNAME\x12\x15\n\rreportBanType\x18\x02 \x01(\x05\"\x9e\x01\n!SS2C_LOBBY_REPORT_PUNISH_LIST_NOT\x12-\n\x05infos\x18\x01 \x03(\x0b\x32\x1e.DC.Packet.SREPORT_PUNISH_INFO\"J\n\x0fREPORT_BAN_TYPE\x12\x11\n\rNONE_BAN_TYPE\x10\x00\x12\x11\n\rPERMANENT_BAN\x10\x01\x12\x11\n\rTEMPORARY_BAN\x10\x02\"b\n&SC2S_USER_CHARACTER_GAME_STAT_INFO_REQ\x12\x10\n\x08seasonId\x18\x01 \x01(\t\x12\x10\n\x08gameType\x18\x02 \x01(\x05\x12\x14\n\x0c\x64ungeonIdTag\x18\x03 \x01(\t\"\x8b\x01\n&SS2C_USER_CHARACTER_GAME_STAT_INFO_RES\x12\x10\n\x08seasonId\x18\x01 \x01(\t\x12\x10\n\x08gameType\x18\x02 \x01(\x05\x12\'\n\tgameStats\x18\x03 \x03(\x0b\x32\x14.DC.Packet.SGameStat\x12\x14\n\x0c\x64ungeonIdTag\x18\x04 \x01(\t\"%\n#SC2S_KNIGHT_PROGRAM_LINK_SELECT_REQ\"B\n#SS2C_KNIGHT_PROGRAM_LINK_SELECT_RES\x12\x0e\n\x06result\x18\x01 \x01(\x05\x12\x0b\n\x03url\x18\x02 \x01(\t\"|\n\x1aSC2S_GM_TRADE_CHAT_BAN_REQ\x12\x11\n\taccountId\x18\x01 \x01(\t\x12\x13\n\x0b\x63haracterId\x18\x02 \x01(\t\x12\x10\n\x08nickName\x18\x03 \x01(\t\x12\x13\n\x0blastChatMsg\x18\x04 \x01(\t\x12\x0f\n\x07\x62\x61nType\x18\x05 \x01(\r\",\n\x1aSS2C_GM_TRADE_CHAT_BAN_RES\x12\x0e\n\x06result\x18\x01 \x01(\rB\x1c\n\x11\x63om.packets.lobbyB\x05lobbyP\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'Lobby_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\021com.packets.lobbyB\005lobbyP\000'
  _globals['_SC2S_CHARACTER_SELECT_ENTER_REQ']._serialized_start=57
  _globals['_SC2S_CHARACTER_SELECT_ENTER_REQ']._serialized_end=90
  _globals['_SS2C_CHARACTER_SELECT_ENTER_RES']._serialized_start=92
  _globals['_SS2C_CHARACTER_SELECT_ENTER_RES']._serialized_end=141
  _globals['_SC2S_LOBBY_CHARACTER_INFO_REQ']._serialized_start=143
  _globals['_SC2S_LOBBY_CHARACTER_INFO_REQ']._serialized_end=174
  _globals['_SS2C_LOBBY_CHARACTER_INFO_RES']._serialized_start=176
  _globals['_SS2C_LOBBY_CHARACTER_INFO_RES']._serialized_end=278
  _globals['_SC2S_OPEN_LOBBY_MAP_REQ']._serialized_start=280
  _globals['_SC2S_OPEN_LOBBY_MAP_REQ']._serialized_end=305
  _globals['_SS2C_OPEN_LOBBY_MAP_RES']._serialized_start=307
  _globals['_SS2C_OPEN_LOBBY_MAP_RES']._serialized_end=332
  _globals['_SC2S_LOBBY_REGION_SELECT_REQ']._serialized_start=334
  _globals['_SC2S_LOBBY_REGION_SELECT_REQ']._serialized_end=380
  _globals['_SS2C_LOBBY_REGION_SELECT_RES']._serialized_start=382
  _globals['_SS2C_LOBBY_REGION_SELECT_RES']._serialized_end=444
  _globals['_SC2S_LOBBY_ENTER_FROM_GAME_REQ']._serialized_start=446
  _globals['_SC2S_LOBBY_ENTER_FROM_GAME_REQ']._serialized_end=478
  _globals['_SS2C_LOBBY_ENTER_FROM_GAME_RES']._serialized_start=480
  _globals['_SS2C_LOBBY_ENTER_FROM_GAME_RES']._serialized_end=528
  _globals['_SC2S_LOBBY_GAME_TYPE_SELECT_REQ']._serialized_start=530
  _globals['_SC2S_LOBBY_GAME_TYPE_SELECT_REQ']._serialized_end=586
  _globals['_SS2C_LOBBY_GAME_TYPE_SELECT_RES']._serialized_start=588
  _globals['_SS2C_LOBBY_GAME_TYPE_SELECT_RES']._serialized_end=660
  _globals['_SACCOUNT_CURRENCY_INFO']._serialized_start=662
  _globals['_SACCOUNT_CURRENCY_INFO']._serialized_end=731
  _globals['_SS2C_LOBBY_ACCOUNT_CURRENCY_LIST_NOT']._serialized_start=733
  _globals['_SS2C_LOBBY_ACCOUNT_CURRENCY_LIST_NOT']._serialized_end=858
  _globals['_SS2C_LOBBY_CHARACTER_LOBBY_EMOTE_NOT']._serialized_start=860
  _globals['_SS2C_LOBBY_CHARACTER_LOBBY_EMOTE_NOT']._serialized_end=957
  _globals['_SREPORT_PUNISH_INFO']._serialized_start=959
  _globals['_SREPORT_PUNISH_INFO']._serialized_end=1051
  _globals['_SS2C_LOBBY_REPORT_PUNISH_LIST_NOT']._serialized_start=1054
  _globals['_SS2C_LOBBY_REPORT_PUNISH_LIST_NOT']._serialized_end=1212
  _globals['_SS2C_LOBBY_REPORT_PUNISH_LIST_NOT_REPORT_BAN_TYPE']._serialized_start=1138
  _globals['_SS2C_LOBBY_REPORT_PUNISH_LIST_NOT_REPORT_BAN_TYPE']._serialized_end=1212
  _globals['_SC2S_USER_CHARACTER_GAME_STAT_INFO_REQ']._serialized_start=1214
  _globals['_SC2S_USER_CHARACTER_GAME_STAT_INFO_REQ']._serialized_end=1312
  _globals['_SS2C_USER_CHARACTER_GAME_STAT_INFO_RES']._serialized_start=1315
  _globals['_SS2C_USER_CHARACTER_GAME_STAT_INFO_RES']._serialized_end=1454
  _globals['_SC2S_KNIGHT_PROGRAM_LINK_SELECT_REQ']._serialized_start=1456
  _globals['_SC2S_KNIGHT_PROGRAM_LINK_SELECT_REQ']._serialized_end=1493
  _globals['_SS2C_KNIGHT_PROGRAM_LINK_SELECT_RES']._serialized_start=1495
  _globals['_SS2C_KNIGHT_PROGRAM_LINK_SELECT_RES']._serialized_end=1561
  _globals['_SC2S_GM_TRADE_CHAT_BAN_REQ']._serialized_start=1563
  _globals['_SC2S_GM_TRADE_CHAT_BAN_REQ']._serialized_end=1687
  _globals['_SS2C_GM_TRADE_CHAT_BAN_RES']._serialized_start=1689
  _globals['_SS2C_GM_TRADE_CHAT_BAN_RES']._serialized_end=1733
# @@protoc_insertion_point(module_scope)