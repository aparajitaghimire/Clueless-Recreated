#!/usr/bin/env python3

def Color_type(rgbTup):
   color = 0
   r = rgbTup[0];
   g = rgbTup[1];
   b = rgbTup[2];

		#color will either be 0,1,2,3,4,5
		#initialize to 0
		
   if r>=245 and g>=245 and b>=245:
      color = 0 #white
   elif r<=40 and g<=0 and b<=40:
      color = 1 #black
   elif abs(r-b)<=5 and abs(r-g)<=5 and abs(b-g)<=5:
      color = 2 #gray
   elif r<=190 and b<=190 and g<=190:
      color = 3 #dark
   elif abs(r-b)<=5 and abs(r-g)<=85 and abs(b-g)<=85:
      color = 4 #pastel
   else:
      color = 5 #bright
   return(color)
		#print(color)
