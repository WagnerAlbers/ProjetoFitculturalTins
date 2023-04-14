from django.views.generic.base import TemplateView
from django.shortcuts import reverse, HttpResponseRedirect, render
from .forms import *
from django.views.generic import CreateView, UpdateView, FormView


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


class FinalizaFit(TemplateView):
    template_name = 'finaliza.html'


class NovoFitCult01(CreateView):
    template_name = "criarfit01.html"
    form_class = CriarFitCult01

    def get_object(self, queryset=None):
        email = self.kwargs.get('email')
        return email

    def get(self, request, *args, **kwargs):
        email = self.get_object(self)
        form = self.form_class(initial={'e_mail':email})
        return render(request, self.template_name, {'e_mail':email, 'form':form})

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        email = self.get_object(self)
        registro = Cad_colab_parte1.objects.filter(e_mail=email).first()
        codigo = registro.campo_cpf
        return reverse('candidato:criarfit02', kwargs={'cpf':codigo})


class NovoFitCult02(CreateView):
    template_name = "criarfit02.html"
    form_class = CriarFitCult02

    def get_object(self, queryset=None):
        cpf_candidato = self.kwargs.get('cpf')
        # Retorna o objeto encontrado
        return cpf_candidato

    def get(self, request, *args, **kwargs):
        cpf_candidato = self.get_object(self)
        form = self.form_class(initial={'campo_cpf': cpf_candidato})
        return render(request, self.template_name, {'cpf': cpf_candidato, 'form': form})

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        cpf_candidato = self.get_object(self)
        registro = Cad_colab_parte1.objects.filter(campo_cpf=cpf_candidato).first()
        codigo = registro.campo_cpf
        return reverse('candidato:criarfit03', kwargs={'cpf':codigo})


class NovoFitCult03(CreateView):
    template_name = "criarfit03.html"
    form_class = CriarFitCult03

    def get_object(self, queryset=None):
        cpf_candidato = self.kwargs.get('cpf')
        # Retorna o objeto encontrado
        return cpf_candidato

    def get(self, request, *args, **kwargs):
        cpf_candidato = self.get_object(self)
        form = self.form_class(initial={'campo_cpf':cpf_candidato})
        return render(request, self.template_name, {'cpf':cpf_candidato, 'form':form})

    # #94dcfa cor do fundo deta página
    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        cpf_candidato = self.get_object(self)
        registro = Cad_colab_parte1.objects.filter(campo_cpf=cpf_candidato).first()
        codigo = registro.campo_cpf
        return reverse('candidato:contpt01', kwargs={'cpf':codigo})


class ContFitCult01(CreateView):
    template_name = "contpt01.html"
    form_class = ColabDetailForm01

    def get_object(self, queryset=None):
        cpf_candidato = self.kwargs.get('cpf')
        # Retorna o objeto encontrado
        return cpf_candidato

    def get(self, request, *args, **kwargs):
        cpf_candidato = self.get_object(self)
        form = self.form_class(initial={'campo_cpf':cpf_candidato})
        return render(request, self.template_name, {'cpf':cpf_candidato, 'form':form})

    # #94dcfa cor do fundo deta página
    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        cpf_candidato = self.get_object(self)
        registro = Cad_colab_parte1.objects.filter(campo_cpf=cpf_candidato).first()
        codigo = registro.campo_cpf
        return reverse('candidato:contpt02', kwargs={'cpf':codigo})


class ContFitCult02(CreateView):
    template_name = "contpt02.html"
    form_class = ColabDetailForm02

    def get_object(self, queryset=None):
        cpf_candidato = self.kwargs.get('cpf')
        # Retorna o objeto encontrado
        return cpf_candidato

    def get(self, request, *args, **kwargs):
        cpf_candidato = self.get_object(self)
        form = self.form_class(initial={'campo_cpf':cpf_candidato})
        return render(request, self.template_name, {'cpf':cpf_candidato, 'form':form})

    # #94dcfa cor do fundo deta página
    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        cpf_candidato = self.get_object(self)
        registro = Cad_colab_parte1.objects.filter(campo_cpf=cpf_candidato).first()
        codigo = registro.campo_cpf
        return reverse('candidato:contpt03', kwargs={'cpf':codigo})


class ContFitCult03(CreateView):
    template_name = "contpt03.html"
    form_class = ColabDetailForm03

    def get_object(self, queryset=None):
        cpf_candidato = self.kwargs.get('cpf')
        # Retorna o objeto encontrado
        return cpf_candidato

    def get(self, request, *args, **kwargs):
        cpf_candidato = self.get_object(self)
        form = self.form_class(initial={'campo_cpf':cpf_candidato})
        return render(request, self.template_name, {'cpf':cpf_candidato, 'form':form})

    # #94dcfa cor do fundo deta página
    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        cpf_candidato = self.get_object(self)
        registro = Cad_colab_parte1.objects.filter(campo_cpf=cpf_candidato).first()
        codigo = registro.campo_cpf
        return reverse('candidato:contpt04', kwargs={'cpf':codigo})


class ContFitCult04(CreateView):
    template_name = "contpt04.html"
    form_class = ColabDetailForm04

    def get_object(self, queryset=None):
        cpf_candidato = self.kwargs.get('cpf')
        # Retorna o objeto encontrado
        return cpf_candidato

    def get(self, request, *args, **kwargs):
        cpf_candidato = self.get_object(self)
        form = self.form_class(initial={'campo_cpf':cpf_candidato})
        return render(request, self.template_name, {'cpf':cpf_candidato, 'form':form})

    # #94dcfa cor do fundo deta página
    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        cpf_candidato = self.get_object(self)
        registro = Cad_colab_parte1.objects.filter(campo_cpf=cpf_candidato).first()
        codigo = registro.campo_cpf
        return reverse('candidato:contpt05', kwargs={'cpf':codigo})


class ContFitCult05(CreateView):
    template_name = "contpt05.html"
    form_class = ColabDetailForm05

    def get_object(self, queryset=None):
        cpf_candidato = self.kwargs.get('cpf')
        # Retorna o objeto encontrado
        return cpf_candidato

    def get(self, request, *args, **kwargs):
        cpf_candidato = self.get_object(self)
        form = self.form_class(initial={'campo_cpf':cpf_candidato})
        return render(request, self.template_name, {'cpf':cpf_candidato, 'form':form})

    # #94dcfa cor do fundo deta página
    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        cpf_candidato = self.get_object(self)
        registro = Cad_colab_parte1.objects.filter(campo_cpf=cpf_candidato).first()
        codigo = registro.campo_cpf
        return reverse('candidato:contpt06', kwargs={'cpf':codigo})


class ContFitCult06(CreateView):
    template_name = "contpt06.html"
    form_class = ColabDetailForm06

    def get_object(self, queryset=None):
        cpf_candidato = self.kwargs.get('cpf')
        # Retorna o objeto encontrado
        return cpf_candidato

    def get(self, request, *args, **kwargs):
        cpf_candidato = self.get_object(self)
        form = self.form_class(initial={'campo_cpf':cpf_candidato})
        return render(request, self.template_name, {'cpf':cpf_candidato, 'form':form})

    # #94dcfa cor do fundo deta página
    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        cpf_candidato = self.get_object(self)
        registro = Cad_colab_parte1.objects.filter(campo_cpf=cpf_candidato).first()
        codigo = registro.campo_cpf
        return reverse('candidato:contpt07', kwargs={'cpf':codigo})


class ContFitCult07(CreateView):
    template_name = "contpt07.html"
    form_class = ColabDetailForm07

    def get_object(self, queryset=None):
        cpf_candidato = self.kwargs.get('cpf')
        # Retorna o objeto encontrado
        return cpf_candidato

    def get(self, request, *args, **kwargs):
        cpf_candidato = self.get_object(self)
        form = self.form_class(initial={'campo_cpf':cpf_candidato})
        return render(request, self.template_name, {'cpf':cpf_candidato, 'form':form})

    # #94dcfa cor do fundo deta página
    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        cpf_candidato = self.get_object(self)
        registro = Cad_colab_parte1.objects.filter(campo_cpf=cpf_candidato).first()
        codigo = registro.campo_cpf
        return reverse('candidato:contpt08', kwargs={'cpf':codigo})


class ContFitCult08(CreateView):
    template_name = "contpt08.html"
    form_class = ColabDetailForm08

    def get_object(self, queryset=None):
        cpf_candidato = self.kwargs.get('cpf')
        # Retorna o objeto encontrado
        return cpf_candidato

    def get(self, request, *args, **kwargs):
        cpf_candidato = self.get_object(self)
        form = self.form_class(initial={'campo_cpf':cpf_candidato})
        return render(request, self.template_name, {'cpf':cpf_candidato, 'form':form})

    # #94dcfa cor do fundo deta página
    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        cpf_candidato = self.get_object(self)
        registro = Cad_colab_parte1.objects.filter(campo_cpf=cpf_candidato).first()
        codigo = registro.campo_cpf
        return reverse('candidato:contpt09', kwargs={'cpf':codigo})


class ContFitCult09(CreateView):
    template_name = "contpt09.html"
    form_class = ColabDetailForm09

    def get_object(self, queryset=None):
        cpf_candidato = self.kwargs.get('cpf')
        # Retorna o objeto encontrado
        return cpf_candidato

    def get(self, request, *args, **kwargs):
        cpf_candidato = self.get_object(self)
        form = self.form_class(initial={'campo_cpf':cpf_candidato})
        return render(request, self.template_name, {'cpf':cpf_candidato, 'form':form})

    # #94dcfa cor do fundo deta página
    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        cpf_candidato = self.get_object(self)
        registro = Cad_colab_parte1.objects.filter(campo_cpf=cpf_candidato).first()
        codigo = registro.campo_cpf
        return reverse('candidato:contpt10', kwargs={'cpf':codigo})


class ContFitCult10(CreateView):
    template_name = "contpt10.html"
    form_class = ColabDetailForm10

    def get_object(self, queryset=None):
        cpf_candidato = self.kwargs.get('cpf')
        # Retorna o objeto encontrado
        return cpf_candidato

    def get(self, request, *args, **kwargs):
        cpf_candidato = self.get_object(self)
        form = self.form_class(initial={'campo_cpf':cpf_candidato})
        return render(request, self.template_name, {'cpf':cpf_candidato, 'form':form})

    # #94dcfa cor do fundo deta página
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


class NovoFitCult01Edita(UpdateView):
    template_name = "criarfit01edita.html"
    model = Cad_colab_parte1
    form_class = CriarFitCult01
    context_object_name = 'candidatofit'

    def get_object(self, queryset=None):
        candidatofit = None
        cpf_candidato = self.kwargs.get('cpf')
        if cpf_candidato:
            candidatofit = Cad_colab_parte1.objects.filter(campo_cpf=cpf_candidato).first()

        # Retorna o objeto encontrado
        return candidatofit

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        candidato = self.get_object(self)
        cpf_candidato = candidato.campo_cpf
        return reverse('candidato:criarfit02', kwargs={'cpf':cpf_candidato})


class NovoFitCult02Edita(UpdateView):
    template_name = "criarfit02edita.html"
    model = Cad_colab_parte2
    form_class = CriarFitCult02
    context_object_name = 'candidatofit'

    def get_object(self, queryset=None):
        candidatofit = None
        cpf_candidato = self.kwargs.get('cpf')
        if cpf_candidato:
            candidatofit = Cad_colab_parte2.objects.filter(campo_cpf=cpf_candidato).first()

        # Retorna o objeto encontrado
        return candidatofit

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        candidato = self.get_object(self)
        cpf_candidato = candidato.campo_cpf
        return reverse('candidato:criarfit03', kwargs={'cpf':cpf_candidato})


class NovoFitCult03Edita(UpdateView):
    template_name = "criarfit03edita.html"
    model = Cad_colab_parte3
    form_class = CriarFitCult03
    context_object_name = 'candidatofit'

    def get_object(self, queryset=None):
        candidatofit = None
        cpf_candidato = self.kwargs.get('cpf')
        if cpf_candidato:
            candidatofit = Cad_colab_parte3.objects.filter(campo_cpf=cpf_candidato).first()

        # Retorna o objeto encontrado
        return candidatofit

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        candidato = self.get_object(self)
        cpf_candidato = candidato.campo_cpf
        return reverse('candidato:contpt01', kwargs={'cpf':cpf_candidato})