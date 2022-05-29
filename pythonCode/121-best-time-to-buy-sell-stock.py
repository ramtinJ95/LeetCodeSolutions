from typing import List

prices= [7,1,5,3,6,4]
# Very similar to problem 53. A variant of kadens algorithm again. 
def maxProfit(prices: List[int]) -> int:
    max_profit = 0
    min_price = 99999
    for price in prices:
        if price < min_price:
            min_price = price
        if price - min_price > max_profit:
            max_profit = price - min_price
    return max_profit

print(str(maxProfit(prices)))