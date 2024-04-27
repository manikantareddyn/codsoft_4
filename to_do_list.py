# Creating To do list application
print('TO-DO LIST')

# let create an empty list and name it as tasks
tasks=[  ]
# define a function named to_do_list
# It can call multiple times
def to_do_list( ):
    


# let create a variable named 'choice' to get user input to add , edit or to remove tasks
   choice=input('''Enter :
        1 to add task 
        2 to edit tas
        3 to remove task : ''')
   try :
       choice=int(choice)
       if 0<choice<=3:
           if choice==1:
               task=input('Add task :')
               tasks.append(task)
               
           elif choice==2 :
               try:
                   index=int(input('Enter serial no. of task to edit :'))
                   index-=1
                   if 0<=index<len(tasks):
                       task=input('Enter new task :')
                       tasks[index]=task
                   else :
                       print('Serial no. not found')    
               except ValueError:
                   print('Invalid input')
                   
           else:
               try :
                    index=int(input('Enter serial no. of task to remove :'))
                    index-=1
                    if 0<=index<len(tasks):
                       tasks.pop(index)
                    else :
                       print('Serial no. not found')    
               except ValueError:
                      print('Invalid input')
       else :
           print('Input between 1 and 3')
   except Valueerror:
       print('Invalid input')
# the below for loop prints all modified tasks
   print('')
   for i,task in enumerate(tasks,start=1):
       print(f'task_{i} : {task}')  
   print('')  
# Call the above function multiple times
while True:
   to_do_list( )
   

    
