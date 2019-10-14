from django.shortcuts import render, redirect
# from django.contrib import messages
from .forms import UserRegistrationForm


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
        # FLASH MESSAGES IN BASE.HTML TEMPLATE!!!!!
            # username = form.cleaned_data.get('username')
        # messages.success(request, f"Account Created For {username}!, You're Now Able To Log In")
        # return redirect('diary:index')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})
