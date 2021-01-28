from django import forms
from blogapp.models import Post, Comment, Category, Settings


class addPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'body', 'category', 'image')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Post title'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username', 'id': 'username', 'type': 'hidden'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }


class editPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body', 'category', 'image')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Post title'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }


class addCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('post', 'owner', 'body')
        widgets = {
            'post': forms.TextInput(attrs={'class': 'form-control', 'id': 'post'}),
            'owner': forms.TextInput(attrs={'class': 'owner', 'id': 'owner'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }


class addCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Category title'}),
        }


class editCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Category title'}),
        }


class addCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('post', 'owner', 'body')
        widgets = {
            'post': forms.TextInput(attrs={'class': 'form-control', 'id': 'post'}),
            'owner': forms.TextInput(attrs={'class': 'owner', 'id': 'owner'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }


class editSettingsForm(forms.ModelForm):
    class Meta:
        model = Settings
        fields = ('facebook', 'instagram', 'twitter', 'pinterest', 'About')
        widgets = {
            'facebook': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'facebook url'}),
            'instagram': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'instagram url'}),
            'twitter': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'twitter url'}),
            'pinterest': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'pinterest url'}),
            'About': forms.Textarea(attrs={'class': 'form-control'}),
        }


class createSettingsForm(forms.ModelForm):
    class Meta:
        model = Settings
        fields = ('facebook', 'instagram', 'twitter', 'pinterest', 'About')
        widgets = {
            'facebook': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'facebook url'}),
            'instagram': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'instagram url'}),
            'twitter': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'twitter url'}),
            'pinterest': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'pinterest url'}),
            'About': forms.Textarea(attrs={'class': 'form-control'}),
        }
