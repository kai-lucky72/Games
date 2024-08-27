print("""
Begin - to play the game""")
x = input("> ").lower()
i = 0
car_started = False
car_stopped = False
if x == "begin":
    print("""
start - to start the car
stop - to stop the car
quit - to quit""")
    while i < 3:
        y = input("> ").lower()
        if y == "start":
            if car_started == False:
                print("Car started...Ready to go!")
                car_stopped = False
                car_started = True
            else:
                print("the car has already started")


        elif y == "stop":
            if car_stopped == False:
                print("Car stopped.")
                car_started = False
                car_stopped = True

            else:
                print("the car has already stopped")

        elif y == "quit":
            break

else:
    print("i dont understand that!")
