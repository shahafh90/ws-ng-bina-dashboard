import uuid
from enum import Enum
import time


class ACTION_TYPE_ENUM(Enum):
    EntityCreated = 'EntityCreated'
    UserSearch = 'UserSearch'
    UserLogin = 'UserLogin'


class ENTITY_TYPE_ENUM(Enum):
    BinaInsight = 'BinaInsight'
    BinaNews = 'BinaNews'
    BinaEmail = 'BinaEmail'
    BinaFile = 'BinaFile'
    BinaRelation = 'BinaRelation'
    BinaChapter = 'BinaChapter'
    BinaCase = 'BinaCase'


actions = [
    {
        "_id": uuid.uuid4(),
        "doc": {
            'actionType': ACTION_TYPE_ENUM.EntityCreated.value,
            'actionTimeStamp': int(time.time() * 1000 - (1000 * 60 * 30)),
            'actionMetaData': '',
            'userId': 'wstu15',
            'userArena': 'זירה א',
            'userDepartment': 'מדור ג',
            'userEnv': 'EnvA',
            'entityType': ENTITY_TYPE_ENUM.BinaInsight.value,
            'entityId': 'BI12345'
        }
    },
    {
        "_id": uuid.uuid4(),
        "doc": {
            'actionType': ACTION_TYPE_ENUM.UserSearch.value,
            'actionTimeStamp': int(time.time() * 1000 - (1000 * 60 * 15)),
            'actionMetaData': 'Al Mabhuh',
            'userId': 'ssouser3',
            'userArena': 'זירה ד',
            'userDepartment': 'מדור א',
            'userEnv': 'EnvB',
            'entityType': ENTITY_TYPE_ENUM.BinaNews.value,
            'entityId': ''
        }
    },
    {
        "_id": uuid.uuid4(),
        "doc": {
            'actionType': ACTION_TYPE_ENUM.UserSearch.value,
            'actionTimeStamp': int(time.time() * 1000 - (1000 * 60 * 60)),
            'actionMetaData': 'Al Kayda',
            'userId': 'ssouser5',
            'userArena': 'זירה ד',
            'userDepartment': 'מדור א',
            'userEnv': 'EnvB',
            'entityType': '',
            'entityId': ''
        }
    },
    {
        "_id": uuid.uuid4(),
        "doc": {
            'actionType': ACTION_TYPE_ENUM.EntityCreated.value,
            'actionTimeStamp': int(time.time() * 1000),
            'actionMetaData': '',
            'userId': 'wstu15',
            'userArena': 'זירה א',
            'userDepartment': 'מדור ג',
            'userEnv': 'EnvA',
            'entityType': ENTITY_TYPE_ENUM.BinaNews.value,
            'entityId': 'BI12346'
        }
    },
    {
        "_id": uuid.uuid4(),
        "doc": {
            'actionType': ACTION_TYPE_ENUM.EntityCreated.value,
            'actionTimeStamp': int(time.time() * 1000 - (1000 * 60 * 5)),
            'actionMetaData': '',
            'userId': 'wstu15',
            'userArena': 'זירה ד',
            'userDepartment': 'מדור ג',
            'userEnv': 'EnvA',
            'entityType': ENTITY_TYPE_ENUM.BinaFile.value,
            'entityId': ''
        }
    },
    {
        "_id": uuid.uuid4(),
        "doc": {
            'actionType': ACTION_TYPE_ENUM.UserLogin.value,
            'actionTimeStamp': int(time.time() * 1000),
            'actionMetaData': '',
            'userId': 'wstu15',
            'userArena': 'זירה א',
            'userDepartment': 'מדור ג',
            'userEnv': 'EnvX',
            'entityType': '',
            'entityId': ''
        }
    },
    {
        "_id": uuid.uuid4(),
        "doc": {
            'actionType': ACTION_TYPE_ENUM.UserLogin.value,
            'actionTimeStamp': int(time.time() * 1000),
            'actionMetaData': '',
            'userId': 'ssouser3',
            'userArena': 'זירה ד',
            'userDepartment': 'מדור א',
            'userEnv': 'EnvX',
            'entityType': '',
            'entityId': ''
        }
    },
    {
        "_id": uuid.uuid4(),
        "doc": {
            'actionType': ACTION_TYPE_ENUM.UserLogin.value,
            'actionTimeStamp': int(time.time() * 1000 - (1000 * 60 * 60)),
            'actionMetaData': '',
            'userId': 'ssouser5',
            'userArena': 'זירה ד',
            'userDepartment': 'מדור א',
            'userEnv': 'EnvX',
            'entityType': '',
            'entityId': ''
        }
    }

]
