from rest_framework.pagination import PageNumberPagination

class CustomPagination(PageNumberPagination):
    """
    Custom pagination class to handle page size and maximum page size.
    """
    page_size = 10  # Default page size
    page_size_query_param = 'page_size'  # Allow clients to set the page size
    max_page_size = 100  # Maximum allowed page size
    page_query_param = 'page'  # Query parameter for the page number