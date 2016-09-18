#coding=utf-8
#backup_ver1.py
'''
1,需要备份的文件和目录由列表指定
2,备份保存在主备份目录
3,文件备份城1个zip文件
4,ZIP文件名是当前的日期时间
5,标准ZIP命令.
'''
'''
#v2
import os
import time

source =[r'd:\\pythonbyte']

target_dir =r'd:\\backup\\'

#target = target_dir+time.strftime('%Y%m%d%H%M%S')+'.zip'
today = target_dir + time.strftime('%Y%m%d')

now = time.strftime('%H%M%S')

if not os.path.exists(today):
	os.mkdir(today)
	print'success create dir',today
	
target = today + os.sep +now +'.zip'

print target
zip_command =r'"D:\infozip\Wiz.exe" -qr %s%s'%(target,''.join(source))
#zip_command = r'"C:\Program Files\WinRAR\WinRAR.exe" A %s %s -r' % (target,source)
print zip_command
if os.system(zip_command)==0:
	print'successfulbackup to',target
else:
	print'backup failed'
'''
'''	
#v1
import os  
import time  
  
# 1. The files and directories to be backed up are specified in a list.  被保存文件路径
source = r'D:\pythonbyte'  
  
# 2. The backup must be stored in a main backup directory  保存路径
target_dir = r'D:\backup\\' # Remember to change this to what you will be using  
  
# 3. The files are backed up into a rar file.  
# 4. The name of the rar archive is the current date and time  文件名
target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.rar'  
# 5. We use the rar command in windows to put the files in a zip archive,you must to be sure  you have installed WinRARA and that in your path  
#rar_command = "WinRAR A %s %s -r" % (target,source)  
rar_command = r'"C:\Program Files\WinRAR\WinRAR.exe" A %s %s -r' % (target,source)
print rar_command
# Run the backup  
if os.system(rar_command) == 0:  
    print 'Successful backup to', target  
else:  
    print 'Backup FAILED'   
raw_input ("dd")  

'''
'''
#v2
import os  
import time  
  
# 1. The files and directories to be backed up are specified in a list.  被保存文件路径
source = r'D:\pythonbyte'  
  
# 2. The backup must be stored in a main backup directory  保存路径
target_dir = r'D:\backup\\' # Remember to change this to what you will be using  
  
# 3. The files are backed up into a rar file.  
# 4. The name of the rar archive is the current date and time  文件名
today = target_dir + time.strftime('%Y%m%d')

now = time.strftime('%H%M%S')

if not os.path.exists(today):
	os.mkdir(today)
	print'success create dir',today
	
target = today + os.sep +now +'.rar'
# 5. We use the rar command in windows to put the files in a zip archive,you must to be sure  you have installed WinRARA and that in your path  
#rar_command = "WinRAR A %s %s -r" % (target,source)  
rar_command = r'"C:\Program Files\WinRAR\WinRAR.exe" A %s %s -r' % (target,source)
print rar_command
# Run the backup  
if os.system(rar_command) == 0:  
    print 'Successful backup to', target  
else:  
    print 'Backup FAILED'   
raw_input ("dd")  
'''
#v3
import os  
import time  
  
# 1. The files and directories to be backed up are specified in a list.  被保存文件路径
source = r'D:\pythonbyte'  
  
# 2. The backup must be stored in a main backup directory  保存路径
target_dir = r'D:\backup\\' # Remember to change this to what you will be using  
  
# 3. The files are backed up into a rar file.  
# 4. The name of the rar archive is the current date and time  文件名
today = target_dir + time.strftime('%Y%m%d')

now = time.strftime('%H%M%S')

comment = raw_input('enter a comment-->')

if len(comment) == 0:
	target = today+os.sep+now+'.rar'
else:
	target = today+os.sep+now+'_'+ \
	comment.replace('','_')+'.rar'

if not os.path.exists(today):
	os.mkdir(today)
	print'success create dir',today
	
target = today + os.sep +now +'.rar'
# 5. We use the rar command in windows to put the files in a zip archive,you must to be sure  you have installed WinRARA and that in your path  
#rar_command = "WinRAR A %s %s -r" % (target,source)  
rar_command = r'"C:\Program Files\WinRAR\WinRAR.exe" A %s %s -r' % (target,source)
print rar_command
# Run the backup  
if os.system(rar_command) == 0:  
    print 'Successful backup to', target  
else:  
    print 'Backup FAILED'   
raw_input ("dd")  
