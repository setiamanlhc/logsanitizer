# Introduction

This utility is to sanitize your Log Files 
by replacing sensitice information with any string that deemed insensitive and you can reference it back.
As teh sensitive information in one file are more than one, I use CSV file to define source string to search and target string to replace with.

This utility also can handle nested directory and multiple files in the same directory. It works by copying it from Source Directory to Target Directory so you can cross check with original file content to make sure that it will do the job correctly.

# CSV File Structure

As this utility can handle multiple string and dynamically search and replace at runtime, the CSV file is used to define sensitive information to replace with any string you would like to mask it. For Example you can define your IP Address 102.200.22.4 to be replaced with x.x.33.4.

Field Name | Description
---------- | ------------
Sourcce | Source string you would like to search
Target | String you would like to be replaced with

# Sample CSV File


    source,target
    10.1.20.22,"x.x.x.22"
    john@mycompany.com,user01@abc.com
