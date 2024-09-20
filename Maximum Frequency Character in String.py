str = "Rakesh is best"
res = max(str, key=lambda x: str.count(x))
print(res)
