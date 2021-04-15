# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


import time
start = time.time()
def sorting(filename):
  infile = open('20k.txt')
  words = []
  for line in infile:
    temp = line.split()
    for i in temp:
      words.append(i)
  infile.close()

  def partition(words, low, high):
    i = (low - 1)
    pivot = words[high]

    for j in range(low, high):

      if words[j] <= pivot:
        i = i + 1
        words[i], words[j] = words[j], words[i]

    words[i + 1], words[high] = words[high], words[i + 1]
    return (i + 1)

  def quickSort(words, low, high):
    if len(words) == 1:
      return words
    if low < high:

      pi = partition(words, low, high)


      quickSort(words, low, pi - 1)
      quickSort(words, pi + 1, high)

  n = len(words)
  quickSort(words, 0, n - 1)
  print("Sorted words list is:")
  for i in range(len(words)):
    print("%s" % words[i])

  outfile = open("result.txt", "w")
  for i in words:
    outfile.writelines(i)
    outfile.writelines("\n")
  outfile.close()
sorting("sample.txt")

end = time.time()
print("Execution time:", end-start)