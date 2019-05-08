'''
Created on Oct 23, 2015

@author: uidj6043
'''
from datetime import date
from dateutil import rrule
import datetime
import time


class MksDateCalculations(object):
    
    def calculateDiffDays(self, createdDate):
        dy = time.strftime("%Y")
        dm = time.strftime("%m")
        dd = time.strftime("%d")
        todayDate = date(int(dy),int(dm),int(dd))
        #todayDate = date(2015,12,29)
        result = len(list(rrule.rrule(rrule.DAILY,dtstart=createdDate,until=todayDate - datetime.timedelta(days=1),byweekday=(rrule.MO, rrule.TU, rrule.WE, rrule.TH, rrule.FR))))
        #giani
		return result
