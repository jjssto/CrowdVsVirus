import csv

class WriteToCSV:

    def __init__(self, file_name):
        self.file_name = file_name

    def write( self, data_list, colnames = ''):
        '''write the csv line by line'''
        with open( self.file_name, 'w', newline='' ) as f:
            out = csv.writer(f, dialect = 'unix' )
            if colnames != '':
                out.writerow(colnames)
            for element in data_list :
                out.writerow(element)
