# Module: Element Search
# In a school, class teacher wants to organize a game for L.K.G students and the game is like there will be a
# basket  with numbered balls teacher will give one number and student has to search for that particular
# numbered ball if student found that  numbered ball  then he has to say "Got It!" otherwise  "Sorry!".
# Help the students to write a program to search the numbered ball.
# Input  Format: 
# The first line of input corresponds to the number of balls in the basket,n.
# The next n  line of input consists of the numbered balls in the basket.
# The last line of input consists of a numbered ball to be searched.
# Output Format:
# The output is a  string consist of 'Got It!' or 'Sorry!' (without quotes).
# [All text in bold corresponds to input and the rest corresponds to output.]
# Sample Input and Output 1:
# 5
# 21
# 18
# 90
# 6
# 74
# 6
# Got It!
# Sample Input and Output 2:
# 5
# 21
# 18
# 90
# 6
# 74
# 10
# Sorry!

def main():
    n = int(input())  # Number of balls in the basket
    basket = []
    
    # Reading the numbered balls into the basket list
    for i in range(n):
        basket.append(int(input()))
    
    ball_to_search = int(input())  # Numbered ball to be searched
    found = False
    
    # Loop through the basket to check if the ball_to_search is present
    for ball in basket:
        if ball == ball_to_search:
            found = True
            break
    
    # Output the result based on whether the ball was found or not
    if found:
        print("Got It!")
    else:
        print("Sorry!")

if __name__ == "__main__":
    main()
