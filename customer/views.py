from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm, UserUpdateForm, ProfileUpdateForm, CustomerForm

from store.utils import cookieCart, cartData, guestOrder

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        customer_form = CustomerForm(request.POST)
        
        if form.is_valid() and customer_form.is_valid():
            user = form.save()
            
            customer = customer_form.save(commit=False) # This will save the data in the form but will not commit it to the database
            
            # Adding Addtional data in to a form before saving it to the database
            customer.user = user
            customer.save()
            
            # group = Group.objects.get(name='Customers')
            # user.groups.add(group)
            
            # Automatically logining in newly register user 
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
           
            return redirect('store')
    else:
        form = CreateUserForm()
        customer_form = CustomerForm()
    context = {
        'form': form,
        'customer_form': customer_form,
    }
    return render(request, 'customer/register.html', context)


def profile(request):
    user = User.objects.get(username=request.user)
    data = cartData(request)
    cartItems = data['cartItems']
    context = {
        'cartItems': cartItems,
    }
    return render(request, 'customer/profile.html', context)


def profile_update(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.customer)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('user-profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.customer)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'customer/profile_update.html', context)
