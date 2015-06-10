from app001.web.forms.business import (
    NewBusinessForm,
    NewReviewForm,
    SearchBusinessesForm,
    GetBusinessInfoForm
)
from app001.web.models.business import BusinessModel
from app001.utils.core import get_logger
from flask import Blueprint, request, jsonify
from werkzeug.datastructures import MultiDict


businessbp = Blueprint('businessbp', __name__, url_prefix='/business')
logger = get_logger(__file__)


@businessbp.route('/add', methods=['POST'])
def add_business():
    """Add new business

    """
    form = NewBusinessForm(MultiDict(request.json))

    if not form.validate():
        logger.debug('Form validation errors:\n{0}'.format(form.errors))
        resp = jsonify()
        resp.status_code = 400
        logger.debug('i ama here')
        return resp

    success = BusinessModel(
        name=form.name.data,
        location=[float(i) for i in form.location.data.split(',')]).add()

    return jsonify(success=success)


@businessbp.route('/review', methods=['POST'])
def add_review():
    """Add new review

    """
    form = NewReviewForm(MultiDict(request.json))

    if not form.validate():
        logger.debug('Form validation errors:\n{0}'.format(form.errors))
        resp = jsonify()
        resp.status_code = 400
        return resp

    success = BusinessModel(name=form.name.data,
                            rating=form.rating.data,
                            review=form.review.data,
                            tags=[tag.strip() for tag in form.tags.data.split(',')]).add_review()
    return jsonify(success=success)


@businessbp.route('/search', methods=['POST'])
def search_businesses():
    """Returns a list of business

    """
    form = SearchBusinessesForm(MultiDict(request.json))

    if not form.validate():
        logger.debug('Form validation errors:\n{0}'.format(form.errors))
        resp = jsonify()
        resp.status_code = 400
        return resp

    location = [float(i) for i in form.location.data.split(',')]
    businesses = BusinessModel(location=location,
                                radius=form.radius.data).find()

    return jsonify(businesses=businesses)


@businessbp.route('/info/<business_name>', methods=['GET'])
def get_business_info(business_name):
    """Returns business info

    """
    form = GetBusinessInfoForm(MultiDict(dict(name=business_name)))

    if not form.validate():
        logger.debug('Form validation errors:\n{0}'.format(form.errors))
        resp = jsonify()
        resp.status_code = 400
        return resp

    business_info = BusinessModel(name=form.name.data).get()

    return jsonify(business_info=business_info)
