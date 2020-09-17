import graphene
from backend import schema

# Create a query schema based off of the backend schema
class Query(schema.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)

