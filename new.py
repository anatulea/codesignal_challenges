def averageScore(scoreInput): 
    result =[int(i) for i in scoreInput.split()]
    return sum(result)
scoreInput = input("Enter the scores separated by space:") 
print(averageScore(scoreInput))