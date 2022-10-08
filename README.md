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
