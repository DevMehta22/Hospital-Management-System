import pandas as pd
import matplotlib.pyplot as plt
from pyfiglet import figlet_format


print('======================================================================')
print(figlet_format(' MDR HOSPITAL',font='standard'))
print('======================================================================')

patdf = pd.read_csv("csvfile\\patientnew.csv" , index_col = 0)
################################################
#        PATIENT MANAGEMENT MENU               #
################################################

def pmenu():
    print("\t\t\t +--------------------------+")
    print("\t\t\t |     PATIENT MAIN MENU    |")
    print("\t\t\t +--------------------------+")
    print("\t\t\t |1. New Patiet Registration|")
    print("\t\t\t |2. Update Patient Details |")
    print("\t\t\t |3. Remove Patient         |")
    print("\t\t\t |4. Search Patient by PNo  |")
    print("\t\t\t |5. All Patient List       |")
    print("\t\t\t |6. Deceased analysis      |")
    print("\t\t\t |7. Recovery analysis      |")
    print("\t\t\t |8. Log out                |")
    print("\t\t\t +--------------------------+")
    print()

 
################################################
#          NEW PATIENT REGISTRATION            #
################################################
def patRegister():
   
    rno = len(patdf)
    #print(rno)
    while True:
        print("Please Enter Patient Details")
        pid = input("Patient Id[For ex-P00X] : ")
        
        if serPatientbyId(pid)> 0 :
            print("Duplicate Patient Id, ENTER A VALID PATIENT ID")        
        else:
            break
    
    name = input("Name : ")
    age = input("Age : ")
    weight = input("Weight : ")
    gender = input("Gender : ")
    address = input("Address : ")
    phoneno = input("Phone Number : ")
    disease = input("Disease : ")
    patdf.loc[pid,:] = [pid,name,age,weight,gender,address,phoneno,disease]
    #print(patdf)
    patdf.to_csv("csvfile\\patientnew.csv", mode='w')

################################################
#              UPDATE PATIE                   #
################################################

def patUpdate():
    
    pid = input("Enter Patient Id to Update[For ex-P00X]:")

    if serPatientbyId(pid)> 0 :
        print("Patient Found")
        print("Enter details to update patient")
        name = input("Name : ")
        age = input("Age : ")
        weight = input("Weight : ")
        gender = input("Gender : ")
        address = input("Address : ")
        phoneno = input("Phone Number : ")
        disease = input("Disease : ")
        patdf.loc[patdf.loc[patdf['pid'] == pid].index,:] = [pid,name,age,weight,gender,address,phoneno,disease]
        
        patdf.to_csv("csvfile\\patientnew.csv", mode='w')
        print("Updated Successfully")
    else:
        print("Invaid Patient ID")

################################################
#                    REMOVE PATIENT            #
################################################
          
def patRemove():
    
    pid = input("Enter Patient Id to Delete[For ex-P00X]: ")
    patdf.drop(patdf.loc[patdf['pid']==pid].index, inplace=True) #Remove
    
    patdf.to_csv("csvfile\\patientnew.csv", mode='w')    
    
################################################
#              DISPLAY ALL PATIENT              #
################################################

def dispPatient():
    print(patdf)

################################################
#              SEARCH PATIENT BY ID            #
################################################

def serPatientbyId(pid):
    
    if patdf.empty:
        return 0
    else:
        return len(patdf.loc[patdf['pid'] == pid])

################################################
#           GET PATIENT  DF BY ID              #
################################################
def getPatient(pid):
    
    if patdf.empty:
        return "Invalid ID"
    else:
        return patdf.loc[patdf['pid'] == pid]

################################################
#           GET PATIENT  NAME BY ID            #
################################################

def getPatientName(pid):
    
    if patdf.empty:
        return "Invalid ID"
    else:
        return patdf.iat[0,1]


################################################
#              SEARCH PATIENT BY NAME          #
################################################
def serPatientbyName():
    global patdf
    
    pname  = input("Patient Name :: ")
    print(patdf.loc[patdf['name'] == pname])

def serPatientbyIDPrint():
    global patdf
    
    tid  = input("Patient ID[For ex-P00X] :: ")
    
    print(patdf.loc[patdf['pid'] == tid])

################################################
#              DECEASED ANALYSIS               #
################################################
def deathanalysis():
    years=[2015,2016,2017,2018,2019,2020]
    death_count=[25,27,32,26,29,50]
    bars=plt.bar(years,death_count,color=['red','#9B30FF','orange','blue','silver','gold'])
    bars[0].set_hatch("x*")
    bars[1].set_hatch("*")
    bars[2].set_hatch('o+')
    bars[3].set_hatch('x')
    bars[4].set_hatch('xox')
    bars[5].set_hatch('ox')
    plt.xlabel('years')
    plt.ylabel('death_count')
    plt.show()

################################################
#              RECOVERY ANALYSIS               #
################################################
def recovanalysis():
    years=[2015,2016,2017,2018,2019,2020]
    rec_count=[325,274,342,266,229,250]
    bars=plt.bar(years,rec_count,color=['red','#C76114','orange','blue','silver','gold'])
    bars[0].set_hatch("x*")
    bars[1].set_hatch("*")
    bars[2].set_hatch('o+')
    bars[3].set_hatch('x')
    bars[4].set_hatch('xox')
    bars[5].set_hatch('ox')
    plt.xlabel('years')
    plt.ylabel('rec_count')
    plt.show()
    
    

################################################
#              GET CHOICE                      #
################################################
def getchoice():
    while True:
        pmenu()
        ch = input("\t\t\t Enter Your Choice :: ")
        if ch == '1':
            print("PATIENT REGISTRATION")
            patRegister()
        elif ch=='2':
            print("PATIENT UPDATION")
            patUpdate()
        elif ch=='3':
            print("PATIENT DELETION")
            patRemove()
        elif ch=='4':
            print("PATIENT SEARCHING")
            print("1. By ID")
            print("2. By Name")
            ch = input("Enter your search criteria :: ")
            if ch == '1':
                serPatientbyIDPrint()
                print()
                print()
            elif ch == '2':
                serPatientbyName()
                print()
                print()
        elif ch=='5':
            print("\t\tLIST OF PATIENTS")
            print("----------------------------------------")
            dispPatient()
        elif ch== '6':
            deathanalysis()
        elif ch== '7':
            recovanalysis()    
        elif ch == '8':
            break
        else:
            print("INVALID CHOICE")

        input("Press ENTER KEY to continue.....")

#main

#################
#          login sys    #
################
A= 10
while A== 10:
	username= input("what is your username:- ")
	if username == 'meet'.lower():
		pw = input("please enter your password:- ")
		if pw=="meet@123":
			getchoice()
		else:
			print("inalid passward")
			
	elif username == 'dev'.lower():
		pw = input("please enter your password:- ")
		if pw=="dev@123":
			getchoice()
		else:
			print("inalid passward ")
			
	elif username == 'raj'.lower():
		pw = input("please enter your password:- ")
		if pw=="raj@123":
			getchoice()
		else:
			print("inalid passward ")
			
	else:
		print("invalid username")
	
		
			
	
            
	
        
            
			
            
            
            
            
                
	     
			
		
		




