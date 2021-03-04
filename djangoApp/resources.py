
from import_export import resources
from djangoApp.models import Manufacturer

class ManufacturerResources(resources.ModelResource):
    class Meta:
        model = Manufacturer