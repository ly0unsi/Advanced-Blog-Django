from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime
from ckeditor.fields import RichTextField
import readtime
# Create your models here.


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=250)
    message = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.message


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    username = models.CharField(max_length=50, null=True, blank=True)
    role = models.CharField(max_length=250, null=True,
                            blank=True, default="sub admin")
    profile_pic = models.ImageField(
        upload_to="media/members/", null=True, default='profile_pic.png', blank=True)
    bio = models.TextField(null=True, blank=True)
    iam = models.CharField(max_length=50, default="")
    CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    facebook = models.URLField(
        max_length=200, default='', null=True, blank=True)
    instagram = models.URLField(
        max_length=200, default='', null=True, blank=True)
    twitter = models.URLField(
        max_length=200, default='', null=True, blank=True)
    sexe = models.CharField(max_length=50, default="Male", choices=CHOICES)

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('profile',  kwargs={'aid': self.id})


class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('allcats')


class Post(models.Model):
    title = models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="media/images/")
    body = RichTextField()
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(
        Category, null=True, on_delete=models.CASCADE, default="")

    def get_readtime(self):
        result = readtime.of_text(self.body)
        return result.text

    likes = models.ManyToManyField(
        User, related_name='blog_post')
    views = models.ManyToManyField(
        User, related_name='blog_post_views')

    def __str__(self):
        return self.title+' | '+str(self.author)

    def get_absolute_url(self):
        return reverse('post',  kwargs={'pid': self.id})


class Comment(models.Model):
    post = models.ForeignKey(
        Post, related_name="comments", on_delete=models.CASCADE)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    body = models.TextField()
    created_at = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.body + '|'+str(self.owner)

    def get_absolute_url(self):
        return reverse("post", kwargs={"pk": post.pk})


class Reply(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE)
    comment = models.ForeignKey(
        Comment, related_name='replies', on_delete=models.CASCADE)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    body = models.TextField()
    created_at = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.body+"|"+self.owner.username

    def get_absolute_url(self):
        return reverse("post", kwargs={"pk": post.pk})


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published',)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class Settings(models.Model):
    facebook = models.URLField(max_length=200, null=True, blank=True)
    instagram = models.URLField(max_length=200, null=True, blank=True)
    pinterest = models.URLField(max_length=200, null=True, blank=True)
    twitter = models.URLField(max_length=200, null=True, blank=True)
    About = RichTextField()

    def __str__(self):
        return "settings"

    def get_absolute_url(self):
        return reverse("Social_detail", kwargs={"pk": self.pk})
