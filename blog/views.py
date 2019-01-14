from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post

# Create your views here.

def home(request):
    context = {
            'posts': Post.objects.all()
            }
    return render(request, 'blog/home.html', context)

# membuat class untuk ListView
class PostListView(ListView):
    model               = Post
    template_name       = 'blog/home.html' # reverinsi url ( <app>/<model>_<viewtype>.html )
    context_object_name = 'posts'
    ordering            = ['-date']
    paginate_by         = 5 # untuk mengatur paginate


class UserPostListView(ListView):  
    model               = Post
    template_name       = 'blog/user_post.html' # reverinsi url ( <app>/<model>_<viewtype>.html )
    context_object_name = 'posts'
    paginate_by         = 5 # untuk mengatur paginate

    def get_queryset(self): # setting authenticade untuk tampilan sesuai dengan user(author)
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date')

# membuat class untuk DetailView
class PostDetailView(DetailView):
    model               = Post


################################ CRUD dari django ############################################
class PostCreateView(LoginRequiredMixin, CreateView):
    model               = Post
    fields              = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model               = Post
    fields              = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# function untuk mencegah agar author lain tidak bisa update pos author lain
    def test_func(self):
        post    = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model           = Post
    success_url     = '/'

    def test_func(self):
        post        = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
