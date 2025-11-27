"""
Number of ways to make change for a target cash amount..
Eg
$10 - target amount of money to break into change
[1, 5, 10, 25] - array 0f integers rep coins denominations available - infinite amount of each
Answer = 4 ways ( 1*10 | 2*5 | 1*5 + 5*1 | 10*1 )
Dynamic programming...
Time Complexity: O(N*M) = 0(target*number_of_coins)
Space Complexity: O(N) = 0(target)
"""

#AltSolution1
def number_of_ways_to_make_change(target, coins):
    #track how many ways to add up to target amount
    ways = [0] * (target + 1)
    ways[0] = 1

    for coin in coins:
        for amount in range(coin, target + 1):
            ways[amount] += ways[amount - coin]

    return ways[target]

#AltSolution2
def number_of_ways_to_make_change(target, coins):
    ways = [0 for amount in range(target + 1)]
    ways[0] = 1
    for coin in coins:
        for amount in range(coin, target + 1):
            if amount < coin:
                ways[amount] += ways[amount - coin]
    return ways[target]

target = 10
coins = [1, 5, 10, 25]
print(number_of_ways_to_make_change(target, coins))