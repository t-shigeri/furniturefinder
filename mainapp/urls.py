
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import IndexView, AboutView, GalleryView, ServicesView, ReferenceView, ContactView, SuccessView, SearchView, ResultView, ProfileView,RegisterView
from . import views
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('reference/', ReferenceView.as_view(), name='reference'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('search/', SearchView.as_view(), name='search'),
    path('success/', SuccessView.as_view(), name='success'),
    path('search_result/', ResultView.as_view(), name='result'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('register/', RegisterView.as_view(), name='register'), 
    path('furniture/<int:id>/', views.furniture_detail, name='furniture_detail'),
    # 他のURLパターン
]
