# list of available cars and their prices at Henry Motors
cars = {
'Lamborghini Aventador' : 89948,
'Lamborghini Urus' : 70004,
'Bugatti Chiron' : 88765,
'Bugatti Divo' : 98655,
'Ferrari 250 GTO' : 298939,
'Ferrari 599 GTO' : 469903,
'Toyota Landcruiser' : 45637,
'Toyota Corolla' : 3894,
'Toyota Rav4': 5800,
'Toyota Prado' : 34700,
'Lexus Lx570' : 68000,
'Lexus Gx 460' : 78300,
'Mazda 3' : 56000,
'Mazda 6' : 83400,
'Ford Focus' : 5700,
'Ford Explorer' : 7600,
'Ford Escape' : 3608,
'Jeep Wrangler' : 65000,
'Jeep Compass' : 69500,
'Jeep Grand Cherokee' : 57000,
'Chevrolet Cruze' : 48000,
'Chevrolet Equinox' : 56000,
'Chevrolet Camaro' : 97006,
'Tesla Cybertruck' : 89000,
'Tesla Model S' : 47600,
'Tesla Model Y' : 52000,
'Hyundai Elantra' : 47000,
'Hyundai Tucson' : 36000,
'Hyundai Accent' : 28000,
'Audi R8' : 56000,
'Audi A3' : 74000,
'Audi Q5' : 66000,
'Mitsubishi Pajero' : 20000,
'Mitsubishi Outlander' : 15000,
'Honda Civic' : 26500,
'Honda Accord' : 46000,
'Honda CR-V' : 35000,
'Honda Pilot' : 38000,
'Bentley Bentayga' :470000,
'Land rover Defender' : 50000,
'Range Rover Sport' : 780000,
'Range Rover Evoque' : 5650000,
'Lincoln Navigator' : 70000,
'Rolls-Royce Phantom' : 589000,
'Rolls-Royce Cullinan' : 999000,
'Rolls-Royce Ghost' : 680000,
'Infiniti QX60' :34000,
'Infiniti Q60' :29000,
'BMW X3' : 55000,
'BMW X4' : 60000,
'BMW X3' : 55000,
'BMW 530i' : 75000,
}  
carName = input("Enter Your Preferred Car's Name': ")
if carName in cars:
    print("Yes Your Car is Available")
    carPrice = cars[carName]
    print(f"The price of {carName} is ${carPrice}.")
else:   
    print(f"Sorry,{carName} is not available") 
# Github link https://github.com/okaihenry/computer-programming-