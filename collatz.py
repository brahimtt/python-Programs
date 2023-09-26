def collatz(number):
    if number%2==0:
        return number//2
    elif number%2==1:
        return 3*number+1
print('enter a number:')
seq=0
while seq!=1:
    num=int(input())
    seq=collatz(num)
    print(seq)
    


    
    