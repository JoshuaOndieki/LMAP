print("Welcome to LMAP")

skills={}
while 0==0:
    print("\n1. To add skill. \n2. To view skills. \n3. To mark skill as studied. \n4. To view progress. \n5. View studied skils.")
    option=int(input("Option: "))
    if option == 1:
        skill = input("skill name : ")
        skills[skill] = "Not Studied"
        print("Skill added successfully")
    if option == 2:
        print(skills)
    if option==3:
        study=input("Type skill to mark as studied")
        skills[study]="Studied"
    if option==4:
        count=0
        for i in skills:
            if skills[i]=="Studied":
                count+=1
        progress=(count/len(skills))*100
        print (progress)
    if option ==5:
        studied=[]
        for skill in skills:
            if skills[skill]=="Studied":
                studied.append(skill)
        print(studied)