try:
  x = int(input("enter number x my lord: "))
  y = int(input("enter number y my lord: "))
  result = x**y

#print(str(x)+" power "+str(y)+ " = "+str(result))
#print("{} power {} = {}".format(x,y,result))
#print("{0} power {1} = {2}".format(x,y,result))
#dear TA I've used different ways to do this exercise and I've commented the all execpt for one of them.

  

except ValueError as e:
  print(e)
  print("enter only numbers please")  
except Exception as e:
  print(e)
  print("Something went wrong my lord")  
else:
  text = "{} power {} = {}"
  print(text.format(x,y,result))
finally:
  print("Practice makes perfect")  




