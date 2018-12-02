def main():
  data = open('./aoc2018-day2.data', "r")

  strings = []
  for line in data:
    strings.append(line[:-1])

  for i in range(0, len(strings), 1):
    for j in range(i + 1, len(strings), 1): # TODO: clumsy
      if compare(strings[i], strings[j]) == 1:
        get_common_characters(strings[i], strings[j])
        exit()

def compare(str1, str2):
  hamming_distance = 0
  for i in range(0, len(str1), 1):
    if str1[i] != str2[i]:
      hamming_distance = hamming_distance + 1
  
  return hamming_distance

def get_common_characters(str1, str2):
  output = ''
  for i in range(0, len(str1), 1):
    if str1[i] == str2[i]:
      output = output + str1[i]
  
  print(output)

if __name__ == '__main__':
  main()