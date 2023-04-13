from django.db import models
from django.utils import timezone

# Create your models here.
FUNCAO_COLAB = (
    ("ANALISTAPROGRAMADOR", "Analista/Programador"),
    ("ARQUIVISTADOCTOS", "Arquivista de Documentos"),
    ("ARQUIVISTA", "Arquivista"),
    ("ADMINISTRATIVO", "Administrativo"),
    ("ASG", "Auxíliar de Serviços Gerais"),
    ("CONSULTOR", "Consultor de vendas"),
    ("ADMINISTRADORBD", "Administrador de Banco de Dados"),
    ("FINANCEIRO", "Financeiro"),
    ("GERENTE", "Gerente Comercial"),
    ("GERENTEPROJETOS", "Gerente de Projetos"),
    ("SUPORTE", "Suporte de TI"),
    ("CENTROARMAZENA", "Centro de Armazenamento"),
    ("MRKETING", "Marketing"),
)

ESTADO_CIVIL = (
    ("SOLTEIRO", "Solteira(o)"),
    ("CASADO", "Casada(o)"),
    ("SEPARADO", "Separada(o)"),
    ("DESQUITADO", "Desquitada(o)"),
    ("VIUVO", "Viuva(o)"),
    ("OUTROS", "Outras(os)"),
)

POSSUI_FILHOS = (
    ("SIM", "Sim"),
    ("NAO", "Não"),
)

OPCOES_DIVERSAS = (
    ("RUIM", "Ruim"),
    ("REGULAR", "Regular"),
    ("BOM", "Bom"),
    ("OTIMA", "Ótima"),
)

GRAU_ESCOLAR = (
    ("FUNDAMENTAL", "Fundamental"),
    ("MEDIO", "Médio"),
    ("SUPERIOR", "Superior"),
    ("ESPECIALIZACAO", "Especialização"),
    ("MESTRADO", "Mestrado"),
    ("POSMESTRADO", "Pós Mestrado"),
    ("DOUTORADO", "Doutorado"),
    ("POSDOUTORADO", "Pós Doutorado"),
)

# Criar a tabela principal


class Cad_colab_parte1(models.Model):
    """ Uma típica classe definindo um modelo, deriva da classe Model."""
    codigo_id = models.AutoField(primary_key=True)
    campo_cpf = models.CharField(unique=True, max_length=14, verbose_name='CPF', help_text='Digite o CPF, só é aceito CPF válido!')
    nome_candidato = models.CharField(max_length=60, verbose_name='Nome', null=True, help_text='Preencha o nome completo')
    e_mail = models.EmailField(max_length=200, verbose_name='E-Mail', help_text='Preencha seu E-Mail')
    funcao_candidato = models.CharField(max_length=20, verbose_name='Função', choices=FUNCAO_COLAB, help_text='Função do candidato')
    cep_candidato = models.CharField(max_length=10, verbose_name='Cep', help_text='Digite o Cep. Precisa ser válido!')
    endereco_candidato = models.CharField(max_length=50, verbose_name='Preencha o endereço', help_text='Preencha com o endereço completo')
    bairro_candidato = models.CharField(max_length=40, verbose_name='Preencha com o bairro', help_text='Bairro onde reside')
    cidade_candidato = models.CharField(max_length=40, verbose_name='Nome da cidade', help_text='Cidade onde o candidato reside')
    uf_candidato = models.CharField(max_length=2, verbose_name='Estado', help_text='Estado onde reside')
    data_cadastro = models.DateTimeField(verbose_name='Data de cadastro', auto_now=True)
    ultima_altera = models.DateTimeField(verbose_name='Data da última alteração', auto_now=True)

    # metadados
    class Meta:
        ordering = ['-nome_candidato']

    def __str__(self):
        return self.nome_candidato


class Cad_colab_parte2(models.Model):
    codigo_id = models.AutoField(primary_key=True)
    campo_cpf = models.CharField(unique=True, max_length=14, verbose_name='CPF', help_text='Digite o CPF, só é aceito CPF válido!')
    naturalidade_candidato = models.CharField(max_length=60, verbose_name='Naturalidade', help_text='Cidade onde nasceu')
    data_nascimento = models.DateField(default=timezone.now)
    estado_civil = models.CharField(max_length=10, verbose_name='Estado Civil', choices=ESTADO_CIVIL, help_text='Estado civil do candidato')
    possui_filhos = models.CharField(max_length=3, verbose_name='Possui Filhos', choices=POSSUI_FILHOS, help_text='Possui Filhos Sim/Não?')
    quantos_filhos = models.IntegerField(default=0, blank=True, verbose_name='Quantidade de Filhos', help_text='Digite a quantidade de filhos')
    grau_escolar = models.CharField(max_length=15, verbose_name='Grau Escolar', choices=GRAU_ESCOLAR, help_text='Digite o grau máximo que estudou')
    curso_academico = models.CharField(max_length=50, blank=True, verbose_name='Curso Acadêmico', help_text='Último curso acadêmico realizado')
    periodo_curso = models.CharField(max_length=15, blank=True, verbose_name='Período', help_text='Se ainda cursa, em qual período se encontra.')
    faculdade_curso = models.CharField(max_length=40, blank=True, verbose_name='Faculdade', help_text='Qual a faculdade em que cursa?')
    data_cadastro = models.DateTimeField(verbose_name='Data de cadastro', auto_now=True)

    def __str__(self):
        return self.campo_cpf


class Cad_colab_parte3(models.Model):
    codigo_id = models.AutoField(primary_key=True)
    campo_cpf = models.CharField(unique=True, max_length=14, verbose_name='CPF', help_text='Digite o CPF, só é aceito CPF válido!')
    pai_candidato = models.CharField(max_length=60, blank=True, verbose_name='Nome do Pai', help_text='Nome do pai da candidato')
    mae_candidato = models.CharField(max_length=60, verbose_name='Nome da Mãe', help_text='Nome da Mãe da candidato')
    telefone_residencia = models.CharField(max_length=14, blank=True, verbose_name='Telefone Residencial', help_text='Telefone residencial')
    celular_candidato = models.CharField(max_length=14, verbose_name='Telefone Celular', help_text='Telefone celular')
    instagram_candidato = models.CharField(max_length=45, blank=True, verbose_name='Qual o seu instagram', help_text='Digite o endereço do Instagram')
    foto_candidato = models.ImageField(upload_to='pictures', blank=True, verbose_name='Foto do candidato', help_text='Anexar uma foto que esteja com boa qualidade')
    data_cadastro = models.DateTimeField(verbose_name='Data de cadastro', auto_now=True)

    def __str__(self):
        return self.campo_cpf

# criar o questionário


class Questoes_parte1(models.Model):
    codigo_id = models.AutoField(primary_key=True)
    campo_cpf = models.CharField(unique=True, max_length=14, verbose_name='CPF', help_text='Digite o CPF, só é aceito CPF válido!')
    ficou_sabendo = models.CharField(max_length=90, verbose_name='Como ficou sabendo', null=True, help_text='Como ficou sabendo da vaga?')
    objetivo = models.CharField(max_length=200, verbose_name='Seu Objetivo', help_text='Qual seu objetivo na TINS, em que área pretende atuar?')
    como_conheceu = models.CharField(max_length=100, verbose_name='O que sabe sobre a TINS', help_text='O que você sabe sobre a TINS?')
    candidato_why = models.CharField(max_length=100, verbose_name='Candidato Porque?',
                          help_text='Porque se candidatou para esta oportunidade? O que chamou sua atenção na TINS?')
    sucesso_prof = models.TextField(max_length=200, verbose_name='Sucesso profissional', help_text='O que é sucesso PROFISSIONAL pra você?')
    mundo_tins = models.TextField(max_length=250, verbose_name='Podemos lhe agregar valor profissional?',
                          help_text='Você vê a TINS como uma empresa que pode lhe agregar valor profissional, pretende investir no mundo TINS? Em que área gostaria de crescer?')
    data_cadastro = models.DateTimeField(verbose_name='Data de cadastro', auto_now=True)

    def __str__(self):
        return self.campo_cpf


class Questoes_parte2(models.Model):
    codigo_id = models.AutoField(primary_key=True)
    campo_cpf = models.CharField(unique=True, max_length=14, verbose_name='CPF', help_text='Digite o CPF, só é aceito CPF válido!')
    digitacao = models.CharField(max_length=7, choices=OPCOES_DIVERSAS, verbose_name='Digitação', help_text='Selecione uma opção')
    software = models.CharField(max_length=7, choices=OPCOES_DIVERSAS, verbose_name='Softwares em geral', help_text='Selecione uma opção')
    hardware = models.CharField(max_length=7, choices=OPCOES_DIVERSAS, verbose_name='Hardware em geral', help_text='Selecione uma opção')
    internet = models.CharField(max_length=7, choices=OPCOES_DIVERSAS, verbose_name='Internet em geral', help_text='Selecione uma opção')
    curso_extra = models.TextField(max_length=199, verbose_name='Cursos extracurriculares',
                         help_text='Liste os seus cursos extracurriculares, um em cada linha não esquecendo de informar a cidade.')
    trabalho_anterior = models.TextField(max_length=200, verbose_name='Trabalhos anteriores.',
                         help_text='Nesta seção, informe a (s) empresa (s), função (ões), contato (s), telefone (s), período (s) e o motivo (s) da saída (Pré-requisito para processo de seleção).')
    pret_salarial = models.TextField(max_length=200, verbose_name='Pretensão salarial',
                         help_text='Qual a sua pretensão salarial hoje? E qual a sua pretensão salarial em 5 anos? e o que você fará pra alcançar esse objetivo?')
    data_cadastro = models.DateTimeField(verbose_name='Data de cadastro', auto_now=True)

    def __str__(self):
        return self.campo_cpf


class Questoes_parte3(models.Model):
    codigo_id = models.AutoField(primary_key=True)
    campo_cpf = models.CharField(unique=True, max_length=14, verbose_name='CPF', help_text='Digite o CPF, só é aceito CPF válido!')
    mark_digital = models.TextField(max_length=200, verbose_name='Fale sobre Marketing Digital',
                         help_text='O quanto você entende sobre Marketing Digital? Caso entenda, nos conte o que você entende.')
    auxilio_governo = models.CharField(max_length=45, verbose_name='Benefício ou Auxílio.',
                         help_text='Você tem algum benefício ou auxilio do governo Federal? (vale gas, bolsa familia, prouni...) Qual?')
    disponivel_viagem = models.CharField(max_length=3, verbose_name='Disponível para viagens?', choices=POSSUI_FILHOS,
                         help_text='Escolha uma opção')
    Notebook_disponivel = models.CharField(max_length=3, verbose_name='Tem Notebook', choices=POSSUI_FILHOS,
                         help_text='Escolha uma opção')
    descreva_lider = models.TextField(max_length=200, verbose_name='Descreva-me um chefe ou líder ideal.')
    diferencial = models.TextField(max_length=150, verbose_name='Qual o seu maior deferencial?',
                         help_text='O que lhe faz se destacar em relação aos outros candidatos?')
    data_cadastro = models.DateTimeField(verbose_name='Data de cadastro', auto_now=True)

    def __str__(self):
        return self.campo_cpf


class Questoes_parte4(models.Model):
    codigo_id = models.AutoField(primary_key=True)
    campo_cpf = models.CharField(unique=True, max_length=14, verbose_name='CPF', help_text='Digite o CPF, só é aceito CPF válido!')
    religiao = models.CharField(max_length=40, verbose_name='Qual a sua religião?')
    praticante = models.CharField(max_length=3, verbose_name='É Praticante?', choices=POSSUI_FILHOS,
                      help_text='Escolha uma opção')
    quem_deus = models.TextField(max_length=200, verbose_name='Quem é Deus pra você?',
                      help_text='O que Deus representa na sua vida?')
    residente = models.CharField(max_length=10, verbose_name='Ha quanto tempo reside em Palmas?')
    possui_cnh = models.CharField(max_length=3, verbose_name='Possui CNH', choices=POSSUI_FILHOS,
                      help_text='Escolha uma opção')
    categoria_cnh = models.CharField(max_length=10, verbose_name='Se possui, qual a categoria da CNH?')
    possui_veiculo = models.CharField(max_length=3, verbose_name='Possui Veículos', choices=POSSUI_FILHOS,
                      help_text='Escolha uma opção')
    qual_veiculo = models.CharField(max_length=30, verbose_name='Se sim, qual veículo?')
    data_cadastro = models.DateTimeField(verbose_name='Data de cadastro', auto_now=True)

    def __str__(self):
        return self.campo_cpf


class Questoes_parte5(models.Model):
    codigo_id = models.AutoField(primary_key=True)
    campo_cpf = models.CharField(unique=True, max_length=14, verbose_name='CPF', help_text='Digite o CPF, só é aceito CPF válido!')
    possui_vicios = models.CharField(max_length=3, verbose_name='Possui Vícios (bebidas/cigarro)?', choices=POSSUI_FILHOS,
                              help_text='Escolha uma opção')
    qual_vicio = models.CharField(max_length=40, verbose_name='Se sim, qual(is)?')
    Faz_no_lazer = models.CharField(max_length=50, verbose_name='O que gostas de fazer nos momentos de lazer?')
    alergias = models.CharField(max_length=3, verbose_name='Possui alergia a pó, ácaros ou outros fungos?',
                                choices=POSSUI_FILHOS, help_text='Escolha uma opção')
    qual_alergia = models.CharField(max_length=50, verbose_name='Se sim, qual?')
    planejamento_pessoal = models.TextField(max_length=200, verbose_name='Você faz planejamento pessoal e profissional?',
                                help_text='Como você se vê daqui 5 anos e o que está fazendo para que isso se torne realidade?')
    sua_imagem = models.TextField(max_length=100, verbose_name='Que imagem você tem a seu respeito?')
    data_cadastro = models.DateTimeField(verbose_name='Data de cadastro', auto_now=True)

    def __str__(self):
        return self.campo_cpf


class Questoes_parte6(models.Model):
    codigo_id = models.AutoField(primary_key=True)
    campo_cpf = models.CharField(unique=True, max_length=14, verbose_name='CPF', help_text='Digite o CPF, só é aceito CPF válido!')
    fazer_bem = models.TextField(max_length=150, verbose_name='O que você acredita fazer muito bem ?')
    dificu_enfrentou = models.TextField(max_length=200, verbose_name='Que tipo de dificuldade já enfrentou ou está enfrentando?')
    sua_saude = models.CharField(max_length=85, verbose_name='Como está sua saúde? Faz uso rotineiro de medicamento?')
    melhor_filme = models.CharField(max_length=60, verbose_name='Qual melhor filme que já assistiu?')
    livro_import = models.CharField(max_length=60, verbose_name='Qual o título do livro mais importante que já leu?')
    esporte_favorito = models.CharField(max_length=40, verbose_name='Qual seu esporte preferido?')
    cor_preferida = models.CharField(max_length=15, verbose_name='Qual sua cor favorita?')
    musica_preferida = models.CharField(max_length=30, verbose_name='Qual o tipo de música de sua preferência?')
    data_cadastro = models.DateTimeField(verbose_name='Data de cadastro', auto_now=True)

    def __str__(self):
        return self.campo_cpf


class Questoes_parte7(models.Model):
    codigo_id = models.AutoField(primary_key=True)
    campo_cpf = models.CharField(unique=True, max_length=14, verbose_name='CPF', help_text='Digite o CPF, só é aceito CPF válido!')
    acontece = models.CharField(max_length=60, verbose_name='Cite um acontecimento que lhe trouxe muita emoção.')
    sua_forca = models.TextField(max_length=100, verbose_name='Qual sua maior força?')
    sua_capacidade = models.TextField(max_length=100, verbose_name='Qual sua maior capacidade?')
    maior_erro = models.TextField(max_length=100, verbose_name='Qual seu maior erro?')
    maior_realiza = models.TextField(max_length=150, verbose_name='Qual sua maior realização?')
    se_morrer = models.CharField(max_length=70, verbose_name='Se você morresse hoje, o que as pessoas que te conhecem diriam a seu respeito?')
    pessoa_identif = models.CharField(max_length=80, verbose_name='Com que pessoa você se identifica na sua família? Porque?')
    tipo_droga = models.CharField(max_length=50, verbose_name='Que tipo de droga lícita usa ou já usou? Em que época de sua vida isso aconteceu?')
    data_cadastro = models.DateTimeField(verbose_name='Data de cadastro', auto_now=True)

    def __str__(self):
        return self.campo_cpf


class Questoes_parte8(models.Model):
    codigo_id = models.AutoField(primary_key=True)
    campo_cpf = models.CharField(unique=True, max_length=14, verbose_name='CPF', help_text='Digite o CPF, só é aceito CPF válido!')
    resolve_problema = models.TextField(max_length=150, verbose_name='Quando lhe ocorre um problema, qual sua reação diante dele? O que faz pra resolvê-lo?')
    trab_equipe = models.TextField(max_length=150, verbose_name='Você prefere trabalhar individualmente ou em equipe? Justifique.')
    nervoso = models.TextField(max_length=150, verbose_name='O que te deixa ou te faz ficar nervoso?')
    tres_comporta = models.TextField(max_length=150, verbose_name='Cite três comportamentos que você não suporta nas pessoas.')
    erro_trabalho = models.TextField(max_length=150, verbose_name='Quando você comete algum erro no trabalho, qual sua reação?')
    bebado_reage = models.CharField(max_length=85, verbose_name='Quando você fica bêbado, qual sua reação?')
    honestidade = models.TextField(max_length=100, verbose_name='Sua opinião. Disserte livremente sobre Honestidade')
    lealdade = models.TextField(max_length=100, verbose_name='Sua opinião. Disserte livremente sobre Lealdade')
    data_cadastro = models.DateTimeField(verbose_name='Data de cadastro', auto_now=True)

    def __str__(self):
        return self.campo_cpf


class Questoes_parte9(models.Model):
    codigo_id = models.AutoField(primary_key=True)
    campo_cpf = models.CharField(unique=True, max_length=14, verbose_name='CPF', help_text='Digite o CPF, só é aceito CPF válido!')
    trabalho = models.TextField(max_length=100, verbose_name='Sua opinião. Disserte livremente sobre Trabalho')
    religiao_importa = models.TextField(max_length=100, verbose_name='Sua opinião. Disserte livremente sobre Religião.')
    contrato_pj = models.CharField(max_length=50, verbose_name='Caso você seja selecionado, teria interesse em ser contratado como Pessoa Jurídica?')
    cnpj_ativo = models.CharField(max_length=3, verbose_name='Se sua resposta foi sim, você possui CNPJ ativo?', choices=POSSUI_FILHOS, help_text='Escolha uma opção...')
    abrir_cnpj = models.CharField(max_length=3, verbose_name='Se sua resposta foi NÃO, estaria disposto a criar CNPJ (MEI)? Para viabilizar sua contratação?', choices=POSSUI_FILHOS, help_text='Escolha uma opção...')
    pontos_fortes = models.TextField(max_length=160, verbose_name='Liste pelo o menos 5 (cinco) pontos FORTES que consideras mais importante em você:')
    pontos_fracos = models.TextField(max_length=150, verbose_name='Liste pelo o menos 5 (cinco) pontos FRACOS que consideras mais marcantes em você:')
    texto_sobre_vc = models.TextField(max_length=200, verbose_name='Escreva um texto com pelo menos 100 caracteres falando um pouco mais sobre você:')
    data_cadastro = models.DateTimeField(verbose_name='Data de cadastro', auto_now=True)

    def __str__(self):
        return self.campo_cpf


class Questoes_parte10(models.Model):
    codigo_id = models.AutoField(primary_key=True)
    campo_cpf = models.CharField(unique=True, max_length=14, verbose_name='CPF', help_text='Digite o CPF, só é aceito CPF válido!')
    busca_informacoes = models.TextField(max_length=200, verbose_name='Nos dias de hoje, como e onde você geralmente busca conhecimento e informação?')
    aprende_rapido = models.TextField(max_length=200, verbose_name='O quanto você considera que aprende rápido?',
                           help_text='Conte-nos uma situação na qual você vivenciou isso. Seu aprendizado e o resultado após isso:')
    exec_tarefa = models.TextField(max_length=199, verbose_name='Você foi escolhido para executar uma tarefa que você nunca fez antes na vida. Qual seu primeiro instinto? Como você reage nesta situação?')
    feed_melhor = models.TextField(max_length=200, verbose_name='Você já recebeu algum feedback de MELHORIA? Se sim, qual foi ele?')
    reacao_feed = models.TextField(max_length=200, verbose_name='Após recebê-lo, qual foi sua reação, o que fez para mudar a situação e quais foram os resultados dessas atitudes na prática?')
    melhor_amigo = models.TextField(max_length=200, verbose_name='Pense no seu melhor amigo, e imagine a seguinte situação: ele está roubando a empresa há 3 meses sem ninguém saber. Quais seriam as atitudes propostas e realizadas por você? E por que você acredita que esse seria o melhor caminho?')
    precisou_aprender = models.TextField(max_length=200, verbose_name='Houve alguma situação na qual você precisasse de algum aprendizado, ou informação, e isso estava comprometendo seu trabalho ou sua atividade? Conte-nos uma situação na qual você vivenciou isso, e quais foram as atitudes propostas e realizadas por você para virar esse jogo?')
    maior_orgulho = models.TextField(max_length=200, verbose_name='Do que mais se orgulha, qual sua maior vitória hoje? O que você precisou fazer até atingí-la e por quê o fez?')
    data_cadastro = models.DateTimeField(verbose_name='Data de cadastro', auto_now=True)

    def __str__(self):
        return self.campo_cpf


