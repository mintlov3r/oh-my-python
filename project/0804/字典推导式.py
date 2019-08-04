d2 = dict(k4=4, k5=5, k6=6, k7=7)

# d1 = {
#     "k1": 1,
#     "k2": 2,
#     "k3": 3,
# }
# print(d1)
# print(d2)
# 键值反向
# k:v v:k
d3 = {v:k for k, v in d2.items()}
# print(d2.items())
# for k, v in d2.items():
#    print(k, v)
print(d3)
d4 = [k for k, v in d2.items()]
print(d4)
d5 = [v for k, v in d2.items()]
print(d5)

d6 = {k for k, v in d2.items()}

print(d6)

d7 = {k:v for k, v in zip(list('niaho'), range(6))}

print(d7)
