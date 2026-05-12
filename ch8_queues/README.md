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