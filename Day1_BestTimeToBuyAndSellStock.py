class Solution(object):
    def maxProfit(self, prices):
        answer=0
        minimumSoFar=prices[0]
        for i in range(1, len(prices)):
            currentProfit=prices[i] - minimumSoFar
            if(currentProfit > answer): answer=currentProfit
            minimumSoFar=min(minimumSoFar, prices[i])
        return answer