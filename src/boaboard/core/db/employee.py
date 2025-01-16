from mongoengine import Document, StringField, BooleanField, EmbeddedDocumentField, ImageField, ReferenceField
from wiederverwendbar.mongoengine.security.hashed_password import HashedPasswordDocument

from boaboard.core.db.location import LocationDocument


class EmployeeDocument(Document):
    meta = {"collection": "employee"}

    username: str = StringField(required=True, unique=True)
    email: str = StringField(required=True, unique=True)
    first_name: str = StringField(required=True, max_length=50)
    surname: str = StringField(required=True, max_length=50)
    avatar: ImageField = ImageField()
    department: str = StringField(required=True, max_length=50)
    default_location: LocationDocument = ReferenceField(LocationDocument, required=True)
    hashed_password: HashedPasswordDocument = EmbeddedDocumentField(HashedPasswordDocument)
    status: bool = BooleanField(default=True)
