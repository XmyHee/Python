i = 0
while i < 9:
	i += 1
	#创建一个内层循环来控制图形的宽度
	j=0
	while j < i:
		j += 1
		print(f"{j}*{i}={i*j} ",end="")
	print()