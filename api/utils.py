from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Model
from django.db.models.fields.files import ImageFieldFile,FieldFile
from django.forms import model_to_dict
from random import choice


class ExtendedEncoder(DjangoJSONEncoder):

    def default(self, o):
        if isinstance(o, FieldFile):
            try:
                mypath = o.path
            except:
                return ''
            else:
                return mypath
        if isinstance(o, ImageFieldFile):
            try:
                mypath = o.path
            except:
                return ''
            else:
                return mypath
        # this will either recusively return all atrributes of the object or return just the id
        elif isinstance(o, Model):
            # return model_to_dict(o)
            return o.id

        return super().default(o)


class ExtendedEncoderAllFields(DjangoJSONEncoder):

    def default(self, o):
        if isinstance(o, FieldFile):
            try:
                mypath = o.url
            except:
                return ''
            else:
                return mypath
        if isinstance(o, ImageFieldFile):
            try:
                mypath = o.url
            except:
                return ''
            else:
                return mypath
        # this will either recusively return all atrributes of the object or return just the id
        elif isinstance(o, Model):
            return model_to_dict(o)
            # return o.id


        return super().default(o)
