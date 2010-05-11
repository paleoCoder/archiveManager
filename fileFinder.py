# Emgarten.com April 26th, 2007
import os,sys

def findFiles(dir):
  files = []

  # remove a trailing slash if it exists
  if dir[-1:] == “/”:
    dir = dir[0:-1]

  # loop through files and directories
  for x in os.listdir(dir):
    if os.path.isdir(dir + “/” + x):
      # list this dir also
      files.extend(findFiles(dir + “/” + x))
    else:
      # add the file to the list
      files.append(dir + “/” + x)
  return files

if __name__ == “__main__”:
  if len(sys.argv) != 2:
    print “Usage: %s <dir>” % sys.argv[0]
    sys.exit(1)

  # get the list of files
  files = findFiles(sys.argv[1])

  for file in files:
    print file