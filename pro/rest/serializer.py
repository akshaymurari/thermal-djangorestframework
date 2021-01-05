from rest_framework import serializers
from .models import User
from datetime import datetime
from rest_framework import serializers    
from django.utils import timezone as tz

class Base64ImageField(serializers.ImageField):

    def to_internal_value(self, data):
        from django.core.files.base import ContentFile
        import base64
        import six
        import uuid

        if isinstance(data, six.string_types):
            if 'data:' in data and ';base64,' in data:
                header, data = data.split(';base64,')

            try:
                decoded_file = base64.b64decode(data)
            except TypeError:
                self.fail('invalid_image')

            file_name = str(uuid.uuid4())[:12] # 12 characters are more than enough.
            file_extension = self.get_file_extension(file_name, decoded_file)
            complete_file_name = "%s.%s" % (file_name, file_extension, )
            data = ContentFile(decoded_file, name=complete_file_name)

        return super(Base64ImageField, self).to_internal_value(data)

    def get_file_extension(self, file_name, decoded_file):
        import imghdr

        extension = imghdr.what(file_name, decoded_file)
        extension = "jpg" if extension == "jpeg" else extension

        return extension
class UserSerializer(serializers.ModelSerializer):
    # temp = serializers.DecimalField(max_digits=5,decimal_places=2)
    img=Base64ImageField( max_length=None, use_url=True,)
    # datetime = serializers.DateTimeField(default=tz.now)

    class Meta:
        model = User
        fields = ['temp','datetime','img']
        # extra_kwargs = {'datetime': {'required': False}}
