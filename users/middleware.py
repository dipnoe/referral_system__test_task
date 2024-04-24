from http import HTTPStatus
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError

from django.http import JsonResponse

from config.settings import DEBUG


class ExceptionHandlerMiddleware:
    """
    Middleware that handles exceptions during request processing by returning
    appropriate JSON responses and HTTP status codes based on the exception type.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    @staticmethod
    def process_exception(request, exception):
        message = ''
        status_code = HTTPStatus.BAD_REQUEST

        if isinstance(exception, ObjectDoesNotExist):
            message = 'Object does not exist.'
            status_code = HTTPStatus.NOT_FOUND
        elif isinstance(exception, IntegrityError):
            message = 'Duplicate key value violates unique constraint.'
            status_code = HTTPStatus.BAD_REQUEST
        else:
            if DEBUG:
                return None

            message = 'Unknown error.'
            status_code = HTTPStatus.INTERNAL_SERVER_ERROR

        return JsonResponse(
            {'error': message},
            status=status_code
        )
