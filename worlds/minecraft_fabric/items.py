from dataclasses import dataclass

from jinja2.nodes import List

from BaseClasses import ItemClassification

@dataclass
class MCItem:
    name: str
    item_type: ItemClassification
    item_id: int

@dataclass
class MCItemPart:
    items: list[MCItem]
    last_index: int

# Items that can be added ##############################################################################################

progression = [
    "Apple"
]

useful_index = len(progression) - 1

useful = [
    "Sword"
]

traps_index = len(useful) + useful_index - 1

traps = [
    "Reverse Trap",
    "Ice Trap",
    "Random Status Trap",
    "Stun Trap",
    "TNT Trap",
    "Teleport Trap",
    "Bee Trap",
    "Insomnia Trap",
    "Soul Sand Trap",
    "Literature Trap"
]

end_index = len(traps) + traps_index - 1

# Helper methods #######################################################################################################

# initializes the item table
def get_item_table():
    items = []

    progression_part = get_items_part(ItemClassification.progression, 1, progression)
    items += progression_part.items
    traps_part = get_items_part(ItemClassification.trap, len(items), traps)
    items += traps_part.items

    return items

# This returns an MCItemPart, which is a list of items and an index for the next list's item ids
def get_items_part(item_type: ItemClassification, new_index: int, names: list[str]):
    return MCItemPart([MCItem(name, item_type, index + new_index) for index, name in enumerate(names)], new_index + len(names))


item_table: list[MCItem] = get_item_table()
