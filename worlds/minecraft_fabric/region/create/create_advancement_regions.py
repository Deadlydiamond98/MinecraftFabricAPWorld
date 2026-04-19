from __future__ import annotations


from worlds.minecraft_fabric.region.regions_helper import create_locations_and_connect
from worlds.minecraft_fabric.logic.create_logic import *


if TYPE_CHECKING:
   from worlds.minecraft_fabric import FabricMinecraftWorld


def create_create_advancement_regions(world: FabricMinecraftWorld):
    create_locations_and_connect(world, "Menu", "MenuCreateAdvancements", {

    })

    # Has Andesite Alloy
    create_region(world, "Menu", "AndesiteAlloy", {
        "Sturdier Rocks": 0,
        "The Andesite Age": 0,
        "Workout Session": 0
    }, lambda state: canCraftAndesiteAlloyCreate(world, state))

    # Has Cogs
    create_region(world, "AndesiteAlloy", "Cogs", {
        "Shifting Gears": 0,
        "Embrace the Grind": 0
    }, lambda state: hasCogs(world, state))

    # Has Water Wheel
    create_region(world, "AndesiteAlloy", "WaterWheel", {
        "Harnessed Hydraulics": 0
    }, lambda state: hasWaterWheel(world, state))

    # Has Windmill
    create_region(world, "AndesiteAlloy", "Windmill", {
        "A mild Breeze": 0,
        "A strong Breeze": 0
    }, lambda state: hasWindmill(world, state))

    # Has Press
    create_region(world, "AndesiteAlloy", "Press", {
        "Area of Connect": 0,
        "Moving with Purpose": 0,
        "Drive-by Exchange": 0,
        "Rope to Nowhere": 0,
        "Bonk!": 0,
        "Wind Maker": 0,
        "Processing by Particle": 0,
        "Workshop's Most Feared": 0,
        "Compactification": 0,
        "Vertical Logistics": 0
    }, lambda state: hasPress(world, state))

    # Has Mixer
    create_region(world, "AndesiteAlloy", "Mixer", {
        "Mixing It Up": 0
    }, lambda state: hasMixer(world, state))

    # Has Kelp
    create_region(world, "AndesiteAlloy", "Kelp", {
        "Kelp Drive": 0
    }, lambda state: canCraftAndesiteAlloy(world, state) and canCraftDriedKelp(world, state))

    # Has Cardboard
    create_region(world, "AndesiteAlloy", "Cardboard", {
        "Part and Parcel": 0
    }, lambda state: canCraftCardboard(world, state))

    # Has Water Wheel And Bucket
    create_region(world, "WaterWheel", "WaterWheelAndBucket", {
        "Magma Wheel": 0
    }, lambda state: hasWaterWheel(world, state) and canUseBucket(world, state))

    # Has Kelp And Press
    create_region(world, "Kelp", "KelpAndPress", {
        "The Parrots and the Flaps": 0
    }, lambda state: canCraftAndesiteAlloy(world, state) and canCraftDriedKelp(world, state) and hasPress(world, state))

    # Has Press and Nether
    create_region(world, "Press", "PressAndNether", {
        "Sentient Fireplace": 0
    }, lambda state: hasPress(world, state) and canAccessNether(world, state))

    # Has Kelp And Chests
    create_region(world, "Kelp", "KelpAndChests", {
        "Kelp Drive": 0
    }, lambda state: canCraftAndesiteAlloy(world, state) and canCraftDriedKelp(world, state) and canAccessChests(world, state))

    # Has Press and Minecarts
    create_region(world, "Press", "PressAndMinecart", {
        "Strong Arms": 1
    }, lambda state: hasPress(world, state) and canUseMinecart(world, state))

    # Has Press and Cogs
    create_region(world, "Press", "PressAndCogs", {
        "Springboard Champion": 0
    }, lambda state: hasPress(world, state) and hasCogs(world, state))

    # Has Iron Tools
    create_region(world, "AndesiteAlloy", "AlloyAndIronTools", {
        "Is it Time?": 0
    }, lambda state: canUseIronTools(world, state))

    # Has Press and Armor
    create_region(world, "Press", "PressAndArmor", {
        "Kitted Out": 0,
        "Stress for Nerds": 0,
        "Perfectly Stressed": 0
    }, lambda state: hasPress(world, state) and canWearLeatherArmor(world, state) and canUseIronTools(world, state))

    # Has Mechanical Press and Enchanting
    create_region(world, "AndesiteAlloy", "MechanicalPressAndEnchant", {
        "Blacksmith Artillery": 0
    }, lambda state: canCraftAndesiteAlloyCreate(world, state) and canEnchant(world, state))

    # Has Blaze Burner and Mechanical Arm
    create_region(world, "AndesiteAlloy", "FeedBlazeBurnerWithArm", {
        "Combust-o-Tron": 0
    }, lambda state: canCraftBrass(world, state) and canCraftPercisionMechanism(world, state) and hasBlazeBurner(world, state))


def create_region(world: FabricMinecraftWorld, region_name: str, new_region_name: str, locations: dict[str, int], rule=None):
    create_locations_and_connect(world, region_name + "CreateAdvancements", new_region_name + "CreateAdvancements", locations, rule)