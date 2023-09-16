from django.urls import path


from blog import views


app_name = 'blog'

urlpatterns = [
    path('blog', views.BlogListCreateApi.as_view()), 
    path('blog/<int:pk>', views.BlogUpdateApi.as_view()),

    path('comment', views.CommentCreateApi.as_view()),

    path('author/', views.RegisterApi.as_view()),

    path('me', views.Me.as_view())

]