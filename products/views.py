from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.urls import reverse
from django.views.generic import ListView
from .models import Product

# Create your views here.
# def home(request):
#     return render(request, 'display/test.html')

# def signin(request):

#     if request.user.is_authenticated:
#         return redirect(reverse('home'))

#     username = request.POST.get('username', '')
#     password = request.POST.get('password', '')

#     user = auth.authenticate(username=username, password=password)

#     if user is not None and user.is_active:
#         auth.login(request, user)
#         return redirect(reverse('home'))
#     else:
#         return render(request, 'registration/signin.html')

# def logout(request):
#     auth.logout(request)
#     return redirect(reverse('home'))

# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             auth.login(request, user)
#             return redirect(reverse('home'))
#     else:
#         form = UserCreationForm()
#     return render(request, 'registration/signup.html', {'form': form})


# def api_product(request):
class Home(ListView):
    model = Product
    template_name = 'display/index.html'
