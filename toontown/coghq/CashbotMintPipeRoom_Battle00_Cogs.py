from SpecImports import *
import random
CogParent = 10000
FrontCogParent = 10002
LeftCogParent = 10007
RightCogParent = 10010
BattleCellId = 0
FrontBattleCellId = 1
LeftBattleCellId = 2
RightBattleCellId = 3
BattleCells = {BattleCellId: {'parentEntId': CogParent,
                'pos': Point3(0, 0, 0)},
 FrontBattleCellId: {'parentEntId': FrontCogParent,
                     'pos': Point3(0, 0, 0)},
 LeftBattleCellId: {'parentEntId': LeftCogParent,
                    'pos': Point3(0, 0, 0)},
 RightBattleCellId: {'parentEntId': RightCogParent,
                     'pos': Point3(0, 0, 0)}}
CogData = [{'parentEntId': CogParent,
  'boss': 0,
  'level': random.choice([9, 10, 11, 12]),
  'battleCell': BattleCellId,
  'pos': Point3(-6, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0},
 {'parentEntId': CogParent,
  'boss': 0,
  'level': random.choice([9, 10, 11, 12]),
  'battleCell': BattleCellId,
  'pos': Point3(-2, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0},
 {'parentEntId': CogParent,
  'boss': 0,
  'level': random.choice([9, 10, 11, 12]),
  'battleCell': BattleCellId,
  'pos': Point3(2, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0},
 {'parentEntId': CogParent,
  'boss': 0,
  'level': random.choice([9, 10, 11, 12]),
  'battleCell': BattleCellId,
  'pos': Point3(6, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0},
 {'parentEntId': FrontCogParent,
  'boss': 0,
  'level': random.choice([9, 10, 11, 12]),
  'battleCell': FrontBattleCellId,
  'pos': Point3(-6, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0},
 {'parentEntId': FrontCogParent,
  'boss': 0,
  'level': random.choice([9, 10, 11, 12]),
  'battleCell': FrontBattleCellId,
  'pos': Point3(-2, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0},
 {'parentEntId': FrontCogParent,
  'boss': 0,
  'level': random.choice([9, 10, 11, 12]),
  'battleCell': FrontBattleCellId,
  'pos': Point3(2, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0},
 {'parentEntId': FrontCogParent,
  'boss': 0,
  'level': random.choice([9, 10, 11, 12]),
  'battleCell': FrontBattleCellId,
  'pos': Point3(6, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0},
 {'parentEntId': LeftCogParent,
  'boss': 0,
  'level': random.choice([9, 10, 11, 12]),
  'battleCell': LeftBattleCellId,
  'pos': Point3(-6, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0},
 {'parentEntId': LeftCogParent,
  'boss': 0,
  'level': random.choice([9, 10, 11, 12]),
  'battleCell': LeftBattleCellId,
  'pos': Point3(-2, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0},
 {'parentEntId': LeftCogParent,
  'boss': 0,
  'level': random.choice([9, 10, 11, 12]),
  'battleCell': LeftBattleCellId,
  'pos': Point3(2, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0},
 {'parentEntId': LeftCogParent,
  'boss': 0,
  'level': random.choice([9, 10, 11, 12]),
  'battleCell': LeftBattleCellId,
  'pos': Point3(6, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0},
 {'parentEntId': RightCogParent,
  'boss': 0,
  'level': random.choice([9, 10, 11, 12]),
  'battleCell': RightBattleCellId,
  'pos': Point3(-6, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0},
 {'parentEntId': RightCogParent,
  'boss': 0,
  'level': random.choice([9, 10, 11, 12]),
  'battleCell': RightBattleCellId,
  'pos': Point3(-2, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0},
 {'parentEntId': RightCogParent,
  'boss': 0,
  'level': random.choice([9, 10, 11, 12]),
  'battleCell': RightBattleCellId,
  'pos': Point3(2, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0},
 {'parentEntId': RightCogParent,
  'boss': 0,
  'level': random.choice([9, 10, 11, 12]),
  'battleCell': RightBattleCellId,
  'pos': Point3(6, 0, 0),
  'h': 180,
  'behavior': 'stand',
  'path': None,
  'skeleton': 0}]
ReserveCogData = []
