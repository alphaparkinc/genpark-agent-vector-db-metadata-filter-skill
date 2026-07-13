class AgentVectorDBMetadataFilterClient:
    def build_filter(self, query: str, filters: dict) -> dict:
        expr = " AND ".join([f"{k} == {v}" for k, v in filters.items()])
        return {"applied_filter_expression": expr}