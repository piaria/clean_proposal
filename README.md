app
    api
        serializers
        viewsets
    views
        admins
    business_logic
        validators
        unit_of_work (caso de uso)
        dto (schemas de pydantic o dataclases)
        exceptions
    domain_model
    tests

mkdir -p api/serializers api/viewsets
mkdir -p views/admins
mkdir -p business_logic/validators
mkdir -p business_logic/unit_of_work
mkdir -p business_logic/dto
mkdir -p business_logic/exceptions
mkdir -p domain_model
mkdir -p tests


## Extras
Puede simplificar las views https://github.com/oxan/djangorestframework-dataclasses

Para usar Pydantic con DRF 
https://github.com/yezz123/pyngo
https://www.obytes.com/blog/integrate-pydantic-with-django-and-django-rest-framework


Typed Views
https://rsinger86.github.io/drf-typed/views/request_elements/
```python
from rest_framework import serializers
from rest_typed import typed_api_view

class CommentSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField(read_only=True)

"""
    POST
    {
        "email": "mscott@paperco.com",
        "content": "great job team!",
    }
"""
@typed_api_view(["POST"])
def create_comment(comment: CommentSerializer):
    # is_valid() automatically called.
    # ready to access comment.validated_data
```

https://github.com/django-polymorphic/django-polymorphic