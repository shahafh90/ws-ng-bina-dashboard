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


# res = es.index(index="audit", id=111, body=doc)