from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from . models import Post


def post_list(request):
    posts = Post.objects.all()
    return render(
        request,
        'bookblog/list.html',
        {
            'posts': posts,
            'title': 'all posts',
        }
    )


class ListViewPublish(ListView):
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['title'] = 'My Title'
        return ctx

    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    title = 'published'
    template_name = 'bookblog/list.html'


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                             publish__year=year, publish__month=month, publish__day=day)
    return render(
        request,
        'bookblog/detail.html',
        {
            'post': post,
            'title': 'detail posts',
        }
    )
