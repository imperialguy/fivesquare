from app001.utils.mappings import Business, BusinessReview
from app001.utils.core import Connection
from datetime import datetime


class BusinessModel(object):

    """ This class provides methods to manage businesses

    """

    def __init__(self,
                 name=None,
                 location=None,
                 rating=None,
                 review=None,
                 tags=None,
                 radius=None):
        """Constructor

        :param name: Business Name
        :param location: Business Location
        :param rating: Business Rating
        :param review: Business Review
        :param tags: tags associated with the Business
        :param radius: search radius
        :type name: str
        :type location: list
        :type rating: int
        :type review: str
        :type tags: list
        :type radius: int

        """
        self.name = name
        self.location = location
        self.rating = rating
        self.review = review
        self.tags = tags
        self.radius = radius

    def add(self):
        """Add a new Business

        Required Constructor params:
        1. name
        2. location

        """
        if not self.name:
            raise ValueError(
                'A valid business name is required')
        if not self.location or not isinstance(self.location, list):
            raise ValueError(
                'A valid business location is required')

        with Connection() as c:
            obj = Business(
                name=self.name, location=self.location)
            obj.save()
        return True

    def exists(self):
        """This method checks if the business already exists in the db

        Required Constructor params:
        1. name

        """
        if not self.name:
            raise ValueError(
                'A valid business name is required')

        with Connection() as c:
            exists = bool(Business.objects(name=self.name).count())
        return exists

    def find(self):
        """Find all businesses within a search radius of a specific location

        Required Constructor params:
        1. location
        2. radius

        """
        if not self.radius:
            raise ValueError('A valid search radius is required')
        if not self.location or not isinstance(self.location, list):
            raise ValueError(
                'A valid business location is required')

        with Connection() as c:
            business_objects = Business.objects(
                location__geo_within_center=[self.location,
                                             self.radius])

        return list(map(self.format_business, business_objects))

    def add_review(self):
        """Adds a review for a business

        Required Constructor params:
        1. name
        2. rating
        3. review
        4. tags

        """
        if not self.name:
            raise ValueError(
                'A valid business name is required')
        if not self.rating:
            raise ValueError(
                'A valid business rating is required')
        if not self.review:
            raise ValueError(
                'A valid business review is required')
        if not self.tags or not isinstance(self.tags, list):
            raise ValueError(
                'valid tags are required')

        with Connection() as c:
            business = Business.objects(name=self.name)[0]
            business_review = BusinessReview(business=business,
                                             rating=self.rating,
                                             review=self.review,
                                             tags=self.tags,
                                             created_at=datetime.now())
            business_review.save()
        return True

    def get(self):
        """Gets the business info

        Required Constructor params:
        1. name

        """
        if not self.name:
            raise ValueError(
                'A valid business name is required')

        with Connection() as c:
            business_review_objects = BusinessReview.objects.filter(
                business__in=Business.objects.filter(name__exact=self.name))
            avg_rating = round(business_review_objects.average('rating'), 1)
            tag_summary = list(set([
                tag for obj in business_review_objects for tag in obj.tags]))
            reviews = [obj.review for obj in business_review_objects]

        return {'name': self.name,
                'avg_rating': avg_rating,
                'reviews': reviews,
                'tags': tag_summary}

    @classmethod
    def format_business(cls, business_object):
        """returns formatted `Business` object

        """
        return {'name': business_object.name,
                'location': business_object.location
                }
