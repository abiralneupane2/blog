from django.shortcuts import render, get_object_or_404

from django.views import View

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, BasePermission

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie, vary_on_headers



from blog.models import Blog, Comment, Author, User

from blog.serializers import BlogSerializer, CommentSerializer, AuthorSerializer, MeSerializer

from blog.filters import BlogFilter

# Create your views here.

class IsAuthorOrSuperUser(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        if obj.author.user == request.user:
            return True
        return False

class BlogListCreateApi(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Blog.objects.all().prefetch_related("comment_set")
    serializer_class = BlogSerializer
    filterset_class = BlogFilter

    @method_decorator(cache_page(60*60*2))
    @method_decorator(vary_on_cookie)
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)


class BlogUpdateApi(generics.RetrieveAPIView, generics.DestroyAPIView, generics.UpdateAPIView):
    permission_classes = [IsAuthenticated, IsAuthorOrSuperUser]
    serializer_class = BlogSerializer
    lookup_field = 'pk'
    queryset = Blog.objects.all()


class CommentCreateApi(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

class CommentDeleteApi(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()
    def get_object(self):
        obj = get_object_or_404(self.queryset, pk=self.kwargs.get("pk"))
        if obj.blog.author.user != self.request.user and not self.request.user.is_superuser:
            raise PermissionDenied("You cannot delete the comment.", code=403)
        return obj

class RegisterApi(generics.CreateAPIView):
    serializer_class = AuthorSerializer
    queryset = User.objects.filter(author__isnull=False)

class Me(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = MeSerializer

    def get_object(self):
        return get_object_or_404(self.queryset, username=self.request.user.username)
