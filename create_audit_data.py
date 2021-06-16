from elasticsearch import Elasticsearch
from enum import Enum
from datetime import datetime
import time
import uuid

es = Elasticsearch(hosts=['localhost:9207'])


# {
#   "mappings": {
#     "dynamic": false,
#     "properties": {
#       "actionType": {
#         "type": "text"
#       },
#       "actionTimeStamp": {
#         "type": "date"
#       },
#       "actionMetaData": {
#         "type": "text"
#       },
#       "userId": {
#         "type": "text"
#       },
#       "userArena": {
#         "type": "text"
#       },
#       "userDepartment": {
#         "type": "text"
#       },
#       "userEnv": {
#         "type": "text"
#       },
#       "entityType": {
#         "type": "text"
#       },
#       "entityId": {
#         "type": "text"
#       }
#     }
#   }
# }
# make an API call to the Elasticsearch cluster
# and have it return a response:
# response = elastic_client.indices.create(
#     index="some_new_index",
#     body=mapping,
#     ignore=400 # ignore 400 already exists code
# )
# # print out the response:
# print ('response:', response)

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


new_event = {
    'actionType': ACTION_TYPE_ENUM.EntityCreated.value,
    'actionTimeStamp': str(time.time()*1000),
    'actionMetaData': '',
    'userId': 'wstu15',
    'userArena': 'זירה א',
    'userDepartment': 'מדור ג',
    'userEnv': 'EnvA',
    'entityType': ENTITY_TYPE_ENUM.BinaInsight.value,
    'entityId': 'BI12345'
}
# res = es.index(index="audit", id=111, body=doc)

doc_id = uuid.uuid4()

# doc_type='event',
res = es.index(
    index='audit',
    id=doc_id,
    body=new_event
)
print(res['result'])

res = es.get(index="audit", id=doc_id)
print(res['_source'])

es.indices.refresh(index="audit")

res = es.search(index="audit", body={"query": {"match_all": {}}})

print("Got %d Hits:" % res['hits']['total']['value'])
for hit in res['hits']['hits']:
    print(hit['_source'])
