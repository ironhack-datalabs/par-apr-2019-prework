# Assign spell power lists to variables

gandalf = [10, 11, 13, 30, 22, 11, 10, 33, 22, 22]
saruman = [23, 66, 12, 43, 12, 10, 44, 23, 12, 17]

gandalf_len = len(gandalf)
saruman_len = len(saruman)

# Assign 0 to each variable that stores the victories

gandalf_victories = 0
saruman_victories = 0

# Execution of spell clashes

for i in range(0,gandalf_len):
    if gandalf[i] > saruman[i]:
        gandalf_victories +=1
    elif gandalf[i] < saruman [i]:
        saruman_victories +=1
    else:
        gandalf_victories += 1
        saruman_victories += 1


if gandalf_victories == saruman_victories:
    print('Ties')
elif gandalf_victories > saruman_victories:
    print('Gandalf wins')
else:
    print('Saruman wins')
