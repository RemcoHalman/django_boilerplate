from django.shortcuts import render

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import DetailView, ListView

from .models import BlogPost, Page, Project, User, Testimonial


### Generic Views
class PageDetailView(DetailView):
    model = Page

### Custom Pages
def Home(request):
    context = {
        'home': Page.objects.get(pk=1),
        'testimonials': Testimonial.objects.all(),
        'title': 'Home',
    }
    return render(request, "home.html", context)

def Blog(request):
    context = {
        'blog_posts': BlogPost.objects.all(),
        'title': 'Blog',
    }
    return render(request, "website/blog_posts.html", context)

def Project_items(request):
    context = {
        'portfolio_items': Project.objects.all(),
        'title': 'Portfolio',
    }
    return render(request, "website/project_posts.html", context)


def Profile(request):
    context = {
        'title': 'Profile',
    }
    return render(request, "website/profile.html", context)

#### Error pages
def error_400_view(request, exception=None, template_name="400.html"):
    response = render_to_response("errors/400.html")
    response.status_code = 400
    return response

def error_403_view(request, exception=None, template_name="403.html"):
    response = render_to_response("errors/403.html")
    response.status_code = 403
    return response

def error_400_view(request, exception=None, template_name="400.html"):
    response = render_to_response("errors/400.html")
    response.status_code = 400
    return response

def error_500_view(request, exception=None, template_name="500.html"):
    response = render_to_response("errors/500.html")
    response.status_code = 500
    return response
