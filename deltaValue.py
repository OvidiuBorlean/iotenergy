import csv
with open('consumption.csv', newline='') as csvfile:
  reader = reversed(list(csv.reader(csvfile)))
  last_row = next(reader)
  deltaValue = last_row[-1]
  print(deltaValue)
  #elem = (str(last_row).split(','))
  #print(elem[2])
