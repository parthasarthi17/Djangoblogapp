from django.urls import path
from .views import index, authorview, add, remove, ArticleViews, commentsView, registerview, personview, checkview


app_name ='blog'


urlpatterns = [
    path('', index, name='index'),
    path('<int:id>', authorview, name ='authorview'),
    path('add', add, name='add'),
    path('del/<int:id>', remove, name="del"),
    path('posts/<int:id>', ArticleViews, name = 'articles'),
    path('posts/<int:id>/comment', commentsView, name='addcomment'),
    path('register/', registerview, name='registeruser'),
    path('<str:name>/', personview, name='peeps'),
    path('check/<str:name>/', checkview, name='checking'),


]
