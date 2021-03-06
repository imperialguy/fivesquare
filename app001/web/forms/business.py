from app001.web.models.business import BusinessModel
from wtforms import (
    Form,
    validators,
    TextField,
    IntegerField,
    ValidationError
)


class NewBusinessForm(Form):
    name = TextField(u'name', [validators.required()])
    location = TextField(u'coordinates', [validators.required()])

    def validate_name(form, field):
        if BusinessModel(name=field.data).exists():
            raise ValidationError("This business already exists in our system")

    def validate_location(form, field):
        num_coordinates = len(field.data.split(','))
        if num_coordinates not in range(1, 3):
            raise ValidationError("invalid co-ordinates")


class NewReviewForm(Form):
    name = TextField(u'name', [validators.required()])
    review = TextField(u'review', [validators.required()])
    rating = IntegerField(u'rating', [validators.required()])
    tags = TextField(u'tags', [validators.required()])

    def validate_name(form, field):
        if not BusinessModel(name=field.data).exists():
            raise ValidationError("This business does not exist in our system")


class SearchBusinessesForm(Form):
    location = TextField(u'coordinates', [validators.required()])
    radius = IntegerField(u'radius', [validators.required()])

    def validate_location(form, field):
        num_coordinates = len(field.data.split(','))
        if num_coordinates not in range(1, 3):
            raise ValidationError("invalid co-ordinates")


class GetBusinessInfoForm(Form):
    name = TextField(u'name', [validators.required()])

    def validate_name(form, field):
        if not BusinessModel(name=field.data).exists():
            raise ValidationError("This business does not exist in our system")
