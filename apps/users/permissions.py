from rest_framework.permissions import BasePermission
from .models import User

class IsAdminRole(BasePermission):


    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and
            request.user.role_type == User.Role.ADMIN
        )


class IsOwnerRole(BasePermission):

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and
            request.user.role_type == User.Role.OWNER
        )


class IsCustomerRole(BasePermission):

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and 
            request.user.role_type == request.user.Role.CUSTOMER
        )


class IsDeliveryBoyRole(BasePermission):

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and
            request.user.role_type == request.user.Role.DELIVERY_BOY
        )

