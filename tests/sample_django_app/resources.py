from tastypie.resources import ModelResource
from kivy_django_restful.resources import KDRResourceMixin

from .models import TestModel

class TestModelResource(KDRResourceMixin, ModelResource):
    api_name = "test_api"

    class Meta():
        queryset = TestModel.objects.all()
        resource_name = 'test_model'
        authorization = SecureAuthorization()
        authentication = ApiKeyAuthentication()
        allowed_methods = ['get', 'post', 'put', 'delete']
        filtering = {
            'user': ALL_WITH_RELATIONS,
            'last_updated':ALL
        }   