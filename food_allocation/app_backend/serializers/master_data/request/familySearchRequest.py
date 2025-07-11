from rest_framework import serializers
from app_backend.enums import HalalStatus
from app_backend.serializers.base.request.paginationRequest import PaginationRequest


class FamilySearchRequest(PaginationRequest, serializers.Serializer):
    family_no = serializers.CharField(
        max_length=100, allow_blank=True, required=False, default=""
    )
    family_or_person_name = serializers.CharField(
        max_length=100, allow_blank=True, required=False, default=""
    )
    halal_status = serializers.ChoiceField(
        choices=HalalStatus.choices, default=HalalStatus.ALL
    )
    allocation_creatable_only = serializers.BooleanField(default=False)
