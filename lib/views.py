from django.views.generic import DetailView, ListView, FormView, TemplateView
from django.views.generic.base import RedirectView
from django.urls import reverse
from django.shortcuts import get_object_or_404

from lib.models import *
from lib_social.users.models import User



class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all().order_by('title')
        return context


class UserListView(ListView):
    template_name = 'user_list.html'
    model = User

    def get_queryset(self):
        return self.model.objects.all()

    
class UserDetailView(DetailView):
    template_name = 'user_detail.html'
    model = User


class BookListView(ListView):
    template_name = 'book_list.html'
    model = Book

    def get_queryset(self):
        if self.kwargs.get('category_pk'):
            query_set = self.model.objects.filter(category_id=self.kwargs.get('category_pk')).order_by('title')
        else:
            query_set = self.model.objects.all().order_by('title')
        return query_set

    
class BookDetailView(DetailView):
    template_name = 'book_detail.html'
    model = Book

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_id'] = self.request.user.id
        print(self.request.user.id)
        return context


class BookRateView(RedirectView):
    permanent = False
    
    def get_redirect_url(self, *args, **kwargs):
        book = get_object_or_404(Book, pk=kwargs['pk'])
        user = get_object_or_404(User, pk=kwargs['user_pk'])
        rating_score = pk=kwargs['rating']
        if not Rating.objects.filter(book=book, user=user).exists():
            rating = Rating(book=book, user=user, rating=rating_score)
            rating.save()
        return reverse('book-detail', args=(kwargs['pk'],))


class BookBookView(RedirectView):
    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        book = get_object_or_404(Book, pk=kwargs['pk'])
        user = get_object_or_404(User, pk=kwargs['user_pk'])
        book.booker = user
        book.save()
        return reverse('book-detail', args=(kwargs['pk'],))

    
class BookUnbookview(RedirectView):
    permanent = False
    
    def get_redirect_url(self, *args, **kwargs):
        book = get_object_or_404(Book, pk=kwargs['pk'])
        book.booker = None
        book.save()
        return reverse('book-detail', args=(kwargs['pk'],))


class AuthorListView(ListView):
    template_name = 'author_list.html'
    model = Author

    def get_queryset(self):
        return self.model.objects.all().order_by('title')


class AuthorDetailView(DetailView):
    template_name = 'author_detail.html'
    model = Author


class ThreadListView(ListView):
    template_name = 'thread_list.html'
    model = Thread

    def get_queryset(self):
        return self.model.objects.all()


class ThreadDetailView(DetailView):
    template_name = 'thread_detail.html'
    model = Thread
