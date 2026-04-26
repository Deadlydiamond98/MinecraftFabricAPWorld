from worlds.minecraft_fabric.location.create.create_advancements import create_advancements
from worlds.minecraft_fabric.location.create.create_itemsanity import create_itemsanity
from worlds.minecraft_fabric.location.healpgood.healpgood_itemsanity import healpgood_itemsanity
from worlds.minecraft_fabric.location.ironchests.ironchests_itemsanity import ironchests_itemsanity
from worlds.minecraft_fabric.location.vanilla.vanilla_advancements import vanilla_advancements, archipelago_advancements
from worlds.minecraft_fabric.location.vanilla.vanilla_itemsanity import vanilla_itemsanity

########################################################################################################################
# ALL LOCATIONS IN RANDOMIZER ##########################################################################################
########################################################################################################################

def get_location_table():
    table = {}
    # VANILLA LOCATIONS
    table.update(add_locations(table, vanilla_advancements))
    table.update(add_locations(table, archipelago_advancements))
    table.update(add_locations(table, vanilla_itemsanity))
    # CREATE LOCATIONS
    table.update(add_locations(table, create_advancements))
    table.update(add_locations(table, create_itemsanity))
    # HEALING PRETTY GOOD LOCATIONS
    table.update(add_locations(table, healpgood_itemsanity))
    # IRON CHESTS: RESTOCKED LOCATIONS
    table.update(add_locations(table, ironchests_itemsanity))
    return table

def add_locations(table: dict[str, int], locations: list[str]):
    return {name: (index + len(table) + 1) for index, name in enumerate(locations)}

# Table of EVERY LOCATION
location_table = get_location_table()