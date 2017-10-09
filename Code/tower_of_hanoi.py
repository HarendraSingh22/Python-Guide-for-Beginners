def toh(source,dest,aux,n):
    '''
    Objective  : To Solve the tower of hanoi
    Parameters :
        source : Source disk - initially containing disks
        dest   : Destination disk - where we need to move the disk
        aux    : Auxiliary disk - the spare helper disk
    Return value : None
    '''
    '''
    approach  : Recursive
                Move n-1 disks from source to aux disk
                Move remaining 1 disk from source to destination
                Move n-1 disks from aux to destination disk
    '''
    
    if n==0:
        return
    toh(source,aux,dest,n-1)
    print("Move Disk from",source,"to",dest)
    toh(aux,dest,source,n-1)

def main():
    '''
    Objective : To Solve the tower of hanoi
    User inputs:
        n - integer - number of disks in the tower of hanoi
    return value : None
    '''
    # approach - Invoke function toh(source,dest,aux,n)
    
    print("Tower of Hanoi")
    n=int(input("Enter the number of disks : "))
    source=1
    aux=2
    destination=3
    print("Required steps are : ")
    toh(source,destination,aux,n)


if __name__ == "__main__":
    main()
