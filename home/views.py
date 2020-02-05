from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from django.views.generic import TemplateView, ListView, DetailView, FormView, View
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Post
from .forms import PostForm

# Create your views here.
class HomePage(LoginRequiredMixin, TemplateView):
    template_name = "home/home.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['name'] = "Artem"
        return context

class PostsView(LoginRequiredMixin, ListView):
    template_name = "home/posts.html"
    context_object_name = "posts"
    model = Post

class DetailPage(LoginRequiredMixin, DetailView):
    model = Post
    pk_url_kwarg = 'id'

class CreatePost(LoginRequiredMixin, FormView):
    form_class = PostForm
    template_name = "home/create_post.html"
    success_url = "posts_page"

    def form_valid(self, form):
        form.save()
        return redirect(self.get_success_url())

class ChangePost(LoginRequiredMixin, View):
    
    def get(self, request, id):
        obj = Post.objects.get(id=id)
        form = PostForm(instance=obj)

        return render(request, "home/change_post.html", context={"form": form, "post": obj})

    def post(self, request, id):
        obj = Post.objects.get(id=id)
        bound_form = PostForm(request.POST, instance=obj)

        if bound_form.is_valid():
            bound_form.save()
            return redirect("posts_page")
        else:
            error = "Ошибка! Невозможно создать пост!!!"
            return render(request, "home/change_post.html", context={"form": bound_form, "error": error, "post": obj})


def redirect_view(requests):
    return redirect("home_page")