from django.contrib import admin
from .models import SinalDePontuacao, EstruturaSintatica, MapeamentoFuncao


@admin.register(SinalDePontuacao)
class SinalDePontuacaoAdmin(admin.ModelAdmin):
    list_display = ('sinal_grafico', 'nome', 'descricao')
    search_fields = ('nome', 'sinal_grafico')


@admin.register(EstruturaSintatica)
class EstruturaSintaticaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')
    search_fields = ('nome',)


@admin.register(MapeamentoFuncao)
class MapeamentoFuncaoAdmin(admin.ModelAdmin):
    list_display = ('sinal', 'estrutura', 'funcao_gramatical')

    list_filter = ('sinal', 'estrutura')

    search_fields = (
        'sinal__nome',
        'estrutura__nome',
        'funcao_gramatical',
        'exemplo_de_uso'
    )
    autocomplete_fields = ['sinal', 'estrutura']