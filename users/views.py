from django.contrib import redirects
from django.shortcuts import render


# Create your views here.
from users.forms import UserForm


def index(request):
    return render(request, 'users/homepage.html')


def register(request):
    if request.method != 'POST':     # If it is a get request, do what is below
        form = UserForm()     # Fill the empty form(providing username, email, etc)
    else:
        # form has been filled, ready for processing
        form = UserForm(request.POST, request.FILES)    # Else, it is a POST request

        if form.is_valid():  # If form is filled properly, save it
            form.save()
            # return redirects('')    # To be able to save the file
            return render(request, 'users/success.html')

    context = {     # Sending the saves file to the html
        'form': form
    }

    return render(request, 'users/register.html', context)

