from elasticsearch import Elasticsearch, helpers
from audit_data_dict import actions

elastic = Elasticsearch(hosts=['localhost:9200'])

try:
    # make the bulk call, and get a response
    # response = helpers.bulk(elastic, bulk_json_data("people.json", "employees", "people"))
    response = helpers.bulk(elastic, actions, index='audit')
    print("\nRESPONSE:", response)
except Exception as e:
    print("\nERROR:", e)

new_event = {

}

# doc_id = uuid.uuid4()
#
# res = elastic.index(
#     index='audit',
#     id=doc_id,
#     body=new_event
# )
# print(res['result'])
#
# res = elastic.get(index="audit", id=doc_id)
# print(res['_source'])

elastic.indices.refresh(index="audit")
res = elastic.search(index="audit", body={"query": {"match_all": {}}})
print("Got %d Hits:" % res['hits']['total']['value'])
for hit in res['hits']['hits']:
    print(hit['_source'])
