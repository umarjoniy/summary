from django.shortcuts import render, redirect
from .models import *
from .forms import *


def main(request):
    ctx = {}

    person = Person.objects.get()
    ctx['person'] = person

    ctx['partners'] = person.partners.all().order_by('place')

    ctx['educations'] = Education.objects.all().order_by('place')

    ctx['experience'] = Experience.objects.all().order_by('place')

    ctx['skills_main'] = Skills.objects.filter(is_main=True)[:3]
    ctx['skills_minor'] = Skills.objects.filter(is_main=False)[:6]

    ctx['awards'] = Awards.objects.all().order_by('place')

    ctx['services'] = Services.objects.all()[:6]

    ctx['projects'] = Projects.objects.all()[:6]

    ctx['another'] = Another.objects.get()

    ctx['posts'] = Posts.objects.filter(is_published=True).order_by('-created_at')[:3]

    form = FormContact(request.POST or None)
    if form.is_valid():
        form.save()

    if request.method == 'POST':
        return redirect('/')

    ctx['form'] = form
    for i in ctx['posts']:
        com = len(Comments.objects.filter(article=i))
        i.com = com
    return render(request, 'index.html', ctx)


def single(request, slug):
    ctx = {}
    post = Posts.objects.get(slug=slug)
    ctx['post'] = post
    ctx['comment'] = Comments.objects.filter(article=post)
    ctx['comment_num'] = len(Comments.objects.filter(article=post))

    form = FormComment(request.POST or None)

    if form.is_valid():
        form.article = post
        a = form.save(commit=False)
        a.article = post
        a.save()

    if request.method == 'POST':
        return redirect(f'/single/{post.slug}')

    ctx['form'] = form

    return render(request, 'single.html', ctx)
