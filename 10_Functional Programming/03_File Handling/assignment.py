file_path = "C:\\Users\\peterdav000\\POC_Sem2_Assignments\\10_Functional Programming\\03_File Handling\\assignment.py"

try:
    stream = open(file_path)
    print(stream.read())
    print(stream.close())
    #YOUDO print to consule using stream.read()
    #YOUDO don't forget to close the stream
except Exception as e:
    print('An error ocurred:, e')
##YOUDO rest of the program for reading and printing to the console
##remember pass in file_path to open 
