# -*- coding: UTF-8 -*- 
# 定义车数
cars = 100

# 定义每辆车坐的人数
space_in_a_car = 4.0

# 定义司机数
drivers = 30

# 定义乘客数
passengers = 90

# 定义没有用到的车数
cars_not_driven = cars - drivers

# 定义用到的车数
cars_driven = drivers

# 定义总载客人数
carpool_capacity = cars_driven * space_in_a_car

# 定义每辆车平均载客人数
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available"
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "empty cars today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
