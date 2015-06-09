from app001.utils.mappings import Business, BusinessReview
from app001.utils.core import Connection


def refresh():
    with Connection() as c:
        Business.objects().delete()
        BusinessReview.objects().delete()
