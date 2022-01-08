# iterate through folders and read result.txt file in each folder
import os
for(dirname, dirs, files) in os.walk('.'):
    for filename in files:
        if filename == 'result.txt':
            filepath = os.path.join(dirname, filename)
            with open(filepath) as f:
                for line in f:
                    '''
                    sample line: Num: 01,   121 to  3575, step1:   98, loss: 0.0000, step2:  802, loss1: 0.0000, loss2: 0.0400, success number:  41, total number:  41, success rate: 100.00
                    read from 9 to 16
                    '''
                    num1 = int(line[9:15].strip())
                    num2 = int(line[19:23].strip())
                    filetocopy = str(num1)+'_'+str(num2)
                    # read filetocopy from step1 folder
                    filetocopy2 = os.path.join(
                        dirname, 'step1/'+filetocopy+'.wav')
                    # copy filetocopy to step2 folder

                    os.system('cp '+filetocopy2+' ' +
                              os.path.join(dirname, '../step1/'+filetocopy+'.wav'))
                    filetocopy = str(num1)+'_'+str(num2)
                    # read filetocopy from step1 folder
                    filetocopy2 = os.path.join(
                        dirname, 'step2/'+filetocopy+'.wav')
                    # copy filetocopy to step2 folder

                    os.system('cp '+filetocopy2+' ' +
                              os.path.join(dirname, '../step2/'+filetocopy+'.wav'))
                    # write line to result.txt
                    with open(os.path.join(dirname, '../result.txt'), 'a') as f:
                        f.write(line)
