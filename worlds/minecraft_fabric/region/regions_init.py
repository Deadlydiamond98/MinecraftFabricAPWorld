from __future__ import annotations


from typing import TYPE_CHECKING, Optional

from worlds.minecraft_fabric.region.create.create_advancement_regions import create_create_advancement_regions
from worlds.minecraft_fabric.region.create.create_itemsanity_regions import create_create_itemsanity_regions
from worlds.minecraft_fabric.region.healpgood.healpgood_advancement_regions import create_healpgood_advancements_regions
from worlds.minecraft_fabric.region.healpgood.healpgood_itemsanity_regions import create_healpgood_itemsanity_regions
from worlds.minecraft_fabric.region.ironchests.ironchests_itemsanity_regions import create_ironchests_itemsanity_regions
from worlds.minecraft_fabric.region.regions_helper import create_locations_advanced
from worlds.minecraft_fabric.region.vanilla.vanilla_advancement_regions import create_vanilla_advancement_regions
from worlds.minecraft_fabric.region.vanilla.vanilla_itemsanity_regions import create_vanilla_itemsanity_regions
from worlds.minecraft_fabric.logic.vanilla_logic import *

if TYPE_CHECKING:
   from worlds.minecraft_fabric import FabricMinecraftWorld

def get_goal_condition(world, state):
    goal_id = world.options.goal_condition.value

    # I wish Python had Switch Case Statements :,(
    if goal_id == 0: # Ender Dragon
        return canGoalEnderDragon(world, state)
    elif goal_id == 1: # Wither
        return canGoalWither(world, state)
    elif goal_id == 2: # Both Bosses
        return canBeatDragonAndWither(world, state)
    elif goal_id == 4: # Ruby Hunt
        return canCompleteRubyHunt(world, state)

    # Since Advancements are Locations, just make game try to reach end of game
    return canAccessVanillaEndGame(world, state)

# Creates all Regions in the Randomizer!
def create_regions(world: FabricMinecraftWorld):
    # Creates a Main Region for everything to branch from!
    create_locations_advanced(world, "Menu", {})
    # Vanilla Regions
    create_vanilla_advancement_regions(world)
    create_vanilla_itemsanity_regions(world)
    # Create Regions
    if "create" in world.options.enabled_mods.value:
        create_create_advancement_regions(world)
        create_create_itemsanity_regions(world)
    # Healing Pretty Good Regions
    if "healpgood" in world.options.enabled_mods.value:
        create_healpgood_advancements_regions(world)
        create_healpgood_itemsanity_regions(world)
    # Iron Chests: Restocked Regions
    if "ironchests" in world.options.enabled_mods.value:
        create_ironchests_itemsanity_regions(world)

    world.multiworld.completion_condition[world.player] = lambda state: get_goal_condition(world, state)

