from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [

    path('login/',
         auth_views.LoginView.as_view(template_name="login_page.html", redirect_authenticated_user=True),
         name='login'),
    path('signup/', views.signup_form, name='signup'),

    # django refresh token
    path('gettoken/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refreshtoken/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verifytoken/', TokenVerifyView.as_view(), name='token_verify'),

]
