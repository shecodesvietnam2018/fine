"""
Theo luật giao thông đường bộ (2021) việc chạy quá tốc độ cho phép sẽ bị xử phạt:
- Với ô tô
	Phạt tiền từ 800,000 đồng đến 1,000,000 đồng đối với người điều khiển xe chạy quá tốc độ quy định từ 5 km/h đến dưới 10 km/h;

	Phạt tiền từ 3,000,000 đồng đến 5,000,000 đồng đối với người điều khiển xe chạy quá tốc độ quy định từ 10 km/h đến 20 km/h;

	Phạt tiền từ 6,000,000 đồng đến 8,000,000 đồng đối với người điều khiển xe chạy quá tốc độ quy định trên 20 km/h đến 35 km/h;

	Phạt tiền từ 10,000,000 đồng đến 12,000,000 đồng đối với người điều khiển xe chạy quá tốc độ quy định trên 35 km/h.
- Với xe máy
	Phạt tiền từ 200,000 đồng đến 300,000 đồng đối với người điều khiển xe chạy quá tốc độ quy định từ 5 km/h đến dưới 10 km/h;

 	Phạt tiền từ 600,000 đồng đến 1,000,000 đồng đối với người điều khiển xe chạy quá tốc độ quy định từ 10 km/h đến 20 km/h;

 	Phạt tiền từ 4,000,000 đồng đến 5,000,000 đồng đối với người điều khiển xe chạy quá tốc độ quy định trên 20 km/h.
Ngoài ra, nếu người vi phạm không có bằng lái xe sẽ bị phạt từ 800.000 đến 1.200.000 đồng đối với xe máy, 4.000.000 đến 6.000.000 đồng đối với ô tô.
	
Hãy viết một chương trình để tính số tiền tối thiểu và số tiền tối đa nếu vi phạm những điều trên.
"""

min_fine = 0
max_fine = 0

vehicle = input("What vehicle are you driving (Car/Motorcycle)? ")
while vehicle != "Car" and vehicle != "Motorcycle":
  	vehicle = input("What vehicle are you driving (Car/Motorcycle)? ")

has_license = input("Has license (y/n)? ")
while has_license != "y" and has_license != "n":
  	has_license = input("Has license (y/n)? ")

if has_license == "y":
  	has_license = True
else:
  	has_license = False

speed = float(input("Your speed: "))
while speed < 0:
  	speed = float(input("Your speed: "))

if vehicle == "Car":
  	if speed >= 5 and speed < 10:
    	min_fine = 800000
    	max_fine = 1000000
  	elif speed >= 10 and speed < 20:
    	min_fine = 3000000
    	max_fine = 5000000
  	elif speed >= 20 and speed < 35:
    	min_fine = 6000000
    	max_fine = 8000000
  	else:
   	 	min_fine = 10000000
    	max_fine = 12000000

  	if not has_license:
    	min_fine = min_fine + 4000000
    	max_fine = max_fine + 6000000
	else:
  		if speed >= 5 and speed < 10:
    		min_fine = 200000
    		max_fine = 300000
  		elif speed >= 10 and speed < 20:
    		min_fine = 600000
    		max_fine = 1000000
  		else:
    		min_fine = 4000000
    		max_fine = 5000000

  	if not has_license:
    	min_fine = min_fine + 800000
    	max_fine = max_fine + 1200000

print("Minimum fine: " + str(min_fine))
print("Maximum fine: " + str(max_fine))
