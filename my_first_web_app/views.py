from random import randint
from django.http import HttpResponse
from django.shortcuts import render

# our first function
# request for HTTP request
# a client makes a request to our home URL
# our function needs to take one argument representing the HTTP request
def home_page(request):
    context = {'name': 'Betty Maker'}
    response = render(request, 'index.html', context)
    return HttpResponse(response)

def portfolio_page(request):
    image_urls = []
    for i in range(5):
        random_number = randint(0,100)
        image_urls.append("https://picsum.photos/400/600/?image={}".format(random_number))
    context = {'gallery_images': image_urls}
    reposnse = render(request, 'gallery.html', context)
    return HttpResponse(reposnse)

def about_me_page(request):
    context = {'skills': ['HTML', 'CSS', 'python', 'django'], 'interests': ['psychology', 'neuroscience', 'math', 'running']}
    response = render(request, 'about_me.html', context)
    return HttpResponse(response)

def favourites_page(request):
    context = {'fave_links': ['https://www.reddit.com/', 'https://www.goodreads.com/', 'https://www.vice.com/en_ca']}
    reposnse = render(request, 'favourites.html', context)
    return HttpResponse(reposnse)
