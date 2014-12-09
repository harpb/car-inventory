from tastypie.resources import ModelResource
from eponym.models import Company, Brand, CarModel, CarModelOption
from tastypie import fields
from tastypie.constants import ALL, ALL_WITH_RELATIONS

class CompanyResource(ModelResource):
    class Meta:
        queryset = Company.objects.all()
        resource_name = 'company'

class BrandResource(ModelResource):
    company = fields.ForeignKey(CompanyResource, 'company', full = True)

    class Meta:
        queryset = Brand.objects.all()
        resource_name = 'brand'
        filtering = {
            'name': ALL
        }

class CarModelOptionResource(ModelResource):

    class Meta:
        queryset = CarModelOption.objects.all()
        resource_name = 'car_model_option'

class CarModelResource(ModelResource):
    brand = fields.ForeignKey(BrandResource, 'brand', full = True)
    options = fields.ManyToManyField(CarModelOptionResource, 'options', full = True)

    class Meta:
        queryset = CarModel.objects.all()
        resource_name = 'car_model'
        filtering = {
            'brand': ALL_WITH_RELATIONS
        }
