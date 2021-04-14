from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls.base import reverse
from django.views.generic import ListView
from django.core.mail import send_mail
from . models import Post, Comment
from . form import EmailForm, CommentForm


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
    template_name = 'bookblog/list.html'


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                             publish__year=year, publish__month=month, publish__day=day)

    comments = post.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return HttpResponseRedirect(reverse('bookblog:post_detail', args=[year, month, day, post.slug]))
    else:
        comment_form = CommentForm()

    return render(
        request,
        'bookblog/detail.html',
        {
            'post': post,
            'title': 'detail posts',
            'comments': comments,
            'new_comment': new_comment,
            'comment_form': comment_form,
        }
    )

def post_share(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    send = False

    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(
                post.get_absolute_url()
            )
            subject = f"{cd['name']} recomend to read {post.title}"
            message = f"Read: {post.title} at {post_url}"
            send_mail(subject, message, 'korea60@abv.bg', [cd['to']])
            send = True
            # return HttpResponse("Email send successfull")
    else:
        form = EmailForm()
    return render(request, 'bookblog/share.html', {'post': post, 'form': form, 'send': send})
