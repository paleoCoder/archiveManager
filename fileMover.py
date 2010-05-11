"""fileMover.py
matches files with defined regular expressions and moves them
to appropriate folder
"""
__author__ = "Scott Truger (http://wwww.truger.net)"
__version__ = "$Revision: 0.1 $"
__date__ = "$Date: 2009/09 $"
__copyright__ = "Copyright (c) 2009 Scott Truger"
__license__ = "Python"

import os 
import sys
import fileinput
import shutil
import re

class FileMover:
  "Moves files based on defined expressions"
  
  def __init__(self, searchPath):
    self.searchPath = searchPath
    
  def findFiles(self):
    """finds avi all files of the given type, returns a list.
     """
    foundFiles = []
    for root, dirs, files in os.walk(searchPath):
      for elem in files:
	if (os.path.splitext(elem)[1] == ".avi"):
	  foundFiles.append(os.path.join(root,elem))
    return foundFiles
    
  def moveFiles(self, fileList):
    """moves files in specified list if they match the defined expressions"""
    
    filePattern = re.compile('.*(whale)+.*(wars)+.*(.avi)$',re.IGNORECASE)
    for elem in fileList:
      print elem
      if re.search(filePattern, elem):
	print "moved one"
    
  
if __name__ == "__main__":
  print "  -   -   -   -   -   -   -"
  
  searchPath = "/home/scott/Dev/archive_manager/test/from"
  mover = FileMover(searchPath)
  files = mover.findFiles()
  mover.moveFiles(files)
  
  print "  -   -   -   -   -   -   -"