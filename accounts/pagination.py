from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class CustomPagination(PageNumberPagination):
    page_size = 20 # Nombre d’éléments par page par défaut
    page_size_query_param = 'page_size'  # Permet à l’utilisateur de spécifier la taille
    max_page_size = 100  # Taille maximale par page

    def get_paginated_response(self, data):
        return Response({
            'status': 'success',
            'total_items': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'current_page': self.page.number,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'results': data
        })
