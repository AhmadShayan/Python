import os
import sys
import datetime

class CommandArgs:
    
    def date():
        arg = sys.argv
        a = arg[2::2]
        date = []
        for i in a:
            x = i.split('/')
            # y = [int(j) for j in x]
            z = date.append(x)
        return(date)

    def command():
        arg = sys.argv
        command = arg[1::2]
        return(command)
    
class WeatherData:
    
    def yearwiseFiles():
        files = os.listdir('weatherfiles')
        yearwise = []
        date = CommandArgs.date()
        
        for i in files: 
            if date[0][0] in i:
                yearwise.append(i)
        return(yearwise)
    
    def monthwiseFiles():
        files = WeatherData.yearwiseFiles()
        monthwise = []
        date = CommandArgs.date()
        
        x = datetime.datetime.strptime(date[0][1], '%m')
        month = x.strftime('%b')
        
        for i in files:
            if month in i:
                monthwise.append(i)
        return(monthwise)
    
    def getYearFileData():
        x = WeatherData.yearwiseFiles()
        data = []
        for i in x:
            with open('weatherfiles/'+i, 'r') as file:
                data.append(file.readline())
        return(data)
            
    def getMonthFileData():
        x = WeatherData.monthwiseFiles()
        with open ('weatherfiles/'+x[0], 'r') as file:
            data = file.readlines()
        return(data)        
        
class Calculations:
    pass

class Display:
    pass

data = WeatherData.getMonthFileData()
# data = WeatherData.getYearFileData()
print(data)
print(type(data))


    




           