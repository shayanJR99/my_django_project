
from django.utils import timezone
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, TemplateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post
# Create your views here.

class HomeView(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "ali" 
        return context
    
    
class PostList(ListView):

    # model = Post  
    context_object_name = "posts"
    paginate_by = 2
    
    def get_queryset(self):
        posts = Post.objects.filter(status=1)
        return posts
    
    
class PostDetail(DetailView):
    model = Post
    
   
class PostCreate(CreateView):

    model = Post

    fields = [
        "title",
        "image",
        "content",
        "category",
    ]

    template_name = "blog/post_create.html"

    success_url = reverse_lazy("blog:post_list")


    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.published_date = timezone.now()
        return super().form_valid(form)


    def form_invalid(self, form):

        print(form.errors)

        return super().form_invalid(form)
    
    
class PostUpdate(UpdateView):

    model = Post

    fields = [
        "title",
        "image",
        "content",
        "category",
    ]

    template_name = "blog/post_update.html"

    success_url = reverse_lazy("blog:myposts")
    


class PostDelete(DeleteView):
    
    

    model = Post

    template_name = "blog/post_delete.html"

    success_url = reverse_lazy("blog:myposts")


    def get_queryset(self):

        return Post.objects.filter(
            author=self.request.user
        )
        

class MyPosts(LoginRequiredMixin,ListView):

    model = Post

    template_name = "blog/my_posts.html"
    paginate_by = 2
    context_object_name = "posts"


    def get_queryset(self):

        return Post.objects.filter(author=self.request.user,status=1).order_by("-created_date")
        