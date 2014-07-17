import os
fp = open('J:/test1/keypage-test-2014-07-10-14-30-01.983972.txt','r')
fnew = open('J:/test1/save.txt','w+')
flist = fp.readlines()
total=0
pageadd=0
pagelist = list()
j=0

for lines in flist:
   division = lines.split('\t')
   if(not lines.startswith("task_id")):
      if(len(division)>3):
         total_page = division[3]
         total_num = float(total_page)
         time = division[2]
         time_num = float(time)
         pagesecond = total_num/time_num
         pagesecond_str=str(pagesecond)
         lines=lines.replace('\n',pagesecond_str+'\t\n')
         pageadd += pagesecond
         total = total+1
         pagelist.append(pagesecond)
         flist[j] = lines
         j+=1
         print lines
      else:
         print 'error'
    
   else:
      lines=lines.replace('\n','pagePersecond\t\n')
      division = lines.split('\t')
      flist[j] = lines
      j+=1
      print lines

avg = pageadd/total

d_value = list()
copy = list()
for p in pagelist:
   d_value.append(abs(p-avg))
   copy.append(abs(p-avg))
   
d_value.sort()

num = d_value[len(d_value)-1]

i=0
print copy
for c in copy:
   i=i+1
   if(num==c):
      del(flist[i])
      break
   
print i
print flist
fnew.writelines(flist)
fp.close()
fnew.close()





