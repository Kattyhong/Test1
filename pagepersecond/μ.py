import os
import math
import variable
fp = open('keypage-test-2014-07-10-14-30-01.983972.txt','r')
fnew = open('./save1.txt','w+')
flist = fp.readlines()

pagelist = list()
totallist = list()
#calculate the pagepersecond
def pagepersecond():
   j=0
   total=0
   pageadd=0
   for lines in flist:
      division = lines.split('\t')
      if(not lines.startswith("task_id")):
         if(len(division)>3):
            total_page = division[3]
            total_num = float(total_page)
            time = division[2]
            time_num = float(time)
            pagesecond = total_num/time_num
            pagelist.append(pagesecond)
            pagesecond_str=str(pagesecond)
            lines=lines.replace('\n',pagesecond_str+'\t\n')
            pageadd += pagesecond
            total = total+1
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
#calculate the average and standard deviation
def other():
   sum1 = 0
   sum2 = 0
   sum3 = 0
   pagepersecond()
   length = len(pagelist)
   for pl in pagelist:
      sum1+=pl
   variable.avg = sum1/length

   for p2 in pagelist:
      #num = pow(p2-variable.avg,4)
      #sum2 += num
      ss = pow(p2-variable.avg,2)
      sum3 +=ss
   s = sum3/length
   #f = sum2/(pow(s,2)*(length-1))
   variable.sq = math.sqrt(s)

other()
#judge which num is in the range
def Gaussian(n):
   comp = variable.avg-1*variable.sq
   comp2 = variable.avg+1*variable.sq
   if((n<=comp2) and (n>=comp)):
      return 1
   else:
      return 0

def filterByTotalpages():
   for lines in flist:
      division = lines.split('\t')
      if(not lines.startswith("task_id")):
         if(len(division)>3):
            total_page = division[3]
            total_num = float(total_page)
            totallist.append(total_num)
         else:
            print "Index over range"
      else:
         continue
   tasknum = len(totallist)
   pagenum =0
   for page in totallist:
      pagenum +=page
   standsum = 0
   variable.pageavg = pagenum/tasknum
   for page in totallist:
      standsum += pow(page-variable.pageavg,2)
   stddivison1 = standsum/tasknum
   variable.stddivison = math.sqrt(stddivison1)
filterByTotalpages()
 
def Gaussianforpages(n):
   comp = variable.pageavg-1.96*variable.stddivison
   comp2 = variable.pageavg+1.96*variable.stddivison
   if((n<=comp2) and (n>=comp)):
      return 1
   else :
      return 0
i=0
j=0
del(flist[0])
for pi in pagelist:
   if(Gaussian(pi)==0 ):
      del(totallist[i])
      del(flist[i]) 
   else :
      i+=1

for ti in totallist:
   if(Gaussianforpages(ti)==0):
      del(pagelist[j])
      del(totallist[j])
      del(flist[j]) 
   else :
      j+=1

#write context into files
fnew.writelines(flist)
fp.close()
fnew.close()





