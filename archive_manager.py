"""archive_mangager.py
used for seaching for archive files in the filesystem and uncompressing them.
"""

__author__ = "Scott Truger (http://wwww.truger.net)"
__version__ = "$Revision: 0.2 $"
__date__ = "$Date: 2009/03 $"
__copyright__ = "Copyright (c) 2009 Scott Truger"
__license__ = "Python"

import os 
import sys
import fileinput
import datetime
import time
import shutil

class ArchiveManager:
  "searches filesystem for archives to decompress"

  def __init__(self, searchPath, storePath):
    self.searchPath = searchPath
    self.storePath = storePath
    
  def processRARlist(self, archiveList):
    curdate = datetime.datetime.now()
    for archive in archiveList:
      fileName = os.path.join(os.path.dirname(archive),"breadCrumb")
      command = "unrar e %s %s" % (archive, self.storePath) 
      os.system(command)
      f = open(fileName, "w")
      f.write(curdate.strftime("%Y.%m.%d"))
      f.close
	# TODO: log archive
    
  def findArchives(self, searchPath, cleanDays=90):
    """Finds all .rar files in the searchPath provided. If cleanDays is passed
    previously processed archieves will be deleted if it was processed more than
    cleanDays ago. If zero is passed for cleanDays archives will not be deleted.
    If nothing is passed for cleanDays the default of 90 days will be used."""
    
    archives = []
    for root, dirs, files in os.walk(searchPath):
      if not "breadCrumb" in files:
	for elem in files:
	  if (os.path.splitext(elem)[1] == ".rar"):
	    archives.append(os.path.join(root, elem))
      else:
	crumb = open(os.path.join(root, "breadCrumb"))
	print "found bread crumb: "
	processedDate = crumb.readline()
	if cleanDays > 0:
	  if self.laterThan(processedDate, cleanDays):
	    shutil.rmtree(root)
	
    return archives
    
  def laterThan(self, date, daysToClean):
    cleanIt = False
    #get cur time in seconds
    today = time.time()
    #get arch date
    dateCol = date.split(".")
    #conv arch date to tuple
    dateTuple = (int(dateCol[0]),int(dateCol[1]),int(dateCol[2]),0,0,0,0,0,0)
    #conv arch tuple to seconds
    archSec = time.mktime(dateTuple)
    # 86400 seconds in 1 day
    timeClean = 86400 * daysToClean
    if today > archSec + timeClean:
      cleanIt = True
    return cleanIt	

if __name__ =="__main__":
  searchPath = "/home/scott/Dev/archive_manager/test"
  storePath = "/home/scott/Dev/archive_manager/test/files"
  days = 30
  
  finder = ArchiveManager(searchPath, storePath)
  archives = finder.findArchives(searchPath, days)
  finder.processRARlist(archives)