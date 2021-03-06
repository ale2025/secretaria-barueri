# Generated by Django 2.2.9 on 2020-02-03 13:44

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Acessibilidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('outros_tipos_deficiencia', models.CharField(blank=True, max_length=255, null=True, verbose_name='qual tipo?')),
                ('tipo_deficiencia', models.CharField(blank=True, choices=[('FISICA', 'Fisica'), ('AUDITIVA', 'Auditiva'), ('Visual', (('MONOCULAR', 'monocular'), ('TOTAL', 'total'), ('BAIXAVISAO', 'baixa visao'))), ('INTELECTUAL', 'Intelectual'), ('MULTIPLA', 'Multipla'), ('TEA', 'TEA'), ('TRANSTORNO MENTAL', 'Transtorno mental'), ('PSICOSOCIAL', 'Psicosocial'), ('OUTRA', 'Outra')], max_length=255, null=True, verbose_name='Qual sua deficiência ?')),
                ('cid', models.CharField(blank=True, max_length=255, null=True, verbose_name='Qual o CID ?')),
                ('protese', models.BooleanField(blank=True, choices=[(True, 'Sim'), (False, 'Não')], default=False, null=True, verbose_name='Faz uso de alguma órtese, prótese ou meios auxiliares de locomoção? (ex: cadeira de rodas, muleta, aparelho auditivo, etc')),
                ('restricao_fisica', models.BooleanField(blank=True, choices=[(True, 'Sim'), (False, 'Não')], default=False, null=True, verbose_name='Restrição para alguma atividade? Já teve adoecimento ou fastamento devido trabalho ou fora do trabalho? Acidente de trabalho anterior?')),
                ('tecnologia', models.BooleanField(choices=[(True, 'Sim'), (False, 'Não')], default=False, verbose_name='Necessita de Tecnologia Assistiva para o Trabalho? Qual?')),
                ('autonomia_transporte', models.BooleanField(choices=[(True, 'Sim'), (False, 'Não')], default=False, verbose_name='Tem autonomia / independência para transporte público?')),
                ('automovel', models.BooleanField(choices=[(True, 'Sim'), (False, 'Não')], default=False, verbose_name='Tem e faz uso de automóvel próprio?')),
                ('recursos', models.BooleanField(choices=[(True, 'Sim'), (False, 'Não')], default=False, verbose_name='Tem recursos financeiros para locomoção?')),
            ],
            options={
                'verbose_name': 'Acessibilidade',
            },
        ),
        migrations.CreateModel(
            name='PessoaFisica',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('nome', models.CharField(max_length=255, null=True, verbose_name='Nome completo:')),
                ('cpf', models.CharField(max_length=25, null=True, unique=True, verbose_name='CPF')),
                ('genero', models.CharField(choices=[('ESCOLHA O GÊNERO', 'Escolha o gênero'), ('MASCULINO', 'Masculino'), ('FEMININO', 'Feminino'), ('NÃO-BINÁRIO', 'Não-Binário'), ('OUTROS', 'Outros')], max_length=25, null=True, verbose_name='Gênero')),
                ('estado_civil', models.CharField(choices=[('ESCOLHA O ESTADO CIVIL', 'Escolha o estado Civil'), ('SOLTEIRO(A)', 'Solteiro(a)'), ('CASADO(A)', 'Casado(a)'), ('DIVORCIADO(A)', 'Divociado(a)'), ('VIÚVO(A)', 'Viúvo(a)')], max_length=255, null=True, verbose_name='Estado Civil')),
                ('data_nascimento', models.DateField(null=True, verbose_name='Data de nascimento')),
                ('telefone_fixo', models.CharField(blank=True, max_length=25, null=True, verbose_name='Telefone fixo')),
                ('celular', models.CharField(max_length=25, null=True, verbose_name='Celular')),
                ('ativo', models.BooleanField(default=True)),
                ('criado_em', models.DateField(default=django.utils.timezone.now, verbose_name='Criado em')),
                ('teste', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Pessoa Física',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='PessoaJuridica',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('nome_fantasia', models.CharField(max_length=255, null=True, verbose_name='Nome fantasia da empresa')),
                ('razao_social', models.CharField(blank=True, max_length=255, null=True, verbose_name='Razão social da empresa')),
                ('cnpj', models.CharField(blank=True, max_length=18, null=True, verbose_name='CNPJ')),
                ('contato_empresa', models.CharField(blank=True, max_length=128, null=True, verbose_name='Contato da empresa')),
                ('ramo_atividade', models.CharField(blank=True, max_length=255, null=True, verbose_name='Ramo de atividade')),
                ('numero_funcionarios', models.IntegerField(blank=True, null=True, verbose_name='Número de funcionários')),
                ('numero_pcds', models.IntegerField(blank=True, null=True, verbose_name='Número de PCDs')),
            ],
            options={
                'verbose_name': 'Pessoa Juridica',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logradouro', models.CharField(blank=True, max_length=128, null=True, verbose_name='Endereço:')),
                ('numero', models.CharField(blank=True, max_length=128, null=True, verbose_name='Número')),
                ('complemento', models.CharField(blank=True, max_length=128, null=True, verbose_name='Complemento')),
                ('cidade', models.CharField(max_length=128, verbose_name='Cidade')),
                ('estado', models.CharField(choices=[('', ''), ('AC', 'AC'), ('AL', 'AL'), ('AM', 'AM'), ('AP', 'AP'), ('BA', 'BA'), ('CE', 'CE'), ('DF', 'DF'), ('ES', 'ES'), ('GO', 'GO'), ('MA', 'MA'), ('MG', 'MG'), ('MS', 'MS'), ('MT', 'MT'), ('PA', 'PA'), ('PB', 'PB'), ('PE', 'PE'), ('PI', 'PI'), ('PR', 'PR'), ('RJ', 'RJ'), ('RN', 'RN'), ('RO', 'RO'), ('RR', 'RR'), ('RS', 'RS'), ('SC', 'SC'), ('SE', 'SE'), ('SP', 'SP'), ('TO', 'TO')], max_length=128, verbose_name='Estado')),
                ('cep', models.CharField(max_length=20, verbose_name='CEP')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Endereço',
            },
        ),
    ]
