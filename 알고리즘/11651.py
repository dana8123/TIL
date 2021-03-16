case = int(input())
xpoint = []
ypoint = []


def sorty(xarray, yarray):
      result = []
      for i in range(case):   # i = 0,1, 2
            x, y = map(float, input().split())
            xpoint.append(x)
            ypoint.append(y)
            n = len(ypoint)   #
            for j in range(1, n):  # j = 1, 2, 3
                for k in range(j):   # k = 0, 1, 2
                    if ypoint[k - j - 1] > ypoint[k - j]:
                        ypoint[k - j - 1], ypoint[k -
                                                  j] = ypoint[k - j], ypoint[k - j - 1]
        return
# sort이용하여 풀기

sorty(xpoint, ypoint)
print(xpoint, ypoint)
