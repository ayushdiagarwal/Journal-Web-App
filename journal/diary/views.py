from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Entry
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.list import MultipleObjectMixin
from django.db.models import Q


class index(LoginRequiredMixin, ListView):
    template_name = 'diary/index.html'
    context_object_name = 'entries'
    paginate_by = 9

    def get_queryset(self):
        self.query = self.request.GET.get("q")
        if self.query:
            return Entry.objects.filter(
                Q(title__icontains=self.query),
                author=self.request.user
            ).distinct()
        else:
            return Entry.objects.filter(author=self.request.user)


class EntryCreate(LoginRequiredMixin, MultipleObjectMixin, CreateView):
    model = Entry
    fields = ['title', 'content']
    template_name = 'diary/create.html'
    object_list = Entry.objects.all()

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class EntryUpdate(LoginRequiredMixin, MultipleObjectMixin, UserPassesTestMixin, UpdateView):  # MultipleObjectMixin
    model = Entry
    fields = ['title', 'content']
    template_name = 'diary/update.html'
    object_list = Entry.objects.all()

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


class EntryDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Entry
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


@login_required
def Profile(request):
    return render(request, 'diary/profile.html')
