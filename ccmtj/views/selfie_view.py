from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from ..models import SelfieHistorica

# FBV para galeria (já existia)
def selfie_historica(request):
    thumbs = SelfieHistorica.objects.all().order_by('nome')
    return render(request, 'ccmtj/selfie/selfie.html', {'thumbs': thumbs})

# CBVs para CRUD
class SelfieListView(LoginRequiredMixin, ListView):
    model = SelfieHistorica
    template_name = 'ccmtj/selfie/selfie_list.html'

class SelfieDetailView(LoginRequiredMixin, DetailView):
    model = SelfieHistorica
    template_name = 'ccmtj/selfie/selfie_detail.html'

class SelfieCreateView(LoginRequiredMixin, CreateView):
    model = SelfieHistorica
    fields = ['titulo', 'descricao', 'imagem']
    template_name = 'ccmtj/selfie/selfie_form.html'
    success_url = reverse_lazy('selfie-list')

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

class SelfieUpdateView(LoginRequiredMixin, UpdateView):
    model = SelfieHistorica
    fields = ['titulo', 'descricao', 'imagem']
    template_name = 'ccmtj/selfie/selfie_form.html'
    success_url = reverse_lazy('selfie-list')

    def get_queryset(self):
        return SelfieHistorica.objects.filter(usuario=self.request.user)

class SelfieDeleteView(LoginRequiredMixin, DeleteView):
    model = SelfieHistorica
    template_name = 'ccmtj/selfie/selfie_confirm_delete.html'
    success_url = reverse_lazy('selfie-list')

    def get_queryset(self):
        return SelfieHistorica.objects.filter(usuario=self.request.user)
