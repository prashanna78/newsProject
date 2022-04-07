from django.views.generic import *
from django.views import View
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib import messages

from django.http import JsonResponse

# Create your views here.
class HomeView(TemplateView):
	template_name ='main/home.html'
	success_url =reverse_lazy("Accounts:home")

#register 
class RegisterView(SuccessMessageMixin,TemplateView):
    template_name = 'register/register.html'
    success_url = reverse_lazy("Accounts:register")
    success_message = 'User information is created'

    #using post to validate the form of the user
    def post(self,request, *args, **kwargs):
        if request.method == "POST":
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            username = request.POST['username']
            email = request.POST['email']
            password1 = request.POST['password1']
            password2 = request.POST['password2']

            if password1 == password2:
                if User.objects.filter(username=username).exists():
                    messages.info(request,'Username is taken. Choose Another')
                    return redirect('Accounts:register')
                elif User.objects.filter(email=email).exists():
                    messages.info(request,'Email already exits')
                    return redirect('Accounts:register')
                else:
                    user = User.objects.create_user(username = username, password = password1,first_name = first_name,
                    last_name = last_name, email = email)
                    user.save()
                    messages.success(request, self.success_message)
            else:
                messages.info(request, 'enter correct password')

        return redirect(self.success_url)

    
#for login
class LoginView(FormView):
	template_name='registration/login.html'
	success_url=reverse_lazy('News:dashboard')
	form_class=LoginForm

	def form_valid(self, form):
		uname = form.cleaned_data['username']
		print(uname,"--------------")
		pword = form.cleaned_data['password']
		print(pword,"-----------")

		#this check the user and return the user otherwise 
		#None authenticate means just to check user
		#if there is no user it return None

		user = authenticate(username = uname, password = pword)

		if user is not None:
			login(self.request, user)
		else:
			return render(self.request,"registration/login.html",
				{'Error':'Invalid username or password','form':form})

		#super is to return form to super class
		return super().form_valid(form)

class LogoutView(View):
	def get(self, request):
		logout(request)
		return redirect("Accounts:login")


class PasswordReset(TemplateView):
	template_name='registration/reset_password.html'