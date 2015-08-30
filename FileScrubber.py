""" This is the FileScrubber ServiceNow Utility, for analyzing the horrible data sent in to CMDB
Hope it works out
"""
from datetime import datetime
# Data Division

now = datetime.now()
version = "1.0L"
rec_cnt = 0
SN_url = "service-now.com"
HighSNqual = " "



#note version must be declared first for this to work

#Console messages
welcome_message = "Welcome to CMDB File Analyzer, version %s, brought to you by Bitseve Software"  % (version)
#finished_message = "CMDB File Analyzer finished. A total of %s records were processed. " % (rec_cnt)



# Procedure Division

# Initialize processing

print welcome_message

#Get ServiceNow instance qualifier
#HighSNqual = raw_input('Please enter top ServiceNow instance qualifier:')
#print "Your ServiceNow instance is https://%s." % (HighSNqual) + SN_url 





#This is how increment record in Python
#rec_cnt += 1



# End processing


print "CMDB File Analyzer finished. A total of " + str(rec_cnt) + " records were processed. Finished on %s/%s/%s %s:%s:%s" % (now.month,now.day,now.year,now.hour, now.minute, now.second)




