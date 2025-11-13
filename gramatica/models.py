from django.db import models


class SinalDePontuacao(models.Model):

    sinal_grafico = models.CharField(("Sinal Gráfico"),max_length=10,unique=True,help_text="O caractere gráfico (ex: ',', ';', '—')")
    nome = models.CharField(("Nome"),max_length=100,help_text="O nome por extenso (ex: 'Vírgula')")
    descricao = models.TextField(("Descrição"),help_text="Descrição geral do sinal.")

    class Meta:
        verbose_name = ("Sinal de Pontuação")
        verbose_name_plural = ("Sinais de Pontuação")
        ordering = ['nome']

    def __str__(self):
        return f"{self.nome} ({self.sinal_grafico})"


class EstruturaSintatica(models.Model):

    nome = models.CharField(("Nome da Estrutura"),max_length=255,unique=True)
    descricao = models.TextField(("Descrição"),help_text="Definição da estrutura sintática.")

    class Meta:
        verbose_name = ("Estrutura Sintática")
        verbose_name_plural = ("Estruturas Sintáticas")
        ordering = ['nome']

    def __str__(self):
        return self.nome


class MapeamentoFuncao(models.Model):

    sinal = models.ForeignKey(
        SinalDePontuacao,
        on_delete=models.RESTRICT,
        related_name="mapeamentos",
        verbose_name=("Sinal de Pontuação"))

    estrutura = models.ForeignKey(
        EstruturaSintatica,
        on_delete=models.RESTRICT,
        related_name="mapeamentos",
        verbose_name=("Estrutura Sintática"))

    funcao_gramatical = models.CharField(
        ("Função Gramatical"),
        max_length=255,
        help_text="A função exata (ex: 'Isolar', 'Separar', 'Indicar')")

    exemplo_de_uso = models.TextField(
        ("Exemplo de Uso"))

    observacoes = models.TextField(
        ("Observações"),
        null=True,
        blank=True,
        help_text="Regras de exceção, notas de estilo ou usos alternativos.")

    class Meta:
        verbose_name = ("Mapeamento de Função")
        verbose_name_plural = ("Mapeamentos de Funções")
        constraints = [
            models.UniqueConstraint(
                fields=['sinal', 'estrutura', 'funcao_gramatical'],
                name='regra_unica_constraint'
            )
        ]
        ordering = ['sinal', 'estrutura']

    def __str__(self):
        return f"{self.sinal.nome} -> {self.funcao_gramatical} o/a {self.estrutura.nome}"