from django.shortcuts import render
from blogapp.models import Post, Category, Question, Settings, Message
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .forms import addPostForm, editPostForm, addCategoryForm, editCategoryForm, editSettingsForm, createSettingsForm
from itertools import chain
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator

# Create your views here.


@staff_member_required
def dashboard(request):
    posts = Post.objects.all()
    Total = posts.count()
    sum = Post.objects.all()
    messages = Message.objects.all()
    messages = messages.order_by('-id')[:4]
    interractions = Post.objects.none()
    for i in sum:
        interractions = list(chain(interractions,  i.likes.all()))

    Comments = Post.objects.none()
    for c in sum:
        Comments = list(chain(Comments,  c.comments.all()))
    Users = User.objects.all()
    siteSettings = Settings.objects.all()
    intPercent = round((100*len(interractions))/(len(sum)*len(Users)))
    context = {
        'Total': Total,
        'intPercent': intPercent,
        'Comments': Comments,
        'Users': Users,
        'siteSettings': siteSettings,
        'messages': messages
    }
    return render(request, 'dashboard.html', context)


@method_decorator(staff_member_required, name='dispatch')
class all(ListView):

    model = Post
    template_name = 'all.html'
    ordering = ['-id']


@method_decorator(staff_member_required, name='dispatch')
class localdetail(DetailView):
    model = Post
    template_name = 'localdetail2.html'


@method_decorator(staff_member_required, name='dispatch')
class addLocal(CreateView):
    model = Post
    form_class = addPostForm
    template_name = 'addLocal.html'

    def get_context_data(self, **kwargs):
        messages.success(self.request, 'Post added succesfully')
        siteSettings = Settings.objects.all()
        context = {
            'mesages': messages,
            'siteSettings': siteSettings
        }
        kwargs.update(context)
        return super().get_context_data(**kwargs)


@method_decorator(staff_member_required, name='dispatch')
class updateLocal(UpdateView):
    model = Post
    form_class = editPostForm
    template_name = 'editLocal.html'

    def get_context_data(self, **kwargs):
        messages.success(self.request, 'Post updated succesfully')
        siteSettings = Settings.objects.all()
        context = {
            'mesages': messages,
            'siteSettings': siteSettings
        }
        kwargs.update(context)
        return super().get_context_data(**kwargs)


@method_decorator(staff_member_required, name='dispatch')
class deleteLocal(DeleteView):
    model = Post
    template_name = 'deleteLocal.html'
    success_url = reverse_lazy('all')

    def get_context_data(self, **kwargs):
        messages.success(self.request, 'Category deleted succesfully')
        siteSettings = Settings.objects.all()
        context = {
            'mesages': messages,
            'siteSettings': siteSettings
        }
        kwargs.update(context)
        return super().get_context_data(**kwargs)


@method_decorator(staff_member_required, name='dispatch')
class allCats(ListView):

    model = Category
    template_name = 'allcats.html'
    ordering = ['-id']


@method_decorator(staff_member_required, name='dispatch')
class addCat(CreateView):
    model = Category
    form_class = addCategoryForm
    template_name = 'addCat.html'

    def get_context_data(self, **kwargs):
        messages.success(self.request, 'Category added succesfully')
        success_url = reverse_lazy('allcats')
        siteSettings = Settings.objects.all()
        context = {
            'mesages': messages,
            'siteSettings': siteSettings
        }
        kwargs.update(context)
        return super().get_context_data(**kwargs)


@method_decorator(staff_member_required, name='dispatch')
class updateCat(UpdateView):
    model = Category
    form_class = editCategoryForm
    template_name = 'editCat.html'

    def get_context_data(self, **kwargs):
        messages.success(self.request, 'Category Updated succesfully')
        success_url = reverse_lazy('allcats')
        siteSettings = Settings.objects.all()
        context = {
            'mesages': messages,
            'siteSettings': siteSettings
        }
        kwargs.update(context)
        return super().get_context_data(**kwargs)


@method_decorator(staff_member_required, name='dispatch')
class deleteCat(DeleteView):
    model = Category
    template_name = 'deleteCat.html'
    success_url = reverse_lazy('allcats')

    def get_context_data(self, **kwargs):
        messages.success(self.request, 'Category deleted succesfully')
        links = Settings.objects.get(id=1)
        facebookicon = links.facebook.split('.')[1]
        instagramicon = links.instagram.split('.')[1]
        twittericon = links.twitter.split('.')[1]
        pinteresticon = links.pinterest.split('.')[1]
        context = {
            'mesages': messages,
            'facebookicon': facebookicon,
            'instagramicon': instagramicon,
            'twittericon': twittericon,
            'pinteresticon': pinteresticon,
            'links': links,
        }
        kwargs.update(context)
        return super().get_context_data(**kwargs)


@method_decorator(staff_member_required, name='dispatch')
class allUsers(ListView):

    model = User
    template_name = 'allusers.html'
    ordering = ['-id']


@method_decorator(staff_member_required, name='dispatch')
class userDetail(DetailView):

    model = User
    template_name = 'userdetail.html'


@method_decorator(staff_member_required, name='dispatch')
class allPolls(ListView):

    model = Question
    template_name = 'allpolls.html'
    ordering = ['-id']


@method_decorator(staff_member_required, name='dispatch')
class editSettings(UpdateView):
    model = Settings
    form_class = editSettingsForm
    template_name = 'editsettings.html'
    success_url = reverse_lazy('allcats')

    def get_context_data(self, **kwargs):
        messages.success(self.request, 'Settings Updated succesfully')
        siteSettings = Settings.objects.all()
        context = {
            'mesages': messages,
            'siteSettings': siteSettings
        }
        kwargs.update(context)
        return super().get_context_data(**kwargs)


@method_decorator(staff_member_required, name='dispatch')
class createSettings(CreateView):
    model = Settings
    form_class = createSettingsForm
    template_name = 'createsettings.html'
    success_url = reverse_lazy('allcats')

    def get_context_data(self, **kwargs):
        messages.success(self.request, 'Settings Created succesfully')
        siteSettings = Settings.objects.all()
        context = {
            'mesages': messages,
            'siteSettings': siteSettings
        }
        kwargs.update(context)
        return super().get_context_data(**kwargs)
