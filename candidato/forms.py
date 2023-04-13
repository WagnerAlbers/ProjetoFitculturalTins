from django import forms
from candidato.models import *


class FormHomePage(forms.Form):
    email = forms.EmailField(label=False)


class ColabDetailForm01(forms.ModelForm):
    class Meta:
        model = Questoes_parte1
        fields = ("campo_cpf", "ficou_sabendo", "objetivo", "como_conheceu", "candidato_why", "sucesso_prof",
                  "mundo_tins")

        exclude = ("codigo_id", "data_cadastro")
        widgets = {
            'campo_cpf':forms.TextInput(attrs={'readonly': 'readonly'})
        }


class ColabDetailForm02(forms.ModelForm):
    class Meta:
        model = Questoes_parte2
        fields = ("campo_cpf", "digitacao", "software", "hardware", "internet", "curso_extra", "trabalho_anterior",
                  "pret_salarial")

        exclude = ("codigo_id", "data_cadastro")
        widgets = {
            'campo_cpf':forms.TextInput(attrs={'readonly': 'readonly'})
        }


class ColabDetailForm03(forms.ModelForm):
    class Meta:
        model = Questoes_parte3
        fields = ("campo_cpf", "mark_digital", "auxilio_governo", "disponivel_viagem", "Notebook_disponivel",
                  "descreva_lider", "diferencial")

        exclude = ("codigo_id", "data_cadastro")
        widgets = {
            'campo_cpf':forms.TextInput(attrs={'readonly': 'readonly'})
        }


class ColabDetailForm04(forms.ModelForm):
    class Meta:
        model = Questoes_parte4
        fields = ("campo_cpf", "religiao", "praticante", "quem_deus", "residente", "possui_cnh", "categoria_cnh",
                  "possui_veiculo", "qual_veiculo")

        exclude = ("codigo_id", "data_cadastro")
        widgets = {
            'campo_cpf':forms.TextInput(attrs={'readonly': 'readonly'})
        }


class ColabDetailForm05(forms.ModelForm):
    class Meta:
        model = Questoes_parte5
        fields = ("campo_cpf", "possui_vicios", "qual_vicio", "Faz_no_lazer", "alergias", "qual_alergia",
                  "planejamento_pessoal", "sua_imagem")

        exclude = ("codigo_id", "data_cadastro")
        widgets = {
            'campo_cpf':
                forms.TextInput(attrs={'readonly': 'readonly'})
        }


class ColabDetailForm06(forms.ModelForm):
    class Meta:
        model = Questoes_parte6
        fields = ("campo_cpf", "fazer_bem", "dificu_enfrentou", "sua_saude", "melhor_filme", "livro_import",
                  "esporte_favorito", "cor_preferida", "musica_preferida")

        exclude = ("codigo_id", "data_cadastro")
        widgets = {
            'campo_cpf':
                forms.TextInput(attrs={'readonly': 'readonly'})
        }


class ColabDetailForm07(forms.ModelForm):
    class Meta:
        model = Questoes_parte7
        fields = ("campo_cpf", "acontece", "sua_forca", "sua_capacidade", "maior_erro", "maior_realiza",
                  "se_morrer", "pessoa_identif", "tipo_droga")

        exclude = ("codigo_id", "data_cadastro")
        widgets = {
            'campo_cpf':
                forms.TextInput(attrs={'readonly': 'readonly'})
        }


class ColabDetailForm08(forms.ModelForm):
    class Meta:
        model = Questoes_parte8
        fields = ("campo_cpf", "resolve_problema", "trab_equipe", "nervoso", "tres_comporta", "erro_trabalho",
                  "bebado_reage", "honestidade", "lealdade")

        exclude = ("codigo_id", "data_cadastro")
        widgets = {
            'campo_cpf':
                forms.TextInput(attrs={'readonly': 'readonly'})
        }

class ColabDetailForm09(forms.ModelForm):
    class Meta:
        model = Questoes_parte9
        fields = ("campo_cpf", "trabalho", "religiao_importa", "contrato_pj", "cnpj_ativo", "abrir_cnpj", "pontos_fortes",
                  "pontos_fracos", "texto_sobre_vc")

        exclude = ("codigo_id", "data_cadastro")
        widgets = {
            'campo_cpf':
                forms.TextInput(attrs={'readonly': 'readonly'})
        }


class ColabDetailForm10(forms.ModelForm):
    class Meta:
        model = Questoes_parte10
        fields = ("campo_cpf", "busca_informacoes", "aprende_rapido", "exec_tarefa", "feed_melhor", "reacao_feed",
                  "melhor_amigo", "precisou_aprender", "maior_orgulho")

        exclude = ("codigo_id", "data_cadastro")
        widgets = {
            'campo_cpf':
                forms.TextInput(attrs={'readonly': 'readonly'})
        }


class CriarFitCult01(forms.ModelForm):
    class Meta:
        model = Cad_colab_parte1
        fields = ("campo_cpf", "nome_candidato", "e_mail", "funcao_candidato", "cep_candidato",
                  "endereco_candidato", "bairro_candidato", "cidade_candidato", "uf_candidato")

        exclude = ("codigo_id", "data_cadastro", "ultima_altera")
        widgets = {
            'e_mail':
                forms.TextInput(attrs={'readonly': 'readonly'})
        }


class CriarFitCult02(forms.ModelForm):
    class Meta:
        model = Cad_colab_parte2
        fields = ("campo_cpf", "naturalidade_candidato", "data_nascimento", "estado_civil", "possui_filhos",
                  "quantos_filhos", "grau_escolar", "curso_academico", "periodo_curso", "faculdade_curso")

        exclude = ("codigo_id", "data_cadastro")
        widgets = {
            'campo_cpf':
            forms.TextInput(attrs={'readonly': 'readonly'})
        }


class CriarFitCult03(forms.ModelForm):
    class Meta:
        model = Cad_colab_parte3
        fields = ("campo_cpf", "pai_candidato", "mae_candidato", "telefone_residencia", "celular_candidato",
                  "instagram_candidato", "foto_candidato")

        exclude = ("codigo_id", "data_cadastro")
        widgets = {
            'campo_cpf':
            forms.TextInput(attrs={'readonly': 'readonly'})
        }