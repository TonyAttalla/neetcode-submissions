class Solution:
    def maxProfit(self, prices: List[int]) -> int:


        def calculate_profit(buy, sell):
            return sell - buy
        # use two pointers
        # while time_to_sell < len(prices)
        # check profit, if greater than current max, update
        # else increment time to sell
        # if time to buy > time to sell, time_to_buy = time_to_sell

        # 10,1,5,15

        # ttb =0, tts=0, mp = 0, len(prices = 3)
        # profit = 0
        # ttb = 0, tts=1, mp = 0
        # profit = -9, mp = 0 
        # ttb = 1, tts = 2, mp=4

        time_to_buy = 0 
        time_to_sell = 0 
        max_profit = 0
        while time_to_sell < len(prices):
            profit = calculate_profit(prices[time_to_buy], prices[time_to_sell])
            if profit > max_profit:
                max_profit = profit
            if prices[time_to_buy] > prices[time_to_sell]:
                time_to_buy = time_to_sell
            time_to_sell +=1
        return max_profit

        