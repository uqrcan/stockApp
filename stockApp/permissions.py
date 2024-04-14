from rest_framework import permissions

class IsAuthenticatedAndWriteOnly(permissions.BasePermission):
    """
    Siteye giriş yapan (authenticated) kullanıcıların sadece yazma işlemlerine (POST, PUT, PATCH, DELETE) izin verir.
    GET isteklerine izin vermez.
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            # GET isteklerine izin verme
            return False
        # Diğer metodlara izin ver
        return request.user and request.user.is_authenticated
