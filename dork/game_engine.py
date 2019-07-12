"""
A module that works as an interface between the main classes in the game
"""
import incoming_data as ymal_data


def building_map(data):
    """
    Map classes uses this method to build map information.
    """
    # building_map(data)
    room_names = ymal_data.load_rooms(data)
    room_cardinals = ymal_data.load_cardinals(data, room_names)
    room_doors = ymal_data.load_doors(data, room_names)
    room_descrips = ymal_data.load_room_descrips(data, room_names)
    room_items = ymal_data.load_list_room_items(data, room_names )
    #We will pass this to the Map Class and then Map will pass it to the room class.
    print('The map has been successfully loaded')

def loading_item(data):
    """
    """
    # loading_items(data)
    items_name= ymal_data.load_items(data)
    items_descriptions = ymal_data.load_items_descriptions(data, items_name)
    items_properties = ymal_data.load_items_properties(data, items_name)
    #We will pass this to the Item Manager and the Item Manager will pass it to Item Class

def move(cardinal):
    """
    
    """
    pass


def use_item(item_name, action):
    """
    
    """
    pass
