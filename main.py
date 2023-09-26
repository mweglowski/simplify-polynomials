def simplify(poly):
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
  for i in range(values_len):
    if i == special_chars_len and poly[0] not in ['-', '+']:
      values[-i - 1] = '+' + "".join(sorted(values[-i - 1]))
    else:
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

  # CREATING FINAL VALUES DICTIONIARY
  # FIRSTLY ENTER NEGATIVES, THEN ADD POSITIVES
  final_values_dict = {}
  for v in negatives:
    if v in final_values_dict:
      final_values_dict[v] -= 1
    else:
      final_values_dict[v] = -1

  for v in positives:
    if v in final_values_dict:
      final_values_dict[v] += 1
    else:
      final_values_dict[v] = 1

  # SORTING LIKE IN NORMAL MATH EQUATION NOT ONLY ALPHABETICALLY BUT ALSO BY LENGTH
  final_values = list(final_values_dict.items())
  final_values_len = len(final_values)
  for i in range(final_values_len - 1):
    for j in range(final_values_len - 1):
      if len(final_values[j][0]) != len(final_values[j + 1][0]):
        if len(final_values[j][0]) > len(final_values[j + 1][0]):
          final_values[j], final_values[j + 1] = final_values[j + 1], final_values[j]
      else:
        if final_values[j][0] > final_values[j + 1][0]:
          final_values[j], final_values[j + 1] = final_values[j + 1], final_values[j]

  result = ""
  for k, v in final_values:
    if v > 0:
      if v == 1:
        result += "+" + k
      else:
        result += "+" + str(v) + k
    elif v < 0:
      if v == -1:
        result += "-" + k
      else:
        result += str(v) + k
    else:
      continue

  if result[0] == '+':
    result = result[1:]
  
  return result

print(simplify("-6bac+2ab-4a+b-c+5acb-8a+9ba+2c-9cb"))