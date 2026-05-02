'''
O(K^N) - Where [K] represents a constant branching factor, e.g [3^N] - is the first Big O class
that we've dealt with that falls into the scary exponential category of algorithms.

Algorithms that grow at an exponential rate become impossible to compute after so little scale-up
that they're usually almost worthless in practically.

Letter Combinations of a Phone Number

Take a phone number and calculate all possible sequences of letters that it could represent.
Then the ad team can give influencers numbers that make brand-frindly words.

Each digit can represent three or four different letters. For this reason, the number of letter
sequences associated with a stringo of digits grows very quickly as the number of digits increases.
The possibilites either triple (3^N) or quadruple (4^N) with each additional digit.

Example Number:

6 -> 3(m, n, o)
67 -> 12(mp, mq, mr)
678 -> 36 (mpt, mpu, mpv)
6789 -> 144 (mptw, mptx)
345-6789 -> 3,888

A 7-digit phone number will produce between 2,187 (3 ^ 7) and 16,384 (4 ^ 7) letter sequences - through usually closer to the low end of that range.

It's a good thing phone numbers are short! If you had 32-digit phone number, it could form
at least ~1.85 quadrillion letter sequences (assuming 3 ^ N)

Unfortunately, if we want to check all the possible combinations from a given number, 
there's no real shortcut for us to take - we're stuck with an exponential-class algorithm.

Assignment:

Complete the letter_combinations function using the algorithm outlined below. It takes a string of digits and returns a list of strings of letters.

1 - If the input string is empty, return an empty list.
2 - Define a result list to hold the output strings. Have it contain just an
empty string to start (we need that one element to build on)
3 - Iterate over the input digits. For each of them:
    1 - If the digit is any invalid character, i.e. not found in the provided
    digit_to_letters dictionary, raise a ValueError to abort the function:

    raise ValueError(f"invalid digit: {digit}")

    2 - Get the string of letters that can be represented by the current digit, from
    digit_to_letters.

    3 - Define a new_result list - empty to start with.

    4 - Enter two nested for loops:
        - For each existing letter combo in result, iterate over each letter in the current digit's letters.
        - Append combo + letter to new_result

    5 - After the two nested loops, but still inside the main loop over digits, set result equal to new_result.
4 - After the main loop, return result.
'''

def letter_combinations(digits):
    pass


digit_to_letters = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
}
