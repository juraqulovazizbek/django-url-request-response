from django.http import HttpRequest, HttpResponse


def get_product_by_uuid_view(request: HttpRequest, id: str) -> HttpResponse:
    return HttpResponse(f'salom, {id}')
