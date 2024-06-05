def substring(s1:str,s2:str) ->bool:
    if len(s2)>len(s1):
        return False
    
    big= 0
    small= 0

    while big < len(s1):
        if s1[big] == s2[small]:
            small+=1
            if small == len(s2):
                return True
        else:
            big= big - small
            small=0
        big+=1
    return False

print(substring("laboratory","rat"))        # True
print(substring("cat","meow"))              # False
print(substring("cacacat","cacat"))         # True
