import os
import re
import sys

def validHashLength(strHashCompare):
  if len(strHashCompare) == 32 or len(strHashCompare) == 40 or len(strHashCompare) == 56 or len(strHashCompare) == 64 or len(strHashCompare) == 96 or len(strHashCompare) == 128:
    return True  
  

dirName = "E:\\test\\rules-master"

package_output_directory = "e:\\test"

with open(os.path.join(package_output_directory, "hashlist.txt"), 'w') as writer:

    for (dirpath, dirnames, filenames) in os.walk(dirName):
        for file in filenames:
            scanPath = os.path.join(dirpath, file)
            try:
              with open(scanPath, 'r') as licenseContent:
                strFileContents = licenseContent.read()
            except:
                strFileContents = ""
            hashvalues = re.findall("[A-Fa-f0-9]{32,128}",strFileContents)
            for hashval in hashvalues:
              if validHashLength(hashval) == True:
                writer.write(hashval + "\n")
