from django.urls import path
from tourism  import views
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,  
    TokenRefreshView,     
)





urlpatterns = [
      
    # path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  
    
    
    # path('users/me/',views.curent_user , name='current_user'),  

    path('destinations/', views.manage_destination),
    path('destination/<int:pk>/', views.manage_destination),

    path('attractions/', views.manage_attraction),
    path('attraction/<int:pk>/', views.manage_attraction),
    
    path('reviews/', views.manage_review),
    path('review/<int:pk>/', views.manage_review),

    path('booking/', views.manage_booking),
    path('booking/<int:pk>/', views.manage_booking),
]