from django.shortcuts import render
from .models import MapeamentoFuncao, SinalDePontuacao


def lista_regras(request):

    mapeamentos = MapeamentoFuncao.objects.all().select_related('sinal', 'estrutura')
    context = {
        'mapeamentos': mapeamentos
    }

    return render(request, 'gramatica/lista_regras.html', context)


def analisador_view(request):
    context = {
        'texto_usuario': '',
        'sinais_encontrados': []
    }

    if request.method == 'POST':
        texto = request.POST.get('texto_usuario', '')
        context['texto_usuario'] = texto

        todos_sinais = SinalDePontuacao.objects.all()

        char_to_sinal_map = {}
        for s in todos_sinais:
            if s.sinal_grafico == '()':
                char_to_sinal_map['('] = s
                char_to_sinal_map[')'] = s
            elif s.sinal_grafico == '""' or s.sinal_grafico == '"':
                char_to_sinal_map['"'] = s
            elif s.sinal_grafico == '—':  # Travessão
                char_to_sinal_map['—'] = s
                char_to_sinal_map['–'] = s  # (Meio-travessão, opcional)
            else:
                char_to_sinal_map[s.sinal_grafico] = s

        sinais_obj_encontrados = set()
        for char in texto:
            if char in char_to_sinal_map:
                sinais_obj_encontrados.add(char_to_sinal_map[char])

        context['sinais_encontrados'] = list(sinais_obj_encontrados)

    return render(request, 'gramatica/analisador.html', context)