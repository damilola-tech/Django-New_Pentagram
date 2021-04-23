from django.shortcuts import render
from django.shortcuts import render
# Create your views here.

from posts.forms import PostForm


def create_post(request):
    if request.method != 'POST':
        form = PostForm()
    else:
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return render(request, 'posts/success.html')

    context = {
        'form': form
    }

    return render(request, 'posts/posts.html', context)
