from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.http import HttpResponse
from .models import Post, EducationItem, WorkItem, TechnicalItem, OtherItem
from .forms import PostForm, EducationForm, WorkForm, TechnicalForm, OtherForm

'''
def home_page(request):
    if (request.method == "POST"):
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')

    items = Item.objects.all()
    return render(request, 'blog/home.html', {'items': items})
'''

def post_list(request):
    posts = Post.objects.filter(published_date__lte = timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def cv(request):
    e_items = EducationItem.objects.all()
    t_items = TechnicalItem.objects.all()
    w_items = WorkItem.objects.all()
    o_items = OtherItem.objects.all()
    return render(request, 'blog/cv.html', {'e_items': e_items, 't_items': t_items, 'w_items': w_items, 'o_items': o_items})

def valid_start_end_years(form):
    start_year = form.cleaned_data.get("start_year")
    end_year = form.cleaned_data.get("end_year")
    return (start_year <= end_year)

def cv_new(request, form_title):
    if request.method == "POST":
        if ("Education" in form_title):
            form = EducationForm(request.POST)
        elif ("Technical Skill" in form_title):
            form = TechnicalForm(request.POST)
        elif ("Work Experience" in form_title):
            form = WorkForm(request.POST)
        else:
            form = OtherForm(request.POST)

        if form.is_valid():
            if (("Education" in form_title) or ("Work Experience" in form_title)):
                if valid_start_end_years(form):
                    post = form.save(commit=False)
                    post.save()
                    return redirect('cv')
            else:
                post = form.save(commit=False)
                post.save()
                return redirect('cv')
    else:
        if ("Education" in form_title):
            form = EducationForm()
        elif ("Technical Skill" in form_title):
            form = TechnicalForm()
        elif ("Work Experience" in form_title):
            form = WorkForm()
        else:
            form = OtherForm()
    return render(request, 'blog/cv_new.html', {'form': form, 'form_title': form_title})

def cv_edit(request, form_title, pk):
    if ("Education" in form_title):
        post = get_object_or_404(EducationItem, pk=pk)
    elif ("Technical Skill" in form_title):
        post = get_object_or_404(TechnicalItem, pk=pk)
    elif ("Work Experience" in form_title):
        post = get_object_or_404(WorkItem, pk=pk)
    else:
        post = get_object_or_404(OtherItem, pk=pk)

    if request.method == "POST":
        if ("Education" in form_title):
            form = EducationForm(request.POST, instance=post)
        elif ("Technical Skill" in form_title):
            form = TechnicalForm(request.POST, instance=post)
        elif ("Work Experience" in form_title):
            form = WorkForm(request.POST, instance=post)
        else:
            form = OtherForm(request.POST, instance=post)

        if form.is_valid():
            if (("Education" in form_title) or ("Work Experience" in form_title)):
                if valid_start_end_years(form):
                    post = form.save(commit=False)
                    post.save()
                    return redirect('cv')
            else:
                post = form.save(commit=False)
                post.save()
                return redirect('cv')
    else:
        if ("Education" in form_title):
            form = EducationForm(instance=post)
        elif ("Technical Skill" in form_title):
            form = TechnicalForm(instance=post)
        elif ("Work Experience" in form_title):
            form = WorkForm(instance=post)
        else:
            form = OtherForm(instance=post)
    return render(request, 'blog/cv_new.html', {'form': form, 'form_title': form_title})