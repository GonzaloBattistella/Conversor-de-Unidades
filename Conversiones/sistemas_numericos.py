def decimal_a_binario(decimal):

  binary = ""
  
  while decimal > 0:
    binary = f"{decimal % 2}{binary}"
    decimal //= 2
  
  return "0" if binary == "" else binary

def binario_a_decimal(binary: str):
  return int(binary, 2)

