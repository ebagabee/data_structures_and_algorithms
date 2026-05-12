# Stacks

A Stack is a data structure that stores ordered items. It's like a list, but its design is more restrictive. It only allows items to be added or removed from the top of the stack.

It's called a "stack" because it behaves just like a stack of physical items. Imagine a stack of plates: it's easy to take an item of the top of the stack, but you can't really get to the items in the middle or at the bottom withou removing the items on top first. You'll ofter header a stack referred to as a LIFO (last in, first out) data structure.

## Assignment

In this chapter we'll build a stack from scratch! A stack will be useful at LockedIn when we need undo/redo functionality. For example, a user can add other users to their "connections" list, and then undo the last connection they added. Stack are a great way to implement undo functionality.

For now we'll just focus on two methods: `push` and `size`. Notice that the Stack class already has a contructor and the underlying `List` that we'll use to store items.

1. Complete the push method. It should add an item to the top of the stack. The "top" of the stack is the end of the list in our implementation.

2. Complete the size method. It should return the number of items in the stack.

[Go to code](CH7_L1_stacks.py)

# Stack Review

- All supported operations are independent O(1). However, some tasks, such as accessing an item at the bottom of the stack, have higher time complexity because they require multiple `pop` operations.

- Stack operations are limited: no searching, no sorting, no random access.

- Stacks, like all abstract data types, can store items of any type. What defines a stack is the behavior of its operations, not the type of data it stores.

- Stacks are frequently used in the real world for:
    - Function call management
    - Undo/redo functionality
    - Expression evaluation
    - Browser history

# Using a Stack

LockedIn supports a basic scripting language. This allows technically savvy HR managers to write scripts that automate repetitive tasks on the platform. The language uses parentheses to group operations, and we need to verify whether the parentheses in a script are balanced.

## Balanced parentheses

Parentheses are balanced when each opening parenthesis has a matching closing one and the pairs are properly nested. For example:

- ()
- ()()
- ((()))
- (()(()))

## Unbalanced parentheses

- (
- ())
- (()()
- (()))
- )(

## Assignment

Complete the `is_balanced` function.

The function takes a string as input and returns `True` if the parentheses in the string are balanced, and `False` otherwise. Use an instance of the Stack provided in `stack.py` to track the parentheses.

[Go to code](CH7_L7_using_a_stack/main.py)