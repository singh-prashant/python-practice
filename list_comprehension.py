x = int(input())
y = int(input())
z = int(input())
sum_not = int(input())
print ([[xx,yy,zz] for xx in range(0,x+1) for yy in range(0,y+1) for zz in range(0,z+1) if (xx+yy+zz != sum_not)])
