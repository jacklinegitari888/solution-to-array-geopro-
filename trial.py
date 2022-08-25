


def solution(a):
    #initiate dictionally with all single digits as key and default value
    
   digit_dic={
       
       0:0,1:0,2:0,3:0,4:0,4:0,5:0,6:0,7:0,8:0,9:0,
       
   }
   
   #loop through all numbers in the list
   for integers in a:
       #split numbers into digits
       digit_list=[]
       #iterate through every number in the array
       for digit in str (integers):
           digit_list.append(int(digit))
                             
       for digit in digit_list:
           #add the numbers of occurence  of each digit by one in the digit dictionary
           digit_dic[digit]+=1
           
   sorted_dict={k:v for k,v in sorted(digit_dic.items(),key=lambda item:item[1])}
   return sorted_dict

print(solution([25,2,3,57,38,41]))



           
            
           
           
        
 
    