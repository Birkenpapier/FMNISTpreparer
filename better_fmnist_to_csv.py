import pandas as pd
import csv

# distinguish between test and train files
distinguish = False

mnist_orig_file = 'mnist_test_orig.csv'
mnist_orig_file_without_labels = 'mnist_test_orig_manip.csv'
labels = 'test_labels.csv'

if distinguish:
    mnist_orig_file = 'mnist_train_orig.csv'
    mnist_orig_file_without_labels = 'mnist_train_orig_manip.csv'
    labels = 'train_labels.csv'

# read your original file
csvf = pd.read_csv(mnist_orig_file)

# get all thelabels
first_column = csvf.columns[0]
labels_csv = csvf[csvf.columns[0]]
labels = labels_csv.tolist()

# delete labels
csvf = csvf.drop([first_column], axis=1)
csvf.to_csv(mnist_orig_file_without_labels, index=False)

# save labels separately
file = open(labels, 'w+', newline ='')
 
with file:
    write = csv.writer(file)
    write.writerows(map(lambda x: [x], labels))
