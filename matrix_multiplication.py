""" write a function for multiply two matrices of n rows"""
import random


def multiply(A: list[list[float]] , B: list[list[float]]) -> list[list[float]]:


    "your code here JD"


    pass




def rand_list(size : int) -> tuple[list[list[float]],list[list[float]]]:
    A : list[list[float]] = [[0]*size for i in range(size)]      
    B : list[list[float]] = [[0]*size for i in range(size)]
    for i in range(size):
        for j in range(size):
            A[i][j] = float(random.randint(0 , 100000))
            B[i][j] = float(random.randint(0 , 100000))
    return A , B 
def printer(A : list[list[float]]) -> None:
    for i in range(len(A)):
        print(*A[i] , sep = '\t' , end = '\n')
    print()



if __name__ == "__main__":
    size : int = int(input("Size : "))
    A , B  = rand_list(size)    
    printer(A)
    printer(B) 
    C = multiply(A,B)
    printer(C)



    


     

