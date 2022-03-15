
n = 8
m = 8

ban_co =  [[ [] for i in range(n)] for j in range (m)]


# 0 - m
for x in range(m) :
    # 0-n
    for y in range(n) : 
        if (((n*x)+(y)) %2  == 0 and x%2 ==0 ) or(((n*x)+(y)) %2  != 0 and x%2 !=0 ) :
            ban_co[x][y] = "trắng"
        else:
            ban_co[x][y] = "đen"


for comlumn in ban_co:
    print(comlumn)