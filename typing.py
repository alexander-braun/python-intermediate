def caesar(text: str, key: int) -> str:
  result: str = ""
  for char in text:
    c: int = ord(char)
    print(c)
    enc_char: str = chr(c + key)
    if char == " ":
      enc_char = " "
    result += enc_char
  return result

print(caesar(input("Type a word: "), int(input("Type a shift: "))))
