#Passed:1. You should have a variable named distance_mi.
#Passed:2. You should assign a number to your distance_mi variable.
#Passed:3. You should have a variable named is_raining.
#Passed:4. You should assign a boolean to your is_raining variable.
#Passed:5. You should have a variable named has_bike.
#Passed:6. You should assign a boolean to your has_bike variable.
#Passed:7. You should have a variable named has_car.
#Passed:8. You should assign a boolean to your has_car variable.
#Passed:9. You should have a variable named has_ride_share_app.
#Passed:10. You should assign a boolean to your has_ride_share_app variable.
#Passed:11. You should use at least one if statement.
#Passed:12. You should use at least one elif branch in your program.
#Passed:13. You should use at least one boolean operator (and, or, or not) in your code.
#Passed:14. You should use the print() function to display the result.
#Passed:15. When distance_mi is a falsy value, the program should print False.
#Passed:16. When the distance is 1 mile or less and it is not raining, the program should print True.
#Passed:17. When the distance is 1 mile or less and it is raining, the program should print False.
#Passed:18. When the distance is between 1 mile (excluded) and 6 miles (included), and it is raining with no bike, the program should print False.
#Passed:19. When the distance is between 1 mile (excluded) and 6 miles (included), it is not raining but no bike is available, the program should print False.
#Passed:20. When the distance is between 1 mile (excluded) and 6 miles (included), a bike is available, and it is not raining, the program should print True.
#Passed:21. When the distance is greater than 6 miles and a ride share app is available, the program should print True.
#Passed:22. When the distance is greater than 6 miles and a car is available, the program should print True.
#Passed:23. When the distance is greater than 6 miles and no car nor a ride share app is available, the program should print False.


distance_mi = 1
is_raining = False
has_bike = False
has_car = False
has_ride_share_app = False

if not distance_mi:
    print("False")
    
elif distance_mi <= 1 and not is_raining:
    print("True")

elif distance_mi <= 1 and is_raining:
    print("False")

elif distance_mi > 1 and distance_mi <= 6 and is_raining and not has_bike:
    print("False")

elif distance_mi > 1 and distance_mi <= 6 and not is_raining and not has_bike:
    print("False")

elif distance_mi > 1 and distance_mi <= 6 and has_bike and not is_raining:
    print("True")

elif distance_mi > 6 and has_ride_share_app:
    print("True")

elif distance_mi > 6 and has_car:
    print("True")

elif distance_mi > 6 and (not has_car or not has_ride_share_app):
    print("False")