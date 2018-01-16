#! Python3
# rename files with American MM-DD-YYYY date format to European DD-MM-YYYY

import shutil, os, re

# TODO: create a regex that matches files with MM-DD-YYYY
datePattern = re.compile(r"""^(.*?)                              # all text before the date
                        ((0|1)?\d)-                              # one or two digits for the month
                        ((0|1|2|3)?\d)-                          # one or two digits for the day
                        ((19|20)\d\d)                            # four digits for the year
                        (.*?)$                                   # all text after the date
                        """, re.VERBOSE)

# TODO: loop over the files in the working directory
for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)

    # TODO: skip files without a date
    if mo == None:
        continue

    # TODO: get the different parts of the file name
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

    # TODO: form the European-style filename
    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

    # TODO: get the full, absolute file paths
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)

    # TODO: rename the files
    print('Renaming "%s" to "%s"...' % (amerFilename, euroFilename))
    shutil.move(amerFilename, euroFilename)


