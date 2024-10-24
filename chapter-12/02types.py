from typing import List, Union, Tuple , Dict

n : int = 5  #int

name : str = "vaibhav" #str

numbers : List[int] = [1,2,3,4,5] #List of int

person : Tuple[str,int]  = ("vaibhav" , 20) #tuple of str and int

scors : Dict[str, int] = {"vaibhav" : 23 , "bob" : 20}

identifire : Union[str,str] = "ID1234"

def sum(a: int , b : int) -> int:
    return a+b

