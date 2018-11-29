def fac(num):
    if num in range(2):
        return 1 
    else:
        fac=1 
        for i in range(1,num+1):
            fac *= i
            i+=1 
        return fac
        
if __name__ == "__main__":
    print(fac(5))
