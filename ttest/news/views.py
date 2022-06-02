from django.shortcuts import render, get_object_or_404, redirect

from .models import News, Category
from .forms import NewsForm, UserRegisterForm, UserLoginForm, UserEmail
from django.views.generic import ListView, DetailView, CreateView
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth import login, logout
from django.core.mail import send_mail


class HomeNews(ListView):
    model = News
    template_name = 'news/index.html'
    context_object_name = 'news'
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Вход в грот Джунов'
        return context

    def get_queryset(self):
        return News.objects.filter(is_published='True')


class NewsByCategory(ListView):
    model = News
    template_name = 'news/index.html'
    context_object_name = 'news'
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'], is_published='True')


class ViewNews(DetailView):
    model = News
    pk_url_kwarg = 'news_id'
    template_name = 'news/view_news.html'
    context_object_name = 'news_item'


class CreateNews(CreateView):
    form_class = NewsForm
    template_name = 'news/add_news.html'


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Твоя клятва услышана, Джун!')
            return redirect('login')
        else:
            messages.error(request, 'Ты слукавил!')
    else:
        form = UserRegisterForm()
    return render(request, 'news/register.html', {"form": form} )


def login_in(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'news/login.html', {"form": form})


def log_out(request):
    logout(request)
    return redirect('login')


def thanks(request):
    if request.method == 'POST':
        form = UserEmail(data=request.POST)
        if form.is_valid():
            mail = send_mail(form.cleaned_data['subject'], form.cleaned_data['content'], 'extrasearch.ok@gmail.com', ['polinaponamareva3@gmail.com'], fail_silently=False)
            if mail:
                messages.success(request, 'Благодарность успешно доставлена')
                redirect('thanks')
            else:
                messages.error(request, 'Благодарочка не доставлена :(')
        else:
            messages.error(request, 'Упс, что-то ты тут уже сломал ;)')
    else:
        form = UserEmail()
    return render(request, 'news/thanks.html', {"form": form})



'''def index(request):
    news = News.objects.all()
    context = {
        'news': news,
        'title': 'Список новостей',
    }
    return render(request, 'news/index.html', context)'''


'''def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    context = {
        'news': news,
        'category': category,
    }
    return render(request, 'news/categories.html', context)'''


'''def view_news(request, news_id):
    news_item = get_object_or_404(News, pk=news_id)
    context = {
        'news_item': news_item,
    }
    return render(request, 'news/view_news.html', context)'''


'''def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            #news = News.objects.create(**form.cleaned_data)
            news = form.save()
            return redirect(news)
    else:
        form = NewsForm()
    return render(request, 'news/add_news.html', {'form': form})'''
