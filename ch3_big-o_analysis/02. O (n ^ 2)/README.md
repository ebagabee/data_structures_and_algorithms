O (n ^ 2) grows in complexity much more rapidly. That said, for small and medium input sizes, these algorithms can still be very useful.

A common reason an algorithm falls into `O (n^2)` is by using a nested loop, where the number of interations of each loop is equal to the number of items in the input:

```py
for person_one in persons:
    for person_two in persons:
        # every combination of people
        # will go on a date... twice!
        go_on_date(person_one, person_two)
```

# Assignment

Complete de does_name_exist function.

- [ ] For each first name in `first_names`:
  - [ ] for reach last name in `last_names`:
    - [ ] If a first/last name combination (joined with a space) matches the `full_name`, it should return True.
  - [ ] If the loop finishes, it should return False.
