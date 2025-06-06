from django.views.generic import TemplateView
from .models import Exposicao

class ExposicoesView(TemplateView):
    template_name = "ccmtj/exposicoes.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        exposicoes = Exposicao.objects.all()

        context['exposicoes'] = exposicoes
        context['fotos'] = [
            exposicao.imagem.url for exposicao in exposicoes if exposicao.media_type == 'image' and exposicao.imagem
        ]

        context['videos'] = [
            exposicao.video_url for exposicao in exposicoes if exposicao.media_type == 'video' and exposicao.video_url
        ]
        return context
