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
  ° Aprenda a usar pprint(), PrettyPrinter e seus parâmetros
  ° Ser capaz de criar sua própria instância de PrettyPrinter
  ° Salvar saída de string formatada em vez de imprimi-la   
  ° Imprimir e reconhecer estruturas de dados recursivas
```

### Ao longo do caminho, você também verá uma solicitação HTTP para uma [API pública](https://realpython.com/python-json/) e análise JSON em ação.

### Bônus gratuito: [clique aqui para obter uma folha de dicas do Python](https://realpython.com/python-pretty-print/) e aprender os fundamentos do Python 3, como trabalhar com tipos de dados, dicionários, listas e funções do Python.

## Compreendendo a necessidade do Pretty Print do Python:

### O módulo Python pprinté útil em muitas situações. É útil ao fazer solicitações de API, lidar com [JSON files](https://realpython.com/python-json/) ou lidar com dados complicados e aninhados. Você provavelmente descobrirá que usar a função `print()` normal não é adequado para explorar seus dados e [debug](https://realpython.com/python-debugging-pdb/) seu aplicativo com eficiência. Quando você usa print() com [dictionaries](https://realpython.com/python-dicts/) e [lists](https://realpython.com/python-lists-tuples/), a saída não contém novas linhas.

### Antes de começar a explorar pprint, você primeiro urllibfará uma solicitação para obter alguns dados. Você fará uma solicitação ao [{JSON} Placeholder](https://jsonplaceholder.typicode.com/) para algumas informações do usuário simulado. A primeira coisa a fazer é fazer a `solicitação HTTP GET` e colocar a resposta em um dicionário:

```Python
import json
from urllib import request

response = request.urlopen("https://jsonplaceholder.typicode.com/users")

json_response = response.read()
users = json.loads(json_response)
```

### Aqui, você faz uma solicitação GET básica e, em seguida, analisa a resposta em um dicionário com `json.loads()`. Com o dicionário agora em uma variável, uma próxima etapa comum é imprimir o conteúdo com `print()`:

```Python
print(users)

# Output: [{'id': 1, 'name': 'Leanne Graham', 'username': 'Bret', 'email': 'Sincere@april.biz', 'address': {'street': 'Kulas Light', 'suite': 'Apt. 556', 'city': 'Gwenborough', 'zipcode': '92998-3874', 'geo': {'lat': '-37.3159', 'lng': '81.1496'}}, 'phone': '1-770-736-8031 x56442', 'website': 'hildegard.org', 'company': {'name': 'Romaguera-Crona', 'catchPhrase': 'Multi-layered client-server neural-net', 'bs': 'harness real-time e-markets'}}, {'id': 2, 'name': 'Ervin Howell', 'username': 'Antonette', 'email': 'Shanna@melissa.tv', 'address': {'street': 'Victor Plains', 'suite': 'Suite 879', 'city': 'Wisokyburgh', 'zipcode': '90566-7771', 'geo': {'lat': '-43.9509', 'lng': '-34.4618'}}, 'phone': '010-692-6593 x09125', 'website': 'anastasia.net', 'company': {'name': 'Deckow-Crist', 'catchPhrase': 'Proactive didactic contingency', 'bs': 'synergize scalable supply-chains'}}, {'id': 3, 'name': 'Clementine Bauch', 'username': 'Samantha', 'email': 'Nathan@yesenia.net', 'address': {'street': 'Douglas Extension', 'suite': 'Suite 847', 'city': 'McKenziehaven', 'zipcode': '59590-4157', 'geo': {'lat': '-68.6102', 'lng': '-47.0653'}}, 'phone': '1-463-123-4447', 'website': 'ramiro.info', 'company': {'name': 'Romaguera-Jacobson', 'catchPhrase': 'Face to face bifurcated interface', 'bs': 'e-enable strategic applications'}}, {'id': 4, 'name': 'Patricia Lebsack', 'username': 'Karianne', 'email': 'Julianne.OConner@kory.org', 'address': {'street': 'Hoeger Mall', 'suite': 'Apt. 692', 'city': 'South Elvis', 'zipcode': '53919-4257', 'geo': {'lat': '29.4572', 'lng': '-164.2990'}}, 'phone': '493-170-9623 x156', 'website': 'kale.biz', 'company': {'name': 'Robel-Corkery', 'catchPhrase': 'Multi-tiered zero tolerance productivity', 'bs': 'transition cutting-edge web services'}}, {'id': 5, 'name': 'Chelsey Dietrich', 'username': 'Kamren', 'email': 'Lucio_Hettinger@annie.ca', 'address': {'street': 'Skiles Walks', 'suite': 'Suite 351', 'city': 'Roscoeview', 'zipcode': '33263', 'geo': {'lat': '-31.8129', 'lng': '62.5342'}}, 'phone': '(254)954-1289', 'website': 'demarco.info', 'company': {'name': 'Keebler LLC', 'catchPhrase': 'User-centric fault-tolerant solution', 'bs': 'revolutionize end-to-end systems'}}, {'id': 6, 'name': 'Mrs. Dennis Schulist', 'username': 'Leopoldo_Corkery', 'email': 'Karley_Dach@jasper.info', 'address': {'street': 'Norberto Crossing', 'suite': 'Apt. 950', 'city': 'South Christy', 'zipcode': '23505-1337', 'geo': {'lat': '-71.4197', 'lng': '71.7478'}}, 'phone': '1-477-935-8478 x6430', 'website': 'ola.org', 'company': {'name': 'Considine-Lockman', 'catchPhrase': 'Synchronised bottom-line interface', 'bs': 'e-enable innovative applications'}}, {'id': 7, 'name': 'Kurtis Weissnat', 'username': 'Elwyn.Skiles', 'email': 'Telly.Hoeger@billy.biz', 'address': {'street': 'Rex Trail', 'suite': 'Suite 280', 'city': 'Howemouth', 'zipcode': '58804-1099', 'geo': {'lat': '24.8918', 'lng': '21.8984'}}, 'phone': '210.067.6132', 'website': 'elvis.io', 'company': {'name': 'Johns Group', 'catchPhrase': 'Configurable multimedia task-force', 'bs': 'generate enterprise e-tailers'}}, {'id': 8, 'name': 'Nicholas Runolfsdottir V', 'username': 'Maxime_Nienow', 'email': 'Sherwood@rosamond.me', 'address': {'street': 'Ellsworth Summit', 'suite': 'Suite 729', 'city': 'Aliyaview', 'zipcode': '45169', 'geo': {'lat': '-14.3990', 'lng': '-120.7677'}}, 'phone': '586.493.6943 x140', 'website': 'jacynthe.com', 'company': {'name': 'Abernathy Group', 'catchPhrase': 'Implemented secondary concept', 'bs': 'e-enable extensible e-tailers'}}, {'id': 9, 'name': 'Glenna Reichert', 'username': 'Delphine', 'email': 'Chaim_McDermott@dana.io', 'address': {'street': 'Dayna Park', 'suite': 'Suite 449', 'city': 'Bartholomebury', 'zipcode': '76495-3109', 'geo': {'lat': '24.6463', 'lng': '-168.8889'}}, 'phone': '(775)976-6794 x41206', 'website': 'conrad.com', 'company': {'name': 'Yost and Sons', 'catchPhrase': 'Switchable contextually-based project', 'bs': 'aggregate real-time technologies'}}, {'id': 10, 'name': 'Clementina DuBuque', 'username': 'Moriah.Stanton', 'email': 'Rey.Padberg@karina.biz', 'address': {'street': 'Kattie Turnpike', 'suite': 'Suite 198', 'city': 'Lebsackbury', 'zipcode': '31428-2261', 'geo': {'lat': '-38.2386', 'lng': '57.2232'}}, 'phone': '024-648-3804', 'website': 'ambrose.net', 'company': {'name': 'Hoeger LLC', 'catchPhrase': 'Centralized empowering task-force', 'bs': 'target end-to-end models'}}]
```

### Oh céus! Uma linha enorme sem novas linhas. Dependendo das configurações do console, isso pode aparecer como uma linha muito longa. Como alternativa, a saída do console pode estar com o modo de quebra de linha ativado, que é a situação mais comum. Infelizmente, isso não torna a saída muito mais amigável!

### Se você olhar o primeiro e o último caracteres, verá que isso parece ser uma lista. Você pode ficar tentado a começar a escrever um loop para imprimir os itens:

```Python
for i in users:
  print(user)
```

### Esse loop for imprimiria cada objeto em uma linha separada, mas mesmo assim, cada objeto ocuparia muito mais espaço do que caberia em uma única linha. Imprimir desta forma torna as coisas um pouco melhores, mas não é de forma alguma a ideal. O exemplo acima é uma estrutura de dados relativamente simples, mas o que você faria com um dicionário profundamente aninhado com 100 vezes o tamanho?

### Claro, você poderia escrever uma função que use [recursão](https://realpython.com/python-recursion/) para encontrar uma maneira de imprimir tudo. Infelizmente, você provavelmente encontrará alguns casos extremos em que isso não funcionará. Você pode até mesmo se pegar escrevendo um módulo inteiro de funções apenas para se familiarizar com a estrutura dos dados!

### Entre no `pprint`módulo!

## Trabalhando com `pprint`

### `pprint` é um módulo Python feito para imprimir estruturas de dados de uma maneira bonita. Faz muito tempo que faz parte da biblioteca padrão do Python, portanto, não é necessário instalá-lo separadamente. Tudo que você precisa fazer é importar sua `pprint()` função:

```Python
from pprint import pprint
```

### Então, em vez de seguir a `print(users)` abordagem normal como fez no exemplo acima, você pode chamar sua nova função favorita para tornar a saída bonita:

```Python
pprint(users)
```

### Esta função é impressa `users-` mas de uma maneira bonita e nova e aprimorada:

```Python
pprint(users)

"""
Output:

[{'address': {'city': 'Gwenborough',
 'geo': {'lat': '-37.3159', 'lng': '81.1496'},
 'street': 'Kulas Light',
 'suite': 'Apt. 556',
 'zipcode': '92998-3874'},
 'company': {'bs': 'harness real-time e-markets',
 'catchPhrase': 'Multi-layered client-server neural-net',
 'name': 'Romaguera-Crona'},
 'email': 'Sincere@april.biz',
 'id': 1,
 'name': 'Leanne Graham',
 'phone': '1-770-736-8031 x56442',
 'username': 'Bret',
 'website': 'hildegard.org'},
 {'address': {'city': 'Wisokyburgh',
 'geo': {'lat': '-43.9509', 'lng': '-34.4618'},
 'street': 'Victor Plains',
 'suite': 'Suite 879',
 'zipcode': '90566-7771'},
 'company': {'bs': 'synergize scalable supply-chains',
 'catchPhrase': 'Proactive didactic contingency',
 'name': 'Deckow-Crist'},
 'email': 'Shanna@melissa.tv',
 'id': 2,
 'name': 'Ervin Howell',
 'phone': '010-692-6593 x09125',
 'username': 'Antonette',
 'website': 'anastasia.net'},

 ...

 {'address': {'city': 'Lebsackbury',
 'geo': {'lat': '-38.2386', 'lng': '57.2232'},
 'street': 'Kattie Turnpike',
 'suite': 'Suite 198',
 'zipcode': '31428-2261'},
 'company': {'bs': 'target end-to-end models',
 'catchPhrase': 'Centralized empowering task-force',
 'name': 'Hoeger LLC'},
 'email': 'Rey.Padberg@karina.biz',
 'id': 10,
 'name': 'Clementina DuBuque',
 'phone': '024-648-3804',
 'username': 'Moriah.Stanton',
 'website': 'ambrose.net'}]
"""
```

### Quão belo! As teclas dos dicionários são ainda recuadas visualmente! Essa saída torna muito mais simples verificar e analisar visualmente as estruturas de dados.

## OBS: a saída que você verá será mais longa se você executar o código por conta própria. Este bloco de código trunca a saída para facilitar a leitura.

### Se você gosta de digitar o mínimo possível, ficará satisfeito em saber que `pprint()` tem um alias `pp()`:

```Python
from pprint import pp
pp(users)
```

### `pp()` é apenas um invólucro `pprint()` e se comporta exatamente da mesma maneira.

```
Nota: Python incluiu este alias desde a versão 3.8.0 alpha 2
```

### No entanto, mesmo a saída padrão pode ser muita informação para digitalizar no início. Talvez tudo o que você realmente queira é verificar se está lidando com uma lista de objetos simples. Para isso, você vai querer ajustar um pouco a saída.

### Para essas situações, existem vários parâmetros que você pode transmitir pprint()para tornar bonitas até as estruturas de dados mais concisas.

## Explorando Parâmetros Opcionais de `pprint()`

### Nesta seção, você aprenderá sobre todos os parâmetros disponíveis para `pprint()`. Existem sete parâmetros que você pode usar para configurar sua linda impressora Pythonic. Você não precisa usar todos eles e alguns serão mais úteis do que outros. O que você achará mais valioso provavelmente será `depth`.

## _Resumindo seus dados: depth_

### Um dos parâmetros mais úteis para brincar é `depth`. O comando Python a seguir imprimirá apenas o conteúdo completo `users` se a estrutura de dados estiver igual ou inferior à profundidade especificada - tudo ao mesmo tempo em que mantém as coisas bonitas, é claro. O conteúdo de estruturas de dados mais profundas é substituído por três pontos:

```Python
pprint(users, depth=1)

# Output: [{...}, {...}, {...}, {...}, {...}, {...}, {...}, {...}, {...}, {...}]
```

### Agora você pode ver imediatamente que esta é realmente uma lista de dicionários. Para explorar mais a estrutura de dados, você pode aumentar a profundidade em um nível, o que imprimirá todas as chaves de nível superior dos dicionários em `users`:

```Python
pprint(users, depth=2)

"""
Output:

[{'address': {...},
 'company': {...},
 'email': 'Sincere@april.biz',
 'id': 1,
 'name': 'Leanne Graham',
 'phone': '1-770-736-8031 x56442',
 'username': 'Bret',
 'website': 'hildegard.org'},
 {'address': {...},
 'company': {...},
 'email': 'Shanna@melissa.tv',
 'id': 2,
 'name': 'Ervin Howell',
 'phone': '010-692-6593 x09125',
 'username': 'Antonette',
 'website': 'anastasia.net'},

 ...

 {'address': {...},
 'company': {...},
 'email': 'Rey.Padberg@karina.biz',
 'id': 10,
 'name': 'Clementina DuBuque',
 'phone': '024-648-3804',
 'username': 'Moriah.Stanton',
 'website': 'ambrose.net'}]
"""
```

### Agora você pode verificar rapidamente se todos os dicionários compartilham suas chaves de nível superior. Esta é uma observação valiosa a se fazer, especialmente se você estiver encarregado de desenvolver um aplicativo que consome dados como este.

## _Dando espaço aos seus dados: indent_

### O `indent` parâmetro controla o quão recuado será cada nível da representação bem impressa na saída. O recuo padrão é justo 1, o que se traduz em um caractere de espaço:

```Python
pprint(users[0], depth=1)

"""
Output:

{'address': {...},
 'company': {...},
 'email': 'Sincere@april.biz',
 'id': 1,
 'name': 'Leanne Graham',
 'phone': '1-770-736-8031 x56442',
 'username': 'Bret',
 'website': 'hildegard.org'}
"""

pprint(users[0], depth=1, indent=4)

"""
Output:

{ 'address': {...},
 'company': {...},
 'email': 'Sincere@april.biz',
 'id': 1,
 'name': 'Leanne Graham',
 'phone': '1-770-736-8031 x56442',
 'username': 'Bret',
 'website': 'hildegard.org'}
"""
```

### A parte mais importante do comportamento de recuo do `pprint()`é manter todas as teclas alinhadas visualmente. A quantidade de indentação aplicada depende do `indent` parâmetro e de onde está a chave.

### Como não há aninhamento nos exemplos acima, a quantidade de indentação é baseada totalmente no `indent` parâmetro. Em ambos os exemplos, observe como a chave de abertura ({) é contada como uma unidade de recuo para a primeira chave. No primeiro exemplo, a aspa simples de abertura da primeira chave vem logo depois, {sem nenhum espaço entre eles, porque o recuo está definido como 1.

### Quando há aninhamento, no entanto, o recuo é aplicado ao primeiro elemento em linha e, a `pprint()` seguir, mantém todos os elementos seguintes alinhados com o primeiro. Portanto, se você definir seu `indent` como 4 ao imprimir `users`, o primeiro elemento será recuado em quatro caracteres, enquanto os elementos aninhados serão recuados em mais de oito caracteres porque o recuo começa no final da primeira chave:

```Python
pprint(users[0], depth=2, indent=4)

"""
Output:

{   'address': { 'city': 'Gwenborough',
 'geo': {...},
 'street': 'Kulas Light',
 'suite': 'Apt. 556',
 'zipcode': '92998-3874'},
 'company': { 'bs': 'harness real-time e-markets',
 'catchPhrase': 'Multi-layered client-server neural-net',
 'name': 'Romaguera-Crona'},
 'email': 'Sincere@april.biz',
 'id': 1,
 'name': 'Leanne Graham',
 'phone': '1-770-736-8031 x56442',
 'username': 'Bret',
 'website': 'hildegard.org'}
"""
```

### Esta é apenas outra parte do _beleza_ em Python `pprint()`!

## Limitando os comprimentos das linhas: width

### Por padrão, `pprint()` produzirá apenas até oitenta caracteres por linha. Você pode personalizar esse valor passando um argumento `width`. `pprint()` fará um esforço para ajustar o conteúdo em uma linha. Se o conteúdo de uma estrutura de dados ultrapassar esse limite, ele imprimirá todos os elementos da estrutura de dados atual em uma nova linha:

```Python
pprint(users[0])

"""
Output:

{'address': {'city': 'Gwenborough',
 'geo': {'lat': '-37.3159', 'lng': '81.1496'},
 'street': 'Kulas Light',
 'suite': 'Apt. 556',
 'zipcode': '92998-3874'},
 'company': {'bs': 'harness real-time e-markets',
 'catchPhrase': 'Multi-layered client-server neural-net',
 'name': 'Romaguera-Crona'},
 'email': 'Sincere@april.biz',
 'id': 1,
 'name': 'Leanne Graham',
 'phone': '1-770-736-8031 x56442',
 'username': 'Bret',
 'website': 'hildegard.org'}
"""
```

### Quando você deixa a largura padrão de oitenta caracteres, o dicionário `users[0]['address']['geo']` contém apenas um `'lat'` e um `'lng'` atributo. Isso significa que a soma do recuo e o número de caracteres necessários para imprimir o dicionário, incluindo os espaços entre eles, resulta em menos de oitenta caracteres. Uma vez que tem menos de oitenta caracteres, a largura padrão, `pprint()` coloca tudo em uma linha.

### No entanto, o dicionário em `users[0]['company']` iria ultrapassar a largura padrão, então `pprint()` coloca cada chave em uma nova linha. Isso é verdade para dicionários, listas, tuplas e conjuntos:

```Python
pprint(users[0], width=160)

"""
Output:

{'address': {'city': 'Gwenborough', 'geo': {'lat': '-37.3159', 'lng': '81.1496'}, 'street': 'Kulas Light', 'suite': 'Apt. 556', 'zipcode': '92998-3874'},
 'company': {'bs': 'harness real-time e-markets', 'catchPhrase': 'Multi-layered client-server neural-net', 'name': 'Romaguera-Crona'},
 'email': 'Sincere@april.biz',
 'id': 1,
 'name': 'Leanne Graham',
 'phone': '1-770-736-8031 x56442',
 'username': 'Bret',
 'website': 'hildegard.org'}
"""
```

### Se você definir a largura com um valor grande 160, como , todos os dicionários aninhados caberão em uma linha. Você pode até levar isso a extremos e usar um valor enorme como 500, que, neste exemplo, imprime todo o dicionário em uma linha:

```Python
pprint(users[0], width=500)

# Output: {'address': {'city': 'Gwenborough', 'geo': {'lat': '-37.3159', 'lng': '81.1496'}, 'street': 'Kulas Light', 'suite': 'Apt. 556', 'zipcode': '92998-3874'}, 'company': {'bs': 'harness real-time e-markets', 'catchPhrase': 'Multi-layered client-server neural-net', 'name': 'Romaguera-Crona'}, 'email': 'Sincere@april.biz', 'id': 1, 'name': 'Leanne Graham', 'phone': '1-770-736-8031 x56442', 'username': 'Bret', 'website': 'hildegard.org'}
```

### Aqui, você obtém os efeitos da configuração `width` para um valor relativamente alto. Você pode ir para o outro lado e definir `width` um valor baixo, como 1. No entanto, o principal efeito que isso terá é garantir que cada estrutura de dados exiba seus componentes em linhas separadas. Você ainda obterá o recuo visual que alinha os componentes:

```Python
pprint(users[0], width=5)

"""
Output:

{'address': {'city': 'Gwenborough',
 'geo': {'lat': '-37.3159',
 'lng': '81.1496'},
 'street': 'Kulas '
 'Light',
 'suite': 'Apt. '
 '556',
 'zipcode': '92998-3874'},
 'company': {'bs': 'harness '
 'real-time '
 'e-markets',
 'catchPhrase': 'Multi-layered '
 'client-server '
 'neural-net',
 'name': 'Romaguera-Crona'},
 'email': 'Sincere@april.biz',
 'id': 1,
 'name': 'Leanne '
 'Graham',
 'phone': '1-770-736-8031 '
 'x56442',
 'username': 'Bret',
 'website': 'hildegard.org'}
"""
```

### É difícil fazer com que `pprint()` a impressão de Python seja feia. Fará tudo o que puder para ser bonita!

### Neste exemplo, além de aprender sobre width, você também está explorando como a impressora divide longas linhas de texto. Observe como `users[0]["company"]["catchPhrase"]`, que foi inicialmente `'Multi-layered client-server neural-net'`, foi dividido em cada espaço. A impressora evita dividir essa string no meio da palavra porque isso dificultaria a leitura.

## Apertando suas longas sequências: compact

### Você pode pensar que `compact` se refere ao comportamento explorado na seção sobre `width-` isto é, se `compact` faz as estruturas de dados aparecerem em uma linha ou em linhas separadas. No entanto, `compact` só afeta a saída de uma vez por linha vai _ao longo_ do width.

```Nota: compact afeta apenas a saída de sequências: listas, conjuntos e tuplas, e não dicionários. Isso é intencional, embora não esteja claro por que essa decisão foi tomada. Há uma discussão em andamento sobre isso no Python Issue # 34798.```

### Se `compact` for `True`, a saída será quebrada na próxima linha. O comportamento padrão é que cada elemento apareça em sua própria linha se a estrutura de dados for maior que a largura:

```python
pprint(users, depth=1)
# Output: [{...}, {...}, {...}, {...}, {...}, {...}, {...}, {...}, {...}, {...}]

pprint(users, depth=1, width=40)

"""
Output:

[{...},
 {...},
 {...},
 {...},
 {...},
 {...},
 {...},
 {...},
 {...},
 {...}]
"""

pprint(users, depth=1, width=40, compact=True)

"""
Output:

[{...}, {...}, {...}, {...}, {...},
 {...}, {...}, {...}, {...}, {...}]
"""
```

### A impressão bonita desta lista usando as configurações padrão imprime a versão abreviada em uma linha. Limitando-se `width` a 40 caracteres, você força `pprint()` a saída de todos os elementos da lista em linhas separadas. Se você definir `compact=True`, a lista terá quarenta caracteres e será mais compacta do que pareceria normalmente.

```Nota: Cuidado, pois definir a largura para menos de sete caracteres - o que, neste caso, é equivalente à [{...},saída - parece ignorar o depthargumento completamente e pprint()acaba imprimindo tudo sem dobrar. Isso foi relatado como bug # 45611 .```

### `compact` é útil para sequências longas com elementos curtos que, de outra forma, ocupariam muitas linhas e tornariam a saída menos legível.

## Direcionando sua saída: stream

### O `stream` parâmetro se refere à saída de `pprint()`. Por padrão, ele vai para o mesmo lugar que `print()` vai. Especificamente, ele vai para [sys.stdout](https://docs.python.org/3/library/sys.html#sys.stdout), que na verdade é um [objeto de arquivo](https://docs.python.org/3/glossary.html#term-file-object) em Python. No entanto, você pode redirecionar isso para qualquer objeto de arquivo, da mesma forma que pode com `print()`:

```python
# OBS.: Para funcionar, você precisa de 1 arquivo formato .txt
with open("output.txt", mode="w") as file_object:
    pprint(users, stream=file_object)
```

### Aqui, você cria um objeto de arquivo com [`open()`](https://docs.python.org/3/library/functions.html#open) e, em seguida, define o `stream` parâmetro `pprint()` para esse objeto de arquivo. Se você abrir o arquivo `output.txt`, verá que imprimiu bem tudos os `users` dele.

### Python tem seu próprio [módulo de registro](https://realpython.com/python-logging/). No entanto, você também pode usar `pprint()` para enviar saídas bonitas para arquivos e fazer com que funcionem como logs, se preferir.

## Evitando a classificação do dicionário: sort_dicts

### Embora os dicionários sejam geralmente considerados estruturas de dados não ordenadas, desde o Python 3.6, os [dicionários são ordenados por inserção](https://docs.python.org/3.6/whatsnew/3.6.html#new-dict-implementation).

### `pprint()` ordena as chaves em ordem alfabética para impressão:

```python
pprint(users[0], depth=1)

"""
Output:

{'address': {...},
 'company': {...},
 'email': 'Sincere@april.biz',
 'id': 1,
 'name': 'Leanne Graham',
 'phone': '1-770-736-8031 x56442',
 'username': 'Bret',
 'website': 'hildegard.org'}
"""
pprint(users[0], depth=1, sort_dicts=False)

"""
Output:

{'id': 1,
 'name': 'Leanne Graham',
 'username': 'Bret',
 'email': 'Sincere@april.biz',
 'address': {...},
 'phone': '1-770-736-8031 x56442',
 'website': 'hildegard.org',
 'company': {...}}
"""
```

### A menos que você defina `sort_dicts` como `False`, o Python `pprint()` classifica as chaves em ordem alfabética. Ele mantém a saída dos dicionários consistente, legível e - bem - bonita!

### Quando `pprint()` foi implementado pela primeira vez, os dicionários eram desordenados. Sem ordenar as chaves em ordem alfabética, as chaves de um dicionário poderiam teoricamente diferir a cada impressão.

## Enfeitar seus números: underscore_numbers

### O `underscore_numbers` parâmetro é um recurso introduzido no [Python 3.10](https://realpython.com/python310-new-features/) que torna os números longos mais legíveis. Considerando que o exemplo que você está usando até agora não contém nenhum número longo, você precisará de um novo exemplo para testá-lo:

```python
number_list = [123456789, 10000000000000]

pprint(number_list, underscore_numbers=True)
# Output: [123_456_789, 10_000_000_000_000]
```

### Se você tentou executar esta chamada para `pprint()` e obteve um erro, não está sozinho. Em outubro de 2021, esse argumento não funcionava ao ligar `pprint()` diretamente. A comunidade Python percebeu isso rapidamente, e isso [foi corrigido](https://github.com/python/cpython/pull/29133) no [lançamento de correção de bug 3.10.1](https://www.python.org/dev/peps/pep-0619/#bugfix-releases) de dezembro de 2021. O pessoal da Python se preocupa com sua linda impressora! Eles provavelmente já terão corrigido isso no momento em que você estiver lendo este tutorial.

### Se `underscore_numbers` não funcionar quando você ligar `pprint()` diretamente e você realmente quiser números bonitos, há uma solução alternativa: quando você cria seu próprio `PrettyPrinter` objeto, este parâmetro deve funcionar exatamente como no exemplo acima.

### A seguir, você aprenderá a criar um `PrettyPrinter` objeto.

## Criação de um `PrettyPrinter` objeto personalizado

### É possível criar uma instância de `PrettyPrinter` que tenha os padrões que você definiu. Depois de ter essa nova instância de seu `PrettyPrinter` objeto personalizado , você pode usá-la chamando o `.pprint()`método na `PrettyPrinter` instância:

```python
from pprint import PrettyPrinter
custom_printer = PrettyPrinter(
    indent=4,
    width=100,
    depth=2,
    compact=True,
    sort_dicts=False,
    underscore_numbers=True
)

custom_printer.pprint(users[0])

"""
Output:

{   'id': 1,
    'name': 'Leanne Graham',
    'username': 'Bret',
    'email': 'Sincere@april.biz',
    'address': {   'street': 'Kulas Light',
                   'suite': 'Apt. 556',
                   'city': 'Gwenborough',
                   'zipcode': '92998-3874',
                   'geo': {...}},
    'phone': '1-770-736-8031 x56442',
    'website': 'hildegard.org',
    'company': {   'name': 'Romaguera-Crona',
                   'catchPhrase': 'Multi-layered client-server neural-net',
                   'bs': 'harness real-time e-markets'}}
"""

number_list = [123456789, 10000000000000]

custom_printer.pprint(number_list)
# Output: [123_456_789, 10_000_000_000_000]
```

### Com esses comandos, você:

```
    ° Importado PrettyPrinter , que é uma definição de classe
    ° Criou uma nova instância dessa classe com certos parâmetros
    ° Impresso o primeiro usuário emusers
    ° Definiu uma lista de alguns números longos
    ° Impressonumber_list , que também demonstra underscore_numbersem ação
```

### Observe que os argumentos que você passou `PrettyPrinter` são exatamente iguais aos `pprint()` argumentos padrão , exceto que você ignorou o primeiro parâmetro. Em `pprint()`, este é o objeto que você deseja imprimir.

### Dessa forma, você pode ter várias predefinições de impressora - talvez algumas indo para fluxos diferentes - e chamá-las quando precisar delas.

## Obtendo uma corda bonita com `pformat()`

### E se você não quiser enviar a bela saída de `pprint()` para um fluxo? Talvez você queira fazer alguma correspondência de [regex](https://realpython.com/regex-python/) e substituir certas chaves. Para dicionários simples, você pode querer remover os colchetes e aspas para torná-los ainda mais legíveis.

### O que quer que você queira fazer com a pré-saída da string, você pode obter a string usando [`pformat()`](https://docs.python.org/3/library/pprint.html#pprint.pformat):

```python
from pprint import pformat

address = pformat(users[0]["address"])
chars_to_remove = ["{", "}", "'"]

for char in chars_to_remove:
    address = address.replace(char, "")

print(address)

"""
Output:

city: Gwenborough,
 geo: lat: -37.3159, lng: 81.1496,
 street: Kulas Light,
 suite: Apt. 556,
 zipcode: 92998-3874
"""
```

### `pformat()` é uma ferramenta que você pode usar para ficar entre a bela impressora e o fluxo de saída.

### Outro caso de uso para isso pode ser se você estiver [construindo uma API](https://realpython.com/api-integration-in-python/#rest-and-python-building-apis) e quiser enviar uma representação de string bonita da string JSON. Seus usuários finais provavelmente apreciariam isso!
