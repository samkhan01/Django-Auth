from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

def index(request):
    # Check if the user is anonymous (not logged in)
    if request.user.is_anonymous:
        return redirect("/log")  # Redirect to the login page

    return render(request, 'index.html')

def log(request):
    if request.method == 'POST':
        uservalue = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(username=uservalue, password=password)

        if user is not None:
            # A backend authenticated the credentials
            login(request, user)  # Log in the user
            return redirect('/')
        else:
            # No backend authenticated the credentials
            return render(request, 'log.html', {'error_message': "Invalid username or password."})

    # If the request method is not POST (i.e., GET request), show the login page
    return render(request, 'log.html')

def logout_view(request):
    logout(request)  # Log out the user
    return redirect('/log')  # Redirect to the login page after logout
