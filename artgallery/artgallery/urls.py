from django.urls import path, include
from django.contrib import admin
from django.urls import path
from core.views import frontpage
from core.views import base, cart, artworks,auction
from core.views import login_view,register_view
from core.views import artist_dashboard, add_artwork, edit_profile
from django.contrib.auth import views as auth_views
from core.views import logout_view

from core.views import artist_dashboard_development

urlpatterns = [
    path('register/', register_view, name='register'),
    path('artist_dashboard/', artist_dashboard_development, name='artist_dashboard_development'),
    path('login/', login_view, name='login'),
    path('register/core/frontpage/', base, name='frontpage'),
    path('login/core/frontpage/', base, name='frontpage'),
    path('',frontpage,name='frontpage'),
    path('cart/',cart,name='cart'),
    path('auction/',auction,name='auction'),
    # path('upload_auction/', views.upload_auction_view, name='upload_auction'),
    path('artworks/',artworks,name='artworks'),
    path('admin/', admin.site.urls),
    path('artist_dashboard/', artist_dashboard, name='artist_dashboard'),
    path('artist_dashboard/<str:username>/', artist_dashboard, name='artist_dashboard'),
    path('add_artwork/', add_artwork, name='add_artwork'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # path('logout/', logout_view, name='logout'),
]
