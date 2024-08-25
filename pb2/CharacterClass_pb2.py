# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: CharacterClass.proto
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
    'CharacterClass.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import pb2._Item_pb2 as __Item__pb2
import pb2._Character_pb2 as __Character__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14\x43haracterClass.proto\x12\tDC.Packet\x1a\x0b_Item.proto\x1a\x10_Character.proto\"d\n\x15STRAINING_REWARD_INFO\x12\x10\n\x08uniqueId\x18\x01 \x01(\x05\x12\x12\n\nrewardType\x18\x02 \x01(\t\x12\x10\n\x08rewardId\x18\x03 \x01(\t\x12\x13\n\x0brewardCount\x18\x04 \x01(\x05\"\xe5\x01\n\x14SCLASS_TRAINING_INFO\x12\r\n\x05state\x18\x01 \x01(\x05\x12\x1b\n\x13\x63lassAbilityChoices\x18\x02 \x03(\t\x12\x37\n\rrewardChoices\x18\x03 \x03(\x0b\x32 .DC.Packet.STRAINING_REWARD_INFO\x12\x16\n\x0e\x63haracterClass\x18\x04 \x01(\t\x12\x10\n\x08isMaster\x18\x05 \x01(\x05\">\n\x05STATE\x12\x16\n\x12TRAINING_INFO_NONE\x10\x00\x12\x11\n\rCLASS_ABILITY\x10\x01\x12\n\n\x06REWARD\x10\x02\"\xba\x01\n\x18STRAINING_CHARACTER_INFO\x12\x13\n\x0b\x63haracterId\x18\x01 \x01(\t\x12.\n\x08nickname\x18\x02 \x01(\x0b\x32\x1c.DC.Packet.SACCOUNT_NICKNAME\x12\x16\n\x0e\x63haracterClass\x18\x03 \x01(\t\x12\x0e\n\x06gender\x18\x04 \x01(\x05\x12\r\n\x05level\x18\x05 \x01(\x05\x12\x10\n\x08isMaster\x18\x06 \x01(\x05\x12\x10\n\x08hasLearn\x18\x07 \x01(\x05\"\x18\n\x16SC2S_TRAINING_INFO_REQ\"\x80\x01\n\x16SS2C_TRAINING_INFO_RES\x12-\n\x04info\x18\x01 \x01(\x0b\x32\x1f.DC.Packet.SCLASS_TRAINING_INFO\x12\x37\n\ncharacters\x18\x02 \x03(\x0b\x32#.DC.Packet.STRAINING_CHARACTER_INFO\"D\n\'SC2S_TRAINING_REDEEM_LEARNING_TOKEN_REQ\x12\x19\n\x11masterCharacterId\x18\x01 \x01(\t\"p\n\'SS2C_TRAINING_REDEEM_LEARNING_TOKEN_RES\x12\x0e\n\x06result\x18\x01 \x01(\r\x12\x17\n\x0f\x63lassAbilityIds\x18\x02 \x03(\t\x12\x1c\n\x14masterCharacterClass\x18\x03 \x01(\t\"A\n\'SC2S_TRAINING_RECEIVE_CLASS_ABILITY_REQ\x12\x16\n\x0e\x63lassAbilityId\x18\x01 \x01(\t\"9\n\'SS2C_TRAINING_RECEIVE_CLASS_ABILITY_RES\x12\x0e\n\x06result\x18\x01 \x01(\r\"\'\n%SC2S_TRAINING_REDEEM_REWARD_TOKEN_REQ\"j\n%SS2C_TRAINING_REDEEM_REWARD_TOKEN_RES\x12\x0e\n\x06result\x18\x01 \x01(\r\x12\x31\n\x07rewards\x18\x02 \x03(\x0b\x32 .DC.Packet.STRAINING_REWARD_INFO\"\x93\x01\n\x18STRAINING_ITEM_SLOT_INFO\x12\x13\n\x0binventoryId\x18\x01 \x01(\r\x12\x0e\n\x06slotId\x18\x02 \x01(\r\x12\x0e\n\x06itemId\x18\x03 \x01(\t\x12\x14\n\x0citemUniqueId\x18\x04 \x01(\x04\x12\x11\n\titemCount\x18\x05 \x01(\r\x12\x19\n\x11itemContentsCount\x18\x06 \x01(\r\"l\n SC2S_TRAINING_RECEIVE_REWARD_REQ\x12\x10\n\x08uniqueId\x18\x01 \x01(\x05\x12\x36\n\tslotInfos\x18\x02 \x03(\x0b\x32#.DC.Packet.STRAINING_ITEM_SLOT_INFO\"2\n SS2C_TRAINING_RECEIVE_REWARD_RES\x12\x0e\n\x06result\x18\x01 \x01(\x05\"q\n\x11SCLASS_EQUIP_INFO\x12\r\n\x05index\x18\x01 \x01(\r\x12\x17\n\x0fisAvailableSlot\x18\x02 \x01(\r\x12\x15\n\rrequiredLevel\x18\x03 \x01(\r\x12\x0c\n\x04type\x18\x04 \x01(\r\x12\x0f\n\x07\x65quipId\x18\x05 \x01(\t\"M\n\x10SCLASS_MOVE_INFO\x12\r\n\x05index\x18\x01 \x01(\r\x12\x0c\n\x04type\x18\x02 \x01(\r\x12\x0e\n\x06moveId\x18\x03 \x01(\t\x12\x0c\n\x04move\x18\x04 \x01(\r\"\x1b\n\x19SC2S_CLASS_LEVEL_INFO_REQ\"\xc9\x01\n\x19SS2C_CLASS_LEVEL_INFO_RES\x12\r\n\x05level\x18\x01 \x01(\r\x12\x0b\n\x03\x65xp\x18\x02 \x01(\r\x12\x10\n\x08\x65xpBegin\x18\x03 \x01(\r\x12\x10\n\x08\x65xpLimit\x18\x04 \x01(\r\x12\x13\n\x0brewardPoint\x18\x05 \x01(\r\x12\x17\n\x0fnextRewardLevel\x18\x06 \x01(\r\x12\x15\n\rlearningPoint\x18\x07 \x01(\r\x12\x19\n\x11nextLearningLevel\x18\x08 \x01(\r\x12\x0c\n\x04\x66\x61me\x18\t \x01(\r\"\x1b\n\x19SC2S_CLASS_EQUIP_INFO_REQ\"I\n\x19SS2C_CLASS_EQUIP_INFO_RES\x12,\n\x06\x65quips\x18\x01 \x03(\x0b\x32\x1c.DC.Packet.SCLASS_EQUIP_INFO\"\x1a\n\x18SC2S_CLASS_PERK_LIST_REQ\";\n\x18SS2C_CLASS_PERK_LIST_RES\x12\x1f\n\x05perks\x18\x01 \x03(\x0b\x32\x10.DC.Packet.SPerk\"\x1b\n\x19SC2S_CLASS_SKILL_LIST_REQ\">\n\x19SS2C_CLASS_SKILL_LIST_RES\x12!\n\x06skills\x18\x01 \x03(\x0b\x32\x11.DC.Packet.SSkill\"3\n\x19SC2S_CLASS_SPELL_LIST_REQ\x12\x16\n\x0emaxSpellMemory\x18\x01 \x01(\r\">\n\x19SS2C_CLASS_SPELL_LIST_RES\x12!\n\x06spells\x18\x01 \x03(\x0b\x32\x11.DC.Packet.SSpell\"\x1b\n\x19SC2S_CLASS_MUSIC_LIST_REQ\">\n\x19SS2C_CLASS_MUSIC_LIST_RES\x12!\n\x06musics\x18\x01 \x03(\x0b\x32\x11.DC.Packet.SMusic\" \n\x1eSC2S_CLASS_SHAPESHIFT_LIST_REQ\"M\n\x1eSS2C_CLASS_SHAPESHIFT_LIST_RES\x12+\n\x0bshapeShifts\x18\x01 \x03(\x0b\x32\x16.DC.Packet.SShapeShift\"G\n\x1eSC2S_CLASS_SPELL_SLOT_MOVE_REQ\x12\x0f\n\x07spellId\x18\x01 \x01(\t\x12\x14\n\x0c\x64stSlotIndex\x18\x02 \x01(\x05\"[\n\x1eSS2C_CLASS_SPELL_SLOT_MOVE_RES\x12\x0e\n\x06result\x18\x01 \x01(\r\x12)\n\x0e\x65quipSpellList\x18\x02 \x03(\x0b\x32\x11.DC.Packet.SSpell\"Q\n$SC2S_CLASS_SPELL_SEQUENCE_CHANGE_REQ\x12\x0f\n\x07spellId\x18\x01 \x01(\t\x12\x18\n\x10\x64stSequenceIndex\x18\x02 \x01(\r\"a\n$SS2C_CLASS_SPELL_SEQUENCE_CHANGE_RES\x12\x0e\n\x06result\x18\x01 \x01(\r\x12)\n\x0e\x65quipSpellList\x18\x02 \x03(\x0b\x32\x11.DC.Packet.SSpell\"v\n\x18SC2S_CLASS_ITEM_MOVE_REQ\x12,\n\x07oldMove\x18\x01 \x01(\x0b\x32\x1b.DC.Packet.SCLASS_MOVE_INFO\x12,\n\x07newMove\x18\x02 \x01(\x0b\x32\x1b.DC.Packet.SCLASS_MOVE_INFO\"\x86\x01\n\x18SS2C_CLASS_ITEM_MOVE_RES\x12\x0e\n\x06result\x18\x01 \x01(\r\x12,\n\x07oldMove\x18\x02 \x01(\x0b\x32\x1b.DC.Packet.SCLASS_MOVE_INFO\x12,\n\x07newMove\x18\x03 \x01(\x0b\x32\x1b.DC.Packet.SCLASS_MOVE_INFO\"G\n\x1eSC2S_CLASS_MUSIC_SLOT_MOVE_REQ\x12\x0f\n\x07musicId\x18\x01 \x01(\t\x12\x14\n\x0c\x64stSlotIndex\x18\x02 \x01(\x05\"[\n\x1eSS2C_CLASS_MUSIC_SLOT_MOVE_RES\x12\x0e\n\x06result\x18\x01 \x01(\r\x12)\n\x0e\x65quipMusicList\x18\x02 \x03(\x0b\x32\x11.DC.Packet.SMusic\"Q\n$SC2S_CLASS_MUSIC_SEQUENCE_CHANGE_REQ\x12\x0f\n\x07musicId\x18\x01 \x01(\t\x12\x18\n\x10\x64stSequenceIndex\x18\x02 \x01(\r\"a\n$SS2C_CLASS_MUSIC_SEQUENCE_CHANGE_RES\x12\x0e\n\x06result\x18\x01 \x01(\r\x12)\n\x0e\x65quipMusicList\x18\x02 \x03(\x0b\x32\x11.DC.Packet.SMusic\"Q\n#SC2S_CLASS_SHAPESHIFT_SLOT_MOVE_REQ\x12\x14\n\x0cshapeShiftId\x18\x01 \x01(\t\x12\x14\n\x0c\x64stSlotIndex\x18\x02 \x01(\x05\"j\n#SS2C_CLASS_SHAPESHIFT_SLOT_MOVE_RES\x12\x0e\n\x06result\x18\x01 \x01(\r\x12\x33\n\x13\x65quipShapeShiftList\x18\x02 \x03(\x0b\x32\x16.DC.Packet.SShapeShift\"[\n)SC2S_CLASS_SHAPESHIFT_SEQUENCE_CHANGE_REQ\x12\x14\n\x0cshapeShiftId\x18\x01 \x01(\t\x12\x18\n\x10\x64stSequenceIndex\x18\x02 \x01(\r\"p\n)SS2C_CLASS_SHAPESHIFT_SEQUENCE_CHANGE_RES\x12\x0e\n\x06result\x18\x01 \x01(\r\x12\x33\n\x13\x65quipShapeShiftList\x18\x02 \x03(\x0b\x32\x16.DC.Packet.SShapeShiftB.\n\x1a\x63om.packets.characterClassB\x0e\x63haracterClassP\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'CharacterClass_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\032com.packets.characterClassB\016characterClassP\000'
  _globals['_STRAINING_REWARD_INFO']._serialized_start=66
  _globals['_STRAINING_REWARD_INFO']._serialized_end=166
  _globals['_SCLASS_TRAINING_INFO']._serialized_start=169
  _globals['_SCLASS_TRAINING_INFO']._serialized_end=398
  _globals['_SCLASS_TRAINING_INFO_STATE']._serialized_start=336
  _globals['_SCLASS_TRAINING_INFO_STATE']._serialized_end=398
  _globals['_STRAINING_CHARACTER_INFO']._serialized_start=401
  _globals['_STRAINING_CHARACTER_INFO']._serialized_end=587
  _globals['_SC2S_TRAINING_INFO_REQ']._serialized_start=589
  _globals['_SC2S_TRAINING_INFO_REQ']._serialized_end=613
  _globals['_SS2C_TRAINING_INFO_RES']._serialized_start=616
  _globals['_SS2C_TRAINING_INFO_RES']._serialized_end=744
  _globals['_SC2S_TRAINING_REDEEM_LEARNING_TOKEN_REQ']._serialized_start=746
  _globals['_SC2S_TRAINING_REDEEM_LEARNING_TOKEN_REQ']._serialized_end=814
  _globals['_SS2C_TRAINING_REDEEM_LEARNING_TOKEN_RES']._serialized_start=816
  _globals['_SS2C_TRAINING_REDEEM_LEARNING_TOKEN_RES']._serialized_end=928
  _globals['_SC2S_TRAINING_RECEIVE_CLASS_ABILITY_REQ']._serialized_start=930
  _globals['_SC2S_TRAINING_RECEIVE_CLASS_ABILITY_REQ']._serialized_end=995
  _globals['_SS2C_TRAINING_RECEIVE_CLASS_ABILITY_RES']._serialized_start=997
  _globals['_SS2C_TRAINING_RECEIVE_CLASS_ABILITY_RES']._serialized_end=1054
  _globals['_SC2S_TRAINING_REDEEM_REWARD_TOKEN_REQ']._serialized_start=1056
  _globals['_SC2S_TRAINING_REDEEM_REWARD_TOKEN_REQ']._serialized_end=1095
  _globals['_SS2C_TRAINING_REDEEM_REWARD_TOKEN_RES']._serialized_start=1097
  _globals['_SS2C_TRAINING_REDEEM_REWARD_TOKEN_RES']._serialized_end=1203
  _globals['_STRAINING_ITEM_SLOT_INFO']._serialized_start=1206
  _globals['_STRAINING_ITEM_SLOT_INFO']._serialized_end=1353
  _globals['_SC2S_TRAINING_RECEIVE_REWARD_REQ']._serialized_start=1355
  _globals['_SC2S_TRAINING_RECEIVE_REWARD_REQ']._serialized_end=1463
  _globals['_SS2C_TRAINING_RECEIVE_REWARD_RES']._serialized_start=1465
  _globals['_SS2C_TRAINING_RECEIVE_REWARD_RES']._serialized_end=1515
  _globals['_SCLASS_EQUIP_INFO']._serialized_start=1517
  _globals['_SCLASS_EQUIP_INFO']._serialized_end=1630
  _globals['_SCLASS_MOVE_INFO']._serialized_start=1632
  _globals['_SCLASS_MOVE_INFO']._serialized_end=1709
  _globals['_SC2S_CLASS_LEVEL_INFO_REQ']._serialized_start=1711
  _globals['_SC2S_CLASS_LEVEL_INFO_REQ']._serialized_end=1738
  _globals['_SS2C_CLASS_LEVEL_INFO_RES']._serialized_start=1741
  _globals['_SS2C_CLASS_LEVEL_INFO_RES']._serialized_end=1942
  _globals['_SC2S_CLASS_EQUIP_INFO_REQ']._serialized_start=1944
  _globals['_SC2S_CLASS_EQUIP_INFO_REQ']._serialized_end=1971
  _globals['_SS2C_CLASS_EQUIP_INFO_RES']._serialized_start=1973
  _globals['_SS2C_CLASS_EQUIP_INFO_RES']._serialized_end=2046
  _globals['_SC2S_CLASS_PERK_LIST_REQ']._serialized_start=2048
  _globals['_SC2S_CLASS_PERK_LIST_REQ']._serialized_end=2074
  _globals['_SS2C_CLASS_PERK_LIST_RES']._serialized_start=2076
  _globals['_SS2C_CLASS_PERK_LIST_RES']._serialized_end=2135
  _globals['_SC2S_CLASS_SKILL_LIST_REQ']._serialized_start=2137
  _globals['_SC2S_CLASS_SKILL_LIST_REQ']._serialized_end=2164
  _globals['_SS2C_CLASS_SKILL_LIST_RES']._serialized_start=2166
  _globals['_SS2C_CLASS_SKILL_LIST_RES']._serialized_end=2228
  _globals['_SC2S_CLASS_SPELL_LIST_REQ']._serialized_start=2230
  _globals['_SC2S_CLASS_SPELL_LIST_REQ']._serialized_end=2281
  _globals['_SS2C_CLASS_SPELL_LIST_RES']._serialized_start=2283
  _globals['_SS2C_CLASS_SPELL_LIST_RES']._serialized_end=2345
  _globals['_SC2S_CLASS_MUSIC_LIST_REQ']._serialized_start=2347
  _globals['_SC2S_CLASS_MUSIC_LIST_REQ']._serialized_end=2374
  _globals['_SS2C_CLASS_MUSIC_LIST_RES']._serialized_start=2376
  _globals['_SS2C_CLASS_MUSIC_LIST_RES']._serialized_end=2438
  _globals['_SC2S_CLASS_SHAPESHIFT_LIST_REQ']._serialized_start=2440
  _globals['_SC2S_CLASS_SHAPESHIFT_LIST_REQ']._serialized_end=2472
  _globals['_SS2C_CLASS_SHAPESHIFT_LIST_RES']._serialized_start=2474
  _globals['_SS2C_CLASS_SHAPESHIFT_LIST_RES']._serialized_end=2551
  _globals['_SC2S_CLASS_SPELL_SLOT_MOVE_REQ']._serialized_start=2553
  _globals['_SC2S_CLASS_SPELL_SLOT_MOVE_REQ']._serialized_end=2624
  _globals['_SS2C_CLASS_SPELL_SLOT_MOVE_RES']._serialized_start=2626
  _globals['_SS2C_CLASS_SPELL_SLOT_MOVE_RES']._serialized_end=2717
  _globals['_SC2S_CLASS_SPELL_SEQUENCE_CHANGE_REQ']._serialized_start=2719
  _globals['_SC2S_CLASS_SPELL_SEQUENCE_CHANGE_REQ']._serialized_end=2800
  _globals['_SS2C_CLASS_SPELL_SEQUENCE_CHANGE_RES']._serialized_start=2802
  _globals['_SS2C_CLASS_SPELL_SEQUENCE_CHANGE_RES']._serialized_end=2899
  _globals['_SC2S_CLASS_ITEM_MOVE_REQ']._serialized_start=2901
  _globals['_SC2S_CLASS_ITEM_MOVE_REQ']._serialized_end=3019
  _globals['_SS2C_CLASS_ITEM_MOVE_RES']._serialized_start=3022
  _globals['_SS2C_CLASS_ITEM_MOVE_RES']._serialized_end=3156
  _globals['_SC2S_CLASS_MUSIC_SLOT_MOVE_REQ']._serialized_start=3158
  _globals['_SC2S_CLASS_MUSIC_SLOT_MOVE_REQ']._serialized_end=3229
  _globals['_SS2C_CLASS_MUSIC_SLOT_MOVE_RES']._serialized_start=3231
  _globals['_SS2C_CLASS_MUSIC_SLOT_MOVE_RES']._serialized_end=3322
  _globals['_SC2S_CLASS_MUSIC_SEQUENCE_CHANGE_REQ']._serialized_start=3324
  _globals['_SC2S_CLASS_MUSIC_SEQUENCE_CHANGE_REQ']._serialized_end=3405
  _globals['_SS2C_CLASS_MUSIC_SEQUENCE_CHANGE_RES']._serialized_start=3407
  _globals['_SS2C_CLASS_MUSIC_SEQUENCE_CHANGE_RES']._serialized_end=3504
  _globals['_SC2S_CLASS_SHAPESHIFT_SLOT_MOVE_REQ']._serialized_start=3506
  _globals['_SC2S_CLASS_SHAPESHIFT_SLOT_MOVE_REQ']._serialized_end=3587
  _globals['_SS2C_CLASS_SHAPESHIFT_SLOT_MOVE_RES']._serialized_start=3589
  _globals['_SS2C_CLASS_SHAPESHIFT_SLOT_MOVE_RES']._serialized_end=3695
  _globals['_SC2S_CLASS_SHAPESHIFT_SEQUENCE_CHANGE_REQ']._serialized_start=3697
  _globals['_SC2S_CLASS_SHAPESHIFT_SEQUENCE_CHANGE_REQ']._serialized_end=3788
  _globals['_SS2C_CLASS_SHAPESHIFT_SEQUENCE_CHANGE_RES']._serialized_start=3790
  _globals['_SS2C_CLASS_SHAPESHIFT_SEQUENCE_CHANGE_RES']._serialized_end=3902
# @@protoc_insertion_point(module_scope)