from django.views.generic.base import TemplateView
from django.shortcuts import reverse, HttpResponseRedirect, render
from .forms import *
from django.views.generic import CreateView, UpdateView, FormView
from slug import slug


class HomeView(FormView):
    template_name = "homepage.html"
    form_class = FormHomePage

    def get_success_url(self):
        email = self.request.POST.get("email")
        colaborador = Cad_colab_parte1.objects.filter(e_mail=email)
        if colaborador:
            # passar o processo para login, exigir e-mail novamente e cpf
            # para confirmar usuario
            return reverse('candidato:apresenta')
        else:
            return reverse('candidato:criarfit01', kwargs={'email':email})


class ApresentaTins(TemplateView):
    template_name = 'apresenta.html'


class FinalizaFit(CreateView):
    template_name = 'finaliza.html'


class NovoFitCult01(CreateView):
    template_name = "criarfit01.html"
    form_class = CriarFitCult01

    def get_slug_field(self):
        """Get the name of a slug field to be used to look up by slug."""
        return self.slug_field

    def get_object(self, queryset=None):
        slug = self.kwargs.get(self.slug_url_kwarg)
        if slug is not None:
            # Pega o campo slug do Model
            campo_slug = self.get_slug_field()
        else:
            campo_slug=None
        return campo_slug

    def get(self, request, *args, **kwargs):
        email = NovoFitCult01.get_object(self)
        print(email)
        form = self.form_class(initial={'e_mail':email})
        return render(request, self.template_name, {'e_mail':email, 'form':form})

    # #94dcfa cor do fundo deta página
    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        cpf_candidato = NovoFitCult01.get_slug_field(self)
        return reverse('candidato:criarfit02', kwargs={'email':email})


class NovoFitCult02(CreateView):
    template_name = "criarfit02.html"
    form_class = CriarFitCult02

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('candidato:criarfit03')


class NovoFitCult03(CreateView):
    template_name = "criarfit03.html"
    form_class = CriarFitCult03

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('candidato:contpt01')


class ContFitCult01(CreateView):
    template_name = "contpt01.html"
    form_class = ColabDetailForm01

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('candidato:contpt02')


class ContFitCult02(CreateView):
    template_name = "contpt02.html"
    form_class = ColabDetailForm02

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('candidato:contpt03')


class ContFitCult03(CreateView):
    template_name = "contpt03.html"
    form_class = ColabDetailForm03

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('candidato:contpt04')


class ContFitCult04(CreateView):
    template_name = "contpt04.html"
    form_class = ColabDetailForm04

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('candidato:contpt05')


class ContFitCult05(CreateView):
    template_name = "contpt05.html"
    form_class = ColabDetailForm05

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('candidato:contpt06')


class ContFitCult06(CreateView):
    template_name = "contpt06.html"
    form_class = ColabDetailForm06

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('candidato:contpt07')


class ContFitCult07(CreateView):
    template_name = "contpt07.html"
    form_class = ColabDetailForm07

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('candidato:contpt08')


class ContFitCult08(CreateView):
    template_name = "contpt08.html"
    form_class = ColabDetailForm08

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('candidato:contpt09')


class ContFitCult09(CreateView):
    template_name = "contpt09.html"
    form_class = ColabDetailForm09

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('candidato:contpt10')


class ContFitCult10(CreateView):
    template_name = "contpt10.html"
    form_class = ColabDetailForm10

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('candidato:finaliza')


class AlteraFitCult01(UpdateView):
    template_name = "criarfit01.html"
    form_class = CriarFitCult01

    # #94dcfa cor do fundo deta página
    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('candidato:criarfit02')
