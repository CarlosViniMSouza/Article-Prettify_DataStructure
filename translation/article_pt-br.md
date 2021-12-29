![logo_article](https://files.realpython.com/media/Python_s-Pretty-Print-pprint_Watermarked.a3e409650f59.jpeg)

# Enfeite suas estruturas de dados com o Pretty Print em Python

## Artigo por: Ian Currie

```
Índice

  ° Compreendendo a necessidade do Pretty Print do Python
  ° Trabalhando com pprint
  ° Explorando Parâmetros Opcionais de pprint()
        ° Resumindo seus dados: profundidade
        ° Dando espaço aos seus dados: recuo
        ° Limitando os comprimentos das linhas: largura
        ° Apertando suas longas sequências: compacto
        ° Direcionando sua saída: stream
        ° Prevenindo a Classificação de Dicionário: sort_dicts
        ° Enriquecendo seus números: underscore_numbers
  ° Criação de um objeto PrettyPrinter personalizado
  ° Obtendo uma string bonita com pformat()
  ° Tratamento de estruturas de dados recursivas
  ° Conclusão
```

### Lidar com dados é essencial para qualquer Pythonista, mas às vezes esses dados simplesmente não são muito bonitos. Os computadores não se preocupam com a formatação, mas sem uma boa formatação, os humanos podem encontrar algo difícil de ler. A saída não é bonita quando você usa print() em grandes dicionários ou listas longas - é eficiente, mas não é bonita.

### O módulo `pprint` em Python é um módulo utilitário que você pode usar para imprimir estruturas de dados de uma maneira `pretty` e bonita. É uma parte da biblioteca padrão especialmente útil para depurar código que lida com solicitações de API, grandes arquivos JSON e dados em geral.

## Ao final deste tutorial, você:

```
  ° Entenda porque o módulo pprint é necessário
  ° Aprenda a usar pprint (), PrettyPrinter e seus parâmetros
  ° Ser capaz de criar sua própria instância de PrettyPrinter
  ° Salvar saída de string formatada em vez de imprimi-la   
  ° Imprimir e reconhecer estruturas de dados recursivas
```

### Ao longo do caminho, você também verá uma solicitação HTTP para uma [API pública](https://realpython.com/python-json/) e análise JSON em ação.

### Bônus gratuito: [clique aqui para obter uma folha de dicas do Python](https://realpython.com/python-pretty-print/) e aprender os fundamentos do Python 3, como trabalhar com tipos de dados, dicionários, listas e funções do Python.
