import uuid
from enum import Enum
import time
import random

all_actions = []


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


class USER_ARENA_ENUM(Enum):
    ZiraA = 'זירה א'
    ZiraB = 'זירה ב'
    ZiraC = 'זירה ג'
    ZiraD = 'זירה ד'


class USER_DEPT_ENUM(Enum):
    MadorA = 'מדור א'
    MadorB = 'מדור ב'
    MadorC = 'מדור ג'
    MadorD = 'מדור ד'


# Also Possible to make one actions-list with ALL random ACTION_TYPE_ENUM,
# this time i wanted to separate for different reasons

# ################### -------------------- START ENTITY CREATED ACTIONS -------------------- ################### #

data_entity_created_actions = [
    [
        {
            "_id": str(uuid.uuid4()),
            "doc": {
                'actionType': ACTION_TYPE_ENUM.EntityCreated.value,
                'actionTimeStamp': int((time.time() * 1000) - (1000 * 60 * 60 * 24 * days)),
                'actionMetaData': '',
                'userId': 'wstu15',
                'userArena': random.choice(list(USER_ARENA_ENUM)).value,
                'userDepartment': random.choice(list(USER_DEPT_ENUM)).value,
                'userEnv': 'EnvA',
                'entityType': random.choice(list(ENTITY_TYPE_ENUM)).value,
                'entityId': str(uuid.uuid4())
            }
        } for x in range(8)
    ]
    for days in range(31)
]

actions_entity_created = [item for sublist in data_entity_created_actions for item in sublist]
all_actions.append(actions_entity_created)

# ################### -------------------- END ENTITY CREATED ACTIONS -------------------- ################### #

# --------------------------------------------------------------------------------------------------------- #

# ################### -------------------- START USER SEARCH ACTIONS -------------------- ################### #

data_user_search_actions = [
    [
        {
            "_id": str(uuid.uuid4()),
            "doc": {
                'actionType': ACTION_TYPE_ENUM.UserSearch.value,
                'actionTimeStamp': int((time.time() * 1000) - (1000 * 60 * 60 * 24 * days)),
                'actionMetaData': 'Al Kayda',
                'userId': 'ssouser3',
                'userArena': random.choice(list(USER_ARENA_ENUM)).value,
                'userDepartment': random.choice(list(USER_DEPT_ENUM)).value,
                'userEnv': 'EnvB',
                'entityType': random.choice(list(ENTITY_TYPE_ENUM)).value,
                'entityId': ''
            }
        } for x in range(4)
    ]
    for days in range(31)
]

actions_user_search = [item for sublist in data_user_search_actions for item in sublist]
all_actions.append(actions_user_search)

# ################### -------------------- END USER SEARCH ACTIONS -------------------- ################### #

# --------------------------------------------------------------------------------------------------------- #

# ################### -------------------- START USER SEARCH ALL ENTITIES -------------------- ################### #
data_user_search_all_entities = [
    [
        {
            "_id": str(uuid.uuid4()),
            "doc": {
                'actionType': ACTION_TYPE_ENUM.UserSearch.value,
                'actionTimeStamp': int((time.time() * 1000) - (1000 * 60 * 60 * 24 * days)),
                'actionMetaData': 'Al Mabhuh',
                'userId': 'wstu12',
                'userArena': random.choice(list(USER_ARENA_ENUM)).value,
                'userDepartment': random.choice(list(USER_DEPT_ENUM)).value,
                'userEnv': 'EnvB',
                'entityType': '',
                'entityId': ''
            }
        } for x in range(1)
    ]
    for days in range(31)
]

actions_user_search_all_entities = [item for sublist in data_user_search_all_entities for item in sublist]
all_actions.append(actions_user_search_all_entities)

# ################### -------------------- END USER SEARCH ALL ENTITIES -------------------- ################### #

# --------------------------------------------------------------------------------------------------------- #

# ################### -------------------- START USER LOGIN ACTIONS -------------------- ################### #

data_user_login_actions = [
    [
        {
            "_id": str(uuid.uuid4()),
            "doc": {
                'actionType': ACTION_TYPE_ENUM.UserLogin.value,
                'actionTimeStamp': int((time.time() * 1000) - (1000 * 60 * 60 * 24 * days)),
                'actionMetaData': '',
                'userId': 'ssouser5',
                'userArena': random.choice(list(USER_ARENA_ENUM)).value,
                'userDepartment': random.choice(list(USER_DEPT_ENUM)).value,
                'userEnv': 'EnvX',
                'entityType': '',
                'entityId': ''
            }
        } for x in range(6)
    ]
    for days in range(31)
]

actions_user_login = [item for sublist in data_user_login_actions for item in sublist]
all_actions.append(actions_user_login)

# ################### -------------------- END USER LOGIN ACTIONS -------------------- ################### #

# --------------------------------------------------------------------------------------------------------- #
