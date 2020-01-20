for i in range(1,101):
	flag=False
	tem=i	
	while (tem>0):
		if (tem%10==7 or tem==7):
			flag=True
		tem=int(tem/10)
	
	if (i%7!=0 and flag !=True):
		print(i)

