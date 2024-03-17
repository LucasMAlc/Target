def fibonacci(n):
  if n <= 1:
    return n
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)

def is_fibonacci(n):
  i = 0
  while fibonacci(i) <= n:
    if fibonacci(i) == n:
      return True
    i += 1
  return False

number = int(input("Digite um número: "))

if is_fibonacci(number):
  print(f"{number} pertence a sequência de Fibonacci.")
else:
  print(f"{number} não pertence a sequência de Fibonacci.")