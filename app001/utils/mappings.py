from mongoengine import (
    Document,
    StringField,
    PointField,
    ReferenceField,
    IntField,
    ListField,
    DateTimeField
)


class Business(Document):
    name = StringField(required=True, unique=True)
    location = PointField()


class BusinessReview(Document):
    business = ReferenceField(Business)
    rating = IntField(required=True)
    review = StringField(required=True)
    tags = ListField(StringField(max_length=20))
    created_at = DateTimeField()
    meta = {
        'ordering': ['-created_at']
    }
