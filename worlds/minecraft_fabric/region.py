from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from worlds.minecraft_fabric import FabricMinecraftWorld

from BaseClasses import Region, Location, CollectionState
from worlds.minecraft_fabric.locations import location_table


def get_goal_condition(world: FabricMinecraftWorld, state: CollectionState):
    return state.has("Apple", world.player, 2)


def create_regions(world):
    # Menu Region
    create_locations(world, "Menu", [
        "Test Location 1",
        "Test Location 2",
        "Test Location 3",
        "Test Location 4",
        "Test Location 5",
        "Test Location 6",
        "Test Location 7",
        "Test Location 8",
        "Test Location 9",
        "Test Location 10"
    ])

    # Goal
    world.multiworld.completion_condition[world.player] = lambda state: get_goal_condition(world, state)


def create_locations(world: FabricMinecraftWorld, region_name: str, locations: list[str]):
    region = Region(region_name, world.player, world.multiworld, region_name)
    region.locations += [Location(world.player, name, location_table[name], region) for name in locations]
    world.multiworld.regions.append(region)