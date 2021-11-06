code = open("program.wdttsdetiui", "r")
code = code.readlines()

py = ""

# PARSING
for i in range(len(code)-1):
  code[i] = code[i][:-1]
for i in range(len(code)):
  code[i] = code[i].split()
for i in range(len(code)):
  for j in range(len(code[i])):
    try:
      code[i][j] = int(code[i][j])
    except ValueError:
      pass

depth = 0
usesTowel = False

for i in code:
  if i[0] == "towel":
    usesTowel = True

if usesTowel:
  py += "import random as r\n"
py += "mem = 0\n\n"

del usesTowel

for i in code:
  if i[0] == "make":
    py += "stack" + str(i[1]) + " = []"
  elif i[0] == "push":
    py += "stack" + str(i[2]) + ".append(" + str(i[1]) + ")"
  elif i[0] == "pop":
    py += "stack" + str(i[1]) + ".pop()"
  elif i[0] == "towel":
    py += "mem = r.randint(" + str(i[1]) + "," + str(i[2]) + ")"
  elif i[0] == "print":
    if i[1] == "mem":
      py += "print(mem, end='')"
    else:
      py += "print(stack" + str(i[1]) + "[-1], end='')"
  elif i[0] == "letter":
    if i[1] == "mem":
      py += "print(chr(mem), end='')"
    else:
      py += "print(chr(stack" + str(i[1]) + "[-1]), end='')"
  elif i[0] == "add":
    py += "mem += stack" + str(i[1]) + "[-1]"
  elif i[0] == "input":
    py += "try:\n\tmem = int(input('> '))\nexcept ValueError:\n\tmem = 0"
  elif i[0] == "while":
    if i[1] == "mem":
      py += "while False:"
    else:
      py += "while stack" + str(i[1]) + "[-1] != mem:"
    depth += 1
  elif i[0] == "end":
    depth -= 1
  else:
    print("what kinda instruction is", str(i[0]) + "?")
    for j in ["make", "push", "pop", "towel", "print", "letter", "add", "input", "while", "end"]:
      if j in i[0]:
        print("also i think you forgot a space somewhere")
    exit()
  py += "\n" + "\t"*depth

if depth != 0:
  print("while/end depth unbalanced")
  exit()

exec(py)

print()