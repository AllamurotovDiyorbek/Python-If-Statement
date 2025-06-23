a=input("Raqamni kirting: ")
d=a[:2]
if d=="90" or d=="91":
    print("Ucell")
elif d=="93" and d=="94":
    print("Beeline")
elif d=="95" and d=="97":
    print("Uzmobile")
elif d=="88" and d=="99":
    print("Mobiuz")
else:
    print("Noma`lum operator")