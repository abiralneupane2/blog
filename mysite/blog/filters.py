from django.db.models import Q
from django_filters import rest_framework as filters


from blog.models import Blog


class BlogFilter(filters.FilterSet):
    author = filters.CharFilter(method="filter_author")

    class Meta:
        model = Blog
        fields = ("author",)
    
    def filter_author(self, queryset, field_name, value):
        if value:
            queryset = queryset.filter(Q(author__user__username__icontains=value)\
             |Q(author__user__first_name__icontains=value)\
              |Q(author__user__last_name__icontains=value))
        return queryset