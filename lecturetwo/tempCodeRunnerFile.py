ting=int(input("enter the rating of the movie: " ))

if(rating>=4.5):
    print("blockbuster")
elif(rating>=3.5 and rating<4.5):
    print("good")
elif(rating>=2 and rating<3.5):
    print("average")
elif(rating<2):
    print("flop")
else:
   