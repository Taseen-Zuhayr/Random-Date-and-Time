import random
import time

def randate(startdate,enddate):
    print("To print a random date between start date and end date.")
    randomgenerator = random.random()
    dateformat = '%m/%d/%y'
    starttime = time.mktime(time.strptime(startdate,dateformat))
    endtime = time.mktime(time.strptime(enddate,dateformat))
    randomtime = starttime + randomgenerator * (endtime-starttime)
    randomdate = time.strftime(dateformat,time.localtime(randomtime))
    return randomdate
print("Random date : ",randate("1/1/2024","11/8/2024"))








