market={"dairy":["yogurt","cheese"],"fruits":['banana','apple','orange','lemon','apple','banana','banana']}
print(market)
market["candies"]=['mars','kinder','twix']
market["fruits"].sort()
s1=set(market["fruits"])
market["fruits"]=list(s1)
print(market)