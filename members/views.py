from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from .forms import createProfileForm, editProfileForm
from django.urls import reverse_lazy
from blogapp.models import Profile
from django.contrib import messages
# Create your views here.


class editProfile(generic.UpdateView):
    model = Profile
    fiels = "__all__"
    form_class = editProfileForm
    template_name = 'registration/editProfile.html'

    def get_context_data(self, **kwargs):
        messages.success(self.request, 'profile updated successfully')
        context = {
            'messages': messages,
        }
        kwargs.update(context)
        return super().get_context_data(**kwargs)


class createProfile(generic.CreateView):
    model = Profile
    fiels = "__all__"
    form_class = createProfileForm
    template_name = 'registration/createProfile.html'

    def get_context_data(self, **kwargs):
        messages.success(self.request, 'profile created successfully')
        context = {
            'messages': messages,
        }
        kwargs.update(context)
        return super().get_context_data(**kwargs)


class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            messages.success(request, username +
                             " account is created succesfully")

            Profile.objects.create(
                user=user,
                username=username,
            )
            return redirect('login')
    context = {
        'form': form
    }

    return render(request, 'registration/register.html', context)


def authorRequest(request, uid):
    profile = Profile.objects.get(id=uid)
    profile.role = "Admin"
    profile.save()
    messages.success(request, 'You are author now use it wisely')
    return redirect(profile)
