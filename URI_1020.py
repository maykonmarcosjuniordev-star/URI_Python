i = int(input())
a = i//365
am = i - a*365
m = am//30
md = am - m*30
d = md
print("{} ano(s)".format(a))
print("{} mes(es)".format(m))
print("{} dia(s)".format(d))
