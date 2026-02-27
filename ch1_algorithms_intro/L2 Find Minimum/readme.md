## Assignment

We need to show our users the accounts they follow with the *lowest* follower counts. This will help them know who they follow that isn't popular enough to be worth following any more.

Implement the "find minimum" algorithm in Python by completing the `find_minimum()` function. It accepts a list of integers `nums` and returns the smallest number in the list.

1. [ ] Set `minimum` to positive infinity: `float("inf")`.
2. [ ] If the list is empty, return `None`.
3. [ ] For each number in the list `nums`, compare it to `minimum`. If the number is smaller than `minimum`, set `minimum` to that number.
4. [ ] `minimum` is now set to the smallest number in the list. Return it.
