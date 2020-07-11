import os
import csv



def logsanitizer(source_dir, target_dir, string2replaceCSV):
    source_root = source_dir
    target_root = target_dir
    
    #Get string to replace from CSV File and store it into dictionary

    string2replace = {}
    with open(string2replaceCSV) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count > 0:
                string2replace[row[0]] = row[1]
            line_count = line_count + 1
        
    for source_directory, dirnames, files in os.walk(source_root):

        target_directory = source_directory.replace(source_root, target_root)
        #Create Target Directory
        #print(f'Debug 001: {source_directory}')
        if os.path.exists(target_directory) == False:
            os.mkdir(target_directory)

        #loop through all files in the same source directory
        for file in files:
            #Construct Source File and read its contents 
            source_file = source_directory + "\\" + file
            #print(f'Debug 002: {source_file}')
            with open(source_file, 'r+', encoding="utf8") as s:
                content = s.read()
            #Construct Target File
            target_file = target_directory + "\\" + file
            print(f'Debug 003: {target_file}')
            with open(target_file, 'w+', encoding="utf8") as t:
                #t.write(content.replace('10.208.43.22', 'x.x.x.22'))
                #Replace content for certain string with target string
                for str_source in string2replace:
                    content = content.replace(str_source, string2replace[str_source])
                t.write(content)
    return

source_root = "C:\\01WorkingFiles\\python\\LogSanitizer\\Source"
target_root = "C:\\01WorkingFiles\\python\\LogSanitizer\\Target"
string2replace = 'string2replacewith.csv'

logsanitizer(source_root,target_root, string2replace)
