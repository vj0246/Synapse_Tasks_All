runes=str(input("pls enter the string runes"))
runes=runes.lower()
count=0
run=0
for i in runes:
    run+=1
    if i=='l':
        ans1=1
        count+=1
    elif i=='u':
        ans2=1
        count+=1
    elif i=='m':
        ans3=1
        count+=1
    elif i=='o':
        ans4=1
        count+=1
    elif i=='s':
        ans5=1
        count+=1
    if(count==5 and ans1==1 and ans2==1 and ans3==1 and ans4==1 and ans5==1):
        ans=run
        break
    else: 
        ans=-1
print(ans)
    