import neurio
import sys
import pprint
from datetime import datetime, timedelta
import my_keys
import time


# Setup authentication & create client that can authenticate itself -------------------------------
tp = neurio.TokenProvider(key=my_keys.key, secret=my_keys.secret)
nc = neurio.Client(token_provider=tp)


#functions for specifying the time interval -------------------------------------------------------

def getMinuteInterval(minutes):
    return (datetime.utcnow()-timedelta(minutes=minutes)).replace(microsecond=0).isoformat()

def getHourInterval(hours):
    return (datetime.utcnow()-timedelta(hours=hours)).replace(microsecond=0).isoformat()

def getSecondInterval(seconds):
    return (datetime.utcnow()-timedelta(seconds=seconds)).replace(microsecond=0).isoformat()

def specifyTimeInterval(unit, number):
    interval = None
    frequency = None
    if unit == "hours":
        interval = getHourInterval(number)
        frequency = number * 60
        frequency -= frequency % 5
    elif unit == "minutes":
        interval = getMinuteInterval(number)
        frequency = number - number%5
    elif unit == "seconds":
        interval = getSecondInterval(number)
        frequency = number - number%5
    else:
        raise ValueError('Invalid unit')
    return interval, frequency


#functions to retrieve data from the neurio sensor ------------------------------------------------

print "\nNEURIO DATA"

def queryPastHour():
    timeinterval, frequency = specifyTimeInterval("hours", 1)
    data = nc.get_samples(sensor_id=my_keys.sensor_id, start=timeinterval,
        granularity="hours", frequency=1)
    return data


def queryPastDay():
    timeinterval, frequency = specifyTimeInterval("hours", 24)
    data = nc.get_samples(sensor_id=my_keys.sensor_id, start=timeinterval,
        granularity="hours", frequency=1)
    return data


def queryPastWeek():
    timeinterval, frequency = specifyTimeInterval("hours", 168)
    data = nc.get_samples(sensor_id=my_keys.sensor_id, start=timeinterval,
        granularity="hours", frequency=1)
    return data


print "data for the past hour:\n", queryPastHour()
print "data for the past day:\n", queryPastDay()
print "data for the past week:\n", queryPastMonth()



