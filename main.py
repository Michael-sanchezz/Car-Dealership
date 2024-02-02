import dealership as deal

stored1 = []
stored2 = []
toyota = deal.truck("toyota", 10000, 45000)
ford = deal.truck("ford", 20080, 50000)
chevy = deal.truck("chevy", 30000, 45000)
harley = deal.motorcycle("Harley", 200, 45000, 200)
ducati = deal.motorcycle("Ducati", 1080, 50000, 180)
honda = deal.motorcycle("Honda", 2000, 45000, 150)

vehicle_choice = "b"
weight = True
while weight:
    vehicle_choice = input("would you like to view bikes or trucks? b/t or n to exit ")
    if vehicle_choice == "b":
        stored1 = harley
        print(f'1: {harley.make}: with {harley.miles} and a top speed of {harley.top} costs ${harley.price}')
        print(f'2: {ducati.make}: with {ducati.miles} and a top speed of {ducati.top} costs ${ducati.price}')
        print(f'3: {honda.make}: with {honda.miles} and a top speed of {honda.top} costs ${honda.price}')
        compare = input("would you like to compare one of these vehicles today? y/n ")
        if compare == "y":
            which_vehicle = int(input("which vehicle would you like to compare? (please select number) "))
            if which_vehicle == 1:
                print("harley added!")
                stored1 = harley
            elif which_vehicle == 2:
                print("ducati added!")
                stored1 = ducati
            elif which_vehicle == 3:
                print("honda added!")
                stored1 = honda
        elif compare == "n":
            print("ok")
        compare_two = input("would you like to compare your vehicles now? y/n ")
        if compare_two == "y":
            if not stored1:
                print("list 1 is empty")
            elif not stored2:
                print("list 2 is empty!")
            else:
                print(f'{stored1.make}: with {stored1.miles} miles costs ${stored1.price}')
                print(stored1.make_noise())
                print(f'{stored2.make}: with {stored2.miles} miles costs ${stored2.price}')
                print(stored2.make_noise())
        else:
            print("ok")
    elif vehicle_choice == "t":
        print(f'1: {toyota.make}: with {toyota.miles} costs ${toyota.price}')
        print(f'2: {ford.make}: with {ford.miles} costs ${ford.price}')
        print(f'3: {chevy.make}: with {chevy.miles} costs ${chevy.price}')
        compare = input("would you like to compare one of these vehicles today? y/n ")
        if compare == "y":
            which_vehicle = int(input("which vehicle would you like to compare? (please select number) "))
            if which_vehicle == 1:
                print("toyota added!")
                stored2 = toyota
            elif which_vehicle == 2:
                print("ford added!")
                stored2 = ford
            elif which_vehicle == 3:
                print("chevy added!")
                stored2 = chevy
        elif compare == "n":
            print("ok")
        compare_two = input("would you like to compare your vehicles now? y/n ")
        if compare_two == "y":
            if not stored1:
                print("list 1 is empty!")
            elif not stored2:
                print("list 2 is empty!")
            else:
                print(f'{stored1.make}: with {stored1.miles} miles costs ${stored1.price}')
                print(stored1.make_noise())
                print(f'{stored2.make}: with {stored2.miles} miles costs ${stored2.price}')
                print(stored2.make_noise())
                print("thank you and have a nice day")
        else:
            print("okay!")

    elif vehicle_choice == "n":
        break
    else:
        print("invalid answer try again")

purchase = int(input("would you like to purchase a selected vehicle? 1 or 2 "))
if purchase == 1:
    print(f"you purchased a {stored1.make} for ${stored1.price}!")
elif purchase == 2:
    print(f"you purchased a {stored2.make} for ${stored2.price}!")

