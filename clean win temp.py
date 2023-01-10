import os

for j in {r'C:\Users\Madhav\AppData\Local\Temp',r'C:\Windows\Temp'}:
	for i in os.listdir(j):
		file = os.path.join(j,i)
		user = True
		while user:
			try:
				os.remove(file)
				os.rmdir(file)
				user = False
			except Exception as e:
				print(f"Failed. REASON: {e}")
				user = input("\ntry again? (True/False)")


print("DONE!")