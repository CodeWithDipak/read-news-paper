# Read news paper for me

## modules used:
* requests
* json
* pywin32

I have created speak function which read the string, given as an argument to the function. I have used request module to get request from newsapi.org website with the help of api key. This data basically is in the form of json format, so I used json module to parsed the data and convert it into the text file. Then load that data in the python dictionary with help of json module. And finally passed that data to the speak function. 