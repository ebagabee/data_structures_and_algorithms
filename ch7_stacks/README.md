# Stacks

A Stack is a data structure that stores ordered items. It's like a list, but its design is more restrictive. It only allows items to be added or removed from the top of the stack.

It's called a "stack" because it behaves just like a stack of physical items. Imagine a stack of plates: it's easy to take an item of the top of the stack, but you can't really get to the items in the middle or at the bottom withou removing the items on top first. You'll ofter header a stack referred to as a LIFO (last in, first out) data structure.

## Assignment

In this chapter we'll build a stack from scratch! A stack will be useful at LockedIn when we need undo/redo functionality. For example, a user can add other users to their "connections" list, and then undo the last connection they added. Stack are a great way to implement undo functionality.

For now we'll just focus on two methods: `push` and `size`. Notice that the Stack class already has a contructor and the underlying `List` that we'll use to store items.

1. Complete the push method. It should add an item to the top of the stack. The "top" of the stack is the end of the list in our implementation.

2. Complete the size method. It should return the number of items in the stack.

[Go to code](CH7_L1_stacks.py)

```md
A partir desse momento, comecei a escrever os assuntos em portugues, com o proposito de ajudar a pessoas que possam estudar a partir desse doc.
```

# Stack Review

- Todas as operações suportadas são O(1) independentes. No entando, algumas tarefas, como acessar um item na parte inferior da pilha, tem complexidade de tempo maior porque exigem múltiplas `pop` operations.

- As operations na pilha são limitadas: sem busca, sem ordenação, sem acesso aleatório.

- Pilhas, assim como todos os tipos abstratos de dados, podem armazenar itens de qualquer tipo. O que define uma pilha eh o comportamento das operacoes, e nao o tipo de dado que ele armazena.

- Pilhas sao frequentemente usadas no mundo real para:
    - Gerenciamento de chamadas de funcao
    - Funcionalidade de desfazer/refazer
    - Avalicao de Expressao
    - Historico do Navegador

# Using a Stack

O LockedIn oferece suporte a uma linguagem de script basica. Isso permite que gerentes de RH com conhecimento tecnico escrevam scripts capazes de automatizar tarefas repetitivas na plataforma. A linguagem utiliza parenteses para agrupar operacoes, e precisamos verificar se os parenteses em um script estao balanceados.

## Parenteses balanceados

Os parenteses estao balanceados quando cada parentese possui um parentese correspondente e os pares de parenteses estao devidamente aninhados. Por exemplo:

- ()
- ()()
- ((()))
- (()(()))

## Parenteses desequilibrados

- (
- ())
- (()()
- (()))
- )(

## Assignment

Conclua a `is_balanced`

A funcao recebe uma string como entrada e retorna verdade `True` se os parenteses na string estiverem balanceados, e `False` case contrario. Utilize uma instancia da Stack fornecida `stack.py` para controlar os parenteses.

[Va para o Codigo](CH7_L7_using_a_stack/main.py)