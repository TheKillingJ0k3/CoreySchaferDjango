from django.shortcuts import render # to render html
from .models import Post #added in DB and migrations video

# posts = [
#     {
#         'author': 'Th3KillingJ0k3',
#         'title' : 'Blog Post 1',
#         'content' : 'You shouldn\'t trust the story-teller; only trust the story.',
#         'date_posted' : 'July 12, 2022'
#     },
#     {
#         'author': 'Th3KillingJ0k3',
#         'title' : 'Blog Post 2',
#         'content' : 'The price of getting what you want is getting what you once wanted.',
#         'date_posted' : 'July 12, 2022'
#     }
# ]

# def home(request):
#     return HttpResponse('<h1>Blog Home</h1>') #templates to avoid this
def home(request):
    context = {
        # 'posts' : posts
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context) # add context to template

# add blog app to the list of installed apps so that django knows to look for templates directory -> app.py
# class BlogConfig(AppConfig):
    # default_auto_field = 'django.db.models.BigAutoField'
    # name = 'blog'

# def about(request):
#     return HttpResponse('<h1>Blog About</h1>') #templates to avoid this
def about(request):
    return render(request, 'blog/about.html', {'title':'About'})

# def portfolio(request):
#     return HttpResponse('<h1>Portfolio</h1>') #templates to avoid this
def portfolio(request):
    return render(request, 'blog/portfolio.html')