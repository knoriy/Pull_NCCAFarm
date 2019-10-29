import os, getpass, time, datetime, sys
import pysftp


hostname = "tete"
username = getpass.getuser()
password = getpass.getpass()

projectName = raw_input("Input project Name: ")

localDirSave = raw_input("Input the directory you would like to save your file to: ") #"/net/wg0626/transfer/MPJ/Renders/rs_Ground/rs_Ground"

with pysftp.Connection(host=hostname, username=username, password=password) as sftp:
    print "Connection successfully established ... "  

    finalDir = os.path.join(sftp.pwd, projectName, "images/")

    while 1:
        filesToRemoveAttr = sftp.listdir_attr(finalDir)
        filesToRemove = sftp.listdir(finalDir)
        for fileAttr, file in zip (filesToRemoveAttr, filesToRemove):
            m_time = fileAttr.st_atime
            if m_time+120 < time.time():
                sftp.get(os.path.join(finalDir, file), os.path.join(localDirSave, file))
                sftp.remove(finalDir+"/"+file)
                print (">>> %s >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Moved Successfully" % (file))
        time.sleep(60*15)

        print (">>> Last Cheacked: >>>>>>>>>>>>>>>>>>>>>>>>>> " + str(datetime.datetime.now()))
