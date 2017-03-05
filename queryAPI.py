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

#- live consumption power for 30 seconds:
# for x in range(30):
#     sample = nc.get_samples_live_last(sensor_id=my_keys.sensor_id)
#     print "   ", sample['consumptionPower']
#     time.sleep(1)


#print time for the past hour
timeinterval, frequency = specifyTimeInterval("hours", 1)
data = nc.get_samples(sensor_id=my_keys.sensor_id, start=timeinterval,
        granularity="minutes", frequency=frequency)
print "- comsumption power for the past hour:", data[0]['consumptionPower']

#print time for the past two hours
timeinterval, frequency = specifyTimeInterval("hours", 2)
data = nc.get_samples(sensor_id=my_keys.sensor_id, start=timeinterval,
        granularity="minutes", frequency=frequency)
print "- comsumption power for the past two hours:", data[0]['consumptionPower']

# #print time for the past day
# timeinterval, frequency = specifyTimeInterval("hours", 24)
# data = nc.get_samples(sensor_id=my_keys.sensor_id, start=timeinterval,
#         granularity="minutes", frequency=frequency)
# print "- comsumption power for the past day:", data[0]['consumptionPower']



