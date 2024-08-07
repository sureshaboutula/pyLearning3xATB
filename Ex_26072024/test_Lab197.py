import csv
import pandas
import pandas as pd


class Test_CRUD(object):
    def test_update_1(self):
        #Read the file
        with open('pyLearning3xATB/Ex_26072024/userdata.csv') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                print(row[0],row[1])

    def test_update_2(self):
        df = pd.read_csv('pyLearning3xATB/Ex_26072024/userdata.csv')
        print(df)