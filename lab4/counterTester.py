from counterlib import *

def main():
   x = counter(100)
   y = counter(50)
   z = counter(-20)


   x.evolve(20)
   print(x.getState())
   x.evolve(0)
   print(x.getState())submit
   y.evolve(-10)
   print(y.getState())
   z.evolve(21)
   print(z.getState())
   
main()
