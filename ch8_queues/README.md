# What is a Queue? (Fila)

A Queue stores ordered items... again, kind of like a list, but again, like a stack, its design is more restrictive. A queue only allows items to be added to the tail of the queue and removed from the head of the queue. 

It's called a "queue" because it behaves like a queue of people waiting in line to order coffee.

The first person to get in line is also the first person to be served (get out of line). So, you'll often hear a queue referred to as a FIFO (first in, first out) data structure.

# Queue Class

## Assignment

LockedIn uses a Queueto keep track of the order that recruiters should use to reach out to job seekers.

Implement the following operations on the Queue class:

- queue.push(item): Adds an item to the tail of the queue (index O of list)
- queue.pop(): Removes and returns an item from the head of the queue (last index of list)
- queue.peek(): Returns an item from the head of the queue
- queue.size(): Returns the number of items in the queue

Note: You'll often hear words used interchangeably in programming. For example, here we're saying push and pop, but enqueue and dequeue are also common words for the same ideas.

### Tips

- The underlying data type we're using is just a List. Don't forget to guard against IndexErrors by returning 'None' if the queue is empty.
- The .insert List method may be helpful

[go to code](CH8_L2_queue_class.py)

# Queue Speed

So how fast are queue operations? Well, in an optimized queue, they'd be:

- push: O(1) -> Add an item to the back of the queue
- pop: O(1) -> Remove and return the front item from the queue
- peek: O(1) -> Return the front item from the queue without modifying the queue
- size: O(1) -> Return the number of items in the queue

Just like a stack, all operations are O(1)! No matter how many items are in the queue, these operations will always take the same amount time. The reason to choose a queue over a stack is all about ordering. Queues should be used when you need to process items in the order they were added.

LIFO (stack) vs FIFO (queue)

## A Problem

Our current Queue class has a problem... take a look at the push method:

```py
def push(self, item):
    self.items.insert(0, item)
```

It's not O(1)! The List's insert method has to shift all the other items in the list down to make room for the new item.

We'll solve this very solvable problem soon...

# Matchmaking Queue

In LockedIn, users that are founding companies can join a matchmaking queue to find potential co-founders for their projects. We'll use the Queue class we've built to manage the matchmaking process.

Notice the `search_and_remove` method on the Queue class (in queue.py). It breaks the rules of a traditional queue data structure but will be useful in solving this real-world problem.

It's okay to violate academic constraints as software engineers as long as we understand the trade-offs involved

## Assignment

Complete the `matchmake` function that simulates users joining and leaving the matchmaking queue. The function should take a queue instance and a user tuple containing a name and action (either "join" and "leave"):

```py
user = ('Bob', 'join')
user = ('Alice', 'leave')
```

For each call to matchmake:

1. If the action is "leave", search the queue for the user and remove them if they are in the queue.
2. If the action is "join", push the user's name onto the queue
3. Lastly, check if the queue has at least 4 users in it. If so, pop the first 2 users from the queue and return the following string:

`{user1} matched {user2}!`

Where user1 is the first user popped and user2 is the second user popped.

4. If there were less than 4 users in the queue, return the following string: "No match found"

[Go to code]()