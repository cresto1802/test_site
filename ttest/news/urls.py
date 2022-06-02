from django.urls import path
from .views import *
from django.views.decorators.cache import cache_page

urlpatterns = [
    #path('', cache_page(60) (HomeNews.as_view()), name='home'),
    path('', HomeNews.as_view(), name='home'),
    path('category/<int:category_id>/', NewsByCategory.as_view(), name='category'),
    path('news/<int:news_id>/', ViewNews.as_view(), name='view_news'),
    path('news/add_news/', CreateNews.as_view(), name='add_news'),
    path('register/', register, name='register'),
    path('login/', login_in, name='login'),
    path('logout/', log_out, name='logout'),
    path('thanks/', thanks, name='thanks'),
]

