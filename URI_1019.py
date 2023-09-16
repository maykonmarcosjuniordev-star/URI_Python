N = int(input())
H = N//3600
hm = N - H*3600
M = hm//60
S = hm - M*60
print("{}:{}:{}".format(H, M, S))
