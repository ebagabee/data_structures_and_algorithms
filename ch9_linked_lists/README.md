# Linked Lists

Remember how the `push` method on our Queue is `O(n)` insted of `O(1)`?

```py

def push(self, item):
    # everything is self.items has to shift
    # up a position, which takes O(n) time

    self.items.insert(0, item)
```

Let's fix that.

To build a faster queue, we'll use a Linked List instead of a regular List (array) under the hood. A linked list is where elements are not stored next to each other in memory, instead, each item references the next in a chain.

## Nodes

Our nodes will be represented by a simple class with two fields:

- val - The raw string value that the node holds (e.g. 'Carla', 'James', etc)
- next - A reference to the next node in the list.

### Assignment

Let's lock-in and make LockedIn faster!

1. Complete the Node's constructor.
    1. Set its `val` field to the provided value.
    2. Set its next field to None
2. Complete the `Node`'s `set_next` method. It should set the next field to the provided node.

# Linked List vs. List

A linked list is a collection of ordered items, so it's similar to a "normal" list (also called an "array" or "slice" in other languages).

Items in a "normal" list are stored next to each other in memory, and to get an item from a normal `List` we have to use a numbered index:

```py
car = cars[3]
```

You can think of the "index" as simply an offset from the start. The `cars` list in this example refers to the start of the list, and `3` is just the 4th item in that section of memory. With a normal list, all the data is stored in the same place in memory and the index is just a way to find the right spot.

In a linked list, there are no indexes! Each node contains two things: the data itself, and a reference to the next node in the list. Iterating over a linked list requires starting at the head node and following the next references until you reach the end.

```py
current_car_node = head_card_node

while current_car_node is not None:
    print(current_car_node.val)
    current_car_node = current_car_node.next
```

Frankly, linked lists can be annoying to use and incur more overhead, so why use a linked list at all? It's because sometimes linked lists are much faster to make updates to, particularly when inserting or deleting items from teh middle.

In a normal list, if you insert an item in the middle, you have to shift all the items after it down one spot, which take `O(n)` time

In a linked list, once you've traversed to a given node, insertion i `(O(1))` because you can simply update two references