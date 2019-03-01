import queue
import sys
class Square:
   def __init__(self):
      self.val=None
      self.row=None
      self.col=None
      self.avail=[]
   def getVal(self):
      return self.val
   def getRow(self):
      return self.row
   def getCol(self):
      return self.col
   def getAvail(self):
      return self.avail
   def setAvail(self,avail):
      self.avail=avail
   def setVal(self,val):
      self.val=val
   def setRow(self,row):
      self.row=row
   def setCol(self,col):
      self.col=col
   def __lt__(self, other):
      return len(self.avail)<len(other.avail)
class Solution:
   def __init__(self):
      self.grid=None
      self.q=queue.PriorityQueue()
def init_solution(s,message,arrayindex):
   r=int(message[arrayindex][1])
   c=int(message[arrayindex][2])
   s.grid=[[Square() for x in range(c+2)] for y in range(r+2)]
   arrayindex+=1
   for i in range (1, r+1):
      message[arrayindex]=message[arrayindex].split(" ")
      for j in range (1, c+1):
         v=message[arrayindex][j-1]
         s.grid[i][j].setVal(v)
         s.grid[i][j].setRow(i)
         s.grid[i][j].setCol(j)
      arrayindex+=1
   nblock=int(message[arrayindex])
   arrayindex+=1
   for i in range (0, nblock):
      message[arrayindex]=message[arrayindex].split(" ")
      nsquares=int(message[arrayindex][0])
      blk=[]
      for j in range (1,nsquares+1):
         blk+=[j]
      for j in range (1,nsquares+1):
         message[arrayindex][j]=message[arrayindex][j].strip('(),')
         r=int(message[arrayindex][j][0])
         c=int(message[arrayindex][j][2])
         s.grid[r][c].setAvail(blk)
         if s.grid[r][c].getVal()=='-':
            s.q.put(s.grid[r][c])
      arrayindex+=1
   return arrayindex;
def attempt(s):
   if s.q.empty() is True:
      return True
   curr=s.q.get()
   row=curr.getRow()
   col=curr.getCol()
   avail=curr.getAvail().copy();
   for g in range(0,len(avail)):
      p=avail[g]
      if adjacent(s,str(p),row,col) is True:
         s.grid[row][col].getAvail().remove(p)
         s.grid[row][col].setVal(str(p))
         if attempt(s) is True:
            return True
         s.grid[row][col].setVal('-')
         s.grid[row][col].getAvail().append(p)
   s.q.put(s.grid[row][col])
   return False;
def adjacent(s,p,row,col):
   for dr in range(-1,2):
      for dc in range(-1,2):
         if s.grid[row+dr][col+dc].getVal() == p:
            return False;
   return True;
def main():
   f= open(sys.argv[1],'r')
   message = f.read()
   message=message.split("\n")
   f.close()
   p=int(message[0])
   arrayindex=1;
   for i in range (1,p+1):
      message[arrayindex]=message[arrayindex].split(" ")
      k=int(message[arrayindex][0])
      print(k)
      r=int(message[arrayindex][1])
      c=int(message[arrayindex][2])
      soln=Solution()
      arrayindex=init_solution(soln,message,arrayindex)
      attempt(soln)
      for i in range (1,r+1):
         for j in range (1,c+1):
            print(soln.grid[i][j].getVal(),end=' ')
         print()
main();