poly = "-a+2ba-3a+6bca"

def compute(poly):
  v = poly.split()
  special_chars = [c for c in poly if c in ['-', '+']]
  values = []
  string = ""
  for i in range(len(poly)):
    if poly[i] not in special_chars:
      string += poly[i]

    if i == len(poly) - 1:
      values.append(string)
      string = ""
      continue

    try:
      if poly[i + 1] in special_chars:
        values.append(string)
        string = ""
    except:
      string = ""

  # SORTING VALUES
  values_len = len(values)
  special_chars_len = len(special_chars)
  for i in range(special_chars_len):
    values[-i - 1] = special_chars[-i - 1] + "".join(sorted(values[-i - 1]))

  # DIVIDING VALUES INTO POSITIVES AND NEGATIVES
  # DUPLICATING VALUES TO REMOVE NUMBERS
  negatives = []
  positives = []
  for value in values:
    # FINDING NUM
    n = 1
    for char in value:
      if char.isnumeric():
        n = int(char)
        break

    next_value = value[1:]
    if next_value[0].isnumeric():
      next_value = next_value[1:]

    if '-' in value:
      for _ in range(n):
        negatives.append(next_value)
    else:
      for _ in range(n):
        positives.append(next_value)

  print(values)
  print(negatives)
  print(positives)


compute(poly)