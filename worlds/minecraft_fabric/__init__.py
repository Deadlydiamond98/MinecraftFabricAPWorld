from typing import Mapping, Any

from BaseClasses import ItemClassification, Item
from worlds.AutoWorld import World, WebWorld
from worlds.minecraft_fabric.item.items_helper import item_table
from worlds.minecraft_fabric.item.items_init import create_local_fill_items, create_items
from worlds.minecraft_fabric.location.minecraft_locations import location_table
from worlds.minecraft_fabric.options import FMCOptions
from worlds.minecraft_fabric.region.regions_init import create_regions


class FMCWebWorld(WebWorld):
    option_groups = options.option_groups

class FabricMinecraftWorld(World):
    game = "Minecraft Fabric"
    options_dataclass = FMCOptions
    options: FMCOptions
    topology_present = True
    web = FMCWebWorld()

    item_name_to_id = {
        item.name: item.item_id for item in item_table.values()
    }

    location_name_to_id = location_table


    def __init__(self, multiworld, player):
        super().__init__(multiworld, player)
        self.max_ruby_count = 0
        self.itemsanity_locations = []
        self.local_fill_amount = 0

    def create_regions(self):
        create_regions(self)

    def fill_slot_data(self) -> Mapping[str, Any]:
        self.create_puml(False)

        advancements = 0
        items = 0

        for location in self.multiworld.get_locations():
            if location.name.endswith("(Itemsanity)"):
                items += 1
            else:
                advancements += 1

        return {
            "world_version": self.world_version.as_simple_string(),
            # Base
            "goal_condition": self.options.goal_condition.value,
            # Advancements Needed to Goal
            "advancements_to_goal": min(advancements, self.options.advancements_required_for_goal.value),
            # Items Needed to Goal
            "items_to_goal": min(items, self.options.items_required_for_goal.value),
            # Rubies
            "rubies_to_goal": self.options.percentage_of_rubies_needed.value,
            "total_rubies": self.max_ruby_count,
            "deathlink": self.options.deathlink_enabled.value,
            "traplink": self.options.traplink_enabled.value,
            # Other Options
            "keep_inventory": self.options.keep_inventory.value,
            "itemsanity": self.options.itemsanity.value,

            "randomized_abilities": self.options.randomized_abilities.value,
            "possible_randomized_abilities": self.options.randomized_abilities.valid_keys,
            "time_saving_options": self.options.time_saving_options.value,
            "enabled_mods": self.options.enabled_mods.value
        }

    def create_item(self, name: str) -> "Item":
        return Item(name, ItemClassification.progression, self.item_name_to_id[name], self.player)

    def create_items(self):
        create_items(self)

    def pre_fill(self) -> None:
        create_local_fill_items(self)


    # Creates Puml for checking Logic
    def create_puml(self, create: bool):
        if create:
            from Utils import visualize_regions
            state = self.multiworld.get_all_state()
            state.update_reachable_regions(self.player)

            reachable_regions = state.reachable_regions[self.player]
            unreachable_regions: set[Region] = set()  # type: ignore
            for regionb in self.multiworld.regions:
                if regionb not in reachable_regions:
                    unreachable_regions.add(regionb)

            visualize_regions(self.get_region("Menu"), f"{self.player_name}_world.puml", show_entrance_names=True,
                              regions_to_highlight=unreachable_regions)