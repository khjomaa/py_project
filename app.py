from time import strftime, sleep

def start_clock():
    while True:
        try:
            print(strftime("%H:%M:%S"), end='\r')
            sleep(1)
        except KeyboardInterrupt as e:
            print("", end='\r', flush=True)
            print("Bye Bye...")
            exit(0)

start_clock()