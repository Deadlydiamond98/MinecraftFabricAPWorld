from __future__ import annotations

from worlds.minecraft_fabric.region.mc_regions_consts import ITEMSANITY_HARD, DISCS
from worlds.minecraft_fabric.region.regions_helper import create_locations_and_connect
from worlds.minecraft_fabric.logic.vanilla_logic import *


if TYPE_CHECKING:
   from worlds.minecraft_fabric import FabricMinecraftWorld


def create_healpgood_itemsanity_regions(world: FabricMinecraftWorld):
    create_locations_and_connect(world, "Menu", "MenuHealPGoodItemsanity", {
        "Heart Crystal Sliver (Itemsanity) {Healing Pretty Good}": ITEMSANITY_HARD,
        "Heart Crystal Shard (Itemsanity) {Healing Pretty Good}": ITEMSANITY_HARD,
        "Heart Piece (Itemsanity) {Healing Pretty Good}": ITEMSANITY_HARD,
        "Heart Cookie (Itemsanity) {Healing Pretty Good}": ITEMSANITY_HARD,
        "Crystal Apple (Itemsanity) {Healing Pretty Good}": ITEMSANITY_HARD,
        "Empty Heart Container (Itemsanity) {Healing Pretty Good}": ITEMSANITY_HARD,
        "Music Disc Heartstep (Itemsanity) {Healing Pretty Good}": DISCS,
        "Heart Crystal Block (Itemsanity) {Healing Pretty Good}": ITEMSANITY_HARD,
        "Polished Heart Crystal (Itemsanity) {Healing Pretty Good}": ITEMSANITY_HARD,
        "Polished Heart Crystal Stairs (Itemsanity) {Healing Pretty Good}": ITEMSANITY_HARD,
        "Polished Heart Crystal Slab (Itemsanity) {Healing Pretty Good}": ITEMSANITY_HARD,
        "Heart Crystal Bricks (Itemsanity) {Healing Pretty Good}": ITEMSANITY_HARD,
        "Heart Crystal Brick Stairs (Itemsanity) {Healing Pretty Good}": ITEMSANITY_HARD,
        "Heart Crystal Brick Slab (Itemsanity) {Healing Pretty Good}": ITEMSANITY_HARD
    }, lambda state: canUseDiamondTools(world, state))

    create_locations_and_connect(world, "Menu", "TradingHealPGoodItemsanity", {
        "Bottle O' Healing (Itemsanity) {Healing Pretty Good}": ITEMSANITY_HARD
    }, lambda state: canTrade(world, state))

    create_region(world, "Menu", "HasNetherAccess", {
        "Heart Lantern (Itemsanity) {Healing Pretty Good}": ITEMSANITY_HARD,
        "Crystal Heart (Itemsanity) {Healing Pretty Good}": ITEMSANITY_HARD
    }, lambda state: canAccessNether(world, state))

    create_region(world, "HasNetherAccess", "HasNetherAndEndAccess", {
        "Heart Container (Itemsanity) {Healing Pretty Good}": ITEMSANITY_HARD
    }, lambda state: canAccessEnd(world, state))




def create_region(world: FabricMinecraftWorld, region_name: str, new_region_name: str, locations: dict[str, int], rule=None):
    create_locations_and_connect(world, region_name + "HealPGoodItemsanity", new_region_name + "HealPGoodItemsanity", locations, rule)