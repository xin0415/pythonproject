from copy import deepcopy
import sys
SIZE=256
ALL_MASK=0x1ff
valid_masks=[0, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x100]
STYP_ROW=1
STYP_COL=2
STYP_BOX=3
constraints=[[None for x in range(9)] for y in range(15)]
class SEARCH_STATE:
   def __init__(self):
      self.avail_mask=[[0 for x in range(9)] for y in range(9)] 
      self.row_avail_counts=[[0 for x in range(9)] for y in range(9)] 
      self.col_avail_counts=[[0 for x in range(9)] for y in range(9)] 
      self.box_avail_counts=[[[0 for x in range(9)] for y in range(3)] for z in range(3)] 
      self.val_set=[[0 for x in range(9)] for y in range(9)]
      
states=[SEARCH_STATE for x in range(81)]

def search_init(ipss):
   pss=SEARCH_STATE()
   for i in range (0,9):
      for j in range (0,9):
         pss.avail_mask[i][j]=ALL_MASK
         pss.val_set[i][j]=0
         pss.row_avail_counts[i][j]=9
         pss.col_avail_counts[i][j]=9
   for i in range (0,3):
      for j in range (0,3):
         for k in range (0,9):
            pss.box_avail_counts[i][j][k]=9;
   states[ipss]=pss
   return;

def scan_convert(prow,n,s):
   for i in range (0,n):
      if s[i]=='<':
         prow[i]=-1
      elif s[i]=='=':
         prow[i]=0
      elif s[i]=='>':
         prow[i]=1
   return;

def scan_constraints(message,arrayindex):
   for i in range (0,3):
      for j in range (0,3):
         scan_convert(constraints[5*i+2*j],6,message[arrayindex])
         arrayindex+=1
         if j<2:
            scan_convert(constraints[5*i+2*j+1],9,message[arrayindex])
            arrayindex+=1
   return arrayindex;
def checkEqual(baseMask,chkMask):
   result=0
   if valid_masks[5] & baseMask:
      result|=valid_masks[5]
   for i in range (1,10):
      if valid_masks[i]&chkMask==0:
         if valid_masks[10-i]&baseMask:
            result|=valid_masks[10-i]
   return result;
def checkLess(baseMask,chkMask):
   result=0
   if valid_masks[9] & baseMask:
      result|=valid_masks[9]
   for i in range (1,9):
      if valid_masks[i] & chkMask !=0:
         break
      elif valid_masks[9-i] & baseMask:
         result|=valid_masks[9-i]
   return result;
def checkGreater(baseMask, chkMask):
   result=0
   if valid_masks[1] & baseMask:
      result|=valid_masks[1]
   for i in range (9,2,-1):
      if valid_masks[i]&chkMask!=0:
         break
      elif valid_masks[11-i]&baseMask:
         result|=valid_masks[11-i]
   return result;
def checkConstraint(constraint,baseMask,chkMask):
   if constraint <0:
      return checkLess(baseMask,chkMask)
   elif constraint >0:
      return checkGreater(baseMask,chkMask)
   else:
      return checkEqual(baseMask,chkMask)
   return;

def check_constraints(pss):
   change_count = 1
   scan_count = 0
   while change_count>0:
      scan_count+=1
      change_count = 0
      baseConsRow = 0
      for row in range (0,9):
         baseConsCol = 0
         for col in range (0,9):
            if pss.val_set[row][col]==0:
               baseMask = pss.avail_mask[row][col]
               totResult = 0
               if (col%3) !=0:
                  chkMask = pss.avail_mask[row][col-1]
                  resultMask = checkConstraint(constraints[baseConsRow][baseConsCol-1], baseMask, chkMask)
                  if resultMask != 0:
                     baseMask &=~resultMask
                     change_count+=1
                     totResult|=resultMask
               if (col%3) !=2:
                  chkMask=pss.avail_mask[row][col+1]
                  resultMask=checkConstraint(constraints[baseConsRow][baseConsCol], baseMask, chkMask)
                  if resultMask!=0:
                     baseMask &=~resultMask
                     change_count+=1
                     totResult|=resultMask
               if (row%3)!=0:
                  chkMask=pss.avail_mask[row-1][col]
                  resultMask=checkConstraint(constraints[baseConsRow-1][col], baseMask, chkMask)
                  if resultMask!=0:
                     baseMask &=~resultMask
                     change_count+=1
                     totResult|=resultMask
               if (row%3)!=2:
                  chkMask=pss.avail_mask[row+1][col]
                  resultMask=checkConstraint(constraints[baseConsRow+1][col], baseMask, chkMask)
                  if resultMask!=0:
                     baseMask &=~resultMask
                     change_count+=1
                     totResult|=resultMask
               if baseMask==0:
                  return -1;
               pss.avail_mask[row][col]=baseMask
               if totResult != 0:
                  for i in range (0,9):
                     if valid_masks[i]&totResult:
                        pss.col_avail_counts[col][i-1]-=1
                        pss.row_avail_counts[row][i-1]-=1
                        pss.box_avail_counts[int(row/3)][int(col/3)][i-1]-=1
            if (col%3)!=2:
               baseConsCol+=1
         if (row%3) !=2:
            baseConsRow+=2
         else:
            baseConsRow+=1
   return 0;
class SOLVE_DATA:
   def __init__(self):
      self.solve_type=None
      self.solve_val=None
      self.solve_row=None
      self.solve_col=None
      self.solve_cnt=None
      self.solve_index=None
      self.test_row=None
      self.test_col=None
def GetSolveStep(pss,psd):
   psd.solve_cnt=10
   for i in range (0,9):
      for j in range (0,9):
         if pss.row_avail_counts[i][j]<psd.solve_cnt:
            psd.solve_cnt=pss.row_avail_counts[i][j]
            psd.solve_type=STYP_ROW
            psd.solve_row=i
            psd.solve_val=j+1
   for i in range (0,9):
      for j in range (0,9):
         if pss.col_avail_counts[i][j]<psd.solve_cnt:
            psd.solve_cnt=pss.col_avail_counts[i][j]
            psd.solve_type=STYP_COL
            psd.solve_col=i
            psd.solve_val=j+1
   for i in range (0,3):
      for j in range (0,3):
         for k in range (0,9):
            if pss.box_avail_counts[i][j][k]<psd.solve_cnt:
               psd.solve_cnt=pss.box_avail_counts[i][j][k]
               psd.solve_type=STYP_BOX
               psd.solve_row=i
               psd.solve_col=j
               psd.solve_val=k+1
   if psd.solve_cnt==0:
      return -1;
   else:
      return 0;
def FindNextTest(pss,psd):
   mask=valid_masks[psd.solve_val]
   if psd.solve_index >= psd.solve_cnt:
      return -1;
   if psd.solve_type == STYP_ROW:
      if psd.solve_index==0:
         startj=0
      else:
         startj=psd.test_col+1
      i=psd.solve_row
      for j in range (startj, 9):
         if pss.avail_mask[i][j]& mask:
            psd.test_col=j
            psd.test_row=i
            psd.solve_index+=1
            return 0;
      return -1;
   elif psd.solve_type == STYP_COL:
      if psd.solve_index==0:
         starti=0
      else:
         starti= psd.test_row+1
      j=psd.solve_col
      for i in range (starti,9):
         if pss.avail_mask[i][j]&mask:
            psd.test_col=j
            psd.test_row=i
            psd.solve_index+=1
            return 0;
      return -1;
   elif psd.solve_type==STYP_BOX:
      if psd.solve_index==0:
         starti=0
         startj=0
      else:
         starti=psd.test_row-3*psd.solve_row
         startj=psd.test_col+1-3*psd.solve_col
      for i in range (starti,3):
         for j in range (startj,3):
            if pss.avail_mask[i+3*psd.solve_row][j+3*psd.solve_col]&mask:
               psd.test_col=j+3*psd.solve_col
               psd.test_row=i+3*psd.solve_row
               psd.solve_index+=1
               return 0;
      return -1;
def ApplyChoice(pss,row,col,val):
   mask=valid_masks[val]
   if (pss.val_set[row][col])!=0:
      return -1;
   pss.val_set[row][col]=val
   boxr=int(row/3)
   boxc=int(col/3)
   for j in range (0,9):
      if pss.avail_mask[row][j]&mask:
         pss.box_avail_counts[boxr][int(j/3)][val-1]-=1
         pss.col_avail_counts[j][val-1]-=1
      pss.avail_mask[row][j] &=~mask
   for i in range (0,9):
      if pss.avail_mask[i][col] & mask:
         pss.box_avail_counts[int(i/3)][boxc][val-1]-=1
         pss.row_avail_counts[i][val-1]-=1
      pss.avail_mask[i][col] &=~mask
   boxr=int(row/3)
   boxc=int(col/3)
   for i in range (3*boxr,3*(boxr+1)):
      for j in range (3*boxc, 3*(boxc+1)):
         if pss.avail_mask[i][j] & mask:
            pss.col_avail_counts[j][val-1]-=1
            pss.row_avail_counts[i][val-1]-=1
         pss.avail_mask[i][j] &=~mask
   for i in range (1,10):
      if i != val:
         if (pss.avail_mask[row][col]&valid_masks[i])!=0:
            pss.box_avail_counts[int(row/3)][int(col/3)][i-1]-=1
            pss.col_avail_counts[col][i-1]-=1
            pss.row_avail_counts[row][i-1]-=1
   pss.avail_mask[row][col]=mask
   pss.row_avail_counts[row][val-1]=32
   pss.col_avail_counts[col][val-1]=32
   pss.box_avail_counts[boxr][boxc][val-1]=32
   return 0;
def Solve(level):
   pssnxt=SEARCH_STATE()
   pss=states[level]
   sd = SOLVE_DATA()
   if GetSolveStep(pss,sd) !=0:
      return -1;
   sd.solve_index=0
   while FindNextTest(pss,sd)==0:
      if level==80:
         pss.val_set[sd.test_row][sd.test_col]=sd.solve_val
         return 0;
      else:
         pssnxt=deepcopy(pss)
         states[level+1]=pssnxt
         if ApplyChoice(pssnxt,sd.test_row,sd.test_col,sd.solve_val) ==0:
            if check_constraints(pssnxt)==0:
               if Solve(level+1)==0:
                  for i in range (0,9):
                     for j in range (0,9):
                        pss.val_set[i][j]=pssnxt.val_set[i][j]
                  return 0;
   return -1;
def main():
   f= open(sys.argv[1],'r')
   message = f.read()
   message=message.split("\n")
   f.close()
   ipss=0
   nprob=int(message[0])
   arrayindex=1
   for curprob in range (1,nprob+1):
      index=int(message[arrayindex])
      arrayindex+=1
      search_init(ipss)
      arrayindex=scan_constraints(message,arrayindex)
      check_constraints(states[ipss])
      Solve(0)
      print(index,end=' ')
      print()
      for i in range (0,9):
         for j in range (0,9):
            print(states[0].val_set[i][j],end=' ')
         print()
main();