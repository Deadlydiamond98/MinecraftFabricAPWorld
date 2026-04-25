from __future__ import annotations


from worlds.minecraft_fabric.region.regions_helper import create_locations_and_connect
from worlds.minecraft_fabric.logic.create_logic import *


if TYPE_CHECKING:
   from worlds.minecraft_fabric import FabricMinecraftWorld


def create_create_advancement_regions(world: FabricMinecraftWorld):
    create_locations_and_connect(world, "Menu", "MenuCreateAdvancements", {
        "Cuprum Bokum {Create}": 0,
        "The Copper Age {Create}": 0,
        "Tumble Draining {Create}": 0,
        "On a Roll {Create}": 0
    })

    # Has Andesite Alloy
    create_region(world, "Menu", "AndesiteAlloy", {
        "Sturdier Rocks {Create}": 0,
        "The Andesite Age {Create}": 0,
        "Workout Session {Create}": 0
    }, lambda state: canCraftAndesiteAlloyCreate(world, state))

    # REQUIRES ROSE QUARTZ
    create_region(world, "Menu", "RoseQuartz", {
        "Supercharged {Create}": 0
    }, lambda state: canCraftRoseQuartz(world, state))

    # Has Diving Suit
    create_region(world, "AndesiteAlloy", "HasDivingSuit", {
        "Pressure to Go {Create}": 0,
        "Ready for the Depths {Create}": 0
    }, lambda state: canWearGoldArmor(world, state) and canCompactResources(world, state))

    # Has Spout
    create_region(world, "AndesiteAlloy", "HasSpout", {
        "Sploosh {Create}": 0
    }, lambda state: canUseSpout(world, state))

    # Has Steam Engine
    create_region(world, "AndesiteAlloy", "SteamEngine", {
        "The Powerhouse {Create}": 0
    }, lambda state: hasSteamEngine(world, state))

    # Has Cogs
    create_region(world, "AndesiteAlloy", "Cogs", {
        "Shifting Gears {Create}": 0,
        "Embrace the Grind {Create}": 0
    }, lambda state: hasCogs(world, state))

    # Has Water Wheel
    create_region(world, "AndesiteAlloy", "WaterWheel", {
        "Harnessed Hydraulics {Create}": 0
    }, lambda state: hasWaterWheel(world, state))

    # Has Windmill
    create_region(world, "AndesiteAlloy", "Windmill", {
        "A mild Breeze {Create}": 0,
        "A strong Breeze {Create}": 0
    }, lambda state: hasWindmill(world, state))

    # Has Press
    create_region(world, "AndesiteAlloy", "Press", {
        "Area of Connect {Create}": 0,
        "Moving with Purpose {Create}": 0,
        "Drive-by Exchange {Create}": 0,
        "Rope to Nowhere {Create}": 0,
        "Bonk! {Create}": 0,
        "Wind Maker {Create}": 0,
        "Processing by Particle {Create}": 0,
        "Workshop's Most Feared {Create}": 0,
        "Compactification {Create}": 0,
        "Vertical Logistics {Create}": 0,
        "Remote Activation {Create}": 0
    }, lambda state: hasPress(world, state))

    # Has Pump
    create_region(world, "Press", "HasPump", {
        "Under Pressure {Create}": 0,
        "Don't Cross the Streams! {Create}": 0,
        "Flow Discovery {Create}": 0,
        "Puddle Collector {Create}": 0,
        "Industrial Spillage {Create}": 0,
        "Autonomous Bee-Keeping {Create}": 0
    }, lambda state: hasPump(world, state))

    # Has Mixer
    create_region(world, "AndesiteAlloy", "Mixer", {
        "Mixing It Up {Create}": 0
    }, lambda state: hasMixer(world, state))

    # Has Kelp
    create_region(world, "AndesiteAlloy", "Kelp", {
        "Kelp Drive {Create}": 0
    }, lambda state: canCraftAndesiteAlloy(world, state) and canCraftDriedKelp(world, state))

    # Has Cardboard
    create_region(world, "AndesiteAlloy", "Cardboard", {
        "Part and Parcel {Create}": 0,
        "Full Stealth {Create}": 0
    }, lambda state: canCraftCardboard(world, state))

    # Has Packager
    create_region(world, "Cardboard", "Packager", {
        "Post Production {Create}": 0,
        "Order Up! {Create}": 0,
        "Open for business {Create}": 0,
        "Nothing but net {Create}": 0
    }, lambda state: canUsePackager(world, state))

    # Has Brass
    create_region(world, "AndesiteAlloy", "Brass", {
        "Real Alloys {Create}": 0,
        "The Brass Age {Create}": 0,
        "Shadow Sense {Create}": 0,
        "Contraption o'Clock {Create}": 0,
        "Big Data {Create}": 0,
        "Artificial Intelligence {Create}": 0
    }, lambda state: canCraftBrass(world, state))

    # Has Brass And Minecarts
    create_region(world, "Brass", "BrassAndMinecarts", {
        "Self-Driving Cart {Create}": 0
    }, lambda state: canCraftBrass(world, state) and canUseMinecart(world, state))

    # Has Percision Mechanism
    create_region(world, "Brass", "PercisionMechanism", {
        "Complex Curiosities {Create}": 0,
        "Engineers hate this simple trick! {Create}": 0,
        "Busy Hands {Create}": 0,
        "Organize-o-Tron {Create}": 0,
        "DJ Mechanico {Create}": 0,
        "Pound It, Bro! {Create}": 0
    }, lambda state: canCraftPercisionMechanism(world, state))

    # Has Mechanical Crafters
    create_region(world, "Brass", "MechanicalCrafter", {
        "Automated Assembly {Create}": 0,
        "Crushing It {Create}": 0,
        "Wheels of Destruction {Create}": 0
    }, lambda state: hasMechanicalCrafter(world, state))

    # Has Sturdy Sheet
    create_region(world, "Brass", "SturdySheet", {
        "The Sturdiest Rocks {Create}": 0,
        "The Locomotive Age {Create}": 0,
        "All Aboard! {Create}": 0,
        "Choo Choo! {Create}": 0,
        "Dimensional Commuter {Create}": 1,
        "Ambitious Endeavours {Create}": 1,
        "Field Trip {Create}": 3,
        "Conductor Instructor {Create}": 0,
        "Traffic Control {Create}": 0,
        "Blind Spot {Create}": 1,
        "Road Kill {Create}": 0,
        "Dynamic Timetables {Create}": 0,
        "Expert Driver {Create}": 0,
        "Terrible Service {Create}": 1
    }, lambda state: canCraftSturdySheet(world, state))

    # Has Train Tracks
    create_region(world, "AndesiteAlloy", "TrainTracks", {
        "A New Gauge {Create}": 0,
        "Track Factory {Create}": 3
    }, lambda state: canCraftTrainTracks(world, state))

    # Has Percision Mechanism And Mechanical Crafter
    create_region(world, "PercisionMechanism", "PercisionMechanismAndMechanicalCrafter", {
        "Fwoomp! {Create}": 0,
        "Boioioing! {Create}": 0,
        "Veggie Fireworks {Create}": 1,
        "To Full Extent {Create}": 1,
        "Desperate Measures {Create}": 0
    }, lambda state: canCraftPercisionMechanism(world, state) and hasMechanicalCrafter(world, state))

    # Has Percision Mechanism And Blaze Burner
    create_region(world, "PercisionMechanism", "PercisionMechanismAndBlazeBurner", {
        "Combust-o-Tron {Create}": 0
    }, lambda state: canCraftPercisionMechanism(world, state) and hasBlazeBurner(world, state))

    # Has Cardboard and Smithing
    create_region(world, "Cardboard", "CardboardAndSmithing", {
        "Arts and Crafts {Create}": 0
    }, lambda state: canCraftCardboard(world, state) and canGetAndUseArmorTrims(world, state))

    # Has Packager and Precision Mechanism
    create_region(world, "Packager", "PackagerAndPrecisionMechanism", {
        "High Logistics {Create}": 0
    }, lambda state: canUsePackager(world, state) and canCraftPercisionMechanism(world, state))

    # Has Packager and Bucket
    create_region(world, "Packager", "PackagerAndBucket", {
        "Hungry hoppers {Create}": 2
    }, lambda state: canUsePackager(world, state) and canUseBucket(world, state))

    # Has Water Wheel And Bucket
    create_region(world, "WaterWheel", "WaterWheelAndBucket", {
        "Magma Wheel {Create}": 0
    }, lambda state: hasWaterWheel(world, state) and canUseBucket(world, state))

    # Has Kelp And Press
    create_region(world, "Kelp", "KelpAndPress", {
        "The Parrots and the Flaps {Create}": 0
    }, lambda state: canCraftAndesiteAlloy(world, state) and canCraftDriedKelp(world, state) and hasPress(world, state))


    # Has Steam Engine And Press
    create_region(world, "Press", "SteamEngineAndPress", {
        "Voice of an Angel {Create}": 0,
        "The Pipe Organ {Create}": 0
    }, lambda state: hasSteamEngine(world, state) and hasPress(world, state))

    # Has Press and Nether
    create_region(world, "Press", "PressAndNether", {
        "Sentient Fireplace {Create}": 0
    }, lambda state: hasPress(world, state) and canAccessNether(world, state))

    # Has Kelp And Chests
    create_region(world, "Kelp", "KelpAndChests", {
        "Airport Aesthetic {Create}": 0
    }, lambda state: canCraftAndesiteAlloy(world, state) and canCraftDriedKelp(world, state) and canAccessChests(world, state))

    # Has Press and Minecarts
    create_region(world, "Press", "PressAndMinecart", {
        "Strong Arms {Create}": 1
    }, lambda state: hasPress(world, state) and canUseMinecart(world, state))

    # Has Press and Cogs
    create_region(world, "Press", "PressAndCogs", {
        "Springboard Champion {Create}": 0
    }, lambda state: hasPress(world, state) and hasCogs(world, state))

    # Has Press and Cogs and Nether and Buckets
    create_region(world, "PressAndCogs", "PressAndCogsAndNetherAndBuckets", {
        "Tapping the Mantle {Create}": 3
    }, lambda state: hasPress(world, state) and hasCogs(world, state) and canAccessNether(world, state) and canUseBucket(world, state)
                     and canAccessChests(world, state))

    # Can Max Out Boiler
    create_region(world, "Menu", "CanMaxOutBoiler", {
        "Full Steam {Create}": 3
    }, lambda state: hasSteamEngine(world, state) and canUseBlazeCake(world, state) and canUseBucket(world, state)
                     and hasCogs(world, state) and canAccessChests(world, state))

    # Can Use Netherite Diving Gear
    create_region(world, "AndesiteAlloy", "NetheriteDivingGear", {
        "Swimming with the Striders {Create}": 1
    }, lambda state: canCompactResources(world, state) and canWearNetheriteArmor(world, state) and canSmelt(world, state))

    # Can Make Fluid Foods
    create_region(world, "Menu", "CanMakeFluidFoods", {
        "Balanced Diet {Create}": 3
    }, lambda state: canUseSpout(world, state) and canUseBottles(world, state) and canUseBucket(world, state) and hasBlazeBurner(world, state))

    # Has Iron Tools
    create_region(world, "AndesiteAlloy", "AlloyAndIronTools", {
        "Is it Time? {Create}": 0
    }, lambda state: canUseIronTools(world, state))

    # Has Press and Armor
    create_region(world, "Press", "PressAndArmor", {
        "Kitted Out {Create}": 0,
        "Stress for Nerds {Create}": 0,
        "Perfectly Stressed {Create}": 0
    }, lambda state: hasPress(world, state) and canWearLeatherArmor(world, state) and canUseIronTools(world, state))

    # Has Mechanical Press and Enchanting
    create_region(world, "AndesiteAlloy", "MechanicalPressAndEnchant", {
        "Blacksmith Artillery {Create}": 0
    }, lambda state: canCraftAndesiteAlloyCreate(world, state) and canEnchant(world, state))

    # Can Make Chocolate
    create_region(world, "Mixer", "CanMakeChocolate", {
        "A World of Imagination {Create}": 0
    }, lambda state: hasMixer(world, state) and hasPump(world, state) and canUseBucket(world, state) and hasBlazeBurner(world, state))


def create_region(world: FabricMinecraftWorld, region_name: str, new_region_name: str, locations: dict[str, int], rule=None):
    create_locations_and_connect(world, region_name + "CreateAdvancements", new_region_name + "CreateAdvancements", locations, rule)