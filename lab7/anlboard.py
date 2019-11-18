
def analyzeBoard(T):

#Returns -1("error") if list length or list values are invalid
   if not(len(T) == 9):
      return -1
   else:
      for position in T:
         if not(position == 0) and not(position == 1) and not(position == 2): 
            return -1

#Returns -1("error") if one player has 2 or more 'placements' than the other
   countx = 0
   counto = 0
   for index in range(0, 9, 1):
      if T[index] == 1:
         countx = countx + 1
      elif T[index] == 2:
         counto = counto + 1

   if (countx - counto) >= 2 or (counto - countx) >= 2:
      return -1

   xwin = 0
   owin = 0
#Checks if there are any 3 X's in a line
   if T[0] == 1 and T[1] == 1 and T[2] == 1:
      xwin = 1
   elif T[3] == 1 and T[4] == 1 and T[5] == 1:
      xwin = 1
   elif T[6] == 1 and T[7] == 1 and T[8] == 1:
      xwin = 1
   elif T[0] == 1 and T[3] == 1 and T[6] == 1:
      xwin = 1
   elif T[1] == 1 and T[4] == 1 and T[7] == 1:
      xwin = 1
   elif T[2] == 1 and T[5] == 1 and T[8] == 1:
      xwin = 1
   elif T[0] == 1 and T[4] == 1 and T[8] == 1:
      xwin = 1
   elif T[2] == 1 and T[4] == 1 and T[6] == 1:
      xwin = 1

#Checks if there are any 3 O's in a line
   if T[0] == 2 and T[1] == 2 and T[2] == 2:
      owin = 2
   elif T[3] == 2 and T[4] == 2 and T[5] == 2:
      owin = 2
   elif T[6] == 2 and T[7] == 2 and T[8] == 2:    
      owin = 2
   elif T[0] == 2 and T[3] == 2 and T[6] == 2:
      owin = 2
   elif T[1] == 2 and T[4] == 2 and T[7] == 2:
      owin = 2
   elif T[2] == 2 and T[5] == 2 and T[8] == 2:
      owin = 2
   elif T[0] == 2 and T[4] == 2 and T[8] == 2:
      owin = 2
   elif T[2] == 2 and T[4] == 2 and T[6] == 2:
      owin = 2

#Returns -1("error") if both X and O win
   if xwin == 1 and owin == 2:
      return -1

#Checks if X or O won over the other
   if xwin == 1 and not(owin == 2):
      return 1
   elif owin == 2 and not(xwin == 1):
      return 2

#Returns 0("board is in play") if there are still unoccupied positions
   for position in T:
      if position == 0:
         return 0

#Returns 3("draw") if all positions are occupied and no player won yet
   drawcheck = True
   for position in T:
      if position == 0:
         drawcheck = False
   if drawcheck == True:
      return 3
 
#print(analyzeBoard([1,1,0,2,2,0,0,0,0]))

