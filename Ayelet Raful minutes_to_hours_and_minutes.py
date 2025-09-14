"""
This function takes the input of minutes given by the user and calculates how many hours and remaining minutes his minutes come out to.
Ayelet Raful
Purpose of Assignment is to convert mintutes to hours and minutes.
"""
#This row is giving the function a name, the colon signifies that I am starting a new function
def minutes_to_hours_and_minutes():
    
    minutes = int(input("How many minutes?")) #creating a variable of minutes and using the input function to ask the user a question and wrapping it in an interger so that the user's response can be used to calculate a response

    #Here I am explaining to the user what he is asking for, and I am using the print function so it comes up on the screen
    print(" The user wants to calculate how many hours and remaining minutes there are in" ,minutes," minutes")
    
    hours = minutes // 60 #This is the math calculation the program has to do to find out how many hours there are in the minutes input of the user, using // so that it will do integer division, giving me the total number of hours, without any remainder
    
    remaining_minutes =  minutes % 60 #Here it calculates how many minutes there are left over after the hours are calculated, using the remainder % tool
    
    #Here the program is giving the user the answer based on his input of minutes
    print("In" ,minutes,"minutes, there are" ,hours, "hours, and" ,remaining_minutes,"remaining minutes.")
    
#This is calling the function to action    
minutes_to_hours_and_minutes()
    
