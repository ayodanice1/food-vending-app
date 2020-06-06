import datetime


def build_item_quantity_matrix(*args):
    items = args[0].split(',')
    quantities = args[1].split(',')
    
    item_quantity_pairs = []
    
    for i in range(len(items)):
        item = items[i]
        quantity = quantities[i]
        if item.isalnum() and quantity.isalnum():
            item_quantity_pairs.append([item, quantity])
    return item_quantity_pairs

def build_list_from_string(string_input):
    token_list = string_input.split(',')
    return_list = []
    # Filter tokens for non-alphanumerics
    for token in token_list:
        stripped_token = token.strip()
        if stripped_token.isalnum():
            return_list.append(stripped_token.capitalize())
    return return_list

def get_today_name():
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    # Set today's date. E.g. Fri May 00:00:00 2020
    today_string = datetime.date.today().ctime()
    today = today_string.split()[0]
    for day in days:
        if day.startswith(today):
            return day
    return 'Saturday'

# Abandoned due to need for it, but can't delete all the effort put into it
def get_difference_in_time(time_on_order):
    current_daytime = datetime.datetime.now()
    currnt_date = str(current_daytime)[:10].split('-')
    order_creation_date = str(time_on_order)[:10].split('-')
    current_time = str(current_daytime)[11:19].split(':')
    order_creation_time = str(time_on_order)[11:19].split(':')
    
    difference_in_hours = int(order_creation_time[0]) - int(current_time[0])
    if difference_in_hours > 1:
        difference_in_minutes = int(order_creation_time[1]) - int(current_time[1])
        if difference_in_minutes < 10:
            print(difference_in_minutes)
        else:
            print(difference_in_hours)
    
