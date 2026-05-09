'''
Complete the exponential_growth function. Given the initial followers count [n], growth factor [factor],
and number of days [days], return a list containing the exponential growth of followers for each day.

Example:

- Initial Followers: 10
- Growth factor: 2
- Days: 4

result = [10, 20, 40, 80, 160]
'''

def exponential_growth(n, factor, days):
    result = [n]
    current_follower = n

    for _ in range(0, days):
        current = current_follower * factor
        result.append(current)

        current_follower = current
    
    return result