# 5)
def reverse_string(string):
  reversed_string = ""
  for i in range(len(string) - 1, -1, -1):
    reversed_string += string[i]
  return reversed_string

string = input("Digite o texto: ")

reversed_string = reverse_string(string)

print(f"O resultado é: {reversed_string}")
