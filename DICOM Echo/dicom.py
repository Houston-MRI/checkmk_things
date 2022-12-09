import os
import sys
import re

aetitle = sys.argv[1]
dchost = sys.argv[2]
dcport = sys.argv[3]

def checkDCM(title, host, port):
	query = title + '@' + host + ':' + port
	svc = 'DICOM ECHO - ' + query
	success = 'Connected to ' + query + ' in'

	x = os.popen('/etc/dcm4che/2.0.15/bin/dcmecho ' + query).read()

	test = x.find(success)

	if(test != -1):
		status = '0'
		msg = 'DICOM OK'
		qtime = re.search('([0-9]{1,3}.[0-9]{1,3}s)', x)
		qtime = qtime.group(1)
		qtime = qtime.replace('s', '')
		qtime = 'response=' + qtime
	else:
		status = '2'
		try:
			error = re.search('(?<=- ).*$', x)
			error = error.group(0)
			msg = 'DICOM ERROR: ' + error
		except:
			msg = 'DICOM ERROR'
		finally:
			qtime = "response=NULL"

	cmkstat = status + ' "' + svc + '" ' + qtime + ' ' + msg

	print(cmkstat)
	return(cmkstat)


checkDCM(aetitle, dchost, dcport)
