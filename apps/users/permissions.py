from rest_framework.permissions import BasePermission
from .models import User

class IsAdminRole(BasePermission):


    def has_permission(self, request, view):
        print("user:",request.user)
        print('role from db :', repr(request.user.role_type) )
        print(" admin contain ", repr(User.Role.ADMIN))
        print("equal:", request.user.role_type == User.Role.ADMIN)
        return (
            request.user.is_authenticated and
            request.user.role_type == User.Role.ADMIN
        )


class IsOwnerRole(BasePermission):

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and
            request.user.role_type == request.User.Role.OWNER
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

