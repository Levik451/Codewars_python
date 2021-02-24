'''
Create a function (or write a script in Shell) that takes an integer as an argument
and returns "Even" for even numbers or "Odd" for odd numbers.
'''

# Мое стандартное решение
def even_or_odd(number):
  if number % 2 == 0:
    return "Even"
  else:
    return "Odd"
print(even_or_odd(12))

# Красивое решение
# def even_or_odd(number):
#   return ["Even", "Odd"][number % 2]

# Более красивое решение
# def even_or_odd(number):
#     return 'Odd' if number % 2 else 'Even'
# print(even_or_odd(12))

# Решение №1 через lambda функцию
# even_or_odd = lambda number: "Odd" if number % 2 else "Even"

# Решение №2 через lambda функцию
# even_or_odd = lambda n: ["Even","Odd"][n % 2]
