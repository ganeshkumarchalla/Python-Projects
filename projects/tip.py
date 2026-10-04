print ( "Welcome To the Tip calculator")
bill = int(input("What was your total bill"))
tip = int(input("How Much Amount Of tip to be Given "))
people = int(input( "No of people To split The bill "))

print ( "The Total Bill is : " ,( bill+tip*1/100)/people, round( 0,2))