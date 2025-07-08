from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView
from django.views.generic.edit import FormMixin
from django.urls import reverse
from .models import BlogPost, Comment
from .forms import CommentForm

class BlogPostDetailView(FormMixin, DetailView):
    model = BlogPost
    template_name = "blog/post_detail.html"
    context_object_name = "post"
    form_class = CommentForm

    def get_success_url(self):
        return reverse("blog_detail", kwargs={"slug": self.get_object().slug})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.get_form()
        context["comments"] = self.get_object().comments.filter(approved=True)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()

        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog_post = self.object
            comment.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
