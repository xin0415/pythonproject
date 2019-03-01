import sys

maxindex = 0
MAX_SIZE=400
F=[None]
F1=[None]
F2=[None]
F3=[None]
G=[None]
G1=[None]
G2=[None]
G3=[None]
for i in range(0,MAX_SIZE):
   F+=[None]
   F1+=[None]
   F2+=[None]
   F3+=[None]
   G+=[None]
   G1+=[None]
   G2+=[None]
   G3+=[None]

def comp_tiles():
   F[0]=1;F[1]=2;F[2]=11;
   F1[0]=0;F1[1]=2;F1[2]=16;
   F2[0]=0;F2[1]=1;F2[2]=8;
   F3[0]=0;F3[1]=0;F3[2]=4;
   G[0]=0;G[1]=0;G[2]=2;
   G1[0]=G1[1]=0;G1[2]=1;
   G2[0]=G2[1]=0;G2[2]=1;
   G3[0]=G3[1]=0;G3[2]=1;
   for n in range (2, MAX_SIZE-1):
      F[n+1]=2*F[n]+7*F[n-1]+4*G[n]
      F1[n+1] = 2*F1[n] + 2*F[n] + 7*F1[n-1] + 8*F[n-1] + 4*G1[n]+2*G[n]
      F2[n+1] = 2*F2[n] + F[n] + 7*F2[n-1] + 4*F[n-1] + 4*G2[n]+2*G[n]
      F3[n+1] = 2*F3[n] + 7*F3[n-1] + 4*F[n-1] + 4*G3[n]+2*G[n]
      G[n+1] = 2*F[n-1] + G[n]
      G1[n+1] = 2*F1[n-1] + F[n-1] + G1[n]
      G2[n+1] = 2*F2[n-1] + F[n-1] + G2[n] + G[n]
      G3[n+1] = 2*F3[n-1] + F[n-1] + G3[n]


def main():
   f= open(sys.argv[1],'r')
   message = f.read()
   message=message.split("\n")
   f.close()
   nprob=int(message[0])
   comp_tiles();
   for k in range (1, nprob+1):
      message[k]=message[k].split(" ")
      n=int(message[k][1])
      if(n==1):
         print(k,'2 2 1 0')
      else:
         print(k, F[n],F1[n],F2[n],F3[n])
main();