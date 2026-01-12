from BaseClasses import ItemClassification, Item
from worlds.AutoWorld import World
from worlds.minecraft_fabric.items import item_table, end_index
from worlds.minecraft_fabric.locations import location_table
from worlds.minecraft_fabric.options import FMCOptions
from worlds.minecraft_fabric.region import create_regions


class FabricMinecraftWorld(World):
    game = "Minecraft Fabric"
    options_dataclass = FMCOptions
    options: FMCOptions
    topology_present = True

    item_name_to_id = {
        item.name: item.item_id for item in item_table
    }

    location_name_to_id = location_table


    def __init__(self, multiworld, player):
        super().__init__(multiworld, player)

    def create_regions(self):
        create_regions(self)

    def create_item(self, name: str) -> "Item":
        return Item(name, ItemClassification.progression, self.item_name_to_id[name], self.player)

    def create_items(self):
        total_items = len(self.multiworld.get_unfilled_locations(self.player))

        # Progression Items
        total_items = self.add_to_pool(0, total_items)
        total_items = self.add_to_pool(0, total_items)

        # Filler Items
        for i in range(total_items):
            total_items = self.add_to_pool(self.random.randint(0, end_index), total_items)


    def add_to_pool(self, index: int, total_items: int):
        self.multiworld.itempool.append(Item(item_table[index].name, item_table[index].item_type, item_table[index].item_id, self.player))
        total_items -= 1
        return total_items
