def searchRoll(rolls,roll):
    lowest=0
    highest=len(rolls)-1
    while lowest<=highest:
        mid=(lowest+highest)//2
        if rolls[mid]==roll:
            return True
        elif rolls[mid]<roll:
            lowest=mid+1
        elif rolls[mid]>roll:
            highest=mid-1
    return False
