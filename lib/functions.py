

# def greeting(name="Programmer"):
#   print(f"Hello {name}!")

# greeting("Bob")
# greeting("Sarah")
# greeting()

# def animal_with_superpower(animal):
#   def inner_function(superpower):
#     print(f'This {animal} has this {superpower}!')

#   return inner_function

# monkey_creator = animal_with_superpower("Monkey")

# monkey_creator("Banana Throw")
# monkey_creator("Tree Climb")


def func_with_endless_arguments(*args, **kwargs):
  print("The arguements are")
  print(args)
  print(kwargs)

func_with_endless_arguments(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
func_with_endless_arguments(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)
func_with_endless_arguments(num1=1, num2=2, num3=3)