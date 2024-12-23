from rest_framework.response import Response
from rest_framework import status


class StandardResponseMixin:
    def get_user_role(self, user):
        if not user or not user.is_authenticated:
            return '4'
        if user.is_superuser:
            return '1'
        elif user.is_staff:
            return '2'
        else:
            return '3'

    def success_response(self, data=None, user=None, status=status.HTTP_200_OK):
        return Response({
            'is_success': True,
            'data': data,
            'errors': None,
            'userPermission': self.get_user_role(user),
        }, status=status)

    def error_response(self, errors=None, status=status.HTTP_400_BAD_REQUEST):
        return Response({
            'is_success': False,
            'data': None,
            'errors': errors
        }, status=status)
