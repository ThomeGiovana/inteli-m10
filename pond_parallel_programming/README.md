# Atividade: threads em Python

Giovana Lisbôa Thomé

Ciências da Computação 2022.1

## Atividades em código

Os exemplos do vídeo foram implementados em [threads_with_classes](./threads_with_classes.py) e [threads_with_functions](./threads_with_functions.py). A atividade principal foi implementada no arquivo [main](./main.py).

## Respostas dissertativas

### Qual a abordagem utilizada no código conforme os comentários?

As abordagens no uso de threads foram de classes e funções. Podemos criar uma classe que representa uma thread que faz um trabalho específico e chamá-la diversas vezes e também podemos criar threads e passar funções como argumentos para serem executadas na thread criada.

A abordagem utilizada em [main.py](./main.py) foi com a utilização de funções passadas como argumentos para uma thread executar.

### Quais modificações seriam necessárias para execução de 3 ou mais threads?

Para execução de três ou mais threads, o código em [main.py](./main.py) deveria receber o número de threads que queremos executar, chamaremos esse número de `n_threads`. Esse número serviria de base para a separação da lista principal em partes distintas, sem itens repetidos entre si. Podemos criar uma lista de listas para a subseparação (o que adicionaria custo de memória), como `random_number_sublists`.

`n_threads` também serviria para criação de um loop para criação das threads. Para fins de aprendizagem, o código com `n_threads` foi implementado em [main_execution_with_more_threads.py](./main_execution_with_more_threads.py).

### Por que a abordagem com threads possui maior escalabilidade?

A abordagem de utilização de threads possui maior escalabilidade pois consegue executar diferentes partes de um mesmo programa ou processo ao mesmo tempo. Isso faz com que a capacidade computacional seja mais utilizada e diminui o tempo de execução (execução simultânea e compartilhamento de recursos). Porém, no caso específico da atividade de somar números em uma lista, não necessariamente teremos um resultados de tempo de execução melhor se tivermos um número maior de threads:

- O tempo de criação de threads pode ser custoso e;
- Dependendo do número de threads criadas, o número de somas realizadas dentro de cada uma será menor.
  Portanto, trabalhar com threads pode ser agregar muito valor, porém, se feito sem prestar atenção, pode trazer mais prejuízos do que lucros.
