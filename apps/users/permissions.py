from rest_framework.permissions import BasePermission


class IsAdminRole(BasePermission):

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and
            request.user.role_type == request.user.Role.ADMIN
        )


class IsOwnerRole(BasePermission):

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and
            request.user.role_type == request.user.Role.OWNER
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

