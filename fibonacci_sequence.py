def fibsequence(num):
    # deals with low numbers #
    if(num == 0 or num == 1):
        return num
    else:
        # builds list and append further numbers #
        fiblist = [1, 1]
        for i in range(2, num):
            fiblist.append(fiblist[i - 1] + fiblist[i - 2])
        # loops through and prints the sequence #
        for j in range(len(fiblist)):
            print(fiblist[j])
    
fibsequence(7)
