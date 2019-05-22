from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from blog.models import PostForms

def postform(request):
    if request.method == 'POST':
        title_p = request.POST.get('title')
        name_p = request.POST.get('name')
        lt = request.POST.get('ls')
        gq = request.POST.get('question')
        presentation_p = request.POST.get('presentation')
        background_p = request.POST.get('background')
        pt = request.POST.get('perfTask')
        quiz_p = request.POST.get('quiz')
        vocab_p = request.POST.get('vocab')
        wiki_p = request.POST.get('wiki')

        p = PostForms(title=title_p, name=name_p, ls=lt, question=gq, presentation=presentation_p,
        background=background_p, perfTask=pt, quiz=quiz_p, vocab=vocab_p, wiki=wiki_p)
        p.save()

        return(render(request, 'blog/postform.html'))
    else:
        return(render(request, 'blog/postform.html'))

def posts(request, pk):
    post = PostForms.objects.get(pk=pk)
    return render(request, 'post.html', {'post': post})

def search(request):
    query_string = ''
    found_entries = None
    if ('q' in request.GET) and request.GET['q'].strip():
        query_string = request.GET['q']
        posts = PostForms.objects.filter(ls__icontains=query_string)
        context = {
            'query_string': query_string,
            'posts': posts
        }
        return render(request, 'search.html', context)
    else:
        return render(request, 'blog/blog.html', { 'query_string': 'Null', 'found_entries': 'Enter a search term' })
"""
def search(request):
    template = 'blog/blog.html'
    query = request.GET.get('q')
    result = PostForms.objects.filter(Q(ls__icontains=query))

    context = {
        'result': result
    }
    return render(request, template, context)
    """
