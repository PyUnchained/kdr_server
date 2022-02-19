import inspect
import logging
import functools

from django.urls import path
from django.conf.urls import include

from tastypie.api import Api
from tastypie.resources import ModelResource

REGISTERED_APIS = {}

def get_api_urls(api_name, url_root=''):
    """ Returns a path that includes all URLs for the named API. """

    if api_name in REGISTERED_APIS:
        return path(url_root, include(REGISTERED_APIS[api_name][0].urls))

def is_valid_resource(test_item, api_name = None):
    """ Filter function used to determine whether the given objects within a module represent
    valid ModelResources for this API version"""

    if inspect.isclass(test_item):
        if test_item.api_name == api_name and "DefaultResource" not in test_item.__name__:
            return True
    return False

def create_api(api_name, resource_module):
    # Find all the Resources that are part of this version

    if api_name not in REGISTERED_APIS:
        filter_fn = functools.partial(is_valid_resource, api_name = api_name)
        resource_list = filter(filter_fn,
            [x[1] for x in inspect.getmembers(resource_module)])
        api_instance = Api(api_name=api_name)
        for ResourceClass in resource_list:
            api_instance.register(ResourceClass())
        REGISTERED_APIS[api_name] = (api_instance, resource_list)
    return True