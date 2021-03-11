from datetime import datetime

# datetime object containing current date and time
now = datetime.now()


# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)	


print("hello, " + dt_string)

f = open("newfile.txt", "a")
f.write("\n The file was updated at "+ dt_string)
f.close()
