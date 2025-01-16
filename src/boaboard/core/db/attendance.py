from datetime import datetime

from mongoengine import Document, ReferenceField, DateTimeField

from boaboard.core.db.employee import EmployeeDocument
from boaboard.core.db.location import LocationDocument


class AttendanceDocument(Document):
    meta = {"collection": "attendance"}

    employee: EmployeeDocument = ReferenceField(EmployeeDocument, required=True)
    location: LocationDocument = ReferenceField(LocationDocument, required=True)
    check_in: datetime = DateTimeField(required=True)
    check_out: datetime = DateTimeField(required=False)
