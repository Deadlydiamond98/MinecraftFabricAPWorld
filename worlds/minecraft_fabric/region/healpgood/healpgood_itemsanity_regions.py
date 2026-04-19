from __future__ import annotations


from worlds.minecraft_fabric.region.regions_helper import create_locations_and_connect
from worlds.minecraft_fabric.logic.vanilla_logic import *


if TYPE_CHECKING:
   from worlds.minecraft_fabric import FabricMinecraftWorld


def create_healpgood_itemsanity_regions(world: FabricMinecraftWorld):
    create_locations_and_connect(world, "Menu", "MenuHealPGoodItemsanity", {
        "Heart Crystal Sliver (Itemsanity)": 7,
        "Heart Crystal Shard (Itemsanity)": 7,
        "Heart Piece (Itemsanity)": 7,
        "Heart Cookie (Itemsanity)": 7,
        "Crystal Apple (Itemsanity)": 7,
        "Empty Heart Container (Itemsanity)": 7,
        "Music Disc Heartstep (Itemsanity)": 7,
        "Heart Crystal Block (Itemsanity)": 7,
        "Polished Heart Crystal (Itemsanity)": 7,
        "Polished Heart Crystal Stairs (Itemsanity)": 7,
        "Polished Heart Crystal Slab (Itemsanity)": 7,
        "Heart Crystal Bricks (Itemsanity)": 7,
        "Heart Crystal Brick Stairs (Itemsanity)": 7,
        "Heart Crystal Brick Slab (Itemsanity)": 7
    }, lambda state: canUseDiamondTools(world, state))

    create_locations_and_connect(world, "Menu", "TradingHealPGoodItemsanity", {
        "Bottle O' Healing (Itemsanity)": 7
    }, lambda state: canTrade(world, state))

    create_region(world, "Menu", "HasNetherAccess", {
        "Heart Lantern (Itemsanity)": 7,
        "Crystal Heart (Itemsanity)": 7
    }, lambda state: canAccessNether(world, state))

    create_region(world, "HasNetherAccess", "HasNetherAndEndAccess", {
        "Heart Container (Itemsanity)": 7
    }, lambda state: canAccessEnd(world, state))




def create_region(world: FabricMinecraftWorld, region_name: str, new_region_name: str, locations: dict[str, int], rule=None):
    create_locations_and_connect(world, region_name + "HealPGoodItemsanity", new_region_name + "HealPGoodItemsanity", locations, rule)