from tastypie.authorization import Authorization

class KDRResourceMixin():

    @property
    def _django_model_field_list(self):
        return self._meta.queryset.model._meta.fields

    def build_schema(self):
        schema = super().build_schema()
        for field_name, field_object in self.fields.items():

            #Find any generic key fields and include the uri for each resource associated
            #in the related_schema field
            if isinstance(field_object, GenericForeignKeyField):
                uri_list = []
                for model, resource in field_object.to.items():
                    uri = self._build_reverse_url('api_get_schema', kwargs={
                        'api_name': self._meta.api_name,
                        'resource_name': resource._meta.resource_name
                    })
                    uri_list.append(uri)
                schema['fields'][field_name]['related_schema'] = uri_list

            # Find ManyToMany Keys and mark them as distinct from just a related field
            if isinstance(field_object, fields.ManyToManyField):
                schema['fields'][field_name]['type']  = 'm2m'

            # Include any choices defined for CharFields
            choices = self.field_choices(field_name)
            if choices:
                schema['fields'][field_name]['choices'] = choices
            else:
                schema['fields'][field_name]['choices'] = []

        # Remove this information, which is just taking up extra space in my db
        schema_keys_to_prune = ['allowed_detail_http_methods',
            'allowed_list_http_methods', 'default_format', 'default_limit',
            'filtering', 'ordering']
        for target_key in schema_keys_to_prune:
            schema.pop(target_key, None)

        # Add some other useful info
        schema['model_name'] = self._meta.resource_name        
        return schema

    def get_model_field(self, name):
        for f in self._django_model_field_list:
            if f.name == name:
                return f

    def field_choices(self, name):
        model_field_instance = self.get_model_field(name)
        if isinstance(model_field_instance, CharField):
            return model_field_instance.choices
        return None

    class Meta:
        limit = 0
        allowed_methods = ['get', 'post', 'put', 'patch', 'delete']
        always_return_data = True
        filtering = {
            'user': ALL_WITH_RELATIONS,
            'last_updated':ALL
        }
        authorization = Authorization()