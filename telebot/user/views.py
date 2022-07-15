from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import RegisterForm, LoginForm

# Create your views here.
def index(request):
    return render(request, 'index.html', {'email':request.session.get('user')})


class RegisterFormView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = '/'


class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = '/'

    def form_valid(self, form):
        request = self.request
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        request.session['user'] = email
        return super().form_valid(form)


class ProductList(FormView):
    template_name = 'product.html'
    form_class = LoginForm
    success_url = '/'
