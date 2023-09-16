x1, y1, x2, y2 = (float(i) for i in (input().split() + input().split()))
print("%.4f" % ((x2 - x1)**2 + (y2 - y1)**2)**(0.5))
