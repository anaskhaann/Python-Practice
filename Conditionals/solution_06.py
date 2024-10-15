# Choose a mode of transportation based on the distance (e.g., <3 km: Walk, 3-15 km: Bike, >15 km: Car).

distance=int(input("Enter the Distance in KiloMeters: "))

if distance <3:
    print("Walk to the Distance")
elif distance <=15:
    print("Take A Bike")
else:
    print("Take A Car")