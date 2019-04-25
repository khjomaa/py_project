from time import strftime, sleep
   
while True:
    try:
        print(strftime("%H:%M:%S"), end='\r')
        sleep(1)
    except KeyboardInterrupt as e:
        print("", end='\r', flush=True)
        print("Bye Bye...")
        exit(0)
