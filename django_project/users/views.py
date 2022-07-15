from django.shortcuts import render, redirect #to redirect user after creating account
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm

def register(request): # register form
    if request.method == 'POST':  #if post request, validate data, if get request, empthy request
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save() # hash password automatically
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!') # add messages to base template
            return redirect('blog-home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form}) # add context to template

# messages.debug
# messages.info
# messages.success
# messages.warning
# messages.error
