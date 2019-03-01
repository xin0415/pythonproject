import sys
MAX_NODES=20
MAX_QUERIES=10
s=[]
adj=[[None]]
query1=[]
query2=[]
for j in range(0, MAX_NODES+MAX_QUERIES-1):
   s+=[None]
adj[0]+=s
for i in range (1, MAX_NODES+1):
   adj+=[[None]]
   adj[i]+=s
for i in range (0, MAX_QUERIES):
   query1+=[None]
   query2+=[None]
   
   
   
def adjacentInit(nnodes, nqueries):
   for i in range (0,nnodes+1):
      for j in range (0,nnodes+nqueries):
         adj[i][j]=0
   for i in range (0,nnodes):
      adj[nnodes][i]=1.0
   return;
def ScanEdgeData(nnodes, message,arrayindex):
   message[arrayindex]=message[arrayindex].split(" ")
   node=int(message[arrayindex][0])
   count=int(message[arrayindex][1])
   adj[node-1][node-1]+=float(count)
   index=2
   for i in range(0, count):
      val=int(message[arrayindex][index])
      index+=1
      adj[node-1][val-1]=-1.0
      adj[val-1][node-1]=-1.0
      adj[val-1][val-1]+=1.0
   return count;
def SolveMatrix(nnodes, nqueries):
   ncols=nnodes+nqueries
   nrows=nnodes+1
   for currow in range (0, nnodes):
      maxrow=FindMaxRow(nnodes, nqueries,currow)
      if (maxrow !=currow):
         SwapRows(maxrow,currow,nnodes,nqueries)
      pivot=adj[currow][currow]
      pivot=1.0/pivot
      for j in range(currow,ncols):
         adj[currow][j] *=pivot
      Eliminate(currow,nrows,ncols)
   return;
def FindMaxRow(nnodes,nqueries,currow):
   max=abs(adj[currow][currow])
   maxrow=currow
   for i in range(currow+1,nnodes+1):
      tmp=abs(adj[i][currow])
      if (tmp>max):
         max=tmp
         maxrow=i
   return maxrow;
def SwapRows(maxrow, currow, nnodes,nqueries):
   ncols=nnodes+nqueries
   for i in range(0,ncols):
      tmp=adj[currow][i]
      adj[currow][i]=adj[maxrow][i]
      adj[maxrow][i]=tmp
   return;
def Eliminate(currow, nrows,ncols):
   for i in range(0,nrows):
      if i==currow:
         continue
      factor=adj[i][currow]
      for n in range (currow,ncols):
         adj[i][n]-=factor*adj[currow][n]
   return;
def main():
   f= open(sys.argv[1],'r')
   message = f.read()
   message=message.split("\n")
   f.close()
   nprob=int(message[0])
   arrayindex=1;
   for curprob in range (1, nprob+1):
      message[arrayindex]=message[arrayindex].split(" ")
      index= int(message[arrayindex][0])
      nnodes= int(message[arrayindex][1])
      nqueries= int(message[arrayindex][2])
      nedges= int(message[arrayindex][3])
      adjacentInit(nnodes, nqueries);
      edgecnt=0;edgelines=0;
      arrayindex+=1
      while edgecnt<nedges:
         i=ScanEdgeData(nnodes,message,arrayindex)
         edgelines+=1
         edgecnt+=i
         arrayindex+=1
      for i in range (0, nqueries):
         message[arrayindex]=message[arrayindex].split(" ")
         queryno=int(message[arrayindex][0])
         query1[i]=int(message[arrayindex][1])
         query2[i]=int(message[arrayindex][2])
         adj[query1[i]-1][nnodes+i]=1.0
         adj[query2[i]-1][nnodes+i]=-1.0
         arrayindex+=1
      SolveMatrix(nnodes,nqueries)
      print(' ',end=str(curprob))
      for i in range (0,nqueries):
         dist=abs(adj[query1[i]-1][nnodes + i] - adj[query2[i]-1][nnodes + i])
         print(' ',end=format(dist,'.3f'))
      print("\n")
main();