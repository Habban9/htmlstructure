#Sets
cricket={"habban","renuka","ahmed","faiz","sana","saim","zara","ayesha"}
football={"habban","renuka","faiz","zara","ali","murtaza","hassan","zayn"}
#Plays Both
print(cricket.intersection(football))
#Common Names written ones-unique names
print(cricket.union(football))
#Like cricket but not football
print(cricket.difference(football))
#like football but not cricket
print(football.difference(cricket))