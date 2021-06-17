from elasticsearch import Elasticsearch

elastic = Elasticsearch(hosts=['localhost:9200'])

audit_mapping = {
    "mappings": {
        "dynamic": False,
        "properties": {
            "doc": {
                "properties": {
                    "actionMetaData": {
                        "type": "text",
                        "fields": {
                            "keyword": {
                                "type": "keyword",
                                "ignore_above": 256
                            }
                        }
                    },
                    "actionTimeStamp": {
                        "type": "date"
                    },
                    "actionType": {
                        "type": "text",
                        "fields": {
                            "keyword": {
                                "type": "keyword",
                                "ignore_above": 256
                            }
                        }
                    },
                    "entityId": {
                        "type": "text",
                        "fields": {
                            "keyword": {
                                "type": "keyword",
                                "ignore_above": 256
                            }
                        }
                    },
                    "entityType": {
                        "type": "text",
                        "fields": {
                            "keyword": {
                                "type": "keyword",
                                "ignore_above": 256
                            }
                        }
                    },
                    "userArena": {
                        "type": "text",
                        "fields": {
                            "keyword": {
                                "type": "keyword",
                                "ignore_above": 256
                            }
                        }
                    },
                    "userDepartment": {
                        "type": "text",
                        "fields": {
                            "keyword": {
                                "type": "keyword",
                                "ignore_above": 256
                            }
                        }
                    },
                    "userEnv": {
                        "type": "text",
                        "fields": {
                            "keyword": {
                                "type": "keyword",
                                "ignore_above": 256
                            }
                        }
                    },
                    "userId": {
                        "type": "text",
                        "fields": {
                            "keyword": {
                                "type": "keyword",
                                "ignore_above": 256
                            }
                        }
                    }
                }
            }
        }
    }
}

# make an API call to the Elasticsearch cluster
# and have it return a response

print()
response = elastic.indices.create(
    index="audit",
    body=audit_mapping,
    ignore=400  # ignore 400 already exists code
)
print('-- Response --')
print(response)

print()
audit_mapping = elastic.indices.get_mapping("audit")
print('-- GET /audit/_mapping --')
print(audit_mapping)

print()
all_indices = elastic.indices.get_alias('*')
print('-- All Indices --')
print('\n'.join([ind for ind in all_indices]))
print()

elastic.close()
