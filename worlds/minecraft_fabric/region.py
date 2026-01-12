from __future__ import annotations
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from worlds.minecraft_fabric import FabricMinecraftWorld

from BaseClasses import Region, Location, CollectionState, Entrance, LocationProgressType
from worlds.minecraft_fabric.locations import location_table, vanilla_start_locations


# REGIONS ##############################################################################################################


def get_goal_condition(world: FabricMinecraftWorld, state: CollectionState):
    return state.has("Progressive Smelting", world.player)


def create_regions(world: FabricMinecraftWorld):
    # Menu Region
    create_locations(world, "Menu", vanilla_start_locations)

    # Goal
    world.multiworld.completion_condition[world.player] = lambda state: get_goal_condition(world, state)


def create_locations(world: FabricMinecraftWorld, region_name: str, locations: list[str]):
    region = Region(region_name, world.player, world.multiworld, region_name)
    region.locations += [Location(world.player, name, location_table[name], region) for name in locations]
    world.multiworld.regions.append(region)

# ENTRANCES ############################################################################################################

def connect(world, name: str, source: str, target: str, rule=None, reach: Optional[bool] = False,
            rule_to_str: Optional[str] = None, ) -> Optional[Entrance]:
    source_region = world.multiworld.get_region(source, world.player)
    target_region = world.multiworld.get_region(target, world.player)

    connection = Entrance(world.player, name, source_region)

    if rule:
        connection.access_rule = rule

    source_region.exits.append(connection)
    connection.connect(target_region)

    return connection if reach else None


def connect_entrances(world: FabricMinecraftWorld) -> None:
    pass