from django.shortcuts import render
from django.views import generic
from .models import Post
from django.shortcuts import get_object_or_404, redirect

# Create your views here.

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    
class DetailView(generic.DetailView):
    model = Post
    template_name = "post_details.html"
    

class Search(generic.ListView):
    model = Post
    template_name = 'search_results.html' 

    def get_queryset(self):  # Surchargez la méthode get_queryset pour personnaliser la logique de recherche
        query = self.request.GET.get("search")
        if query:
            return Post.objects.filter(title__icontains=query)
        else:
            return Post.objects.none()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get("search", "")
        return context