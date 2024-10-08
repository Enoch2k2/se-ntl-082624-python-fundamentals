
def print_result(callback):
  def inner_func(*args, **kwargs):
    print(f'The result is: {callback(*args, **kwargs)}')

  return inner_func

def multiply_by_3(callback):
  def inner_func(*args, **kwargs):
    return callback(*args, **kwargs) * 3
  
  return inner_func

@print_result
@multiply_by_3
def add_two_nums(num_1, num_2):
  return num_1 + num_2

@print_result
@multiply_by_3
def subtract_two_nums(num_1, num_2):
  return num_1 - num_2

# What decorators do behind the scenes
# add_two_nums = print_result(add_two_nums)

add_two_nums(1, 3)

subtract_two_nums(3, 2)