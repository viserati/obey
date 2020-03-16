# Iterating over a list in Python.

scores = [50, 60, 58, 50, 52, 54, 48, 69,34, 61, 55,
          51, 52, 44, 51, 69, 64, 66, 55, 52,
          46, 31, 57, 52, 44, 18, 41, 53, 55,
          61, 51, 44 ]

i = 0
length = len(scores)
while i < length:
    print ('Bubble solution #' + str(i),  'score:', scores[i])
    i = i + 1
