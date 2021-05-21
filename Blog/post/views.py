from .forms import createPostForm
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django import forms
from .models import Author, Post

# Create your views here.


def index(request):
    posts = Post.objects.all()
    authors = Author.objects.all()

    return render(request, "post/index.html",{
        "posts": posts,
        "authors": authors
    })

def authorPosts(request):
    # get all authors to show them in select list in HTML template
    authors = Author.objects.all()
    if request.method == "POST":
        author = Author.objects.get(pk=int(request.POST["author"]))
        authPosts = author.posts.all()
    

        return render(request, "post/authorPosts.html",{
            "authPosts": authPosts,
            "author": author
        })
    return HttpResponseRedirect(reverse("index"))


#  Create a new post
def createPost(request):
    # get all the authors to display them as list
    authors = Author.objects.all()
    # if the user create a post
    if request.method == "POST":
        form = createPostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            authors = form.cleaned_data["author"]
            status = form.cleaned_data["status"]
        
            # if everything is valid save the post 
            form.save()
            
            return HttpResponseRedirect(reverse("index"))
        else:
            # if the form is not valid, return the same page with a form populated with user data
            return render(request, "post/createPost.html",{
                "form": createPostForm()
            })

    # render the create Post page
    return render(request, "post/createPost.html",{
        'form': createPostForm(),
        'authors': authors
    })

# Edit a post if you are the author
def editPost(request, post_id):
    instance =Post.objects.get(pk=post_id)
    

    # authors = Author.objects.all()
    author = instance.author
    if request.method == "POST":
        # None here to stop instantiate the form with reqest.POST when we are not posting to it.
        form = createPostForm(request.POST or None, instance=instance)
        if form.is_valid():
            requestAuthor = form.cleaned_data["author"]
            if author == requestAuthor:

                instance = form.save(commit=False)
                instance.save()
                return HttpResponseRedirect(reverse("index"))
            else:
                form = createPostForm({'title': instance.title, 'content': instance.content})
                return render(request, "post/editPost.html",{
                    'form': form,
                    'post':instance,
                    'message': "You should be the author to be able to edit this Post"
                })
                
        else:
            form = createPostForm({'title': instance.title, 'content': instance.content})
            return render(request, "post/editPost.html",{
                'form': form,
                'post':instance
            })

    return render(request, "post/editPost.html",{
        'form': createPostForm({'title': instance.title, 'content': instance.content}),
        'post': instance

    })

# delete a post
def deletePost(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    posts= Post.objects.all()
    if request.method == "POST":
        post.delete()
        return HttpResponseRedirect(reverse("index"))
    

    return render(request, "post/postDetails.html",{
        "post": post,
        "posts": posts
    })

# post details
def postDetails(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    return render(request, "post/postDetails.html",{
        "post": post
    })