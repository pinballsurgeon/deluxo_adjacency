import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

print("new changes")

rand = np.arange(50)*2

print(rand.shape)
print(type(rand))
print(rand)


fig = plt.figure(figsize=(22, 16))
gs = gridspec.GridSpec(1, 4)
ax1 = plt.subplot(gs[0])
ax2 = plt.subplot(gs[1])
ax3 = plt.subplot(gs[2])
ax4 = plt.subplot(gs[3])
#ax4 = plt.subplot(gs[-1, 0])
#ax5 = plt.subplot(gs[-1, -2])

#fig, ax = plt.subplots(2, 2, 2)

#ax_2 = fig.add_subplot(111)

min_val, max_val = 0, 15


arr1 = np.random.randint(0, 10, size=(max_val, max_val))
intersection_matrix = arr1
ax1.matshow(intersection_matrix, cmap=plt.cm.Blues)

arr2 = np.random.randint(0, 10, size=(max_val, max_val))
intersection_matrix_2 = arr2
ax2.matshow(intersection_matrix_2, cmap=plt.cm.GnBu)

arr3 = arr1@arr2
intersection_matrix_3 = arr3
ax3.matshow(intersection_matrix_3, cmap=plt.cm.GnBu)

arr4 = np.mean( np.array([ arr1, arr2 ]), axis=0 )
intersection_matrix_4 = arr4
ax4.matshow(intersection_matrix_4, cmap=plt.cm.GnBu)

for i in range(15):
    for j in range(15):
        c = intersection_matrix[j,i]
        ax1.text(i, j, str(c), va='center', ha='center')

for i in range(15):
    for j in range(15):
        c = intersection_matrix_2[j,i]
        ax2.text(i, j, str(c), va='center', ha='center')

for i in range(15):
    for j in range(15):
        c = intersection_matrix_3[j,i]
        ax3.text(i, j, str(c), va='center', ha='center') 

for i in range(15):
    for j in range(15):
        c = intersection_matrix_4[j,i]
        ax4.text(i, j, str(c), va='center', ha='center')                

