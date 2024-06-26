from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('product/<int:pk>', views.product, name='product'),
    # path('category/<str:foo>', views.category, name='category'),
    path('category/<int:cat_id>', views.searchCategory, name='searchCategory'),
    path('writer/<str:writer>', views.searchWriter, name='searchWriter'),
    path('searchAddress', views.searchAddress, name='searchAddress'),
    
    path('add_review/<int:product_id>/', views.add_review, name='add_review'),
    
]