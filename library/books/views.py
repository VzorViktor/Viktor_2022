from django.shortcuts import render

posts = [
    {
        'author': 'CoreyMS',
        'title': 'Book Post 1',
        'content': 'First post content',
        'date_posted': 'October 22, 2022'
    },
    {
        'author': 'Jane Doe',
        'title': 'Book Post 2',
        'content': 'Second post content',
        'date_posted': 'October 23, 2022'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'books/home.html', context)


def about(request):
    return render(request, 'books/about.html', {'title': 'About'})


