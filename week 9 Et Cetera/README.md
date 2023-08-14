# Checklist

## Video Demo

 <https://www.mediafire.com/file/50nqlkdqo5dgohn/project.py_-_project_-_Visual_Studio_Code_2023-05-21_13-32-28.mp4/file>

### Description

User can add,update,delete and view items in a checklist,
mark them as done or undone,
view done items only or undone only or the entire checklist.

#### Details

The program first greets the user with ascii art "checklist".
Then the program enters an infinite loop waiting for input.

*Note* The program will quit if and only if the user inputs 'quit'.

The user can type 'help' which will show him all the commands and its explanation.

He can start adding items by the command 'add'.

He can update the item by the command 'update'

He can delete the item by the command 'delete'

He can view the items by the command 'view'

He can mark the items done by the command 'done'

He can mark the items done by the command 'undone'

He can view done items only by the command 'view done'

He can view undone items only by the command 'view undone'

#### Implementation Details

I was confused at the beeginning whether i should use the sys module or not, i ended up using input() and infinite loop to be more user friendly.

I still dont know how to use gui with python
but i remember ascii art from the lecture so decided to use it to make it even more friendly.

I then added show_help() and included in it all the commands and their explanation that my program should use.

Then I implemented each function.

I made the functions such that they all return none and just print to the user as a side effect to be easier for me to code.

In add_item(), it expects the name of the item. example: "add study" then it should make a dictionary called item with id starting from 1 and then add the dictionary of item to a list called checklist and it assumes the item is marked undone.

In update_item(), it expects ID (for simplicity) then the new item name.
Example: 'update 1 sleep'. It checks every dictionary (item) in the checklist, if Id ebtered matches the dict ID, the text of the dict  is changed to the new text.

In delete_item(), it checks every dict (item) in the checklist and if id inputed matches dict id then it removes the specified dict from the list checklist. Then it reorders the Id of the items.
I thought that an list starting with id 2 will be confusing thats why i decided to automatically view the checklist after each command.

In mark_done() and mark_undone() they search for the Id in items and if found sets the key 'done' of the item to false or true.

*Note* to make the coding easy, I chose to error check in the main function instead of in each function.

In display_checklist(), it defines the header then loops over checklist items and adds each dict to the row changing true and false to emojies ✔ ❌ user friendly:)
Then using tabulate, it prints the row and header in format pretty.

display_done_items() and display_undone_items() do similar behavior but first check if item key done is true or false and doesnt add to the row item key done.

The main function greets the user with an ascii art then enters an infinite loop.

It asks the user for input and recommends typing help for help
if item writes add without knowing how to use it the program teaches him. then the program checks if input start with add and if so store the input stripped to item_text and call add_item function then prints the user that item is saved and displays the new item.

I couldnt force the input to lower because maybe the user wants to actually store items in upper case.
if user prints quit the ascii bye is printed and program breaks.

inputting help, view, view done, view undone will call the appropriate functions.

update, delete, done  and undone will all check for length of user input and if it is not appropriate they will print to the user how to use the commands. Then they will all try sending the id to the specified functions and if any error occurs they warn the user to input a valid ID. If they succeed it will be printed to them the new checklist by calling display_checklist()

*Note* I thought about printing usage examples but perhaps it will annoy frequent users.
