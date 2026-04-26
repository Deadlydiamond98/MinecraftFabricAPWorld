from __future__ import annotations


from worlds.minecraft_fabric.region.regions_helper import create_locations_and_connect
from worlds.minecraft_fabric.logic.vanilla_logic import *


if TYPE_CHECKING:
   from worlds.minecraft_fabric import FabricMinecraftWorld


def create_ironchests_itemsanity_regions(world: FabricMinecraftWorld):
    create_locations_and_connect(world, "Menu", "MenuIronChestsItemsanity", {
        "Blank Chest Upgrade (Itemsanity) {Iron Chests: Restocked}": 5
    })

    # Has Smelting
    create_region(world, "Menu", "HasSmelting", {
        "Crystal Chest Upgrade (Itemsanity) {Iron Chests: Restocked}": 5,
        "Copper Chest Upgrade (Itemsanity) {Iron Chests: Restocked}": 5,
        "Iron Chest Upgrade (Itemsanity) {Iron Chests: Restocked}": 5,
        "Iron Dolly (Itemsanity) {Iron Chests: Restocked}": 7,
    }, lambda state: canSmelt(world, state))

    # Has Smelting And Storage
    create_region(world, "HasSmelting", "HasSmeltingAndStorage", {
        "Copper Chest (Itemsanity) {Iron Chests: Restocked}": 5,
        "Copper Barrel (Itemsanity) {Iron Chests: Restocked}": 5,
        "Iron Chest (Itemsanity) {Iron Chests: Restocked}": 5,
        "Iron Barrel (Itemsanity) {Iron Chests: Restocked}": 5,
    }, lambda state: canSmelt(world, state) and canAccessChests(world, state))

    # Has Smelting And Storage And Gold
    create_region(world, "HasSmeltingAndStorage", "HasSmeltingAndStorageAndGold", {
        "Gold Chest (Itemsanity) {Iron Chests: Restocked}": 5,
        "Gold Barrel (Itemsanity) {Iron Chests: Restocked}": 5
    }, lambda state: canSmelt(world, state) and canAccessChests(world, state) and canGetGold(world, state))

    # Has Smelting And Storage And Gold And Iron Tools
    create_region(world, "HasSmeltingAndStorageAndGold", "HasSmeltingAndStorageAndGoldAndIronTools", {
        "Diamond Chest (Itemsanity) {Iron Chests: Restocked}": 5,
        "Diamond Barrel (Itemsanity) {Iron Chests: Restocked}": 5,
        "Crystal Chest (Itemsanity) {Iron Chests: Restocked}": 5,
        "Crystal Barrel (Itemsanity) {Iron Chests: Restocked}": 5,
    }, lambda state: canSmelt(world, state) and canAccessChests(world, state) and canGetGold(world, state) and canUseIronTools(world, state))

    # Has Smelting And Storage And Gold And Iron Tools And Obsidian
    create_region(world, "HasSmeltingAndStorageAndGoldAndIronTools", "HasSmeltingAndStorageAndGoldAndIronToolsAndObsidian", {
        "Obsidian Chest (Itemsanity) {Iron Chests: Restocked}": 5,
        "Obsidian Barrel (Itemsanity) {Iron Chests: Restocked}": 5,
    }, lambda state: canSmelt(world, state) and canAccessChests(world, state) and canGetGold(world, state) and canUseIronTools(world, state) and canGetObsidian(world, state))

    # Netherite Chest Upgrade And Storage
    create_region(world, "HasSmeltingAndStorageAndGoldAndIronTools", "HasSmeltingAndStorageAndGoldAndIronToolsAndNetherite", {
        "Netherite Chest (Itemsanity) {Iron Chests: Restocked}": 5,
        "Netherite Barrel (Itemsanity) {Iron Chests: Restocked}": 5,
    }, lambda state: canUseDiamondTools(world, state) and canSmith(world, state) and canAccessChests(world, state))

    # Has Gold
    create_region(world, "Menu", "HasGold", {
        "Gold Chest Upgrade (Itemsanity) {Iron Chests: Restocked}": 5,
    }, lambda state: canGetGold(world, state))

    # Has Obsidian
    create_region(world, "Menu", "HasObsidian", {
        "Obsidian Chest Upgrade (Itemsanity) {Iron Chests: Restocked}": 5,
    }, lambda state: canGetObsidian(world, state))

    # Has Gold And Iron Tools
    create_region(world, "HasGold", "HasGoldAndIronTools", {
        "Diamond Chest Upgrade (Itemsanity) {Iron Chests: Restocked}": 5,
        "Diamond Dolly (Itemsanity) {Iron Chests: Restocked}": 7,
    }, lambda state: canUseIronTools(world, state) and canGetGold(world, state))

    # Netherite Chest Upgrade
    create_region(world, "HasGoldAndIronTools", "NetheriteChest", {
        "Netherite Chest Upgrade (Itemsanity) {Iron Chests: Restocked}": 5,
    }, lambda state: canUseDiamondTools(world, state) and canSmith(world, state))

    # Can Smelt and Compact
    create_region(world, "HasSmelting", "CanSmeltItemsAndCompact", {
        "Key (Itemsanity) {Iron Chests: Restocked}": 5,
        "Key Ring (Itemsanity) {Iron Chests: Restocked}": 5,
    }, lambda state: canCompactResources(world, state) and canSmelt(world, state))

    # Can Smelt and Compact
    create_region(world, "Menu", "GoldAndCompacting", {
        "Lock (Itemsanity) {Iron Chests: Restocked}": 5,
    }, lambda state: canCompactResources(world, state) and canGetGold(world, state))


def create_region(world: FabricMinecraftWorld, region_name: str, new_region_name: str, locations: dict[str, int], rule=None):
    create_locations_and_connect(world, region_name + "IronChestsItemsanity", new_region_name + "IronChestsItemsanity", locations, rule)