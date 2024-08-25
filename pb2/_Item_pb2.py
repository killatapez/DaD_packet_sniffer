# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: _Item.proto
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
    '_Item.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0b_Item.proto\x12\tDC.Packet\"\xa4\x01\n\tSItemMeta\x12\x1b\n\x13SoulHeart_AccountId\x18\x01 \x01(\t\x12\x19\n\x11SoulHeart_PartyId\x18\x02 \x01(\t\x12!\n\x19SoulHeart_NickName_origin\x18\x03 \x01(\t\x12$\n\x1cSoulHeart_NickName_streaming\x18\x04 \x01(\t\x12\x16\n\x0e\x41vailableValue\x18\x05 \x01(\r\"\xdb\x02\n\tSDownItem\x12\x14\n\x0citemUniqueId\x18\x01 \x01(\x04\x12\x0e\n\x06itemId\x18\x02 \x01(\t\x12\x11\n\titemCount\x18\x03 \x01(\r\x12\x13\n\x0binventoryId\x18\x04 \x01(\r\x12\x0e\n\x06slotId\x18\x05 \x01(\r\x12\x11\n\tbEquipped\x18\x06 \x01(\r\x12\x15\n\ritemAmmoCount\x18\x07 \x01(\r\x12\x19\n\x11itemContentsCount\x18\x08 \x01(\r\x12&\n\x08metaItem\x18\t \x01(\x0b\x32\x14.DC.Packet.SItemMeta\x12\x36\n\x14primaryPropertyArray\x18\n \x03(\x0b\x32\x18.DC.Packet.SItemProperty\x12\x38\n\x16secondaryPropertyArray\x18\x0b \x03(\x0b\x32\x18.DC.Packet.SItemProperty\x12\x11\n\tlootState\x18\x0c \x01(\x05\"\x9c\x02\n\x05SItem\x12\x14\n\x0citemUniqueId\x18\x01 \x01(\x04\x12\x0e\n\x06itemId\x18\x02 \x01(\t\x12\x11\n\titemCount\x18\x03 \x01(\r\x12\x13\n\x0binventoryId\x18\x04 \x01(\r\x12\x0e\n\x06slotId\x18\x05 \x01(\r\x12\x15\n\ritemAmmoCount\x18\x07 \x01(\r\x12\x19\n\x11itemContentsCount\x18\x08 \x01(\r\x12\x36\n\x14primaryPropertyArray\x18\t \x03(\x0b\x32\x18.DC.Packet.SItemProperty\x12\x38\n\x16secondaryPropertyArray\x18\n \x03(\x0b\x32\x18.DC.Packet.SItemProperty\x12\x11\n\tlootState\x18\x0b \x01(\x05\"?\n\x0fSItemProperties\x12,\n\nproperties\x18\x01 \x03(\x0b\x32\x18.DC.Packet.SItemProperty\">\n\rSItemProperty\x12\x16\n\x0epropertyTypeId\x18\x01 \x01(\t\x12\x15\n\rpropertyValue\x18\x02 \x01(\x05\"(\n\x06SItems\x12\x1e\n\x04item\x18\x01 \x03(\x0b\x32\x10.DC.Packet.SItem\"&\n\x05SPerk\x12\r\n\x05index\x18\x01 \x01(\r\x12\x0e\n\x06perkId\x18\x02 \x01(\t\"(\n\x06SSkill\x12\r\n\x05index\x18\x01 \x01(\r\x12\x0f\n\x07skillId\x18\x02 \x01(\t\"C\n\x06SSpell\x12\x11\n\tslotIndex\x18\x01 \x01(\r\x12\x15\n\rsequenceIndex\x18\x02 \x01(\r\x12\x0f\n\x07spellId\x18\x03 \x01(\t\"C\n\x06SMusic\x12\x0f\n\x07musicId\x18\x01 \x01(\t\x12\x11\n\tslotIndex\x18\x02 \x01(\r\x12\x15\n\rsequenceIndex\x18\x03 \x01(\r\"M\n\x0bSShapeShift\x12\x14\n\x0cshapeShiftId\x18\x01 \x01(\t\x12\x11\n\tslotIndex\x18\x02 \x01(\r\x12\x15\n\rsequenceIndex\x18\x03 \x01(\r\"T\n\x14SCUSTOMIZE_CHARACTER\x12\x1c\n\x14\x63ustomizeCharacterId\x18\x01 \x01(\t\x12\x0f\n\x07isEquip\x18\x02 \x01(\x05\x12\r\n\x05isNew\x18\x03 \x01(\x05\"J\n\x0fSCUSTOMIZE_ITEM\x12\x17\n\x0f\x63ustomizeItemId\x18\x01 \x01(\t\x12\x0f\n\x07isEquip\x18\x02 \x01(\x05\x12\r\n\x05isNew\x18\x03 \x01(\x05\"U\n\x15SCUSTOMIZE_ARMOR_SKIN\x12\x1c\n\x14\x63ustomizeArmorSkinId\x18\x01 \x01(\t\x12\x0f\n\x07isEquip\x18\x02 \x01(\x05\x12\r\n\x05isNew\x18\x03 \x01(\x05\"@\n\x06SEMOTE\x12\x0f\n\x07\x65moteId\x18\x01 \x01(\t\x12\x16\n\x0e\x65quipSlotIndex\x18\x02 \x01(\x05\x12\r\n\x05isNew\x18\x03 \x01(\x05\"N\n\x11SCUSTOMIZE_ACTION\x12\x19\n\x11\x63ustomizeActionId\x18\x01 \x01(\t\x12\x0f\n\x07isEquip\x18\x02 \x01(\x05\x12\r\n\x05isNew\x18\x03 \x01(\x05\"U\n\x16SCUSTOMIZE_LOBBY_EMOTE\x12\x14\n\x0clobbyEmoteId\x18\x01 \x01(\t\x12\x16\n\x0e\x65quipSlotIndex\x18\x02 \x01(\x05\x12\r\n\x05isNew\x18\x03 \x01(\x05\x42\x1a\n\x10\x63om.packets.itemB\x04itemP\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, '_Item_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\020com.packets.itemB\004itemP\000'
  _globals['_SITEMMETA']._serialized_start=27
  _globals['_SITEMMETA']._serialized_end=191
  _globals['_SDOWNITEM']._serialized_start=194
  _globals['_SDOWNITEM']._serialized_end=541
  _globals['_SITEM']._serialized_start=544
  _globals['_SITEM']._serialized_end=828
  _globals['_SITEMPROPERTIES']._serialized_start=830
  _globals['_SITEMPROPERTIES']._serialized_end=893
  _globals['_SITEMPROPERTY']._serialized_start=895
  _globals['_SITEMPROPERTY']._serialized_end=957
  _globals['_SITEMS']._serialized_start=959
  _globals['_SITEMS']._serialized_end=999
  _globals['_SPERK']._serialized_start=1001
  _globals['_SPERK']._serialized_end=1039
  _globals['_SSKILL']._serialized_start=1041
  _globals['_SSKILL']._serialized_end=1081
  _globals['_SSPELL']._serialized_start=1083
  _globals['_SSPELL']._serialized_end=1150
  _globals['_SMUSIC']._serialized_start=1152
  _globals['_SMUSIC']._serialized_end=1219
  _globals['_SSHAPESHIFT']._serialized_start=1221
  _globals['_SSHAPESHIFT']._serialized_end=1298
  _globals['_SCUSTOMIZE_CHARACTER']._serialized_start=1300
  _globals['_SCUSTOMIZE_CHARACTER']._serialized_end=1384
  _globals['_SCUSTOMIZE_ITEM']._serialized_start=1386
  _globals['_SCUSTOMIZE_ITEM']._serialized_end=1460
  _globals['_SCUSTOMIZE_ARMOR_SKIN']._serialized_start=1462
  _globals['_SCUSTOMIZE_ARMOR_SKIN']._serialized_end=1547
  _globals['_SEMOTE']._serialized_start=1549
  _globals['_SEMOTE']._serialized_end=1613
  _globals['_SCUSTOMIZE_ACTION']._serialized_start=1615
  _globals['_SCUSTOMIZE_ACTION']._serialized_end=1693
  _globals['_SCUSTOMIZE_LOBBY_EMOTE']._serialized_start=1695
  _globals['_SCUSTOMIZE_LOBBY_EMOTE']._serialized_end=1780
# @@protoc_insertion_point(module_scope)