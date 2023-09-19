from django.urls import path


from blog import views


app_name = 'blog'

urlpatterns = [
    path('blog', views.BlogListCreateApi.as_view(), name="list_create"), 
    path('blog/<int:pk>', views.BlogUpdateApi.as_view(), name="update"),

    path('comment', views.CommentCreateApi.as_view(), name="comment"),
    path('coment/<int:pk>', views.CommentDeleteApi.as_view(), name="comment_delete"),

    path('author/', views.RegisterApi.as_view()),

    path('me', views.Me.as_view())

]