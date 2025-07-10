from django.shortcuts import render
from django.views.generic import TemplateView

from django.views.generic import TemplateView
from blog.models import BlogPost
#from projects.models import Project


class HomePageView(TemplateView):
    template_name = "core/homepage.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Get the latest blog post
        latest_post = BlogPost.objects.order_by('-created_at').first()
        context['latest_post'] = latest_post


        #context['projects'] = Project.objects.filter(highlighted=True)[:3]


        context['about_text'] = "I'm Jack Tate, a software engineer building cool stuff with code, CAD, and coffee."

        return context
