from __future__ import annotations


from worlds.minecraft_fabric.region.regions_helper import create_locations_and_connect
from worlds.minecraft_fabric.logic.create_logic import *
from worlds.minecraft_fabric.region.mc_regions_consts import *

if TYPE_CHECKING:
   from worlds.minecraft_fabric import FabricMinecraftWorld


def create_create_advancement_regions(world: FabricMinecraftWorld):
    create_locations_and_connect(world, "Menu", "MenuCreateAdvancements", {})

    # Has Andesite Alloy
    create_region(world, "Menu", "AndesiteAlloy", {
        "Sturdier Rocks {Create}": ADVANCEMENT,
        "The Andesite Age {Create}": ADVANCEMENT,
        "Workout Session {Create}": ADVANCEMENT
    }, lambda state: canCraftAndesiteAlloyCreate(world, state))

    # REQUIRES ROSE QUARTZ
    create_region(world, "Menu", "RoseQuartz", {
        "Supercharged {Create}": ADVANCEMENT
    }, lambda state: canCraftRoseQuartz(world, state) and canUseSandpaper(world, state))

    # REQUIRES SMELTING
    create_region(world, "Menu", "Smelting", {
        "Cuprum Bokum {Create}": ADVANCEMENT,
        "The Copper Age {Create}": ADVANCEMENT,
        "Tumble Draining {Create}": ADVANCEMENT,
        "On a Roll {Create}": ADVANCEMENT
    }, lambda state: canGetIron(world, state))

    # Has Diving Suit
    create_region(world, "AndesiteAlloy", "HasDivingSuit", {
        "Pressure to Go {Create}": ADVANCEMENT,
        "Ready for the Depths {Create}": ADVANCEMENT
    }, lambda state: canWearGoldArmor(world, state) and canCompactResources(world, state))

    # Has Spout
    create_region(world, "AndesiteAlloy", "HasSpout", {
        "Sploosh {Create}": ADVANCEMENT
    }, lambda state: canUseSpout(world, state))

    # Has Steam Engine
    create_region(world, "AndesiteAlloy", "SteamEngine", {
        "The Powerhouse {Create}": ADVANCEMENT
    }, lambda state: hasSteamEngine(world, state))

    # Has Cogs
    create_region(world, "AndesiteAlloy", "Cogs", {
        "Shifting Gears {Create}": ADVANCEMENT,
        "Embrace the Grind {Create}": ADVANCEMENT
    }, lambda state: hasCogs(world, state))

    # Has Water Wheel
    create_region(world, "AndesiteAlloy", "WaterWheel", {
        "Harnessed Hydraulics {Create}": ADVANCEMENT
    }, lambda state: hasWaterWheel(world, state))

    # Has Windmill
    create_region(world, "AndesiteAlloy", "Windmill", {
        "A mild Breeze {Create}": ADVANCEMENT,
        "A strong Breeze {Create}": ADVANCEMENT
    }, lambda state: hasWindmill(world, state))

    # Has Press
    create_region(world, "AndesiteAlloy", "Press", {
        "Area of Connect {Create}": ADVANCEMENT,
        "Moving with Purpose {Create}": ADVANCEMENT,
        "Drive-by Exchange {Create}": ADVANCEMENT,
        "Rope to Nowhere {Create}": ADVANCEMENT,
        "Bonk! {Create}": ADVANCEMENT,
        "Wind Maker {Create}": ADVANCEMENT,
        "Processing by Particle {Create}": ADVANCEMENT,
        "Workshop's Most Feared {Create}": ADVANCEMENT,
        "Compactification {Create}": ADVANCEMENT,
        "Vertical Logistics {Create}": ADVANCEMENT,
        "Remote Activation {Create}": ADVANCEMENT
    }, lambda state: hasPress(world, state))

    # Has Pump
    create_region(world, "Press", "HasPump", {
        "Under Pressure {Create}": ADVANCEMENT,
        "Don't Cross the Streams! {Create}": ADVANCEMENT,
        "Flow Discovery {Create}": ADVANCEMENT,
        "Puddle Collector {Create}": ADVANCEMENT,
        "Industrial Spillage {Create}": ADVANCEMENT,
        "Autonomous Bee-Keeping {Create}": ADVANCEMENT
    }, lambda state: hasPump(world, state))

    # Has Mixer
    create_region(world, "AndesiteAlloy", "Mixer", {
        "Mixing It Up {Create}": ADVANCEMENT
    }, lambda state: hasMixer(world, state))

    # Has Kelp
    create_region(world, "AndesiteAlloy", "Kelp", {
        "Kelp Drive {Create}": ADVANCEMENT
    }, lambda state: canCraftAndesiteAlloy(world, state) and canCraftDriedKelp(world, state))

    # Has Cardboard
    create_region(world, "AndesiteAlloy", "Cardboard", {
        "Part and Parcel {Create}": ADVANCEMENT,
        "Full Stealth {Create}": ADVANCEMENT
    }, lambda state: canCraftCardboard(world, state))

    # Has Packager
    create_region(world, "Cardboard", "Packager", {
        "Post Production {Create}": ADVANCEMENT,
        "Order Up! {Create}": ADVANCEMENT,
        "Open for business {Create}": ADVANCEMENT,
        "Nothing but net {Create}": ADVANCEMENT
    }, lambda state: canUsePackager(world, state))

    # Has Brass
    create_region(world, "AndesiteAlloy", "Brass", {
        "Real Alloys {Create}": ADVANCEMENT,
        "The Brass Age {Create}": ADVANCEMENT,
        "Shadow Sense {Create}": ADVANCEMENT,
        "Contraption o'Clock {Create}": ADVANCEMENT,
        "Big Data {Create}": ADVANCEMENT,
    }, lambda state: canCraftBrass(world, state))

    # Has Brass And Sandpaper
    create_region(world, "AndesiteAlloy", "BrassAndSandpaper", {
        "Artificial Intelligence {Create}": ADVANCEMENT,
        "Pound It, Bro! {Create}": ADVANCEMENT
    }, lambda state: canCraftBrass(world, state) and canUseSandpaper(world, state))

    # Has Brass And Minecarts
    create_region(world, "Brass", "BrassAndMinecarts", {
        "Self-Driving Cart {Create}": ADVANCEMENT
    }, lambda state: canCraftBrass(world, state) and canUseMinecart(world, state))

    # Has Percision Mechanism
    create_region(world, "Brass", "PercisionMechanism", {
        "Complex Curiosities {Create}": ADVANCEMENT,
        "Engineers hate this simple trick! {Create}": ADVANCEMENT,
        "Busy Hands {Create}": ADVANCEMENT,
        "Organize-o-Tron {Create}": ADVANCEMENT,
        "DJ Mechanico {Create}": ADVANCEMENT
    }, lambda state: canCraftPercisionMechanism(world, state))

    # Has Mechanical Crafters
    create_region(world, "Brass", "MechanicalCrafter", {
        "Automated Assembly {Create}": ADVANCEMENT,
        "Crushing It {Create}": ADVANCEMENT,
        "Wheels of Destruction {Create}": ADVANCEMENT
    }, lambda state: hasMechanicalCrafter(world, state))

    # Has Sturdy Sheet
    create_region(world, "Brass", "SturdySheet", {
        "The Sturdiest Rocks {Create}": ADVANCEMENT,
        "The Locomotive Age {Create}": ADVANCEMENT,
        "All Aboard! {Create}": ADVANCEMENT,
        "Choo Choo! {Create}": ADVANCEMENT,
        "Dimensional Commuter {Create}": ADVANCEMENT_HARD,
        "Ambitious Endeavours {Create}": ADVANCEMENT_HARD,
        "Field Trip {Create}": ADVANCEMENT_UNREASONABLE,
        "Conductor Instructor {Create}": ADVANCEMENT,
        "Traffic Control {Create}": ADVANCEMENT,
        "Blind Spot {Create}": ADVANCEMENT_HARD,
        "Road Kill {Create}": ADVANCEMENT,
        "Dynamic Timetables {Create}": ADVANCEMENT,
        "Expert Driver {Create}": ADVANCEMENT,
        "Terrible Service {Create}": ADVANCEMENT_HARD
    }, lambda state: canCraftSturdySheet(world, state))

    # Has Train Tracks
    create_region(world, "AndesiteAlloy", "TrainTracks", {
        "A New Gauge {Create}": ADVANCEMENT,
        "Track Factory {Create}": ADVANCEMENT_UNREASONABLE
    }, lambda state: canCraftTrainTracks(world, state))

    # Has Percision Mechanism And Mechanical Crafter
    create_region(world, "PercisionMechanism", "PercisionMechanismAndMechanicalCrafter", {
        "Fwoomp! {Create}": ADVANCEMENT,
        "Boioioing! {Create}": ADVANCEMENT,
        "Veggie Fireworks {Create}": ADVANCEMENT_HARD,
        "To Full Extent {Create}": ADVANCEMENT_HARD,
        "Desperate Measures {Create}": ADVANCEMENT
    }, lambda state: canCraftPercisionMechanism(world, state) and hasMechanicalCrafter(world, state))

    # Has Percision Mechanism And Blaze Burner
    create_region(world, "PercisionMechanism", "PercisionMechanismAndBlazeBurner", {
        "Combust-o-Tron {Create}": ADVANCEMENT
    }, lambda state: canCraftPercisionMechanism(world, state) and hasBlazeBurner(world, state))

    # Has Cardboard and Smithing
    create_region(world, "Cardboard", "CardboardAndSmithing", {
        "Arts and Crafts {Create}": ADVANCEMENT
    }, lambda state: canCraftCardboard(world, state) and canGetAndUseArmorTrims(world, state))

    # Has Packager and Precision Mechanism
    create_region(world, "Packager", "PackagerAndPrecisionMechanism", {
        "High Logistics {Create}": ADVANCEMENT
    }, lambda state: canUsePackager(world, state) and canCraftPercisionMechanism(world, state))

    # Has Packager and Bucket
    create_region(world, "Packager", "PackagerAndBucket", {
        "Hungry hoppers {Create}": ADVANCEMENT_EXPLORATION
    }, lambda state: canUsePackager(world, state) and canUseBucket(world, state))

    # Has Water Wheel And Bucket
    create_region(world, "WaterWheel", "WaterWheelAndBucket", {
        "Magma Wheel {Create}": ADVANCEMENT
    }, lambda state: hasWaterWheel(world, state) and canUseBucket(world, state))

    # Has Kelp And Press
    create_region(world, "Kelp", "KelpAndPress", {
        "The Parrots and the Flaps {Create}": ADVANCEMENT
    }, lambda state: canCraftAndesiteAlloy(world, state) and canCraftDriedKelp(world, state) and hasPress(world, state))


    # Has Steam Engine And Press
    create_region(world, "Press", "SteamEngineAndPress", {
        "Voice of an Angel {Create}": ADVANCEMENT,
        "The Pipe Organ {Create}": ADVANCEMENT
    }, lambda state: hasSteamEngine(world, state) and hasPress(world, state))

    # Has Press and Nether
    create_region(world, "Press", "PressAndNether", {
        "Sentient Fireplace {Create}": ADVANCEMENT
    }, lambda state: hasPress(world, state) and canAccessNether(world, state))

    # Has Kelp And Chests
    create_region(world, "Kelp", "KelpAndChests", {
        "Airport Aesthetic {Create}": ADVANCEMENT
    }, lambda state: canCraftAndesiteAlloy(world, state) and canCraftDriedKelp(world, state) and canAccessChests(world, state))

    # Has Press and Minecarts
    create_region(world, "Press", "PressAndMinecart", {
        "Strong Arms {Create}": ADVANCEMENT_HARD
    }, lambda state: hasPress(world, state) and canUseMinecart(world, state))

    # Has Press and Cogs
    create_region(world, "Press", "PressAndCogs", {
        "Springboard Champion {Create}": ADVANCEMENT
    }, lambda state: hasPress(world, state) and hasCogs(world, state))

    # Has Press and Cogs and Nether and Buckets
    create_region(world, "PressAndCogs", "PressAndCogsAndNetherAndBuckets", {
        "Tapping the Mantle {Create}": ADVANCEMENT_UNREASONABLE
    }, lambda state: hasPress(world, state) and hasCogs(world, state) and canAccessNether(world, state) and canUseBucket(world, state)
                     and canAccessChests(world, state))

    # Can Max Out Boiler
    create_region(world, "Menu", "CanMaxOutBoiler", {
        "Full Steam {Create}": ADVANCEMENT_UNREASONABLE
    }, lambda state: hasSteamEngine(world, state) and canUseBlazeCake(world, state) and canUseBucket(world, state)
                     and hasCogs(world, state) and canAccessChests(world, state))

    # Can Use Netherite Diving Gear
    create_region(world, "AndesiteAlloy", "NetheriteDivingGear", {
        "Swimming with the Striders {Create}": ADVANCEMENT_HARD
    }, lambda state: canCompactResources(world, state) and canWearNetheriteArmor(world, state) and canGetIron(world, state))

    # Can Make Fluid Foods
    create_region(world, "Menu", "CanMakeFluidFoods", {
        "Balanced Diet {Create}": ADVANCEMENT_UNREASONABLE
    }, lambda state: canUseSpout(world, state) and canUseBottles(world, state) and canUseBucket(world, state) and hasBlazeBurner(world, state))

    # Has Iron Tools
    create_region(world, "AndesiteAlloy", "AlloyAndIronTools", {
        "Is it Time? {Create}": ADVANCEMENT
    }, lambda state: canUseIronTools(world, state))

    # Has Press and Armor
    create_region(world, "Press", "PressAndArmor", {
        "Kitted Out {Create}": ADVANCEMENT,
        "Stress for Nerds {Create}": ADVANCEMENT,
        "Perfectly Stressed {Create}": ADVANCEMENT
    }, lambda state: hasPress(world, state) and canWearLeatherArmor(world, state) and canUseIronTools(world, state))

    # Has Mechanical Press and Enchanting
    create_region(world, "AndesiteAlloy", "MechanicalPressAndEnchant", {
        "Blacksmith Artillery {Create}": ADVANCEMENT
    }, lambda state: canCraftAndesiteAlloyCreate(world, state) and canEnchant(world, state))

    # Can Make Chocolate
    create_region(world, "Mixer", "CanMakeChocolate", {
        "A World of Imagination {Create}": ADVANCEMENT
    }, lambda state: hasMixer(world, state) and hasPump(world, state) and canUseBucket(world, state) and hasBlazeBurner(world, state))


def create_region(world: FabricMinecraftWorld, region_name: str, new_region_name: str, locations: dict[str, int], rule=None):
    create_locations_and_connect(world, region_name + "CreateAdvancements", new_region_name + "CreateAdvancements", locations, rule)