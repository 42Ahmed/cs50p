from tabulate import tabulate


checklist = []


asci = """

░█████╗░██╗░░██╗███████╗░█████╗░██╗░░██╗██╗░░░░░██╗░██████╗████████╗
██╔══██╗██║░░██║██╔════╝██╔══██╗██║░██╔╝██║░░░░░██║██╔════╝╚══██╔══╝
██║░░╚═╝███████║█████╗░░██║░░╚═╝█████═╝░██║░░░░░██║╚█████╗░░░░██║░░░
██║░░██╗██╔══██║██╔══╝░░██║░░██╗██╔═██╗░██║░░░░░██║░╚═══██╗░░░██║░░░
╚█████╔╝██║░░██║███████╗╚█████╔╝██║░╚██╗███████╗██║██████╔╝░░░██║░░░
░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝╚═════╝░░░░╚═╝░░░
"""

bye = """

██████╗░██╗░░░██╗███████╗
██╔══██╗╚██╗░██╔╝██╔════╝
██████╦╝░╚████╔╝░█████╗░░
██╔══██╗░░╚██╔╝░░██╔══╝░░
██████╦╝░░░██║░░░███████╗
╚═════╝░░░░╚═╝░░░╚══════╝
"""



# shows the user all the available commands
def show_help():
    print("To add an item, type 'add' followed by the item.")
    print("To update an item, type 'update' followed by the item ID and the new item.")
    print("To delete an item, type 'delete' followed by the item ID.")
    print("To mark an item as done, type 'done' followed by the item ID.")
    print("To mark an item as undone, type 'undone' followed by the item ID.")
    print("To view the entire checklist, type 'view'.")
    print("To view the items that are marked as done, type 'view done'.")
    print("To view the items that are marked as undone, type 'view undone'.")
    print("To quit the program, type 'quit'.\n")





def add_item(item_text):
    """
    Add item to the checklist

    Example:
    add_item("study")
    """

    item = {'id': len(checklist) + 1, 'item': item_text, 'done': False}
    checklist.append(item)





def update_item(item_id, item_text):
    """
    update an item by providing id of the required item and the new item

    Example:
    update_item(1,"sleep")
    """
    for item in checklist:
        if item['id'] == item_id:
            item['item'] = item_text
            break




def delete_item(item_id):
    """
    deletes an item then reorder the ID

    Example:
    delete_item(1)
    """
    for item in checklist:
        if item['id'] == item_id:
            checklist.remove(item)
            break

    # reorder the items ID
    for i, item in enumerate(checklist):
        item['id'] = i + 1





def mark_done(item_id):
    """
    marks an item as done by providing ID

    Example:
    mark_done(1)
    """
    for item in checklist:
        if item['id'] == item_id:
            item['done'] = True
            break




def mark_undone(item_id):
    """
    marks an item as undone by providing ID

    Example:
    mark_undone(1)
    """
    for item in checklist:
        if item['id'] == item_id:
            item['done'] = False
            break




def display_checklist():
    """
    displays all items
    """
    headers = ['ID', 'Item', 'Done']
    rows = []

    for item in checklist:
        rows.append([item['id'], item['item'], '✔' if item['done'] else '❌'])
    print(tabulate(rows, headers=headers, tablefmt='pretty'))




def display_done_items():
    """
    displays done items only
    """
    headers = ['ID', 'Item']
    rows = []

    for item in checklist:
        if item['done']:
            rows.append([item['id'], item['item']])
    if not rows:
        print("No items marked as done.")

    print(tabulate(rows, headers=headers, tablefmt='pretty'))




def display_undone_items():
    """
    displays undone items only
    """

    headers = ['ID', 'Item']
    rows = []

    for item in checklist:
        if not item['done']:
            rows.append([item['id'], item['item']])
    if not rows:
        print("No items marked as undone.")

    print(tabulate(rows, headers=headers, tablefmt='pretty'))





def main():

    print(asci)

    # infinite loop, stops when user inputs 'quit'
    while True:

        user_input = input("Enter a command (type 'help' for assistance): ")


        if user_input.startswith('add'):
            item_text = user_input[4:].strip()
            if item_text:
                add_item(item_text)
                print("Item added to checklist.")
                display_checklist()
            else:
                print("Please enter an item to add to the checklist.")

        elif user_input.startswith('update'):
            input_parts = user_input.split()
            if len(input_parts) < 3:
                print("Please specify an item ID and new text to update.")
            else:
                try:
                    item_id = int(input_parts[1])
                    item_text = ' '.join(input_parts[2:])
                    update_item(item_id, item_text)
                    print("Item updated in checklist.")
                    display_checklist()
                except ValueError:
                    print("Please enter a valid item ID.")

        elif user_input.startswith('delete'):
            input_parts = user_input.split()
            if len(input_parts) < 2:
                print("Please specify an item ID to delete.")
            else:
                try:
                    item_id = int(input_parts[1])
                    delete_item(item_id)
                    print("Item deleted from checklist.")
                    display_checklist()
                except ValueError:
                    print("Please enter a valid item ID.")

        elif user_input.startswith('done'):
            input_parts = user_input.split()
            if len(input_parts) < 2:
                print("Please specify an item ID to mark as done.")
            else:
                try:
                    item_id = int(input_parts[1])
                    mark_done(item_id)
                    print("Item marked as done in checklist.")
                    display_checklist()
                except ValueError:
                    print("Please enter a valid item ID.")

        elif user_input.startswith('undone'):
            input_parts = user_input.split()
            if len(input_parts) < 2:
                print("Please specify an item ID to mark as undone.")
            else:
                try:
                    item_id = int(input_parts[1])
                    mark_undone(item_id)
                    print("Item marked as undone in checklist.")
                    display_checklist()
                except ValueError:
                    print("Please enter a valid item ID.")

        elif user_input == 'view':
            display_checklist()

        elif user_input == 'view done':
            display_done_items()

        elif user_input == 'view undone':
            display_undone_items()

        elif user_input == 'help':
            show_help()

        elif user_input == 'quit':
            print(bye)
            break

        else:
            print("Invalid command. Type 'help' for assistance.")







if __name__ == "__main__":
    main()