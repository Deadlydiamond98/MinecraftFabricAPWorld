from __future__ import annotations


from worlds.minecraft_fabric.region.regions_helper import create_locations_and_connect
from worlds.minecraft_fabric.logic.create_logic import *


if TYPE_CHECKING:
   from worlds.minecraft_fabric import FabricMinecraftWorld


def create_create_itemsanity_regions(world: FabricMinecraftWorld):
    create_locations_and_connect(world, "Menu", "MenuCreateItemsanity", {
        "Crafting Blueprint (Itemsanity) {Create}": 5,
        "Sand Paper (Itemsanity) {Create}": 5,
        "Red Sand Paper (Itemsanity) {Create}": 7,
        "Asurine (Itemsanity) {Create}": 5,
        "Crimsite (Itemsanity) {Create}": 5,
        "Limestone (Itemsanity) {Create}": 5,
        "Ochrum (Itemsanity) {Create}": 5,
        "Veridium (Itemsanity) {Create}": 5,
    })

    # Nether Access
    create_region(world, "Menu", "NetherAccess", {
        "Scoria (Itemsanity) {Create}": 5,
        "Scorchia (Itemsanity) {Create}": 5,
    }, lambda state: canAccessNether(world, state))

    # Can Smelt
    create_region(world, "Menu", "CanSmelt", {
        "Schematic Table (Itemsanity) {Create}": 5,
        "Item Drain (Itemsanity) {Create}": 5,
        "Copper Casing (Itemsanity) {Create}": 5,
        "Copper Diving Helmet (Itemsanity) {Create}": 5,
        "Copper Door (Itemsanity) {Create}": 5,
        "Oak Window (Itemsanity) {Create}": 5,
        "Spruce Window (Itemsanity) {Create}": 5,
        "Birch Window (Itemsanity) {Create}": 5,
        "Jungle Window (Itemsanity) {Create}": 7,
        "Acacia Window (Itemsanity) {Create}": 5,
        "Dark Oak Window (Itemsanity) {Create}": 7,
        "Mangrove Window (Itemsanity) {Create}": 7,
        "Cherry Window (Itemsanity) {Create}": 7,
        "Bamboo Window (Itemsanity) {Create}": 7,
        "Oak Window Pane (Itemsanity) {Create}": 5,
        "Spruce Window Pane (Itemsanity) {Create}": 5,
        "Birch Window Pane (Itemsanity) {Create}": 5,
        "Jungle Window Pane (Itemsanity) {Create}": 7,
        "Acacia Window Pane (Itemsanity) {Create}": 5,
        "Dark Oak Window Pane (Itemsanity) {Create}": 7,
        "Mangrove Window Pane (Itemsanity) {Create}": 7,
        "Cherry Window Pane (Itemsanity) {Create}": 7,
        "Bamboo Window Pane (Itemsanity) {Create}": 7,
    }, lambda state: canSmelt(world, state))

    # Can Smelt And Nether Access
    create_region(world, "CanSmelt", "CanSmeltAndNether", {
        "Crimson Window (Itemsanity) {Create}": 5,
        "Warped Window (Itemsanity) {Create}": 5,
        "Crimson Window Pane (Itemsanity) {Create}": 5,
        "Warped Window Pane (Itemsanity) {Create}": 5
    }, lambda state: canSmelt(world, state) and canAccessNether(world, state))

    # Can Smelt And Compact
    create_region(world, "CanSmelt", "CanSmeltAndCompact", {
        "Copper Nugget (Itemsanity) {Create}": 5,
        "List Filter (Itemsanity) {Create}": 5,
        "Ornate Iron Window (Itemsanity) {Create}": 5,
        "Ornate Iron Window Pane (Itemsanity) {Create}": 5,
    }, lambda state: canSmelt(world, state) and canCompactResources(world, state))

    # Has Iron Tools
    create_region(world, "Menu", "IronTools", {
        "Powered Latch (Itemsanity) {Create}": 5,
        "Powered Toggle Latch (Itemsanity) {Create}": 5,
        "Raw Zinc (Itemsanity) {Create}": 5
    }, lambda state: canUseIronTools(world, state))

    # Has Iron Tools And Compact
    create_region(world, "IronTools", "IronToolsAndCompact", {
        "Block of Raw Zinc (Itemsanity) {Create}": 5
    }, lambda state: canUseIronTools(world, state) and canCompactResources(world, state))

    # Has Zinc
    create_region(world, "Menu", "Zinc", {
        "Zinc Ingot (Itemsanity) {Create}": 5
    }, lambda state: canGetZinc(world, state))

    # Has Zinc And Compact
    create_region(world, "Menu", "ZincAndCompact", {
        "Zinc Nugget (Itemsanity) {Create}": 5,
        "Package Filter (Itemsanity) {Create}": 5,
        "Block of Zinc (Itemsanity) {Create}": 5
    }, lambda state: canGetZinc(world, state) and canCompactResources(world, state))

    # Has Rose Quartz
    create_region(world, "Menu", "RoseQuartz", {
        "Rose Quartz (Itemsanity) {Create}": 5,
        "Polished Rose Quartz (Itemsanity) {Create}": 5
    }, lambda state: canCraftRoseQuartz(world, state))

    # Has Kelp
    create_region(world, "Menu", "Kelp", {
        "Mechanical Belt (Itemsanity) {Create}": 5
    }, lambda state: canCraftDriedKelp(world, state))

    # Has Andesite Alloy
    create_region(world, "Menu", "AndesiteAlloy", {
        "Shaft (Itemsanity) {Create}": 5,
        "Clutch (Itemsanity) {Create}": 5,
        "Encased Chain Drive (Itemsanity) {Create}": 5,
        "Nozzle (Itemsanity) {Create}": 5,
        "Turntable (Itemsanity) {Create}": 5,
        "Hand Crank (Itemsanity) {Create}": 5,
        "Basin (Itemsanity) {Create}": 5,
        "Depot (Itemsanity) {Create}": 5,
        "Wooden Bracket (Itemsanity) {Create}": 5,
        "Metal Bracket (Itemsanity) {Create}": 5,
        "Mechanical Piston (Itemsanity) {Create}": 5,
        "Piston Extension Pole (Itemsanity) {Create}": 5,
        "Mechanical Bearing (Itemsanity) {Create}": 5,
        "Linear Chassis (Itemsanity) {Create}": 5,
        "Secondary Linear Chassis (Itemsanity) {Create}": 5,
        "Radial Chassis (Itemsanity) {Create}": 5,
        "Mechanical Drill (Itemsanity) {Create}": 5,
        "Andesite Casing (Itemsanity) {Create}": 5,
        "Item Hatch (Itemsanity) {Create}": 5,
        "Analog Lever (Itemsanity) {Create}": 5,
        "Andesite Alloy (Itemsanity) {Create}": 5,
        "Clipboard (Itemsanity) {Create}": 5,
        "Andesite Door (Itemsanity) {Create}": 5
    }, lambda state: canCraftAndesiteAlloy(world, state))

    # Has Andesite Alloy And Compact
    create_region(world, "AndesiteAlloy", "AndesiteAlloyAndCompact", {
        "Block of Andesite Alloy (Itemsanity) {Create}": 5
    }, lambda state: canCraftAndesiteAlloy(world, state) and canCompactResources(world, state))

    # Has Andesite Alloy And Iron Tools
    create_region(world, "AndesiteAlloy", "AndesiteAlloyAndIronTools", {
        "Cuckoo Clock (Itemsanity) {Create}": 5,
        "Speedometer (Itemsanity) {Create}": 5,
        "Stressometer (Itemsanity) {Create}": 5,
        "Gantry Shaft (Itemsanity) {Create}": 5,
        "Sticky Mechanical Piston (Itemsanity) {Create}": 7,
        "Sticker (Itemsanity) {Create}": 7
    }, lambda state: canCraftAndesiteAlloy(world, state) and canUseIronTools(world, state))

    # Has Cogs
    create_region(world, "AndesiteAlloy", "Cogs", {
        "Cogwheel (Itemsanity) {Create}": 5,
        "Large Cogwheel (Itemsanity) {Create}": 5,
        "Gearbox (Itemsanity) {Create}": 5,
        "Vertical Gearbox (Itemsanity) {Create}": 5,
        "Gearshift (Itemsanity) {Create}": 5,
        "Chain Conveyor (Itemsanity) {Create}": 5,
        "Millstone (Itemsanity) {Create}": 5,
        "Gantry Carriage (Itemsanity) {Create}": 5,
        "Wheat Flour (Itemsanity) {Create}": 5
    }, lambda state: hasCogs(world, state))

    # Has Waterwheel
    create_region(world, "AndesiteAlloy", "Waterwheel", {
        "Water Wheel (Itemsanity) {Create}": 5,
        "Large Water Wheel (Itemsanity) {Create}": 5
    }, lambda state: hasWaterWheel(world, state))

    # Has Windmill
    create_region(world, "AndesiteAlloy", "Windmill", {
        "Windmill Bearing (Itemsanity) {Create}": 5,
        "Windmill Sail Frame (Itemsanity) {Create}": 5,
        "Windmill Sail (Itemsanity) {Create}": 5
    }, lambda state: hasWindmill(world, state))

    # Has Press
    create_region(world, "AndesiteAlloy", "Press", {
        "Encased Fan (Itemsanity) {Create}": 5,
        "Mechanical Press (Itemsanity) {Create}": 5,
        "Chute (Itemsanity) {Create}": 5,
        "Fluid Pipe (Itemsanity) {Create}": 5,
        "Fluid Valve (Itemsanity) {Create}": 5,
        "Copper Valve Handle (Itemsanity) {Create}": 5,
        "Hose Pulley (Itemsanity) {Create}": 5,
        "Portable Fluid Interface (Itemsanity) {Create}": 5,
        "Rope Pulley (Itemsanity) {Create}": 5,
        "Mechanical Saw (Itemsanity) {Create}": 5,
        "Portable Storage Interface (Itemsanity) {Create}": 5,
        "Redstone Contact (Itemsanity) {Create}": 5,
        "Mechanical Harvester (Itemsanity) {Create}": 5,
        "Mechanical Plough (Itemsanity) {Create}": 5,
        "Propeller (Itemsanity) {Create}": 5,
        "Whisk (Itemsanity) {Create}": 5,
        "Copper Sheet (Itemsanity) {Create}": 5,
        "Iron Sheet (Itemsanity) {Create}": 5,
        "Super Glue (Itemsanity) {Create}": 7,
        "Metal Girder (Itemsanity) {Create}": 5
    }, lambda state: hasPress(world, state))

    # Has Press And Iron Tools
    create_region(world, "Press", "PressAndIronTools", {
        "Redstone Link (Itemsanity) {Create}": 5,
        "Transmitter (Itemsanity) {Create}": 5,
        "Linked Controller (Itemsanity) {Create}": 5
    }, lambda state: hasPress(world, state) and canUseIronTools(world, state))

    # Has Steam Engine
    create_region(world, "Press", "SteamEngine", {
        "Steam Engine (Itemsanity) {Create}": 5
    }, lambda state: hasSteamEngine(world, state))

    # Has Mixer
    create_region(world, "Press", "Mixer", {
        "Mechanical Mixer (Itemsanity) {Create}": 5
    }, lambda state: hasMixer(world, state))

    # Has Mixer And Fluid
    create_region(world, "Mixer", "MixerAndFluid", {
        "Sweet Roll (Itemsanity) {Create}": 5
    }, lambda state: hasMixer(world, state) and canUseBucket(world, state))

    # Has Chocolate
    create_region(world, "MixerAndFluid", "Chocolate", {
        "Bar of Chocolate (Itemsanity) {Create}": 5,
        "Chocolate Glazed Berries (Itemsanity) {Create}": 5,
        "Chocolate Bucket (Itemsanity) {Create}": 5
    }, lambda state: hasBlazeBurner(world, state) and hasMixer(world, state) and canUseBucket(world, state))

    # Has Blaze Burner
    create_region(world, "Press", "BlazeBurner", {
        "Blaze Burner (Itemsanity) {Create}": 5,
        "Empty Blaze Burner (Itemsanity) {Create}": 5
    }, lambda state: hasBlazeBurner(world, state))

    # Has Electron Tube
    create_region(world, "AndesiteAlloy", "ElectronTube", {
        "Adjustable Chain Gearshift (Itemsanity) {Create}": 5,
        "Contraption Controls (Itemsanity) {Create}": 5,
        "Display Board (Itemsanity) {Create}": 5,
        "Nixie Tube (Itemsanity) {Create}": 5,
        "Electron Tube (Itemsanity) {Create}": 5
    }, lambda state: canCraftElectronTube(world, state))

    # Has Crushing Wheel
    create_region(world, "AndesiteAlloy", "CrushingWheel", {
        "Crushing Wheel (Itemsanity) {Create}": 5,
        "Cinder Flour (Itemsanity) {Create}": 5,
        "Blaze Cake Base (Itemsanity) {Create}": 5,
        "Blaze Cake (Itemsanity) {Create}": 5,
        "Nugget of Experience (Itemsanity) {Create}": 5,
        "Crushed Raw Iron (Itemsanity) {Create}": 5,
        "Crushed Raw Gold (Itemsanity) {Create}": 5,
        "Crushed Raw Copper (Itemsanity) {Create}": 5,
        "Crushed Raw Zinc (Itemsanity) {Create}": 5,
        "Block of Experience (Itemsanity) {Create}": 5,
    }, lambda state: hasCrusher(world, state))

    # Has Fluid Tank
    create_region(world, "AndesiteAlloy", "FluidTank", {
        "Fluid Tank (Itemsanity) {Create}": 5
    }, lambda state: hasFluidTank(world, state))

    # Has Spout
    create_region(world, "AndesiteAlloy", "Spout", {
        "Spout (Itemsanity) {Create}": 5
    }, lambda state: canUseSpout(world, state))

    # Has Cardboard
    create_region(world, "AndesiteAlloy", "Cardboard", {
        "Packager (Itemsanity) {Create}": 5,
        "Re-Packager (Itemsanity) {Create}": 5,
        "Pulp (Itemsanity) {Create}": 5,
        "Cardboard (Itemsanity) {Create}": 5,
        "Cardboard Sword (Itemsanity) {Create}": 5,
        "Cardboard Helmet (Itemsanity) {Create}": 5,
        "Cardboard Chestplate (Itemsanity) {Create}": 5,
        "Cardboard Leggings (Itemsanity) {Create}": 5,
        "Cardboard Boots (Itemsanity) {Create}": 5,
        "Block of Cardboard (Itemsanity) {Create}": 5,
        "Bound Block of Cardboard (Itemsanity) {Create}": 5,
    }, lambda state: canCraftCardboard(world, state))

    # Has Brass
    create_region(world, "AndesiteAlloy", "Brass", {
        "Elevator Pulley (Itemsanity) {Create}": 5,
        "Brass Casing (Itemsanity) {Create}": 5,
        "Flywheel (Itemsanity) {Create}": 5,
        "Smart Chute (Itemsanity) {Create}": 5,
        "Smart Fluid Pipe (Itemsanity) {Create}": 5,
        "Clockwork Bearing (Itemsanity) {Create}": 5,
        "Deployer (Itemsanity) {Create}": 5,
        "Sequenced Gearshift (Itemsanity) {Create}": 5,
        "Smart Observer (Itemsanity) {Create}": 5,
        "Threshold Switch (Itemsanity) {Create}": 5,
        "Display Link (Itemsanity) {Create}": 5,
        "Placard (Itemsanity) {Create}": 5,
        "Pulse Repeater (Itemsanity) {Create}": 5,
        "Pulse Extender (Itemsanity) {Create}": 5,
        "Pulse Timer (Itemsanity) {Create}": 5,
        "Brass Hand (Itemsanity) {Create}": 5,
        "Crafter Slot Cover (Itemsanity) {Create}": 5,
        "Brass Ingot (Itemsanity) {Create}": 5,
        "Brass Nugget (Itemsanity) {Create}": 5,
        "Brass Sheet (Itemsanity) {Create}": 5,
        "Attribute Filter (Itemsanity) {Create}": 5,
        "Peculiar Bell (Itemsanity) {Create}": 5,
        "Haunted Bell (Itemsanity) {Create}": 5,
        "Brass Door (Itemsanity) {Create}": 5,
        "Block of Brass (Itemsanity) {Create}": 5,
    }, lambda state: canCraftBrass(world, state))

    # Has Mechanical Crafter
    create_region(world, "Brass", "MechanicalCrafter", {
        "Mechanical Crafter (Itemsanity) {Create}": 5
    }, lambda state: hasMechanicalCrafter(world, state))

    # Has Percision Mechanism
    create_region(world, "Brass", "PercisionMechanism", {
        "Rotation Speed Controller (Itemsanity) {Create}": 5,
        "Mechanical Arm (Itemsanity) {Create}": 5,
        "Incomplete Precision Mechanism (Itemsanity) {Create}": 5,
        "Precision Mechanism (Itemsanity) {Create}": 5
    }, lambda state: canCraftPercisionMechanism(world, state))

    # Has Train Tracks
    create_region(world, "Brass", "TrainTracks", {
        "Train Track (Itemsanity) {Create}": 5,
        "Incomplete Track (Itemsanity) {Create}": 5
    }, lambda state: canCraftTrainTracks(world, state))

    # Has Sturdy Sheet
    create_region(world, "Brass", "SturdySheet", {
        "Train Casing (Itemsanity) {Create}": 5,
        "Train Station (Itemsanity) {Create}": 5,
        "Train Signal (Itemsanity) {Create}": 5,
        "Train Observer (Itemsanity) {Create}": 5,
        "Sturdy Sheet (Itemsanity) {Create}": 5,
        "Unprocessed Obsidian Sheet (Itemsanity) {Create}": 5,
        "Train Schedule (Itemsanity) {Create}": 5,
        "Train Door (Itemsanity) {Create}": 5,
        "Train Trapdoor (Itemsanity) {Create}": 5,
    }, lambda state: canCraftSturdySheet(world, state))

    # Has Sturdy Sheet And Percision Mechanism
    create_region(world, "SturdySheet", "SturdySheetAndPercisionMechanism", {
        "Train Controls (Itemsanity) {Create}": 5
    }, lambda state: canCraftSturdySheet(world, state) and canCraftPercisionMechanism(world, state))

    # Has Mechanical Crafter And Percision Mechanism
    create_region(world, "Brass", "MechanicalCrafterAndPercisionMechanism", {
        "Potato Cannon (Itemsanity) {Create}": 5,
        "Extendo Grip (Itemsanity) {Create}": 5,
    }, lambda state: hasMechanicalCrafter(world, state) and canCraftPercisionMechanism(world, state))

    # Has Mechanical Crafter And Percision Mechanism
    create_region(world, "MechanicalCrafterAndPercisionMechanism", "MechanicalCrafterAndPercisionMechanismAndObsidian", {
        "Wand Of Symmetry (Itemsanity) {Create}": 5
    }, lambda state: hasMechanicalCrafter(world, state) and canCraftPercisionMechanism(world, state) and canGetObsidian(world, state))

    # Has Andesite and Kelp
    create_region(world, "AndesiteAlloy", "AndesiteAlloyAndKelp", {
        "Andesite Funnel (Itemsanity) {Create}": 5,
        "Andesite Tunnel (Itemsanity) {Create}": 5
    }, lambda state: canCraftAndesiteAlloy(world, state) and canCraftDriedKelp(world, state))

    # Has Brass and Kelp
    create_region(world, "Brass", "BrassAndKelp", {
        "Brass Funnel (Itemsanity) {Create}": 5,
        "Brass Tunnel (Itemsanity) {Create}": 5
    }, lambda state: canCraftBrass(world, state) and canCraftDriedKelp(world, state))

    # Has Press And Cogs
    create_region(world, "Press", "PressAndCogs", {
        "Weighted Ejector (Itemsanity) {Create}": 5,
        "Mechanical Pump (Itemsanity) {Create}": 5
    }, lambda state: hasPress(world, state) and hasCogs(world, state))

    # Has Press And Storage
    create_region(world, "Press", "PressAndStorage", {
        "Item Vault (Itemsanity) {Create}": 5,
        "Package Frogport (Itemsanity) {Create}": 7,
        "Stock Link (Itemsanity) {Create}": 7
    }, lambda state: hasPress(world, state) and canAccessChests(world, state))

    # Has Percision Mechanism And Storage
    create_region(world, "Brass", "PercisionMechanismAndStorage", {
        "Factory Gauge (Itemsanity) {Create}": 5
    }, lambda state: canCraftPercisionMechanism(world, state) and canAccessChests(world, state))

    # Has Press And Storage And Iron Tools
    create_region(world, "PressAndStorage", "PressAndStorageAndIronTools", {
        "Stock Ticker (Itemsanity) {Create}": 5,
        "Redstone Requester (Itemsanity) {Create}": 5
    }, lambda state: hasPress(world, state) and canAccessChests(world, state) and canUseIronTools(world, state))

    # Has Press And Gold
    create_region(world, "Press", "PressAndGold", {
        "Steam Whistle (Itemsanity) {Create}": 5,
        "Golden Sheet (Itemsanity) {Create}": 5,
        "Desk Bell (Itemsanity) {Create}": 5
    }, lambda state: hasPress(world, state) and canGetGold(world, state))

    # Has Press And Gold And Armor
    create_region(world, "PressAndGold", "PressAndGoldAndArmor", {
        "Engineer's Goggles (Itemsanity) {Create}": 5
    }, lambda state: hasPress(world, state) and canGetGold(world, state) and canWearLeatherArmor(world, state))

    # Has Press And Gold And Cogs
    create_region(world, "PressAndGold", "PressAndGoldAndCogs", {
        "Wrench (Itemsanity) {Create}": 5
    }, lambda state: hasPress(world, state) and canGetGold(world, state) and hasCogs(world, state))

    # Has Crushing Wheel And Electron Tube
    create_region(world, "CrushingWheel", "CrushingWheelAndElectronTube", {
        "Mechanical Roller (Itemsanity) {Create}": 5
    }, lambda state: hasCrusher(world, state) and canCraftElectronTube(world, state))

    # Has Crushing Wheel and Obsidian
    create_region(world, "CrushingWheel", "CrushingWheelAndObsidian", {
        "Powdered Obsidian (Itemsanity) {Create}": 5
    }, lambda state: hasCrusher(world, state) and canGetObsidian(world, state))

    # Has Press and Minecarts
    create_region(world, "Press", "PressAndMinecarts", {
        "Minecart Coupling (Itemsanity) {Create}": 5
    }, lambda state: hasPress(world, state) and canUseMinecart(world, state))

    # Can Smelt and Can Compact and Has Archery
    create_region(world, "CanSmelt", "CanSmeltAndCompactAndArchery", {
        "Schematicannon (Itemsanity) {Create}": 5
    }, lambda state: canSmelt(world, state) and canCompactResources(world, state) and canUseBow(world, state))

    # Has Gold and Electron Tubes and Minecarts
    create_region(world, "AndesiteAlloy", "GoldAndElectronTubesAndMinecarts", {
        "Controller Rail (Itemsanity) {Create}": 5
    }, lambda state: canGetGold(world, state) and canCraftElectronTube(world, state) and canUseMinecart(world, state))

    # Has Zinc and Rose Quartz
    create_region(world, "Menu", "ZincAndRoseQuartz", {
        "Rose Quartz Lamp (Itemsanity) {Create}": 5
    }, lambda state: canGetZinc(world, state) and canCraftRoseQuartz(world, state))

    # Dough
    create_region(world, "AndesiteAlloy", "Dough", {
        "Dough (Itemsanity) {Create}": 5
    }, lambda state: hasCogs(world, state) and (canUseBucket(world, state) or hasPress(world, state)))

    # Has Mixer And Bottles
    create_region(world, "Mixer", "MixerAndBottles", {
        "Honeyed Apple (Itemsanity) {Create}": 5
    }, lambda state: hasMixer(world, state) and canUseBottles(world, state))

    # Has Mixer And Bottles And Bucket
    create_region(world, "MixerAndBottles", "MixerAndBottlesAndBucket", {
        "Honey Bucket (Itemsanity) {Create}": 5
    }, lambda state: hasMixer(world, state) and canUseBottles(world, state) and canUseBucket(world, state))

    # Builders Tea
    create_region(world, "MixerAndBottles", "BuildersTea", {
        "Builder's Tea (Itemsanity) {Create}": 5
    }, lambda state: hasMixer(world, state) and canUseBottles(world, state) and canUseBucket(world, state) and hasBlazeBurner(world, state) and (
        canUseShears(world, state) or canEnchant(world, state)
    ))

    # Copper Diving Gear
    create_region(world, "AndesiteAlloy", "CopperDivingGear", {
        "Copper Backtank (Itemsanity) {Create}": 5,
        "Copper Diving Boots (Itemsanity) {Create}": 5
    }, lambda state: canCraftAndesiteAlloy(world, state) and canWearGoldArmor(world, state))

    # Netherite Diving Gear
    create_region(world, "CopperDivingGear", "NetheriteDivingGear", {
        "Netherite Backtank (Itemsanity) {Create}": 5,
        "Netherite Diving Boots (Itemsanity) {Create}": 5
    }, lambda state: canCraftAndesiteAlloy(world, state) and canWearNetheriteArmor(world, state))

    # Netherite Diving Gear
    create_region(world, "CanSmelt", "NetheriteDivingHelmet", {
        "Netherite Diving Helmet (Itemsanity) {Create}": 5
    }, lambda state: canSmelt(world, state) and canWearNetheriteArmor(world, state))

    # Has Enchanting
    create_region(world, "Menu", "HasEnchanting", {
        "Zinc Ore (Itemsanity) {Create}": 5,
        "Deepslate Zinc Ore (Itemsanity) {Create}": 5
    }, lambda state: canEnchant(world, state))

    # Has Swimming and Enchanting
    create_region(world, "HasEnchanting", "HasSwimAndEnchanting", {
        "Tree Fertilizer (Itemsanity) {Create}": 5
    }, lambda state: canSwim(world, state) and canEnchant(world, state))

    # Schematic
    create_region(world, "Menu", "Schematic", {
        "Empty Schematic (Itemsanity) {Create}": 5,
        "Schematic And Quill (Itemsanity) {Create}": 5
    }, lambda state: canDyeFull(world, state))

    ####################################################################################################################
    # STONE CUTTING AND SAW EXCLUSIVES #################################################################################
    ####################################################################################################################


    create_region(world, "Menu", "Cutting", {
        "Cut Granite (Itemsanity) {Create}": 5,
        "Cut Granite Stairs (Itemsanity) {Create}": 5,
        "Cut Granite Slab (Itemsanity) {Create}": 5,
        "Cut Granite Wall (Itemsanity) {Create}": 5,
        "Polished Cut Granite (Itemsanity) {Create}": 5,
        "Polished Cut Granite Stairs (Itemsanity) {Create}": 5,
        "Polished Cut Granite Slab (Itemsanity) {Create}": 5,
        "Polished Cut Granite Wall (Itemsanity) {Create}": 5,
        "Cut Granite Bricks (Itemsanity) {Create}": 5,
        "Cut Granite Brick Stairs (Itemsanity) {Create}": 5,
        "Cut Granite Brick Slab (Itemsanity) {Create}": 5,
        "Cut Granite Brick Wall (Itemsanity) {Create}": 5,
        "Small Granite Bricks (Itemsanity) {Create}": 5,
        "Small Granite Brick Stairs (Itemsanity) {Create}": 5,
        "Small Granite Brick Slab (Itemsanity) {Create}": 5,
        "Small Granite Brick Wall (Itemsanity) {Create}": 5,
        "Layered Granite (Itemsanity) {Create}": 5,
        "Granite Pillar (Itemsanity) {Create}": 5,
        "Cut Diorite (Itemsanity) {Create}": 5,
        "Cut Diorite Stairs (Itemsanity) {Create}": 5,
        "Cut Diorite Slab (Itemsanity) {Create}": 5,
        "Cut Diorite Wall (Itemsanity) {Create}": 5,
        "Polished Cut Diorite (Itemsanity) {Create}": 5,
        "Polished Cut Diorite Stairs (Itemsanity) {Create}": 5,
        "Polished Cut Diorite Slab (Itemsanity) {Create}": 5,
        "Polished Cut Diorite Wall (Itemsanity) {Create}": 5,
        "Cut Diorite Bricks (Itemsanity) {Create}": 5,
        "Cut Diorite Brick Stairs (Itemsanity) {Create}": 5,
        "Cut Diorite Brick Slab (Itemsanity) {Create}": 5,
        "Cut Diorite Brick Wall (Itemsanity) {Create}": 5,
        "Small Diorite Bricks (Itemsanity) {Create}": 5,
        "Small Diorite Brick Stairs (Itemsanity) {Create}": 5,
        "Small Diorite Brick Slab (Itemsanity) {Create}": 5,
        "Small Diorite Brick Wall (Itemsanity) {Create}": 5,
        "Layered Diorite (Itemsanity) {Create}": 5,
        "Diorite Pillar (Itemsanity) {Create}": 5,
        "Cut Andesite (Itemsanity) {Create}": 5,
        "Cut Andesite Stairs (Itemsanity) {Create}": 5,
        "Cut Andesite Slab (Itemsanity) {Create}": 5,
        "Cut Andesite Wall (Itemsanity) {Create}": 5,
        "Polished Cut Andesite (Itemsanity) {Create}": 5,
        "Polished Cut Andesite Stairs (Itemsanity) {Create}": 5,
        "Polished Cut Andesite Slab (Itemsanity) {Create}": 5,
        "Polished Cut Andesite Wall (Itemsanity) {Create}": 5,
        "Cut Andesite Bricks (Itemsanity) {Create}": 5,
        "Cut Andesite Brick Stairs (Itemsanity) {Create}": 5,
        "Cut Andesite Brick Slab (Itemsanity) {Create}": 5,
        "Cut Andesite Brick Wall (Itemsanity) {Create}": 5,
        "Small Andesite Bricks (Itemsanity) {Create}": 5,
        "Small Andesite Brick Stairs (Itemsanity) {Create}": 5,
        "Small Andesite Brick Slab (Itemsanity) {Create}": 5,
        "Small Andesite Brick Wall (Itemsanity) {Create}": 5,
        "Layered Andesite (Itemsanity) {Create}": 5,
        "Andesite Pillar (Itemsanity) {Create}": 5,
        "Cut Calcite (Itemsanity) {Create}": 5,
        "Cut Calcite Stairs (Itemsanity) {Create}": 5,
        "Cut Calcite Slab (Itemsanity) {Create}": 5,
        "Cut Calcite Wall (Itemsanity) {Create}": 5,
        "Polished Cut Calcite (Itemsanity) {Create}": 5,
        "Polished Cut Calcite Stairs (Itemsanity) {Create}": 5,
        "Polished Cut Calcite Slab (Itemsanity) {Create}": 5,
        "Polished Cut Calcite Wall (Itemsanity) {Create}": 5,
        "Cut Calcite Bricks (Itemsanity) {Create}": 5,
        "Cut Calcite Brick Stairs (Itemsanity) {Create}": 5,
        "Cut Calcite Brick Slab (Itemsanity) {Create}": 5,
        "Cut Calcite Brick Wall (Itemsanity) {Create}": 5,
        "Small Calcite Bricks (Itemsanity) {Create}": 5,
        "Small Calcite Brick Stairs (Itemsanity) {Create}": 5,
        "Small Calcite Brick Slab (Itemsanity) {Create}": 5,
        "Small Calcite Brick Wall (Itemsanity) {Create}": 5,
        "Layered Calcite (Itemsanity) {Create}": 5,
        "Calcite Pillar (Itemsanity) {Create}": 5,
        "Cut Dripstone (Itemsanity) {Create}": 5,
        "Cut Dripstone Stairs (Itemsanity) {Create}": 5,
        "Cut Dripstone Slab (Itemsanity) {Create}": 5,
        "Cut Dripstone Wall (Itemsanity) {Create}": 5,
        "Polished Cut Dripstone (Itemsanity) {Create}": 5,
        "Polished Cut Dripstone Stairs (Itemsanity) {Create}": 5,
        "Polished Cut Dripstone Slab (Itemsanity) {Create}": 5,
        "Polished Cut Dripstone Wall (Itemsanity) {Create}": 5,
        "Cut Dripstone Bricks (Itemsanity) {Create}": 5,
        "Cut Dripstone Brick Stairs (Itemsanity) {Create}": 5,
        "Cut Dripstone Brick Slab (Itemsanity) {Create}": 5,
        "Cut Dripstone Brick Wall (Itemsanity) {Create}": 5,
        "Small Dripstone Bricks (Itemsanity) {Create}": 5,
        "Small Dripstone Brick Stairs (Itemsanity) {Create}": 5,
        "Small Dripstone Brick Slab (Itemsanity) {Create}": 5,
        "Small Dripstone Brick Wall (Itemsanity) {Create}": 5,
        "Layered Dripstone (Itemsanity) {Create}": 5,
        "Dripstone Pillar (Itemsanity) {Create}": 5,
        "Cut Deepslate (Itemsanity) {Create}": 5,
        "Cut Deepslate Stairs (Itemsanity) {Create}": 5,
        "Cut Deepslate Slab (Itemsanity) {Create}": 5,
        "Cut Deepslate Wall (Itemsanity) {Create}": 5,
        "Polished Cut Deepslate (Itemsanity) {Create}": 5,
        "Polished Cut Deepslate Stairs (Itemsanity) {Create}": 5,
        "Polished Cut Deepslate Slab (Itemsanity) {Create}": 5,
        "Polished Cut Deepslate Wall (Itemsanity) {Create}": 5,
        "Cut Deepslate Bricks (Itemsanity) {Create}": 5,
        "Cut Deepslate Brick Stairs (Itemsanity) {Create}": 5,
        "Cut Deepslate Brick Slab (Itemsanity) {Create}": 5,
        "Cut Deepslate Brick Wall (Itemsanity) {Create}": 5,
        "Small Deepslate Bricks (Itemsanity) {Create}": 5,
        "Small Deepslate Brick Stairs (Itemsanity) {Create}": 5,
        "Small Deepslate Brick Slab (Itemsanity) {Create}": 5,
        "Small Deepslate Brick Wall (Itemsanity) {Create}": 5,
        "Layered Deepslate (Itemsanity) {Create}": 5,
        "Deepslate Pillar (Itemsanity) {Create}": 5,
        "Cut Tuff (Itemsanity) {Create}": 5,
        "Cut Tuff Stairs (Itemsanity) {Create}": 5,
        "Cut Tuff Slab (Itemsanity) {Create}": 5,
        "Cut Tuff Wall (Itemsanity) {Create}": 5,
        "Polished Cut Tuff (Itemsanity) {Create}": 5,
        "Polished Cut Tuff Stairs (Itemsanity) {Create}": 5,
        "Polished Cut Tuff Slab (Itemsanity) {Create}": 5,
        "Polished Cut Tuff Wall (Itemsanity) {Create}": 5,
        "Cut Tuff Bricks (Itemsanity) {Create}": 5,
        "Cut Tuff Brick Stairs (Itemsanity) {Create}": 5,
        "Cut Tuff Brick Slab (Itemsanity) {Create}": 5,
        "Cut Tuff Brick Wall (Itemsanity) {Create}": 5,
        "Small Tuff Bricks (Itemsanity) {Create}": 5,
        "Small Tuff Brick Stairs (Itemsanity) {Create}": 5,
        "Small Tuff Brick Slab (Itemsanity) {Create}": 5,
        "Small Tuff Brick Wall (Itemsanity) {Create}": 5,
        "Layered Tuff (Itemsanity) {Create}": 5,
        "Tuff Pillar (Itemsanity) {Create}": 5,
        "Cut Asurine (Itemsanity) {Create}": 5,
        "Cut Asurine Stairs (Itemsanity) {Create}": 5,
        "Cut Asurine Slab (Itemsanity) {Create}": 5,
        "Cut Asurine Wall (Itemsanity) {Create}": 5,
        "Polished Cut Asurine (Itemsanity) {Create}": 5,
        "Polished Cut Asurine Stairs (Itemsanity) {Create}": 5,
        "Polished Cut Asurine Slab (Itemsanity) {Create}": 5,
        "Polished Cut Asurine Wall (Itemsanity) {Create}": 5,
        "Cut Asurine Bricks (Itemsanity) {Create}": 5,
        "Cut Asurine Brick Stairs (Itemsanity) {Create}": 5,
        "Cut Asurine Brick Slab (Itemsanity) {Create}": 5,
        "Cut Asurine Brick Wall (Itemsanity) {Create}": 5,
        "Small Asurine Bricks (Itemsanity) {Create}": 5,
        "Small Asurine Brick Stairs (Itemsanity) {Create}": 5,
        "Small Asurine Brick Slab (Itemsanity) {Create}": 5,
        "Small Asurine Brick Wall (Itemsanity) {Create}": 5,
        "Layered Asurine (Itemsanity) {Create}": 5,
        "Asurine Pillar (Itemsanity) {Create}": 5,
        "Cut Crimsite (Itemsanity) {Create}": 5,
        "Cut Crimsite Stairs (Itemsanity) {Create}": 5,
        "Cut Crimsite Slab (Itemsanity) {Create}": 5,
        "Cut Crimsite Wall (Itemsanity) {Create}": 5,
        "Polished Cut Crimsite (Itemsanity) {Create}": 5,
        "Polished Cut Crimsite Stairs (Itemsanity) {Create}": 5,
        "Polished Cut Crimsite Slab (Itemsanity) {Create}": 5,
        "Polished Cut Crimsite Wall (Itemsanity) {Create}": 5,
        "Cut Crimsite Bricks (Itemsanity) {Create}": 5,
        "Cut Crimsite Brick Stairs (Itemsanity) {Create}": 5,
        "Cut Crimsite Brick Slab (Itemsanity) {Create}": 5,
        "Cut Crimsite Brick Wall (Itemsanity) {Create}": 5,
        "Small Crimsite Bricks (Itemsanity) {Create}": 5,
        "Small Crimsite Brick Stairs (Itemsanity) {Create}": 5,
        "Small Crimsite Brick Slab (Itemsanity) {Create}": 5,
        "Small Crimsite Brick Wall (Itemsanity) {Create}": 5,
        "Layered Crimsite (Itemsanity) {Create}": 5,
        "Crimsite Pillar (Itemsanity) {Create}": 5,
        "Cut Limestone (Itemsanity) {Create}": 5,
        "Cut Limestone Stairs (Itemsanity) {Create}": 5,
        "Cut Limestone Slab (Itemsanity) {Create}": 5,
        "Cut Limestone Wall (Itemsanity) {Create}": 5,
        "Polished Cut Limestone (Itemsanity) {Create}": 5,
        "Polished Cut Limestone Stairs (Itemsanity) {Create}": 5,
        "Polished Cut Limestone Slab (Itemsanity) {Create}": 5,
        "Polished Cut Limestone Wall (Itemsanity) {Create}": 5,
        "Cut Limestone Bricks (Itemsanity) {Create}": 5,
        "Cut Limestone Brick Stairs (Itemsanity) {Create}": 5,
        "Cut Limestone Brick Slab (Itemsanity) {Create}": 5,
        "Cut Limestone Brick Wall (Itemsanity) {Create}": 5,
        "Small Limestone Bricks (Itemsanity) {Create}": 5,
        "Small Limestone Brick Stairs (Itemsanity) {Create}": 5,
        "Small Limestone Brick Slab (Itemsanity) {Create}": 5,
        "Small Limestone Brick Wall (Itemsanity) {Create}": 5,
        "Layered Limestone (Itemsanity) {Create}": 5,
        "Limestone Pillar (Itemsanity) {Create}": 5,
        "Cut Ochrum (Itemsanity) {Create}": 5,
        "Cut Ochrum Stairs (Itemsanity) {Create}": 5,
        "Cut Ochrum Slab (Itemsanity) {Create}": 5,
        "Cut Ochrum Wall (Itemsanity) {Create}": 5,
        "Polished Cut Ochrum (Itemsanity) {Create}": 5,
        "Polished Cut Ochrum Stairs (Itemsanity) {Create}": 5,
        "Polished Cut Ochrum Slab (Itemsanity) {Create}": 5,
        "Polished Cut Ochrum Wall (Itemsanity) {Create}": 5,
        "Cut Ochrum Bricks (Itemsanity) {Create}": 5,
        "Cut Ochrum Brick Stairs (Itemsanity) {Create}": 5,
        "Cut Ochrum Brick Slab (Itemsanity) {Create}": 5,
        "Cut Ochrum Brick Wall (Itemsanity) {Create}": 5,
        "Small Ochrum Bricks (Itemsanity) {Create}": 5,
        "Small Ochrum Brick Stairs (Itemsanity) {Create}": 5,
        "Small Ochrum Brick Slab (Itemsanity) {Create}": 5,
        "Small Ochrum Brick Wall (Itemsanity) {Create}": 5,
        "Layered Ochrum (Itemsanity) {Create}": 5,
        "Ochrum Pillar (Itemsanity) {Create}": 5,
        "Cut Veridium (Itemsanity) {Create}": 5,
        "Cut Veridium Stairs (Itemsanity) {Create}": 5,
        "Cut Veridium Slab (Itemsanity) {Create}": 5,
        "Cut Veridium Wall (Itemsanity) {Create}": 5,
        "Polished Cut Veridium (Itemsanity) {Create}": 5,
        "Polished Cut Veridium Stairs (Itemsanity) {Create}": 5,
        "Polished Cut Veridium Slab (Itemsanity) {Create}": 5,
        "Polished Cut Veridium Wall (Itemsanity) {Create}": 5,
        "Cut Veridium Bricks (Itemsanity) {Create}": 5,
        "Cut Veridium Brick Stairs (Itemsanity) {Create}": 5,
        "Cut Veridium Brick Slab (Itemsanity) {Create}": 5,
        "Cut Veridium Brick Wall (Itemsanity) {Create}": 5,
        "Small Veridium Bricks (Itemsanity) {Create}": 5,
        "Small Veridium Brick Stairs (Itemsanity) {Create}": 5,
        "Small Veridium Brick Slab (Itemsanity) {Create}": 5,
        "Small Veridium Brick Wall (Itemsanity) {Create}": 5,
        "Layered Veridium (Itemsanity) {Create}": 5,
        "Veridium Pillar (Itemsanity) {Create}": 5,
    }, lambda state: canCraftSPDecorativeStone(world, state))

    # Has Smelting
    create_region(world, "CanSmelt", "SmeltAndCutting", {
        "Copper Table Cover (Itemsanity) {Create}": 5,
        "Copper Ladder (Itemsanity) {Create}": 5,
        "Copper Bars (Itemsanity) {Create}": 5,
        "Copper Scaffolding (Itemsanity) {Create}": 5,
        "Framed Glass Door (Itemsanity) {Create}": 5,
        "Framed Glass Trapdoor (Itemsanity) {Create}": 5,
        "Block of Industrial Iron (Itemsanity) {Create}": 5,
        "Block of Weathered Iron (Itemsanity) {Create}": 5,
        "Copper Shingles (Itemsanity) {Create}": 5,
        "Exposed Copper Shingles (Itemsanity) {Create}": 5,
        "Weathered Copper Shingles (Itemsanity) {Create}": 5,
        "Oxidized Copper Shingles (Itemsanity) {Create}": 5,
        "Copper Shingle Slab (Itemsanity) {Create}": 5,
        "Exposed Copper Shingle Slab (Itemsanity) {Create}": 5,
        "Weathered Copper Shingle Slab (Itemsanity) {Create}": 5,
        "Oxidized Copper Shingle Slab (Itemsanity) {Create}": 5,
        "Copper Shingle Stairs (Itemsanity) {Create}": 5,
        "Exposed Copper Shingle Stairs (Itemsanity) {Create}": 5,
        "Weathered Copper Shingle Stairs (Itemsanity) {Create}": 5,
        "Oxidized Copper Shingle Stairs (Itemsanity) {Create}": 5,
        "Waxed Copper Shingles (Itemsanity) {Create}": 5,
        "Waxed Exposed Copper Shingles (Itemsanity) {Create}": 5,
        "Waxed Weathered Copper Shingles (Itemsanity) {Create}": 5,
        "Waxed Oxidized Copper Shingles (Itemsanity) {Create}": 5,
        "Waxed Copper Shingle Slab (Itemsanity) {Create}": 5,
        "Waxed Exposed Copper Shingle Slab (Itemsanity) {Create}": 5,
        "Waxed Weathered Copper Shingle Slab (Itemsanity) {Create}": 5,
        "Waxed Oxidized Copper Shingle Slab (Itemsanity) {Create}": 5,
        "Waxed Copper Shingle Stairs (Itemsanity) {Create}": 5,
        "Waxed Exposed Copper Shingle Stairs (Itemsanity) {Create}": 5,
        "Waxed Weathered Copper Shingle Stairs (Itemsanity) {Create}": 5,
        "Waxed Oxidized Copper Shingle Stairs (Itemsanity) {Create}": 5,
        "Copper Tiles (Itemsanity) {Create}": 5,
        "Exposed Copper Tiles (Itemsanity) {Create}": 5,
        "Weathered Copper Tiles (Itemsanity) {Create}": 5,
        "Oxidized Copper Tiles (Itemsanity) {Create}": 5,
        "Copper Tile Slab (Itemsanity) {Create}": 5,
        "Exposed Copper Tile Slab (Itemsanity) {Create}": 5,
        "Weathered Copper Tile Slab (Itemsanity) {Create}": 5,
        "Oxidized Copper Tile Slab (Itemsanity) {Create}": 5,
        "Copper Tile Stairs (Itemsanity) {Create}": 5,
        "Exposed Copper Tile Stairs (Itemsanity) {Create}": 5,
        "Weathered Copper Tile Stairs (Itemsanity) {Create}": 5,
        "Oxidized Copper Tile Stairs (Itemsanity) {Create}": 5,
        "Waxed Copper Tiles (Itemsanity) {Create}": 5,
        "Waxed Exposed Copper Tiles (Itemsanity) {Create}": 5,
        "Waxed Weathered Copper Tiles (Itemsanity) {Create}": 5,
        "Waxed Oxidized Copper Tiles (Itemsanity) {Create}": 5,
        "Waxed Copper Tile Slab (Itemsanity) {Create}": 5,
        "Waxed Exposed Copper Tile Slab (Itemsanity) {Create}": 5,
        "Waxed Weathered Copper Tile Slab (Itemsanity) {Create}": 5,
        "Waxed Oxidized Copper Tile Slab (Itemsanity) {Create}": 5,
        "Waxed Copper Tile Stairs (Itemsanity) {Create}": 5,
        "Waxed Exposed Copper Tile Stairs (Itemsanity) {Create}": 5,
        "Waxed Weathered Copper Tile Stairs (Itemsanity) {Create}": 5,
        "Waxed Oxidized Copper Tile Stairs (Itemsanity) {Create}": 5,
        "Tiled Glass (Itemsanity) {Create}": 5,
        "Framed Glass (Itemsanity) {Create}": 5,
        "Horizontal Framed Glass (Itemsanity) {Create}": 5,
        "Vertical Framed Glass (Itemsanity) {Create}": 5,
        "Tiled Glass Pane (Itemsanity) {Create}": 5,
        "Framed Glass Pane (Itemsanity) {Create}": 5,
        "Horizontal Framed Glass Pane (Itemsanity) {Create}": 5,
        "Vertical Framed Glass Pane (Itemsanity) {Create}": 5,
        "Industrial Iron Window (Itemsanity) {Create}": 5,
        "Weathered Iron Window (Itemsanity) {Create}": 5,
        "Industrial Iron Window Pane (Itemsanity) {Create}": 5,
        "Weathered Iron Window Pane (Itemsanity) {Create}": 5,
    }, lambda state: canSmelt(world, state) and canCraftSPDecorativeStone(world, state))

    # Has Nether Access
    create_region(world, "NetherAccess", "NetherAccessAndCutting", {
        "Cut Scoria (Itemsanity) {Create}": 5,
        "Cut Scoria Stairs (Itemsanity) {Create}": 5,
        "Cut Scoria Slab (Itemsanity) {Create}": 5,
        "Cut Scoria Wall (Itemsanity) {Create}": 5,
        "Polished Cut Scoria (Itemsanity) {Create}": 5,
        "Polished Cut Scoria Stairs (Itemsanity) {Create}": 5,
        "Polished Cut Scoria Slab (Itemsanity) {Create}": 5,
        "Polished Cut Scoria Wall (Itemsanity) {Create}": 5,
        "Cut Scoria Bricks (Itemsanity) {Create}": 5,
        "Cut Scoria Brick Stairs (Itemsanity) {Create}": 5,
        "Cut Scoria Brick Slab (Itemsanity) {Create}": 5,
        "Cut Scoria Brick Wall (Itemsanity) {Create}": 5,
        "Small Scoria Bricks (Itemsanity) {Create}": 5,
        "Small Scoria Brick Stairs (Itemsanity) {Create}": 5,
        "Small Scoria Brick Slab (Itemsanity) {Create}": 5,
        "Small Scoria Brick Wall (Itemsanity) {Create}": 5,
        "Layered Scoria (Itemsanity) {Create}": 5,
        "Scoria Pillar (Itemsanity) {Create}": 5,
        "Cut Scorchia (Itemsanity) {Create}": 5,
        "Cut Scorchia Stairs (Itemsanity) {Create}": 5,
        "Cut Scorchia Slab (Itemsanity) {Create}": 5,
        "Cut Scorchia Wall (Itemsanity) {Create}": 5,
        "Polished Cut Scorchia (Itemsanity) {Create}": 5,
        "Polished Cut Scorchia Stairs (Itemsanity) {Create}": 5,
        "Polished Cut Scorchia Slab (Itemsanity) {Create}": 5,
        "Polished Cut Scorchia Wall (Itemsanity) {Create}": 5,
        "Cut Scorchia Bricks (Itemsanity) {Create}": 5,
        "Cut Scorchia Brick Stairs (Itemsanity) {Create}": 5,
        "Cut Scorchia Brick Slab (Itemsanity) {Create}": 5,
        "Cut Scorchia Brick Wall (Itemsanity) {Create}": 5,
        "Small Scorchia Bricks (Itemsanity) {Create}": 5,
        "Small Scorchia Brick Stairs (Itemsanity) {Create}": 5,
        "Small Scorchia Brick Slab (Itemsanity) {Create}": 5,
        "Small Scorchia Brick Wall (Itemsanity) {Create}": 5,
        "Layered Scorchia (Itemsanity) {Create}": 5,
        "Scorchia Pillar (Itemsanity) {Create}": 5,
    }, lambda state: canAccessNether(world, state) and canCraftSPDecorativeStone(world, state))

    # Has Rose Quartz
    create_region(world, "RoseQuartz", "RoseQuartzAndCutting", {
        "Block of Rose Quartz (Itemsanity) {Create}": 5,
        "Rose Quartz Tiles (Itemsanity) {Create}": 5,
        "Small Rose Quartz Tiles (Itemsanity) {Create}": 5,
    }, lambda state: canCraftRoseQuartz(world, state) and canCraftSPDecorativeStone(world, state))

    # Has Zinc
    create_region(world, "Zinc", "ZincCutting", {
        "Copycat Step (Itemsanity) {Create}": 5,
        "Copycat Panel (Itemsanity) {Create}": 5,
    }, lambda state: canGetZinc(world, state) and canCraftSPDecorativeStone(world, state))

    # Has Andesite Alloy
    create_region(world, "AndesiteAlloy", "AndesiteAlloyCutting", {
        "Andesite Table Cover (Itemsanity) {Create}": 5,
        "Andesite Ladder (Itemsanity) {Create}": 5,
        "Andesite Bars (Itemsanity) {Create}": 5,
        "Andesite Scaffolding (Itemsanity) {Create}": 5,
    }, lambda state: canCraftAndesiteAlloy(world, state) and canCraftSPDecorativeStone(world, state))

    # Has Brass
    create_region(world, "Brass", "BrassCutting", {
        "Brass Table Cover (Itemsanity) {Create}": 5,
        "Brass Ladder (Itemsanity) {Create}": 5,
        "Brass Bars (Itemsanity) {Create}": 5,
        "Brass Scaffolding (Itemsanity) {Create}": 5,
    }, lambda state: canCraftBrass(world, state) and canCraftSPDecorativeStone(world, state))

    ####################################################################################################################
    # DYED ITEMS #######################################################################################################
    ####################################################################################################################

    # Regular Dye and Press
    create_region(world, "AndesiteAlloy", "RegularDyeAndPress", {
        "Red Valve Handle (Itemsanity) {Create}": 15,
        "Yellow Valve Handle (Itemsanity) {Create}": 15,
        "Blue Valve Handle (Itemsanity) {Create}": 15,
        "White Valve Handle (Itemsanity) {Create}": 15
    }, lambda state: canDyeBasic(world, state) and hasPress(world, state))

    # Black Dye and Press
    create_region(world, "AndesiteAlloy", "BlackDyeAndPress", {
        "Black Valve Handle (Itemsanity) {Create}": 15,
        "Gray Valve Handle (Itemsanity) {Create}": 15
    }, lambda state: canDyeBlack(world, state) and hasPress(world, state))

    # Green Dye and Press
    create_region(world, "AndesiteAlloy", "GreenDyeAndPress", {
        "Green Valve Handle (Itemsanity) {Create}": 16
    }, lambda state: hasPress(world, state) and canDyeGreen(world, state))

    # Full Dye and Press
    create_region(world, "AndesiteAlloy", "FullDyeAndPress", {
        "Orange Valve Handle (Itemsanity) {Create}": 15,
        "Light Blue Valve Handle (Itemsanity) {Create}": 15,
        "Purple Valve Handle (Itemsanity) {Create}": 15,
        "Light Gray Valve Handle (Itemsanity) {Create}": 15,
        "Brown Valve Handle (Itemsanity) {Create}": 16,
        "Pink Valve Handle (Itemsanity) {Create}": 15,
        "Magenta Valve Handle (Itemsanity) {Create}": 15
    }, lambda state: canDyeFull(world, state) and hasPress(world, state))

    # Lime and Cyan Dye and Press
    create_region(world, "AndesiteAlloy", "LimeAndCyanDyeAndPress", {
        "Lime Valve Handle (Itemsanity) {Create}": 16,
        "Cyan Valve Handle (Itemsanity) {Create}": 16
    }, lambda state: canDyeFull(world, state) and hasPress(world, state) and canDyeGreen(world, state))




    # Regular Dye and Storage
    create_region(world, "AndesiteAlloy", "RegularDyeAndStorageAndAlloy", {
        "Red Postbox (Itemsanity) {Create}": 15,
        "Yellow Postbox (Itemsanity) {Create}": 15,
        "Blue Postbox (Itemsanity) {Create}": 15,
        "White Postbox (Itemsanity) {Create}": 15
    }, lambda state: canDyeBasic(world, state) and canAccessChests(world, state))

    # Black Dye and Storage
    create_region(world, "AndesiteAlloy", "BlackDyeAndStorageAndAlloy", {
        "Black Postbox (Itemsanity) {Create}": 15,
        "Gray Postbox (Itemsanity) {Create}": 15
    }, lambda state: canDyeBlack(world, state) and canAccessChests(world, state))

    # Green Dye and Storage
    create_region(world, "AndesiteAlloy", "GreenDyeAndStorageAndAlloy", {
        "Green Postbox (Itemsanity) {Create}": 16
    }, lambda state: canAccessChests(world, state) and canDyeGreen(world, state))

    # Full Dye and Storage
    create_region(world, "AndesiteAlloy", "FullDyeAndStorageAndAlloy", {
        "Orange Postbox (Itemsanity) {Create}": 15,
        "Light Blue Postbox (Itemsanity) {Create}": 15,
        "Purple Postbox (Itemsanity) {Create}": 15,
        "Light Gray Postbox (Itemsanity) {Create}": 15,
        "Brown Postbox (Itemsanity) {Create}": 16,
        "Pink Postbox (Itemsanity) {Create}": 15,
        "Magenta Postbox (Itemsanity) {Create}": 15
    }, lambda state: canDyeFull(world, state) and canAccessChests(world, state))

    # Lime and Cyan Dye and Storage
    create_region(world, "AndesiteAlloy", "LimeAndCyanDyeAndStorageAndAlloy", {
        "Lime Postbox (Itemsanity) {Create}": 16,
        "Cyan Postbox (Itemsanity) {Create}": 16
    }, lambda state: canDyeFull(world, state) and canAccessChests(world, state) and canDyeGreen(world, state))


    # Regular Dye
    create_region(world, "AndesiteAlloy", "RegularDye", {
        "Red Table Cloth (Itemsanity) {Create}": 15,
        "Yellow Table Cloth (Itemsanity) {Create}": 15,
        "Blue Table Cloth (Itemsanity) {Create}": 15,
        "White Table Cloth (Itemsanity) {Create}": 15,

        "Red Seat (Itemsanity) {Create}": 15,
        "Yellow Seat (Itemsanity) {Create}": 15,
        "Blue Seat (Itemsanity) {Create}": 15,
        "White Seat (Itemsanity) {Create}": 15
    }, lambda state: canDyeBasic(world, state))

    # Black Dye
    create_region(world, "AndesiteAlloy", "BlackDye", {
        "Black Table Cloth (Itemsanity) {Create}": 15,
        "Gray Table Cloth (Itemsanity) {Create}": 15,

        "Black Seat (Itemsanity) {Create}": 15,
        "Gray Seat (Itemsanity) {Create}": 15
    }, lambda state: canDyeBlack(world, state))

    # Green Dye
    create_region(world, "AndesiteAlloy", "GreenDye", {
        "Green Table Cloth (Itemsanity) {Create}": 16,
        "Green Seat (Itemsanity) {Create}": 16,
    }, lambda state: canDyeGreen(world, state))

    # Full Dye
    create_region(world, "AndesiteAlloy", "FullDye", {
        "Orange Table Cloth (Itemsanity) {Create}": 15,
        "Light Blue Table Cloth (Itemsanity) {Create}": 15,
        "Purple Table Cloth (Itemsanity) {Create}": 15,
        "Light Gray Table Cloth (Itemsanity) {Create}": 15,
        "Brown Table Cloth (Itemsanity) {Create}": 16,
        "Pink Table Cloth (Itemsanity) {Create}": 15,
        "Magenta Table Cloth (Itemsanity) {Create}": 15,

        "Orange Seat (Itemsanity) {Create}": 15,
        "Light Blue Seat (Itemsanity) {Create}": 15,
        "Purple Seat (Itemsanity) {Create}": 15,
        "Light Gray Seat (Itemsanity) {Create}": 15,
        "Brown Seat (Itemsanity) {Create}": 16,
        "Pink Seat (Itemsanity) {Create}": 15,
        "Magenta Seat (Itemsanity) {Create}": 15
    }, lambda state: canDyeFull(world, state))

    # Lime and Cyan Dye
    create_region(world, "AndesiteAlloy", "LimeAndCyanDye", {
        "Lime Table Cloth (Itemsanity) {Create}": 16,
        "Cyan Table Cloth (Itemsanity) {Create}": 16,

        "Lime Seat (Itemsanity) {Create}": 16,
        "Cyan Seat (Itemsanity) {Create}": 16
    }, lambda state: canDyeFull(world, state) and canDyeGreen(world, state))


    # Regular Dye and Press And Storage And Gold
    create_region(world, "AndesiteAlloy", "RegularDyeAndPressAndStorageAndGold", {
        "Red Toolbox (Itemsanity) {Create}": 15,
        "Yellow Toolbox (Itemsanity) {Create}": 15,
        "Blue Toolbox (Itemsanity) {Create}": 15,
        "White Toolbox (Itemsanity) {Create}": 15
    }, lambda state: canDyeBasic(world, state) and hasPress(world, state) and canAccessChests(world, state) and canGetGold(world, state))

    # Black Dye and Press And Storage And Gold
    create_region(world, "AndesiteAlloy", "BlackDyeAndPressAndStorageAndGold", {
        "Black Toolbox (Itemsanity) {Create}": 15,
        "Gray Toolbox (Itemsanity) {Create}": 15
    }, lambda state: canDyeBlack(world, state) and hasPress(world, state) and canAccessChests(world, state) and canGetGold(world, state))

    # Green Dye and Press And Storage And Gold
    create_region(world, "AndesiteAlloy", "GreenDyeAndPressAndStorageAndGold", {
        "Green Toolbox (Itemsanity) {Create}": 16
    }, lambda state: hasPress(world, state) and canDyeGreen(world, state) and canAccessChests(world, state) and canGetGold(world, state))

    # Full Dye and Press And Storage And Gold
    create_region(world, "AndesiteAlloy", "FullDyeAndPressAndStorageAndGold", {
        "Orange Toolbox (Itemsanity) {Create}": 15,
        "Light Blue Toolbox (Itemsanity) {Create}": 15,
        "Purple Toolbox (Itemsanity) {Create}": 15,
        "Light Gray Toolbox (Itemsanity) {Create}": 15,
        "Brown Toolbox (Itemsanity) {Create}": 16,
        "Pink Toolbox (Itemsanity) {Create}": 15,
        "Magenta Toolbox (Itemsanity) {Create}": 15
    }, lambda state: canDyeFull(world, state) and hasPress(world, state) and canAccessChests(world, state) and canGetGold(world, state))

    # Lime and Cyan Dye and Press And Storage And Gold
    create_region(world, "AndesiteAlloy", "LimeAndCyanDyeAndPressAndStorageAndGold", {
        "Lime Toolbox (Itemsanity) {Create}": 16,
        "Cyan Toolbox (Itemsanity) {Create}": 16
    }, lambda state: canDyeFull(world, state) and hasPress(world, state) and canDyeGreen(world, state) and canAccessChests(world, state) and canGetGold(world, state))



def create_region(world: FabricMinecraftWorld, region_name: str, new_region_name: str, locations: dict[str, int], rule=None):
    create_locations_and_connect(world, region_name + "CreateItemsanity", new_region_name + "CreateItemsanity", locations, rule)