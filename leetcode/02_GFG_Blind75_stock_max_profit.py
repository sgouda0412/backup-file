# At most one transaction possible -> 1 buy and 1 sell


class Solution:
    def maximumProfit(self, prices):
        # max_profit = 0
        # for i in range(len(prices)):
        #     for j in range(i + 1, len(prices)):
        #         profit = prices[j] - prices[i]
        #         max_profit = max(max_profit, profit)

        # return max_profit if max_profit > 0 else 0

        max_profit = 0
        buy_price = prices[0]

        for i in range(1, len(prices)):
            max_profit = max(max_profit, prices[i] - buy_price)
            buy_price = min(buy_price, prices[i])
        return max_profit


if __name__ == "__main__":
    sol = Solution()
    prices = [7, 10, 1, 3, 6, 9, 2]
    print(sol.maximumProfit(prices))
