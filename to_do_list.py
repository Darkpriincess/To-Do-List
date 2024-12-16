to_do =[]

def add_to_list():
    '''adding tasks to the list'''
    task=''
    while task != 'done':
        task = input("What task would you like to add to your to-do list? Type 'done' when finished.\n")    
        if task != 'done':           
            to_do.append(task)
            print( f"{task} added sucessfully. Would you like to add another? Type done when finished.")


        
        
        
def view_list():
    '''check if a task is on the list or viewing the entire list'''
    display = ''
    while display != 'done':
        display = input("Please type which task you would like to view, or " +
                 "type 'full' to view your entire list. Type 'done when finished.\n")
        if display != 'done':
            if display == 'full':
                if not to_do: #is the list empty?
                    print(f'Your to-do list is empty.')
                else:
                    for i in to_do:
                        print(i)
            elif display in to_do:
                print(f"{display} is in your to-do list.")
            else:
                print(f"{display} is not on your to-do list.")
        
        
def del_from_list():
    '''deleting items from the list'''
    delete = ''
    while delete != 'done':
        delete = input("Which task would you like to delete? Type 'done' if finished.\n")
        if delete != 'done':    
            try:
                to_do.remove(delete)                
            except:
                print("Sorry, that task is not in your to-do list. Would you like to delete something else? Type 'done' when finished\n")
            else:
                print(f'{delete} successfully deleted from your to-do list.')
        
    
def home_page():
    while True:
        prompt = 'Welcome to your to-do list. Would you like add, view, or delete tasks.\n'
        prompt += 'PLease type "add", "view", or "delete". Type "done" when finished.\n'
        menu = (input(prompt))
        if menu == "done":
            break
        elif menu == "add":
            add_to_list()
        elif menu == "view":
            view_list()
        elif menu == "delete":
            del_from_list()
        else:
            print('Sorry, that option is not available. Please type "add", "view", "delete" or "done".\n')
            
home_page()