def fac(num):
    if num <= 1:
        return 1 
    else:
        return num*fac(num-1)

if __name__ == "__main__":
    print(fac(5))
        
