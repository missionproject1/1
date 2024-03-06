# search_indexes.py
from .models import YourModel # Adjust the import based on your actual model name
from elasticsearch_dsl import Document, Text, Date
from elasticsearch_dsl.connections import connections

connections.create_connection()

class YourModelIndex(Document):
    title = Text()
    description = Text()
    created_at = Date()

    class Index:
        name = 'yourmodel_index'

YourModelIndex.init()
