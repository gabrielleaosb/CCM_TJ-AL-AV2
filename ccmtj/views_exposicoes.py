from django.views.generic import TemplateView
from .models import Exposicao

class ExposicoesView(TemplateView):
    template_name = "ccmtj/exposicoes.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        exposicoes = Exposicao.objects.all()
        context["exposicoes"] = exposicoes  
        return context
