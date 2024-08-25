import pb2._Character_pb2 as _Character_pb2
import pb2._Chat_pb2 as _Chat_pb2
import pb2._Defins_pb2 as _Defins_pb2
import pb2._Item_pb2 as _Item_pb2
import pb2._PacketCommand_pb2 as _PacketCommand_pb2
import pb2._Reward_pb2 as _Reward_pb2
import pb2.Account_pb2 as Account_pb2
import pb2.Agent_pb2 as Agent_pb2
import pb2.CharacterClass_pb2 as CharacterClass_pb2
import pb2.Common_pb2 as Common_pb2
import pb2.Customize_pb2 as Customize_pb2
import pb2.DediServer_pb2 as DediServer_pb2
import pb2.Friend_pb2 as Friend_pb2
import pb2.GatheringHall_pb2 as GatheringHall_pb2
import pb2.Gm_pb2 as Gm_pb2
import pb2.InGame_pb2 as InGame_pb2
import pb2.Inventory_pb2 as Inventory_pb2
import pb2.IronMace_pb2 as IronMace_pb2
import pb2.Karma_pb2 as Karma_pb2
import pb2.Lobby_pb2 as Lobby_pb2
import pb2.MarketPlace_pb2 as MarketPlace_pb2
import pb2.Merchant_pb2 as Merchant_pb2
import pb2.Operate_pb2 as Operate_pb2
import pb2.Party_pb2 as Party_pb2
import pb2.Ranking_pb2 as Ranking_pb2
import pb2.Shop_pb2 as Shop_pb2
import pb2.Trade_pb2 as Trade_pb2

import sys

from helpers import messageMap

classes = [_Character_pb2,
_Chat_pb2,
_Defins_pb2,
_Item_pb2,
_PacketCommand_pb2,
_Reward_pb2,
Account_pb2,
Agent_pb2,
CharacterClass_pb2,
Common_pb2,
Customize_pb2,
DediServer_pb2,
Friend_pb2,
GatheringHall_pb2,
Gm_pb2,
InGame_pb2,
Inventory_pb2,
IronMace_pb2,
Karma_pb2,
Lobby_pb2,
MarketPlace_pb2,
Merchant_pb2,
Operate_pb2,
Party_pb2,
Ranking_pb2,
Shop_pb2,
Trade_pb2]

def parse_all(data, proto_type, packet_length):
    method = list(messageMap.keys())[list(messageMap.values()).index(proto_type)]
    selectedClass = None
    try:
        for messageClass in classes:
            selectedClass = getattr(messageClass, 'S'+method, None)
            if callable(selectedClass):
                print(selectedClass)
                break

        methodFunc = getattr(messageClass, 'S'+method)
        info = methodFunc()

        try:
            print('Trying to parse...')
            info.ParseFromString(data[8:packet_length])
            print('Result:')
            print(info)
            return True
        except Exception as e:
            print('Failed')
            print(e)
            return False
        
    except Exception as e:
        print(e)

sys.modules[__name__] = parse_all