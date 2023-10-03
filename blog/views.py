from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView
)
from .models import Post


def home(request):
    context = {'posts': Post.objects.all()}
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    # Django looks for by default: <app>/<model>_<viewtype>.html
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    # This view used django's default variables so you can have less lines of code
    model = Post


class PostCreateView(CreateView):
    model = Post
    fields = [
        'title',
        'content',
    ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
