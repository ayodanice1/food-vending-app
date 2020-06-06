from rest_framework import permissions


class IsVendor(permissions.BasePermission):
    
    def has_permission(self, request, view):
        if request.user.is_vendor or request.user.is_superuser:
            return True
        return False
    
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser or request.user.is_vendor:
            return True
        return False
    
class IsCustomer(permissions.BasePermission):
    
    def has_permission(self, request, view):
        if not request.user.is_vendor or request.user.is_superuser:
            return True
        return False
    
    def check_permissions(self, ):
        pass
    
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser or not request.user.is_vendor:
            return True
        return False
    
class IsMenuOwner(permissions.BasePermission):
    
    def has_permission(self, request, view):
        if request.user.is_vendor or request.user.is_superuser:
            return True
        return False
    
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser or obj.vendor.id == request.user.id:
            return True
        return False
    
class IsOrderOwner(permissions.BasePermission):
    
    def has_permission(self, request, view):
        if not request.user.is_vendor or request.user.is_superuser:
            return True
        return False
    
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        elif obj.customer.id == request.user.id:
            return True
        return False
    
class IsConcerned(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        elif obj.customer.id == request.user.id or obj.vendor.id == request.user.id:
            return True
        return False
    
