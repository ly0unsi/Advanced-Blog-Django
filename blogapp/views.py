from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import addPostForm, editPostForm, addCommentForm, messageForm, addReplyForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count

# Create your views here.


'''def homepage(request):
    return render(request, 'homepage.html')'''


@login_required(login_url='login')
def contact(request):
    user = request.POST.get('user')
    message = Message
    messageformset = messageForm()
    if request.method == 'POST':
        messageformset = messageForm(request.POST)
        if messageformset.is_valid():
            message.objects.create(
                user=request.user,
                message=messageformset.cleaned_data.get('message'),
                subject=messageformset.cleaned_data.get('subject'),
            )
            messages.success(request, 'We received your message thanks')
            return redirect('home')
    return render(request, 'contact.html', {'messageformset': messageformset})


def postcomment(request, cid):
    comment = Comment.objects.get(id=cid)
    comment.delete()
    messages.success(request, 'Comment deleted')
    return redirect(comment.post)


def vote(request, question_id):
    # print(request.POST['choice'])
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        messages.error(request, 'Profile details updated.')
        return render(request, 'homepage.html', {
            'question': question,
            'error_message': "Hmmmm we neeed a response not stupidity.",

        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        messages.warning(request, 'Thanks for sharing ur useless opinion')
        return redirect('home')
    return redirect('home')


def like(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('postId'))
    if post.likes.filter(id=request.user.id):
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return HttpResponseRedirect(reverse('post', args=[str(pk)]))


def reply(request):
    post = get_object_or_404(Post, id=request.POST.get('postId'))
    if request.method == 'POST':
        replyform = addReplyForm(request.POST)
        if replyform.is_valid():
            Reply.objects.create(
                post=post,
                comment=get_object_or_404(
                    Comment, id=request.POST.get('comment')),
                owner=request.user,
                body=replyform.cleaned_data.get('body'),
            )
            messages.success(request, 'reply added')

            return redirect(post)


def postdetail(request, pid):
    categories = Category.objects.all()
    most_liked = Post.objects.all().annotate(
        likes_count=Count('likes')).order_by('-likes_count')
    most_viewed = Post.objects.all().annotate(
        views_count=Count('views')).order_by('-views_count')
    links = Settings.objects.get(id=1)
    facebookicon = links.facebook.split('.')[1]
    instagramicon = links.instagram.split('.')[1]
    twittericon = links.twitter.split('.')[1]
    pinteresticon = links.pinterest.split('.')[1]
    post = get_object_or_404(Post, id=pid)
    related = Post.objects.filter(category=post.category)
    likers = post.likes.all()
    if request.user.id:
        post.views.add(request.user)
    liked = False
    if post.likes.filter(id=request.user.id):
        liked = True
    else:
        liked = False

    commentform = addCommentForm()
    if request.method == 'POST':
        commentform = addCommentForm(request.POST)
        if commentform.is_valid():
            Comment.objects.create(
                post=post,
                owner=request.user,
                body=commentform.cleaned_data.get('body'),
            )
            messages.success(request, 'comment added')
            return redirect(post)
    replyform = addReplyForm()
    context = {
        'categories': categories,
        'post': post,
        'liked': liked,
        'likers': likers,
        'related': related,
        'most_viewed': most_viewed,
        'most_liked': most_liked,
        'links': links,
        'facebookicon': facebookicon,
        'instagramicon': instagramicon,
        'twittericon': twittericon,
        'pinteresticon': pinteresticon,
        'commentform': commentform,
        'replyform': replyform
    }

    return render(request, 'postdetail.html', context)


def Home(request):
    categories = Category.objects.all()
    links = Settings.objects.get(id=1)
    facebookicon = links.facebook.split('.')[1]
    instagramicon = links.instagram.split('.')[1]
    twittericon = links.twitter.split('.')[1]
    pinteresticon = links.pinterest.split('.')[1]
    posts = Post.objects.order_by('-date')
    most_viewed = Post.objects.all().annotate(
        views_count=Count('views')).order_by('-views_count')
    users = User.objects.annotate(
        post_count=Count('post')).order_by('-post_count')
    most_liked = Post.objects.all().annotate(
        likes_count=Count('likes')).order_by('-likes_count')
    latest_question_list = Question.objects.order_by('-pub_date')[:1]
    entertainement = Post.objects.filter(category=4)
    rap = Post.objects.filter(category=5)
    sports = Post.objects.filter(category=1)
    context = {
        'categories': categories,
        'posts': posts,
        'latest_question_list': latest_question_list,
        'links': links,
        'most_viewed': most_viewed,
        'most_liked': most_liked,
        'facebookicon': facebookicon,
        'instagramicon': instagramicon,
        'twittericon': twittericon,
        'pinteresticon': pinteresticon,
        'users': users,
        'entertainement': entertainement,
        'rap': rap,
        'sports': sports
    }
    return render(request, 'homepage.html', context)


class addPost(CreateView):
    model = Post
    form_class = addPostForm
    template_name = 'addPost.html'

    def get_context_data(self, **kwargs):
        categories = Category.objects.all()
        links = Settings.objects.get(id=1)
        facebookicon = links.facebook.split('.')[1]
        instagramicon = links.instagram.split('.')[1]
        twittericon = links.twitter.split('.')[1]
        pinteresticon = links.pinterest.split('.')[1]
        context = {
            'links': links,
            'categories': categories,
            'facebookicon': facebookicon,
            'instagramicon': instagramicon,
            'twittericon': twittericon,
            'pinteresticon': pinteresticon,
        }
        kwargs.update(context)
        return super().get_context_data(**kwargs)


class updatePost(UpdateView):
    model = Post
    form_class = editPostForm
    template_name = 'editpost.html'

    def get_context_data(self, **kwargs):
        categories = Category.objects.all()
        links = Settings.objects.get(id=1)
        facebookicon = links.facebook.split('.')[1]
        instagramicon = links.instagram.split('.')[1]
        twittericon = links.twitter.split('.')[1]
        pinteresticon = links.pinterest.split('.')[1]
        context = {
            'categories': categories,
            'facebookicon': facebookicon,
            'instagramicon': instagramicon,
            'twittericon': twittericon,
            'pinteresticon': pinteresticon,
            'links': links,
        }
        kwargs.update(context)
        return super().get_context_data(**kwargs)


class deletePost(DeleteView):
    model = Post
    categories = Category.objects.all()
    template_name = 'deletePost.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        categories = Category.objects.all()
        links = Settings.objects.get(id=1)
        facebookicon = links.facebook.split('.')[1]
        instagramicon = links.instagram.split('.')[1]
        twittericon = links.twitter.split('.')[1]
        pinteresticon = links.pinterest.split('.')[1]
        context = {
            'categories': categories,
            'facebookicon': facebookicon,
            'instagramicon': instagramicon,
            'twittericon': twittericon,
            'pinteresticon': pinteresticon,
            'links': links,
        }
        kwargs.update(context)
        return super().get_context_data(**kwargs)


def profile(request, aid):
    links = Settings.objects.get(id=1)
    author = Profile.objects.get(id=aid)
    page = request.GET.get('page', 1)
    post_list = author.user.post_set.all()
    paginator = Paginator(post_list, 4)
    try:
        authorposts = paginator.page(page)
    except PageNotAnInteger:
        authorposts = paginator.page(1)
    except EmptyPage:
        authorposts = paginator.page(paginator.num_pages)
    posts = Post.objects.all().order_by('-date')
    categories = Category.objects.all()
    facebookicon = links.facebook.split('.')[1]
    instagramicon = links.instagram.split('.')[1]
    twittericon = links.twitter.split('.')[1]
    pinteresticon = links.pinterest.split('.')[1]
    context = {
        'categories': categories,
        'links': links,
        'author': author,
        'facebookicon': facebookicon,
        'instagramicon': instagramicon,
        'twittericon': twittericon,
        'pinteresticon': pinteresticon,
        'posts': posts,
        'authorposts': authorposts
    }
    return render(request, 'accountSettings.html', context)


def categoryPage(request, cid):
    category1 = Category.objects.get(id=cid)
    links = Settings.objects.get(id=1)
    most_viewed = Post.objects.all().annotate(
        views_count=Count('views')).order_by('-views_count')
    most_liked = Post.objects.all().annotate(
        likes_count=Count('likes')).order_by('-likes_count')
    categories = Category.objects.all()
    facebookicon = links.facebook.split('.')[1]
    instagramicon = links.instagram.split('.')[1]
    posts = Post.objects.all().order_by('-date')
    twittericon = links.twitter.split('.')[1]
    pinteresticon = links.pinterest.split('.')[1]
    latest_question_list = Question.objects.order_by('-pub_date')[:1]
    page = request.GET.get('page', 1)
    posts_category_list = Post.objects.filter(
        category=category1).order_by('-date')
    paginator = Paginator(posts_category_list, 6)
    try:
        posts_category = paginator.page(page)
    except PageNotAnInteger:
        posts_category = paginator.page(1)
    except EmptyPage:
        posts_category = paginator.page(paginator.num_pages)
    context = {
        'categories': categories,

    }
    context = {
        'category1': category1,
        'posts_category': posts_category,
        'categories': categories,
        'links': links,
        'latest_question_list': latest_question_list,
        'facebookicon': facebookicon,
        'instagramicon': instagramicon,
        'most_viewed': most_viewed,
        'most_liked': most_liked,
        'twittericon': twittericon,
        'pinteresticon': pinteresticon,

        'posts': posts
    }
    return render(request, 'category.html', context)
