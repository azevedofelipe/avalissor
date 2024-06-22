from rest_framework import permissions

# Verifica se usuario fazendo o request e o mesmo que criou
class isOwner(permissions.BasePermission):

  def has_object_permission(self, request, view, obj):
    if request.user:
        if request.user.is_superuser:
            return True
        else:
            return obj.autor == request.user
    else:
        return False