from decimal import Decimal
import math

# Exercise 1
list_1 = ["knight", "rook", "king", "queen", "pawn", "bishop"]
tuple_1 = ("knight", "rook", "king", "queen", "pawn", "bishop")
float_1 = 3.14
integer_1 = 1
decimal_1 = Decimal(3.141592653589793238462643383279)
dictionary_1 = {
    "knight" : 3,
    "rook" : 5,
    "king" : 10,
    "queen": 9,
    "pawn" : 1,
    "bishop" : 3
}

print("Exercise 1")
print(list_1)
print(tuple_1)
print(float_1 )
print(integer_1)
print(decimal_1)
print(dictionary_1)

# Exercise 2
float_rounded_up = math.ceil(float_1)
print("\nExercise 2")
print(float_rounded_up)

# Exercise 3
float_sqrt = math.sqrt(float_1)
print("\nExercise 3")
print(float_sqrt)

# Exercise 4
print("\nExercise 4")
print(dictionary_1["knight"])

# Exercise 5
print("\nExercise 5")
print(tuple_1[1])

# Exercise 6
print("\nExercise 6")
list_1 += ["castle"]
print(list_1)

# Exercise 7
print("\nExercise 7")
list_1[0] = "horse"
print(list_1)

# Exercise 8
print("\nExercise 8")
list_1.sort()
print(list_1)

# Exercise 9
print("\nExercise 9")
tuple_1 += ("castle",)
print(tuple_1)