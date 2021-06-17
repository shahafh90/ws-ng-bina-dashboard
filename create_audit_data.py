from elasticsearch import Elasticsearch, helpers
from audit_data_dict import all_actions

elastic = Elasticsearch(hosts=['localhost:9200'])

try:
    # make the bulk call, and get a response
    for actions in all_actions:
        response = helpers.bulk(elastic, actions, index='audit')
        print("\nRESPONSE:", response)

except Exception as e:
    print("\nERROR:", e)

elastic.indices.refresh(index="audit")
res = elastic.search(index="audit", body={"query": {"match_all": {}}}, size=100)

print("Got %d Hits:" % res['hits']['total']['value'])
for hit in res['hits']['hits']:
    print(hit['_source']['doc'])

elastic.close()

