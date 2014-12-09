from tastypie.api import Api
from eponym.v1.resources import CarModelResource, \
    BrandResource
from django.conf.urls import patterns, include

v1_api = Api(api_name = 'v1')
v1_api.register(BrandResource())
v1_api.register(CarModelResource())

urlpatterns = patterns('',
    (r'^api/', include(v1_api.urls)),
)
