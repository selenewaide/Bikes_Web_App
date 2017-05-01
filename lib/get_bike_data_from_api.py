#!/usr/bin/env python3

import time
import datetime
import requests

def main():
    dP = dataPull()
    dP.timer()
    return

class dataPull(object):
    '''
    Gets bike data using api at 15 minute intervals from jcdecaux.com.
    '''
    def __init__(self):
        '''
        Constructor
        '''
    # get bike data
    def getBike(self, filestamp):
        srcdata = requests.get('https://api.jcdecaux.com/vls/v1/stations?contract=Dublin&apiKey=40d8ce05c637ce862bae2802f93241044b3a73d8')
        
        if (srcdata.status_code != 200):
            print("Error - did not receive status code 200 from Dublin Bikes!")
        
        else:
            
            # Now concatenate the time stamp with .JSON extention to create a valid filename
            filename = filestamp + "_bikes.JSON"
            
            # Now write this file to disk
            filehandle = open(filename, 'w')
            filehandle.write(srcdata.text)       # TypeError: write() argument must be str, not Response
            filehandle.close()
        return
    
    
    # every 15 minutes for 2 weeks
    def timer(self):
        counter = 0
        # Note - requests should not be more than once every 10 minutes
        # This timer will be used to prevent excessive calls to the bikes API
        while (counter <= 1344):          # This is for testing phase only, will change to a large number when proven
            filestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
            gW = dataPull()  
            # Calls the pullBikes class to execute a current bikes pull
            gW.getBike(filestamp)
            print("sleeping for 15 mins_", filestamp)
            time.sleep(900)           # Timing function waits 15 mins after triggering the data pull
            counter += 1    
            
if __name__ == '__main__':
    main()