from django.shortcuts import render

posts = [
    {
        'author': 'Leon Kennedy',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'September 14, 2023'
    },
    {
        'author': 'Claire Redfield',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'September 13, 2023'
    },
]


def home(request):
    context = {'posts': posts}
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
