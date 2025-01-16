from mongoengine import Document, StringField


class LocationDocument(Document):
    meta = {"collection": "location"}

    name: str = StringField(required=True, unique=True, max_length=50)
