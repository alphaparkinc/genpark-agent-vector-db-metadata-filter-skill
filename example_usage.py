from client import AgentVectorDBMetadataFilterClient
client = AgentVectorDBMetadataFilterClient()
print(client.build_filter("shoes", {"category": "sports", "active": 1}))