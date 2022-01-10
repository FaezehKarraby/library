from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView

from account.forms import SignupForm
from account.models import Profile


class SignupView(CreateView):
    form_class = SignupForm
    success_url = reverse_lazy('login')
    template_name = 'account/signup.html'


@login_required
def profile(request, id):
    # no real code
    context = {
        'profiles': get_object_or_404(Profile, id=id)
    }
    return render(request, 'account/profile.html', context)


def my_books(request, id):
    user = get_object_or_404(Profile, id=id)
    register_books = [rb.book for rb in request.user.registeredbookmodel_set.all()]
    context = {
        'user': user,
        'register_books': register_books,
    }
    return render(request, 'account/my_books.html', context)
