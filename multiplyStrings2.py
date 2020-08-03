from colorama import Fore, Back, Style
import time

def multiply(str1,str2):
    str1=list(reversed(str1))
    str2=list(reversed(str2))
    answer=[0]*(len(str1)+len(str2))
    for i in range(len(str1)):
        carry=0
        for j in range(len(str2)):
            # summ = n1 * n2 + result[i_n1 + i_n2] + carry 
            # carry = summ // 10
            # Store result 
            # result[i_n1 + i_n2] = summ % 10

            """
                    val=(int(str1[i])*int(str2[j]))%10
                    answer[i+j]=val+answer[i+j]+carry
                    carry=(int(str1[i])*int(str2[j]))//10
            """
            
            n1=int(str1[i])
            n2=int(str2[j])
            print('i,j',i,j,'val',n1,n2)
            val = n1 * n2 + answer[i + j] + carry 
            print(Back.YELLOW + Style.BRIGHT ,end="")
            print('val = n1 * n2 + answer[i + j] + carry',n1,'*',n2,'+',answer[i+j],'+',carry,'val=',val,end="")
            print(Style.RESET_ALL, end="")
            print()
            carry = val // 10
            # Store result 
            answer[i + j] = val % 10
            print('setting','i+j',i+j,answer[i+j])

            print(Back.RED + Style.BRIGHT ,end="")
            print(answer,end="")
            print(Style.RESET_ALL, end="")
            print()
        answer[i+j+1]+=carry
        print('setting carry','i+j+1',i+j+1,answer[i+j+1])



    print(answer)
    return answer

print(multiply('789','123'))
