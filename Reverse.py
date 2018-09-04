def main(y):
	z = 0
	x = y
	
	while y > 0:
		z = abs(y % 10) + abs(z * 10)
		y = abs(y // 10)
		
	print(z)

if __name__ == "__main__":
	x = input("Input a number  ")
	if x.isdigit():
		y = int(x)
	else:
		print("ERROR 612: Only INT Values Accepted")
		raise SystemExit
	main(y)