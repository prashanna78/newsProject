from django.urls import path
from Accounts.views import RegisterView,HomeView, LoginView, LogoutView, PasswordReset


app_name = "Accounts"

urlpatterns = [
	path('', RegisterView.as_view(), name='register'),
	path('login/', LoginView.as_view(), name='login'),
	path('logout/', LogoutView.as_view(), name='logout'),
	path('homePage/', HomeView.as_view(), name='home'),
	path('passwordReset/',PasswordReset.as_view(), name='reset')
]