from __future__ import annotations


from worlds.minecraft_fabric.region.regions_helper import create_locations_and_connect
from worlds.minecraft_fabric.logic.vanilla_logic import *


if TYPE_CHECKING:
   from worlds.minecraft_fabric import FabricMinecraftWorld


def create_healpgood_advancements_regions(world: FabricMinecraftWorld):
    create_locations_and_connect(world, "Menu", "MenuHealPGoodAdvancement", {
        "Heart Breaker {Healing Pretty Good}": 7,
        "Heart Donor {Healing Pretty Good}": 7
    }, lambda state: canUseDiamondTools(world, state))

    create_region(world, "Menu", "HasNetherAccess", {
        "Heart-Side Unlocked {Healing Pretty Good}": 7
    }, lambda state: canAccessNether(world, state))

    create_region(world, "HasNetherAccess", "HasNetherAndEndAccess", {
        "Phanes Blessing {Healing Pretty Good}": 7,
        "Maxed Out {Healing Pretty Good}": 8
    }, lambda state: canAccessEnd(world, state))

def create_region(world: FabricMinecraftWorld, region_name: str, new_region_name: str, locations: dict[str, int], rule=None):
    create_locations_and_connect(world, region_name + "HealPGoodAdvancement", new_region_name + "HealPGoodAdvancement", locations, rule)