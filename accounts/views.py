from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from accounts.forms import FormUser

def login_view(request):
    form = FormUser()
    erros = ''
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dish_list_view')
        else:
            erros = 'Crendicial inválidas'

    return render(request, 'login.html', {'form': form, 'error': erros})


def logout_view(request):
    logout(request)
    return redirect('dish_list_view')