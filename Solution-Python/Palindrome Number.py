def isPalindrome(x):
        temp = x
        sum = 0
        while(temp > 0):
        	rem = temp % 10
        	sum = (sum*10) + rem
        	temp =  temp // 10
        if sum == x:
        	return True
        else :
        	return False
     
        	   	
print(isPalindrome(121))	
        