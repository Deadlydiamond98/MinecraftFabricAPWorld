from __future__ import annotations


from worlds.minecraft_fabric.region.regions_helper import create_locations_and_connect
from worlds.minecraft_fabric.logic.create_logic import *
from worlds.minecraft_fabric.region.mc_regions_consts import *

if TYPE_CHECKING:
   from worlds.minecraft_fabric import FabricMinecraftWorld


def create_create_itemsanity_regions(world: FabricMinecraftWorld):
    create_locations_and_connect(world, "Menu", "MenuCreateItemsanity", {
        "Crafting Blueprint (Itemsanity) {Create}": ITEMSANITY,
        "Asurine (Itemsanity) {Create}": ITEMSANITY,
        "Crimsite (Itemsanity) {Create}": ITEMSANITY,
        "Limestone (Itemsanity) {Create}": ITEMSANITY,
        "Ochrum (Itemsanity) {Create}": ITEMSANITY,
        "Veridium (Itemsanity) {Create}": ITEMSANITY,
    })

    # Nether Access
    create_region(world, "Menu", "NetherAccess", {
        "Scoria (Itemsanity) {Create}": ITEMSANITY,
        "Scorchia (Itemsanity) {Create}": ITEMSANITY,
    }, lambda state: canAccessNether(world, state))

    # Can Use Sandpaper
    create_region(world, "Menu", "Sandpaper", {
        "Sand Paper (Itemsanity) {Create}": ITEMSANITY
    }, lambda state: canUseSandpaper(world, state))

    # Can Use Red Sandpaper
    create_region(world, "Sandpaper", "RedSandpaper", {
        "Red Sand Paper (Itemsanity) {Create}": ITEMSANITY_EXPLORATION
    }, lambda state: canUseSandpaper(world, state) and hasCogs(world, state) and canCraftAndesiteAlloy(world, state))

    # Can Smelt
    create_region(world, "Menu", "CanSmelt", {
        "Schematic Table (Itemsanity) {Create}": ITEMSANITY,
        "Item Drain (Itemsanity) {Create}": ITEMSANITY,
        "Copper Casing (Itemsanity) {Create}": ITEMSANITY,
        "Copper Diving Helmet (Itemsanity) {Create}": ITEMSANITY,
        "Copper Door (Itemsanity) {Create}": ITEMSANITY,
        "Oak Window (Itemsanity) {Create}": ITEMSANITY,
        "Spruce Window (Itemsanity) {Create}": ITEMSANITY,
        "Birch Window (Itemsanity) {Create}": ITEMSANITY,
        "Jungle Window (Itemsanity) {Create}": ITEMSANITY_EXPLORATION,
        "Acacia Window (Itemsanity) {Create}": ITEMSANITY,
        "Dark Oak Window (Itemsanity) {Create}": ITEMSANITY_EXPLORATION,
        "Mangrove Window (Itemsanity) {Create}": ITEMSANITY_EXPLORATION,
        "Cherry Window (Itemsanity) {Create}": ITEMSANITY_EXPLORATION,
        "Bamboo Window (Itemsanity) {Create}": ITEMSANITY_EXPLORATION,
        "Oak Window Pane (Itemsanity) {Create}": ITEMSANITY,
        "Spruce Window Pane (Itemsanity) {Create}": ITEMSANITY,
        "Birch Window Pane (Itemsanity) {Create}": ITEMSANITY,
        "Jungle Window Pane (Itemsanity) {Create}": ITEMSANITY_EXPLORATION,
        "Acacia Window Pane (Itemsanity) {Create}": ITEMSANITY,
        "Dark Oak Window Pane (Itemsanity) {Create}": ITEMSANITY_EXPLORATION,
        "Mangrove Window Pane (Itemsanity) {Create}": ITEMSANITY_EXPLORATION,
        "Cherry Window Pane (Itemsanity) {Create}": ITEMSANITY_EXPLORATION,
        "Bamboo Window Pane (Itemsanity) {Create}": ITEMSANITY_EXPLORATION,
    }, lambda state: canSmelt(world, state))

    # Can Smelt And Nether Access
    create_region(world, "CanSmelt", "CanSmeltAndNether", {
        "Crimson Window (Itemsanity) {Create}": ITEMSANITY,
        "Warped Window (Itemsanity) {Create}": ITEMSANITY,
        "Crimson Window Pane (Itemsanity) {Create}": ITEMSANITY,
        "Warped Window Pane (Itemsanity) {Create}": ITEMSANITY
    }, lambda state: canSmelt(world, state) and canAccessNether(world, state))

    # Can Smelt And Compact
    create_region(world, "CanSmelt", "CanSmeltAndCompact", {
        "Copper Nugget (Itemsanity) {Create}": ITEMSANITY,
        "List Filter (Itemsanity) {Create}": ITEMSANITY,
        "Ornate Iron Window (Itemsanity) {Create}": ITEMSANITY,
        "Ornate Iron Window Pane (Itemsanity) {Create}": ITEMSANITY,
    }, lambda state: canSmelt(world, state) and canCompactResources(world, state))

    # Has Iron Tools
    create_region(world, "Menu", "IronTools", {
        "Powered Latch (Itemsanity) {Create}": ITEMSANITY,
        "Powered Toggle Latch (Itemsanity) {Create}": ITEMSANITY
    }, lambda state: canUseIronTools(world, state))

    # Has Iron Tools And Compact
    create_region(world, "IronTools", "IronToolsAndCompact", {
        "Block of Raw Zinc (Itemsanity) {Create}": ITEMSANITY,
        "Raw Zinc (Itemsanity) {Create}": ITEMSANITY
    }, lambda state: canUseIronTools(world, state) and canCompactResources(world, state))

    # Has Zinc
    create_region(world, "Menu", "Zinc", {
        "Zinc Ingot (Itemsanity) {Create}": ITEMSANITY
    }, lambda state: canGetZinc(world, state))

    # Has Zinc And Compact
    create_region(world, "Menu", "ZincAndCompact", {
        "Zinc Nugget (Itemsanity) {Create}": ITEMSANITY,
        "Package Filter (Itemsanity) {Create}": ITEMSANITY,
        "Block of Zinc (Itemsanity) {Create}": ITEMSANITY
    }, lambda state: canGetZinc(world, state) and canCompactResources(world, state))

    # Has Rose Quartz
    create_region(world, "Menu", "RoseQuartz", {
        "Rose Quartz (Itemsanity) {Create}": ITEMSANITY
    }, lambda state: canCraftRoseQuartz(world, state))

    # Has Rose Quartz and Sand Paper
    create_region(world, "RoseQuartz", "RoseQuartzAndSandpaper", {
        "Polished Rose Quartz (Itemsanity) {Create}": ITEMSANITY
    }, lambda state: canCraftRoseQuartz(world, state) and canUseSandpaper(world, state))

    # Has Kelp
    create_region(world, "Menu", "Kelp", {
        "Mechanical Belt (Itemsanity) {Create}": ITEMSANITY
    }, lambda state: canCraftDriedKelp(world, state))

    # Has Andesite Alloy
    create_region(world, "Menu", "AndesiteAlloy", {
        "Shaft (Itemsanity) {Create}": ITEMSANITY,
        "Clutch (Itemsanity) {Create}": ITEMSANITY,
        "Encased Chain Drive (Itemsanity) {Create}": ITEMSANITY,
        "Nozzle (Itemsanity) {Create}": ITEMSANITY,
        "Turntable (Itemsanity) {Create}": ITEMSANITY,
        "Hand Crank (Itemsanity) {Create}": ITEMSANITY,
        "Basin (Itemsanity) {Create}": ITEMSANITY,
        "Depot (Itemsanity) {Create}": ITEMSANITY,
        "Wooden Bracket (Itemsanity) {Create}": ITEMSANITY,
        "Metal Bracket (Itemsanity) {Create}": ITEMSANITY,
        "Mechanical Piston (Itemsanity) {Create}": ITEMSANITY,
        "Piston Extension Pole (Itemsanity) {Create}": ITEMSANITY,
        "Mechanical Bearing (Itemsanity) {Create}": ITEMSANITY,
        "Linear Chassis (Itemsanity) {Create}": ITEMSANITY,
        "Secondary Linear Chassis (Itemsanity) {Create}": ITEMSANITY,
        "Radial Chassis (Itemsanity) {Create}": ITEMSANITY,
        "Mechanical Drill (Itemsanity) {Create}": ITEMSANITY,
        "Andesite Casing (Itemsanity) {Create}": ITEMSANITY,
        "Item Hatch (Itemsanity) {Create}": ITEMSANITY,
        "Analog Lever (Itemsanity) {Create}": ITEMSANITY,
        "Andesite Alloy (Itemsanity) {Create}": ITEMSANITY,
        "Clipboard (Itemsanity) {Create}": ITEMSANITY,
        "Andesite Door (Itemsanity) {Create}": ITEMSANITY
    }, lambda state: canCraftAndesiteAlloy(world, state))

    # Has Andesite Alloy And Compact
    create_region(world, "AndesiteAlloy", "AndesiteAlloyAndCompact", {
        "Block of Andesite Alloy (Itemsanity) {Create}": ITEMSANITY
    }, lambda state: canCraftAndesiteAlloy(world, state) and canCompactResources(world, state))

    # Has Andesite Alloy And Iron Tools
    create_region(world, "AndesiteAlloy", "AndesiteAlloyAndIronTools", {
        "Cuckoo Clock (Itemsanity) {Create}": ITEMSANITY,
        "Speedometer (Itemsanity) {Create}": ITEMSANITY,
        "Stressometer (Itemsanity) {Create}": ITEMSANITY,
        "Gantry Shaft (Itemsanity) {Create}": ITEMSANITY,
        "Sticky Mechanical Piston (Itemsanity) {Create}": ITEMSANITY_EXPLORATION,
        "Sticker (Itemsanity) {Create}": ITEMSANITY_EXPLORATION
    }, lambda state: canCraftAndesiteAlloy(world, state) and canUseIronTools(world, state))

    # Has Cogs
    create_region(world, "AndesiteAlloy", "Cogs", {
        "Cogwheel (Itemsanity) {Create}": ITEMSANITY,
        "Large Cogwheel (Itemsanity) {Create}": ITEMSANITY,
        "Gearbox (Itemsanity) {Create}": ITEMSANITY,
        "Vertical Gearbox (Itemsanity) {Create}": ITEMSANITY,
        "Gearshift (Itemsanity) {Create}": ITEMSANITY,
        "Chain Conveyor (Itemsanity) {Create}": ITEMSANITY,
        "Millstone (Itemsanity) {Create}": ITEMSANITY,
        "Gantry Carriage (Itemsanity) {Create}": ITEMSANITY,
        "Wheat Flour (Itemsanity) {Create}": ITEMSANITY
    }, lambda state: hasCogs(world, state))

    # Has Waterwheel
    create_region(world, "AndesiteAlloy", "Waterwheel", {
        "Water Wheel (Itemsanity) {Create}": ITEMSANITY,
        "Large Water Wheel (Itemsanity) {Create}": ITEMSANITY
    }, lambda state: hasWaterWheel(world, state))

    # Has Windmill
    create_region(world, "AndesiteAlloy", "Windmill", {
        "Windmill Bearing (Itemsanity) {Create}": ITEMSANITY,
        "Windmill Sail Frame (Itemsanity) {Create}": ITEMSANITY,
        "Windmill Sail (Itemsanity) {Create}": ITEMSANITY
    }, lambda state: hasWindmill(world, state))

    # Has Press
    create_region(world, "AndesiteAlloy", "Press", {
        "Encased Fan (Itemsanity) {Create}": ITEMSANITY,
        "Mechanical Press (Itemsanity) {Create}": ITEMSANITY,
        "Chute (Itemsanity) {Create}": ITEMSANITY,
        "Fluid Pipe (Itemsanity) {Create}": ITEMSANITY,
        "Fluid Valve (Itemsanity) {Create}": ITEMSANITY,
        "Copper Valve Handle (Itemsanity) {Create}": ITEMSANITY,
        "Hose Pulley (Itemsanity) {Create}": ITEMSANITY,
        "Portable Fluid Interface (Itemsanity) {Create}": ITEMSANITY,
        "Rope Pulley (Itemsanity) {Create}": ITEMSANITY,
        "Mechanical Saw (Itemsanity) {Create}": ITEMSANITY,
        "Portable Storage Interface (Itemsanity) {Create}": ITEMSANITY,
        "Redstone Contact (Itemsanity) {Create}": ITEMSANITY,
        "Mechanical Harvester (Itemsanity) {Create}": ITEMSANITY,
        "Mechanical Plough (Itemsanity) {Create}": ITEMSANITY,
        "Propeller (Itemsanity) {Create}": ITEMSANITY,
        "Whisk (Itemsanity) {Create}": ITEMSANITY,
        "Copper Sheet (Itemsanity) {Create}": ITEMSANITY,
        "Iron Sheet (Itemsanity) {Create}": ITEMSANITY,
        "Super Glue (Itemsanity) {Create}": ITEMSANITY_EXPLORATION,
        "Metal Girder (Itemsanity) {Create}": ITEMSANITY
    }, lambda state: hasPress(world, state))

    # Has Press And Iron Tools
    create_region(world, "Press", "PressAndIronTools", {
        "Redstone Link (Itemsanity) {Create}": ITEMSANITY,
        "Transmitter (Itemsanity) {Create}": ITEMSANITY,
        "Linked Controller (Itemsanity) {Create}": ITEMSANITY
    }, lambda state: hasPress(world, state) and canUseIronTools(world, state))

    # Has Steam Engine
    create_region(world, "Press", "SteamEngine", {
        "Steam Engine (Itemsanity) {Create}": ITEMSANITY
    }, lambda state: hasSteamEngine(world, state))

    # Has Mixer
    create_region(world, "Press", "Mixer", {
        "Mechanical Mixer (Itemsanity) {Create}": ITEMSANITY
    }, lambda state: hasMixer(world, state))

    # Has Mixer And Fluid
    create_region(world, "Mixer", "MixerAndFluid", {
        "Sweet Roll (Itemsanity) {Create}": ITEMSANITY
    }, lambda state: hasMixer(world, state) and canUseBucket(world, state))

    # Has Chocolate
    create_region(world, "MixerAndFluid", "Chocolate", {
        "Bar of Chocolate (Itemsanity) {Create}": ITEMSANITY,
        "Chocolate Glazed Berries (Itemsanity) {Create}": ITEMSANITY,
        "Chocolate Bucket (Itemsanity) {Create}": ITEMSANITY
    }, lambda state: hasBlazeBurner(world, state) and hasMixer(world, state) and canUseBucket(world, state))

    # Has Blaze Burner
    create_region(world, "Press", "BlazeBurner", {
        "Blaze Burner (Itemsanity) {Create}": ITEMSANITY,
        "Empty Blaze Burner (Itemsanity) {Create}": ITEMSANITY
    }, lambda state: hasBlazeBurner(world, state))

    # Has Electron Tube
    create_region(world, "AndesiteAlloy", "ElectronTube", {
        "Adjustable Chain Gearshift (Itemsanity) {Create}": ITEMSANITY,
        "Contraption Controls (Itemsanity) {Create}": ITEMSANITY,
        "Display Board (Itemsanity) {Create}": ITEMSANITY,
        "Nixie Tube (Itemsanity) {Create}": ITEMSANITY,
        "Electron Tube (Itemsanity) {Create}": ITEMSANITY
    }, lambda state: canCraftElectronTube(world, state))

    # Has Crushing Wheel
    create_region(world, "AndesiteAlloy", "CrushingWheel", {
        "Crushing Wheel (Itemsanity) {Create}": ITEMSANITY,
        "Cinder Flour (Itemsanity) {Create}": ITEMSANITY,
        "Blaze Cake Base (Itemsanity) {Create}": ITEMSANITY,
        "Blaze Cake (Itemsanity) {Create}": ITEMSANITY,
        "Nugget of Experience (Itemsanity) {Create}": ITEMSANITY,
        "Crushed Raw Iron (Itemsanity) {Create}": ITEMSANITY,
        "Crushed Raw Gold (Itemsanity) {Create}": ITEMSANITY,
        "Crushed Raw Copper (Itemsanity) {Create}": ITEMSANITY,
        "Crushed Raw Zinc (Itemsanity) {Create}": ITEMSANITY,
        "Block of Experience (Itemsanity) {Create}": ITEMSANITY,
    }, lambda state: hasCrusher(world, state))

    # Has Fluid Tank
    create_region(world, "AndesiteAlloy", "FluidTank", {
        "Fluid Tank (Itemsanity) {Create}": ITEMSANITY
    }, lambda state: hasFluidTank(world, state))

    # Has Spout
    create_region(world, "AndesiteAlloy", "Spout", {
        "Spout (Itemsanity) {Create}": ITEMSANITY
    }, lambda state: canUseSpout(world, state))

    # Has Cardboard
    create_region(world, "AndesiteAlloy", "Cardboard", {
        "Packager (Itemsanity) {Create}": ITEMSANITY,
        "Re-Packager (Itemsanity) {Create}": ITEMSANITY,
        "Pulp (Itemsanity) {Create}": ITEMSANITY,
        "Cardboard (Itemsanity) {Create}": ITEMSANITY,
        "Cardboard Sword (Itemsanity) {Create}": ITEMSANITY,
        "Cardboard Helmet (Itemsanity) {Create}": ITEMSANITY,
        "Cardboard Chestplate (Itemsanity) {Create}": ITEMSANITY,
        "Cardboard Leggings (Itemsanity) {Create}": ITEMSANITY,
        "Cardboard Boots (Itemsanity) {Create}": ITEMSANITY,
        "Block of Cardboard (Itemsanity) {Create}": ITEMSANITY,
        "Bound Block of Cardboard (Itemsanity) {Create}": ITEMSANITY,
    }, lambda state: canCraftCardboard(world, state))

    # Has Brass
    create_region(world, "AndesiteAlloy", "Brass", {
        "Elevator Pulley (Itemsanity) {Create}": ITEMSANITY,
        "Brass Casing (Itemsanity) {Create}": ITEMSANITY,
        "Flywheel (Itemsanity) {Create}": ITEMSANITY,
        "Display Link (Itemsanity) {Create}": ITEMSANITY,
        "Placard (Itemsanity) {Create}": ITEMSANITY,
        "Pulse Repeater (Itemsanity) {Create}": ITEMSANITY,
        "Pulse Extender (Itemsanity) {Create}": ITEMSANITY,
        "Pulse Timer (Itemsanity) {Create}": ITEMSANITY,
        "Brass Hand (Itemsanity) {Create}": ITEMSANITY,
        "Crafter Slot Cover (Itemsanity) {Create}": ITEMSANITY,
        "Brass Ingot (Itemsanity) {Create}": ITEMSANITY,
        "Brass Nugget (Itemsanity) {Create}": ITEMSANITY,
        "Brass Sheet (Itemsanity) {Create}": ITEMSANITY,
        "Attribute Filter (Itemsanity) {Create}": ITEMSANITY,
        "Peculiar Bell (Itemsanity) {Create}": ITEMSANITY,
        "Haunted Bell (Itemsanity) {Create}": ITEMSANITY,
        "Brass Door (Itemsanity) {Create}": ITEMSANITY,
        "Block of Brass (Itemsanity) {Create}": ITEMSANITY,
    }, lambda state: canCraftBrass(world, state))

    # Has Brass and ElectronTube
    create_region(world, "Brass", "BrassAndElectronTube", {
        "Smart Observer (Itemsanity) {Create}": ITEMSANITY,
        "Deployer (Itemsanity) {Create}": ITEMSANITY,
        "Sequenced Gearshift (Itemsanity) {Create}": ITEMSANITY,
        "Threshold Switch (Itemsanity) {Create}": ITEMSANITY,
        "Clockwork Bearing (Itemsanity) {Create}": ITEMSANITY,
        "Smart Fluid Pipe (Itemsanity) {Create}": ITEMSANITY,
        "Smart Chute (Itemsanity) {Create}": ITEMSANITY,
    }, lambda state: canCraftBrass(world, state) and canUseSandpaper(world, state))

    # Has Mechanical Crafter
    create_region(world, "Brass", "MechanicalCrafter", {
        "Mechanical Crafter (Itemsanity) {Create}": ITEMSANITY
    }, lambda state: hasMechanicalCrafter(world, state))

    # Has Percision Mechanism
    create_region(world, "Brass", "PercisionMechanism", {
        "Rotation Speed Controller (Itemsanity) {Create}": ITEMSANITY,
        "Mechanical Arm (Itemsanity) {Create}": ITEMSANITY,
        "Incomplete Precision Mechanism (Itemsanity) {Create}": ITEMSANITY,
        "Precision Mechanism (Itemsanity) {Create}": ITEMSANITY
    }, lambda state: canCraftPercisionMechanism(world, state))

    # Has Train Tracks
    create_region(world, "Brass", "TrainTracks", {
        "Train Track (Itemsanity) {Create}": ITEMSANITY,
        "Incomplete Track (Itemsanity) {Create}": ITEMSANITY
    }, lambda state: canCraftTrainTracks(world, state))

    # Has Sturdy Sheet
    create_region(world, "Brass", "SturdySheet", {
        "Train Casing (Itemsanity) {Create}": ITEMSANITY,
        "Train Station (Itemsanity) {Create}": ITEMSANITY,
        "Train Signal (Itemsanity) {Create}": ITEMSANITY,
        "Train Observer (Itemsanity) {Create}": ITEMSANITY,
        "Sturdy Sheet (Itemsanity) {Create}": ITEMSANITY,
        "Unprocessed Obsidian Sheet (Itemsanity) {Create}": ITEMSANITY,
        "Train Schedule (Itemsanity) {Create}": ITEMSANITY,
        "Train Door (Itemsanity) {Create}": ITEMSANITY,
        "Train Trapdoor (Itemsanity) {Create}": ITEMSANITY,
    }, lambda state: canCraftSturdySheet(world, state))

    # Has Sturdy Sheet And Percision Mechanism
    create_region(world, "SturdySheet", "SturdySheetAndPercisionMechanism", {
        "Train Controls (Itemsanity) {Create}": ITEMSANITY
    }, lambda state: canCraftSturdySheet(world, state) and canCraftPercisionMechanism(world, state))

    # Has Mechanical Crafter And Percision Mechanism
    create_region(world, "Brass", "MechanicalCrafterAndPercisionMechanism", {
        "Potato Cannon (Itemsanity) {Create}": ITEMSANITY,
        "Extendo Grip (Itemsanity) {Create}": ITEMSANITY,
    }, lambda state: hasMechanicalCrafter(world, state) and canCraftPercisionMechanism(world, state))

    # Has Mechanical Crafter And Percision Mechanism
    create_region(world, "MechanicalCrafterAndPercisionMechanism", "MechanicalCrafterAndPercisionMechanismAndObsidian", {
        "Wand Of Symmetry (Itemsanity) {Create}": ITEMSANITY
    }, lambda state: hasMechanicalCrafter(world, state) and canCraftPercisionMechanism(world, state) and canGetObsidian(world, state))

    # Has Andesite and Kelp
    create_region(world, "AndesiteAlloy", "AndesiteAlloyAndKelp", {
        "Andesite Funnel (Itemsanity) {Create}": ITEMSANITY,
        "Andesite Tunnel (Itemsanity) {Create}": ITEMSANITY
    }, lambda state: canCraftAndesiteAlloy(world, state) and canCraftDriedKelp(world, state))

    # Has Brass and Kelp
    create_region(world, "Brass", "BrassAndKelp", {
        "Brass Funnel (Itemsanity) {Create}": ITEMSANITY,
        "Brass Tunnel (Itemsanity) {Create}": ITEMSANITY
    }, lambda state: canCraftBrass(world, state) and canCraftDriedKelp(world, state) and canUseSandpaper(world, state))

    # Has Press And Cogs
    create_region(world, "Press", "PressAndCogs", {
        "Weighted Ejector (Itemsanity) {Create}": ITEMSANITY,
        "Mechanical Pump (Itemsanity) {Create}": ITEMSANITY
    }, lambda state: hasPress(world, state) and hasCogs(world, state))

    # Has Press And Storage
    create_region(world, "Press", "PressAndStorage", {
        "Item Vault (Itemsanity) {Create}": ITEMSANITY,
        "Package Frogport (Itemsanity) {Create}": ITEMSANITY_EXPLORATION,
        "Stock Link (Itemsanity) {Create}": ITEMSANITY_EXPLORATION
    }, lambda state: hasPress(world, state) and canAccessChests(world, state))

    # Has Percision Mechanism And Storage
    create_region(world, "Brass", "PercisionMechanismAndStorage", {
        "Factory Gauge (Itemsanity) {Create}": ITEMSANITY
    }, lambda state: canCraftPercisionMechanism(world, state) and canAccessChests(world, state))

    # Has Press And Storage And Iron Tools
    create_region(world, "PressAndStorage", "PressAndStorageAndIronTools", {
        "Stock Ticker (Itemsanity) {Create}": ITEMSANITY,
        "Redstone Requester (Itemsanity) {Create}": ITEMSANITY
    }, lambda state: hasPress(world, state) and canAccessChests(world, state) and canUseIronTools(world, state))

    # Has Press And Gold
    create_region(world, "Press", "PressAndGold", {
        "Steam Whistle (Itemsanity) {Create}": ITEMSANITY,
        "Golden Sheet (Itemsanity) {Create}": ITEMSANITY,
        "Desk Bell (Itemsanity) {Create}": ITEMSANITY
    }, lambda state: hasPress(world, state) and canGetGold(world, state))

    # Has Press And Gold And Armor
    create_region(world, "PressAndGold", "PressAndGoldAndArmor", {
        "Engineer's Goggles (Itemsanity) {Create}": ITEMSANITY
    }, lambda state: hasPress(world, state) and canGetGold(world, state) and canWearLeatherArmor(world, state))

    # Has Press And Gold And Cogs
    create_region(world, "PressAndGold", "PressAndGoldAndCogs", {
        "Wrench (Itemsanity) {Create}": ITEMSANITY
    }, lambda state: hasPress(world, state) and canGetGold(world, state) and hasCogs(world, state))

    # Has Crushing Wheel And Electron Tube
    create_region(world, "CrushingWheel", "CrushingWheelAndElectronTube", {
        "Mechanical Roller (Itemsanity) {Create}": ITEMSANITY
    }, lambda state: hasCrusher(world, state) and canCraftElectronTube(world, state))

    # Has Crushing Wheel and Obsidian
    create_region(world, "CrushingWheel", "CrushingWheelAndObsidian", {
        "Powdered Obsidian (Itemsanity) {Create}": ITEMSANITY
    }, lambda state: hasCrusher(world, state) and canGetObsidian(world, state))

    # Has Press and Minecarts
    create_region(world, "Press", "PressAndMinecarts", {
        "Minecart Coupling (Itemsanity) {Create}": ITEMSANITY
    }, lambda state: hasPress(world, state) and canUseMinecart(world, state))

    # Can Smelt and Can Compact and Has Archery
    create_region(world, "CanSmelt", "CanSmeltAndCompactAndArchery", {
        "Schematicannon (Itemsanity) {Create}": ITEMSANITY
    }, lambda state: canSmelt(world, state) and canCompactResources(world, state) and canUseBow(world, state))

    # Has Gold and Electron Tubes and Minecarts
    create_region(world, "AndesiteAlloy", "GoldAndElectronTubesAndMinecarts", {
        "Controller Rail (Itemsanity) {Create}": ITEMSANITY
    }, lambda state: canGetGold(world, state) and canCraftElectronTube(world, state) and canUseMinecart(world, state))

    # Has Zinc and Rose Quartz and Sandpaper
    create_region(world, "Menu", "ZincAndRoseQuartz", {
        "Rose Quartz Lamp (Itemsanity) {Create}": ITEMSANITY
    }, lambda state: canGetZinc(world, state) and canCraftRoseQuartz(world, state) and canUseSandpaper(world, state))

    # Dough
    create_region(world, "AndesiteAlloy", "Dough", {
        "Dough (Itemsanity) {Create}": ITEMSANITY
    }, lambda state: hasCogs(world, state) and (canUseBucket(world, state) or hasPress(world, state)))

    # Has Mixer And Bottles
    create_region(world, "Mixer", "MixerAndBottles", {
        "Honeyed Apple (Itemsanity) {Create}": ITEMSANITY
    }, lambda state: hasMixer(world, state) and canUseBottles(world, state))

    # Has Mixer And Bottles And Bucket
    create_region(world, "MixerAndBottles", "MixerAndBottlesAndBucket", {
        "Honey Bucket (Itemsanity) {Create}": ITEMSANITY
    }, lambda state: hasMixer(world, state) and canUseBottles(world, state) and canUseBucket(world, state))

    # Builders Tea
    create_region(world, "MixerAndBottles", "BuildersTea", {
        "Builder's Tea (Itemsanity) {Create}": ITEMSANITY
    }, lambda state: hasMixer(world, state) and canUseBottles(world, state) and canUseBucket(world, state) and hasBlazeBurner(world, state) and (
        canUseShears(world, state) or canEnchant(world, state)
    ))

    # Copper Diving Gear
    create_region(world, "AndesiteAlloy", "CopperDivingGear", {
        "Copper Backtank (Itemsanity) {Create}": ITEMSANITY,
        "Copper Diving Boots (Itemsanity) {Create}": ITEMSANITY
    }, lambda state: canCraftAndesiteAlloy(world, state) and canWearGoldArmor(world, state))

    # Netherite Diving Gear
    create_region(world, "CopperDivingGear", "NetheriteDivingGear", {
        "Netherite Backtank (Itemsanity) {Create}": ITEMSANITY,
        "Netherite Diving Boots (Itemsanity) {Create}": ITEMSANITY
    }, lambda state: canCraftAndesiteAlloy(world, state) and canWearNetheriteArmor(world, state))

    # Netherite Diving Gear
    create_region(world, "CanSmelt", "NetheriteDivingHelmet", {
        "Netherite Diving Helmet (Itemsanity) {Create}": ITEMSANITY
    }, lambda state: canSmelt(world, state) and canWearNetheriteArmor(world, state))

    # Has Enchanting
    create_region(world, "Menu", "HasEnchanting", {
        "Zinc Ore (Itemsanity) {Create}": ITEMSANITY,
        "Deepslate Zinc Ore (Itemsanity) {Create}": ITEMSANITY
    }, lambda state: canEnchant(world, state))

    # Has Swimming and Enchanting
    create_region(world, "HasEnchanting", "HasSwimAndEnchanting", {
        "Tree Fertilizer (Itemsanity) {Create}": ITEMSANITY
    }, lambda state: canSwim(world, state) and canEnchant(world, state))

    # Schematic
    create_region(world, "Menu", "Schematic", {
        "Empty Schematic (Itemsanity) {Create}": ITEMSANITY,
        "Schematic And Quill (Itemsanity) {Create}": ITEMSANITY
    }, lambda state: canDyeFull(world, state))

    ####################################################################################################################
    # STONE CUTTING AND SAW EXCLUSIVES #################################################################################
    ####################################################################################################################


    create_region(world, "Menu", "Cutting", {
        "Cut Granite (Itemsanity) {Create}": ITEMSANITY,
        "Cut Granite Stairs (Itemsanity) {Create}": STAIR,
        "Cut Granite Slab (Itemsanity) {Create}": SLAB,
        "Cut Granite Wall (Itemsanity) {Create}": WALL,
        "Polished Cut Granite (Itemsanity) {Create}": ITEMSANITY,
        "Polished Cut Granite Stairs (Itemsanity) {Create}": STAIR,
        "Polished Cut Granite Slab (Itemsanity) {Create}": SLAB,
        "Polished Cut Granite Wall (Itemsanity) {Create}": WALL,
        "Cut Granite Bricks (Itemsanity) {Create}": ITEMSANITY,
        "Cut Granite Brick Stairs (Itemsanity) {Create}": STAIR,
        "Cut Granite Brick Slab (Itemsanity) {Create}": SLAB,
        "Cut Granite Brick Wall (Itemsanity) {Create}": WALL,
        "Small Granite Bricks (Itemsanity) {Create}": ITEMSANITY,
        "Small Granite Brick Stairs (Itemsanity) {Create}": STAIR,
        "Small Granite Brick Slab (Itemsanity) {Create}": SLAB,
        "Small Granite Brick Wall (Itemsanity) {Create}": WALL,
        "Layered Granite (Itemsanity) {Create}": ITEMSANITY,
        "Granite Pillar (Itemsanity) {Create}": ITEMSANITY,
        "Cut Diorite (Itemsanity) {Create}": ITEMSANITY,
        "Cut Diorite Stairs (Itemsanity) {Create}": STAIR,
        "Cut Diorite Slab (Itemsanity) {Create}": SLAB,
        "Cut Diorite Wall (Itemsanity) {Create}": WALL,
        "Polished Cut Diorite (Itemsanity) {Create}": ITEMSANITY,
        "Polished Cut Diorite Stairs (Itemsanity) {Create}": STAIR,
        "Polished Cut Diorite Slab (Itemsanity) {Create}": SLAB,
        "Polished Cut Diorite Wall (Itemsanity) {Create}": WALL,
        "Cut Diorite Bricks (Itemsanity) {Create}": ITEMSANITY,
        "Cut Diorite Brick Stairs (Itemsanity) {Create}": STAIR,
        "Cut Diorite Brick Slab (Itemsanity) {Create}": SLAB,
        "Cut Diorite Brick Wall (Itemsanity) {Create}": WALL,
        "Small Diorite Bricks (Itemsanity) {Create}": ITEMSANITY,
        "Small Diorite Brick Stairs (Itemsanity) {Create}": STAIR,
        "Small Diorite Brick Slab (Itemsanity) {Create}": SLAB,
        "Small Diorite Brick Wall (Itemsanity) {Create}": WALL,
        "Layered Diorite (Itemsanity) {Create}": ITEMSANITY,
        "Diorite Pillar (Itemsanity) {Create}": ITEMSANITY,
        "Cut Andesite (Itemsanity) {Create}": ITEMSANITY,
        "Cut Andesite Stairs (Itemsanity) {Create}": STAIR,
        "Cut Andesite Slab (Itemsanity) {Create}": SLAB,
        "Cut Andesite Wall (Itemsanity) {Create}": WALL,
        "Polished Cut Andesite (Itemsanity) {Create}": ITEMSANITY,
        "Polished Cut Andesite Stairs (Itemsanity) {Create}": STAIR,
        "Polished Cut Andesite Slab (Itemsanity) {Create}": SLAB,
        "Polished Cut Andesite Wall (Itemsanity) {Create}": WALL,
        "Cut Andesite Bricks (Itemsanity) {Create}": ITEMSANITY,
        "Cut Andesite Brick Stairs (Itemsanity) {Create}": STAIR,
        "Cut Andesite Brick Slab (Itemsanity) {Create}": SLAB,
        "Cut Andesite Brick Wall (Itemsanity) {Create}": WALL,
        "Small Andesite Bricks (Itemsanity) {Create}": ITEMSANITY,
        "Small Andesite Brick Stairs (Itemsanity) {Create}": STAIR,
        "Small Andesite Brick Slab (Itemsanity) {Create}": SLAB,
        "Small Andesite Brick Wall (Itemsanity) {Create}": WALL,
        "Layered Andesite (Itemsanity) {Create}": ITEMSANITY,
        "Andesite Pillar (Itemsanity) {Create}": ITEMSANITY,
        "Cut Calcite (Itemsanity) {Create}": ITEMSANITY,
        "Cut Calcite Stairs (Itemsanity) {Create}": STAIR,
        "Cut Calcite Slab (Itemsanity) {Create}": SLAB,
        "Cut Calcite Wall (Itemsanity) {Create}": WALL,
        "Polished Cut Calcite (Itemsanity) {Create}": ITEMSANITY,
        "Polished Cut Calcite Stairs (Itemsanity) {Create}": STAIR,
        "Polished Cut Calcite Slab (Itemsanity) {Create}": SLAB,
        "Polished Cut Calcite Wall (Itemsanity) {Create}": WALL,
        "Cut Calcite Bricks (Itemsanity) {Create}": ITEMSANITY,
        "Cut Calcite Brick Stairs (Itemsanity) {Create}": STAIR,
        "Cut Calcite Brick Slab (Itemsanity) {Create}": SLAB,
        "Cut Calcite Brick Wall (Itemsanity) {Create}": WALL,
        "Small Calcite Bricks (Itemsanity) {Create}": ITEMSANITY,
        "Small Calcite Brick Stairs (Itemsanity) {Create}": STAIR,
        "Small Calcite Brick Slab (Itemsanity) {Create}": SLAB,
        "Small Calcite Brick Wall (Itemsanity) {Create}": WALL,
        "Layered Calcite (Itemsanity) {Create}": ITEMSANITY,
        "Calcite Pillar (Itemsanity) {Create}": ITEMSANITY,
        "Cut Dripstone (Itemsanity) {Create}": ITEMSANITY,
        "Cut Dripstone Stairs (Itemsanity) {Create}": STAIR,
        "Cut Dripstone Slab (Itemsanity) {Create}": SLAB,
        "Cut Dripstone Wall (Itemsanity) {Create}": WALL,
        "Polished Cut Dripstone (Itemsanity) {Create}": ITEMSANITY,
        "Polished Cut Dripstone Stairs (Itemsanity) {Create}": STAIR,
        "Polished Cut Dripstone Slab (Itemsanity) {Create}": SLAB,
        "Polished Cut Dripstone Wall (Itemsanity) {Create}": WALL,
        "Cut Dripstone Bricks (Itemsanity) {Create}": ITEMSANITY,
        "Cut Dripstone Brick Stairs (Itemsanity) {Create}": STAIR,
        "Cut Dripstone Brick Slab (Itemsanity) {Create}": SLAB,
        "Cut Dripstone Brick Wall (Itemsanity) {Create}": WALL,
        "Small Dripstone Bricks (Itemsanity) {Create}": ITEMSANITY,
        "Small Dripstone Brick Stairs (Itemsanity) {Create}": STAIR,
        "Small Dripstone Brick Slab (Itemsanity) {Create}": SLAB,
        "Small Dripstone Brick Wall (Itemsanity) {Create}": WALL,
        "Layered Dripstone (Itemsanity) {Create}": ITEMSANITY,
        "Dripstone Pillar (Itemsanity) {Create}": ITEMSANITY,
        "Cut Deepslate (Itemsanity) {Create}": ITEMSANITY,
        "Cut Deepslate Stairs (Itemsanity) {Create}": STAIR,
        "Cut Deepslate Slab (Itemsanity) {Create}": SLAB,
        "Cut Deepslate Wall (Itemsanity) {Create}": WALL,
        "Polished Cut Deepslate (Itemsanity) {Create}": ITEMSANITY,
        "Polished Cut Deepslate Stairs (Itemsanity) {Create}": STAIR,
        "Polished Cut Deepslate Slab (Itemsanity) {Create}": SLAB,
        "Polished Cut Deepslate Wall (Itemsanity) {Create}": WALL,
        "Cut Deepslate Bricks (Itemsanity) {Create}": ITEMSANITY,
        "Cut Deepslate Brick Stairs (Itemsanity) {Create}": STAIR,
        "Cut Deepslate Brick Slab (Itemsanity) {Create}": SLAB,
        "Cut Deepslate Brick Wall (Itemsanity) {Create}": WALL,
        "Small Deepslate Bricks (Itemsanity) {Create}": ITEMSANITY,
        "Small Deepslate Brick Stairs (Itemsanity) {Create}": STAIR,
        "Small Deepslate Brick Slab (Itemsanity) {Create}": SLAB,
        "Small Deepslate Brick Wall (Itemsanity) {Create}": WALL,
        "Layered Deepslate (Itemsanity) {Create}": ITEMSANITY,
        "Deepslate Pillar (Itemsanity) {Create}": ITEMSANITY,
        "Cut Tuff (Itemsanity) {Create}": ITEMSANITY,
        "Cut Tuff Stairs (Itemsanity) {Create}": STAIR,
        "Cut Tuff Slab (Itemsanity) {Create}": SLAB,
        "Cut Tuff Wall (Itemsanity) {Create}": WALL,
        "Polished Cut Tuff (Itemsanity) {Create}": ITEMSANITY,
        "Polished Cut Tuff Stairs (Itemsanity) {Create}": STAIR,
        "Polished Cut Tuff Slab (Itemsanity) {Create}": SLAB,
        "Polished Cut Tuff Wall (Itemsanity) {Create}": WALL,
        "Cut Tuff Bricks (Itemsanity) {Create}": ITEMSANITY,
        "Cut Tuff Brick Stairs (Itemsanity) {Create}": STAIR,
        "Cut Tuff Brick Slab (Itemsanity) {Create}": SLAB,
        "Cut Tuff Brick Wall (Itemsanity) {Create}": WALL,
        "Small Tuff Bricks (Itemsanity) {Create}": ITEMSANITY,
        "Small Tuff Brick Stairs (Itemsanity) {Create}": STAIR,
        "Small Tuff Brick Slab (Itemsanity) {Create}": SLAB,
        "Small Tuff Brick Wall (Itemsanity) {Create}": WALL,
        "Layered Tuff (Itemsanity) {Create}": ITEMSANITY,
        "Tuff Pillar (Itemsanity) {Create}": ITEMSANITY,
        "Cut Asurine (Itemsanity) {Create}": ITEMSANITY,
        "Cut Asurine Stairs (Itemsanity) {Create}": STAIR,
        "Cut Asurine Slab (Itemsanity) {Create}": SLAB,
        "Cut Asurine Wall (Itemsanity) {Create}": WALL,
        "Polished Cut Asurine (Itemsanity) {Create}": ITEMSANITY,
        "Polished Cut Asurine Stairs (Itemsanity) {Create}": STAIR,
        "Polished Cut Asurine Slab (Itemsanity) {Create}": SLAB,
        "Polished Cut Asurine Wall (Itemsanity) {Create}": WALL,
        "Cut Asurine Bricks (Itemsanity) {Create}": ITEMSANITY,
        "Cut Asurine Brick Stairs (Itemsanity) {Create}": STAIR,
        "Cut Asurine Brick Slab (Itemsanity) {Create}": SLAB,
        "Cut Asurine Brick Wall (Itemsanity) {Create}": WALL,
        "Small Asurine Bricks (Itemsanity) {Create}": ITEMSANITY,
        "Small Asurine Brick Stairs (Itemsanity) {Create}": STAIR,
        "Small Asurine Brick Slab (Itemsanity) {Create}": SLAB,
        "Small Asurine Brick Wall (Itemsanity) {Create}": WALL,
        "Layered Asurine (Itemsanity) {Create}": ITEMSANITY,
        "Asurine Pillar (Itemsanity) {Create}": ITEMSANITY,
        "Cut Crimsite (Itemsanity) {Create}": ITEMSANITY,
        "Cut Crimsite Stairs (Itemsanity) {Create}": STAIR,
        "Cut Crimsite Slab (Itemsanity) {Create}": SLAB,
        "Cut Crimsite Wall (Itemsanity) {Create}": WALL,
        "Polished Cut Crimsite (Itemsanity) {Create}": ITEMSANITY,
        "Polished Cut Crimsite Stairs (Itemsanity) {Create}": STAIR,
        "Polished Cut Crimsite Slab (Itemsanity) {Create}": SLAB,
        "Polished Cut Crimsite Wall (Itemsanity) {Create}": WALL,
        "Cut Crimsite Bricks (Itemsanity) {Create}": ITEMSANITY,
        "Cut Crimsite Brick Stairs (Itemsanity) {Create}": STAIR,
        "Cut Crimsite Brick Slab (Itemsanity) {Create}": SLAB,
        "Cut Crimsite Brick Wall (Itemsanity) {Create}": WALL,
        "Small Crimsite Bricks (Itemsanity) {Create}": ITEMSANITY,
        "Small Crimsite Brick Stairs (Itemsanity) {Create}": STAIR,
        "Small Crimsite Brick Slab (Itemsanity) {Create}": SLAB,
        "Small Crimsite Brick Wall (Itemsanity) {Create}": WALL,
        "Layered Crimsite (Itemsanity) {Create}": ITEMSANITY,
        "Crimsite Pillar (Itemsanity) {Create}": ITEMSANITY,
        "Cut Limestone (Itemsanity) {Create}": ITEMSANITY,
        "Cut Limestone Stairs (Itemsanity) {Create}": STAIR,
        "Cut Limestone Slab (Itemsanity) {Create}": SLAB,
        "Cut Limestone Wall (Itemsanity) {Create}": WALL,
        "Polished Cut Limestone (Itemsanity) {Create}": ITEMSANITY,
        "Polished Cut Limestone Stairs (Itemsanity) {Create}": STAIR,
        "Polished Cut Limestone Slab (Itemsanity) {Create}": SLAB,
        "Polished Cut Limestone Wall (Itemsanity) {Create}": WALL,
        "Cut Limestone Bricks (Itemsanity) {Create}": ITEMSANITY,
        "Cut Limestone Brick Stairs (Itemsanity) {Create}": STAIR,
        "Cut Limestone Brick Slab (Itemsanity) {Create}": SLAB,
        "Cut Limestone Brick Wall (Itemsanity) {Create}": WALL,
        "Small Limestone Bricks (Itemsanity) {Create}": ITEMSANITY,
        "Small Limestone Brick Stairs (Itemsanity) {Create}": STAIR,
        "Small Limestone Brick Slab (Itemsanity) {Create}": SLAB,
        "Small Limestone Brick Wall (Itemsanity) {Create}": WALL,
        "Layered Limestone (Itemsanity) {Create}": ITEMSANITY,
        "Limestone Pillar (Itemsanity) {Create}": ITEMSANITY,
        "Cut Ochrum (Itemsanity) {Create}": ITEMSANITY,
        "Cut Ochrum Stairs (Itemsanity) {Create}": STAIR,
        "Cut Ochrum Slab (Itemsanity) {Create}": SLAB,
        "Cut Ochrum Wall (Itemsanity) {Create}": WALL,
        "Polished Cut Ochrum (Itemsanity) {Create}": ITEMSANITY,
        "Polished Cut Ochrum Stairs (Itemsanity) {Create}": STAIR,
        "Polished Cut Ochrum Slab (Itemsanity) {Create}": SLAB,
        "Polished Cut Ochrum Wall (Itemsanity) {Create}": WALL,
        "Cut Ochrum Bricks (Itemsanity) {Create}": ITEMSANITY,
        "Cut Ochrum Brick Stairs (Itemsanity) {Create}": STAIR,
        "Cut Ochrum Brick Slab (Itemsanity) {Create}": SLAB,
        "Cut Ochrum Brick Wall (Itemsanity) {Create}": WALL,
        "Small Ochrum Bricks (Itemsanity) {Create}": ITEMSANITY,
        "Small Ochrum Brick Stairs (Itemsanity) {Create}": STAIR,
        "Small Ochrum Brick Slab (Itemsanity) {Create}": SLAB,
        "Small Ochrum Brick Wall (Itemsanity) {Create}": WALL,
        "Layered Ochrum (Itemsanity) {Create}": ITEMSANITY,
        "Ochrum Pillar (Itemsanity) {Create}": ITEMSANITY,
        "Cut Veridium (Itemsanity) {Create}": ITEMSANITY,
        "Cut Veridium Stairs (Itemsanity) {Create}": STAIR,
        "Cut Veridium Slab (Itemsanity) {Create}": SLAB,
        "Cut Veridium Wall (Itemsanity) {Create}": WALL,
        "Polished Cut Veridium (Itemsanity) {Create}": ITEMSANITY,
        "Polished Cut Veridium Stairs (Itemsanity) {Create}": STAIR,
        "Polished Cut Veridium Slab (Itemsanity) {Create}": SLAB,
        "Polished Cut Veridium Wall (Itemsanity) {Create}": WALL,
        "Cut Veridium Bricks (Itemsanity) {Create}": ITEMSANITY,
        "Cut Veridium Brick Stairs (Itemsanity) {Create}": STAIR,
        "Cut Veridium Brick Slab (Itemsanity) {Create}": SLAB,
        "Cut Veridium Brick Wall (Itemsanity) {Create}": WALL,
        "Small Veridium Bricks (Itemsanity) {Create}": ITEMSANITY,
        "Small Veridium Brick Stairs (Itemsanity) {Create}": STAIR,
        "Small Veridium Brick Slab (Itemsanity) {Create}": SLAB,
        "Small Veridium Brick Wall (Itemsanity) {Create}": WALL,
        "Layered Veridium (Itemsanity) {Create}": ITEMSANITY,
        "Veridium Pillar (Itemsanity) {Create}": ITEMSANITY,
    }, lambda state: canCraftSPDecorativeStone(world, state))

    # Has Smelting
    create_region(world, "CanSmelt", "SmeltAndCutting", {
        "Copper Table Cover (Itemsanity) {Create}": ITEMSANITY,
        "Copper Ladder (Itemsanity) {Create}": ITEMSANITY,
        "Copper Bars (Itemsanity) {Create}": ITEMSANITY,
        "Copper Scaffolding (Itemsanity) {Create}": ITEMSANITY,
        "Framed Glass Door (Itemsanity) {Create}": ITEMSANITY,
        "Framed Glass Trapdoor (Itemsanity) {Create}": ITEMSANITY,
        "Block of Industrial Iron (Itemsanity) {Create}": ITEMSANITY,
        "Block of Weathered Iron (Itemsanity) {Create}": ITEMSANITY,
        "Copper Shingles (Itemsanity) {Create}": ITEMSANITY,
        "Exposed Copper Shingles (Itemsanity) {Create}": ITEMSANITY,
        "Weathered Copper Shingles (Itemsanity) {Create}": ITEMSANITY,
        "Oxidized Copper Shingles (Itemsanity) {Create}": ITEMSANITY,
        "Copper Shingle Slab (Itemsanity) {Create}": SLAB,
        "Exposed Copper Shingle Slab (Itemsanity) {Create}": SLAB,
        "Weathered Copper Shingle Slab (Itemsanity) {Create}": SLAB,
        "Oxidized Copper Shingle Slab (Itemsanity) {Create}": SLAB,
        "Copper Shingle Stairs (Itemsanity) {Create}": STAIR,
        "Exposed Copper Shingle Stairs (Itemsanity) {Create}": STAIR,
        "Weathered Copper Shingle Stairs (Itemsanity) {Create}": STAIR,
        "Oxidized Copper Shingle Stairs (Itemsanity) {Create}": STAIR,
        "Waxed Copper Shingles (Itemsanity) {Create}": ITEMSANITY,
        "Waxed Exposed Copper Shingles (Itemsanity) {Create}": ITEMSANITY,
        "Waxed Weathered Copper Shingles (Itemsanity) {Create}": ITEMSANITY,
        "Waxed Oxidized Copper Shingles (Itemsanity) {Create}": ITEMSANITY,
        "Waxed Copper Shingle Slab (Itemsanity) {Create}": SLAB,
        "Waxed Exposed Copper Shingle Slab (Itemsanity) {Create}": SLAB,
        "Waxed Weathered Copper Shingle Slab (Itemsanity) {Create}": SLAB,
        "Waxed Oxidized Copper Shingle Slab (Itemsanity) {Create}": SLAB,
        "Waxed Copper Shingle Stairs (Itemsanity) {Create}": STAIR,
        "Waxed Exposed Copper Shingle Stairs (Itemsanity) {Create}": STAIR,
        "Waxed Weathered Copper Shingle Stairs (Itemsanity) {Create}": STAIR,
        "Waxed Oxidized Copper Shingle Stairs (Itemsanity) {Create}": STAIR,
        "Copper Tiles (Itemsanity) {Create}": ITEMSANITY,
        "Exposed Copper Tiles (Itemsanity) {Create}": ITEMSANITY,
        "Weathered Copper Tiles (Itemsanity) {Create}": ITEMSANITY,
        "Oxidized Copper Tiles (Itemsanity) {Create}": ITEMSANITY,
        "Copper Tile Slab (Itemsanity) {Create}": SLAB,
        "Exposed Copper Tile Slab (Itemsanity) {Create}": SLAB,
        "Weathered Copper Tile Slab (Itemsanity) {Create}": SLAB,
        "Oxidized Copper Tile Slab (Itemsanity) {Create}": SLAB,
        "Copper Tile Stairs (Itemsanity) {Create}": STAIR,
        "Exposed Copper Tile Stairs (Itemsanity) {Create}": STAIR,
        "Weathered Copper Tile Stairs (Itemsanity) {Create}": STAIR,
        "Oxidized Copper Tile Stairs (Itemsanity) {Create}": STAIR,
        "Waxed Copper Tiles (Itemsanity) {Create}": ITEMSANITY,
        "Waxed Exposed Copper Tiles (Itemsanity) {Create}": ITEMSANITY,
        "Waxed Weathered Copper Tiles (Itemsanity) {Create}": ITEMSANITY,
        "Waxed Oxidized Copper Tiles (Itemsanity) {Create}": ITEMSANITY,
        "Waxed Copper Tile Slab (Itemsanity) {Create}": SLAB,
        "Waxed Exposed Copper Tile Slab (Itemsanity) {Create}": SLAB,
        "Waxed Weathered Copper Tile Slab (Itemsanity) {Create}": SLAB,
        "Waxed Oxidized Copper Tile Slab (Itemsanity) {Create}": SLAB,
        "Waxed Copper Tile Stairs (Itemsanity) {Create}": STAIR,
        "Waxed Exposed Copper Tile Stairs (Itemsanity) {Create}": STAIR,
        "Waxed Weathered Copper Tile Stairs (Itemsanity) {Create}": STAIR,
        "Waxed Oxidized Copper Tile Stairs (Itemsanity) {Create}": STAIR,
        "Tiled Glass (Itemsanity) {Create}": ITEMSANITY,
        "Framed Glass (Itemsanity) {Create}": ITEMSANITY,
        "Horizontal Framed Glass (Itemsanity) {Create}": ITEMSANITY,
        "Vertical Framed Glass (Itemsanity) {Create}": ITEMSANITY,
        "Tiled Glass Pane (Itemsanity) {Create}": ITEMSANITY,
        "Framed Glass Pane (Itemsanity) {Create}": ITEMSANITY,
        "Horizontal Framed Glass Pane (Itemsanity) {Create}": ITEMSANITY,
        "Vertical Framed Glass Pane (Itemsanity) {Create}": ITEMSANITY,
        "Industrial Iron Window (Itemsanity) {Create}": ITEMSANITY,
        "Weathered Iron Window (Itemsanity) {Create}": ITEMSANITY,
        "Industrial Iron Window Pane (Itemsanity) {Create}": ITEMSANITY,
        "Weathered Iron Window Pane (Itemsanity) {Create}": ITEMSANITY,
    }, lambda state: canSmelt(world, state) and canCraftSPDecorativeStone(world, state))

    # Has Nether Access
    create_region(world, "NetherAccess", "NetherAccessAndCutting", {
        "Cut Scoria (Itemsanity) {Create}": ITEMSANITY,
        "Cut Scoria Stairs (Itemsanity) {Create}": STAIR,
        "Cut Scoria Slab (Itemsanity) {Create}": SLAB,
        "Cut Scoria Wall (Itemsanity) {Create}": WALL,
        "Polished Cut Scoria (Itemsanity) {Create}": ITEMSANITY,
        "Polished Cut Scoria Stairs (Itemsanity) {Create}": STAIR,
        "Polished Cut Scoria Slab (Itemsanity) {Create}": SLAB,
        "Polished Cut Scoria Wall (Itemsanity) {Create}": WALL,
        "Cut Scoria Bricks (Itemsanity) {Create}": ITEMSANITY,
        "Cut Scoria Brick Stairs (Itemsanity) {Create}": STAIR,
        "Cut Scoria Brick Slab (Itemsanity) {Create}": SLAB,
        "Cut Scoria Brick Wall (Itemsanity) {Create}": WALL,
        "Small Scoria Bricks (Itemsanity) {Create}": ITEMSANITY,
        "Small Scoria Brick Stairs (Itemsanity) {Create}": STAIR,
        "Small Scoria Brick Slab (Itemsanity) {Create}": SLAB,
        "Small Scoria Brick Wall (Itemsanity) {Create}": WALL,
        "Layered Scoria (Itemsanity) {Create}": ITEMSANITY,
        "Scoria Pillar (Itemsanity) {Create}": ITEMSANITY,
        "Cut Scorchia (Itemsanity) {Create}": ITEMSANITY,
        "Cut Scorchia Stairs (Itemsanity) {Create}": STAIR,
        "Cut Scorchia Slab (Itemsanity) {Create}": SLAB,
        "Cut Scorchia Wall (Itemsanity) {Create}": WALL,
        "Polished Cut Scorchia (Itemsanity) {Create}": ITEMSANITY,
        "Polished Cut Scorchia Stairs (Itemsanity) {Create}": STAIR,
        "Polished Cut Scorchia Slab (Itemsanity) {Create}": SLAB,
        "Polished Cut Scorchia Wall (Itemsanity) {Create}": WALL,
        "Cut Scorchia Bricks (Itemsanity) {Create}": ITEMSANITY,
        "Cut Scorchia Brick Stairs (Itemsanity) {Create}": STAIR,
        "Cut Scorchia Brick Slab (Itemsanity) {Create}": SLAB,
        "Cut Scorchia Brick Wall (Itemsanity) {Create}": WALL,
        "Small Scorchia Bricks (Itemsanity) {Create}": ITEMSANITY,
        "Small Scorchia Brick Stairs (Itemsanity) {Create}": STAIR,
        "Small Scorchia Brick Slab (Itemsanity) {Create}": SLAB,
        "Small Scorchia Brick Wall (Itemsanity) {Create}": WALL,
        "Layered Scorchia (Itemsanity) {Create}": ITEMSANITY,
        "Scorchia Pillar (Itemsanity) {Create}": ITEMSANITY,
    }, lambda state: canAccessNether(world, state) and canCraftSPDecorativeStone(world, state))

    # Has Rose Quartz
    create_region(world, "RoseQuartz", "RoseQuartzAndCutting", {
        "Block of Rose Quartz (Itemsanity) {Create}": ITEMSANITY
    }, lambda state: canCraftRoseQuartz(world, state) and canCraftSPDecorativeStone(world, state))

    # Has Rose Quartz And Sandpaper
    create_region(world, "RoseQuartz", "RoseQuartzAndCuttingAndSandpaper", {
        "Rose Quartz Tiles (Itemsanity) {Create}": ITEMSANITY,
        "Small Rose Quartz Tiles (Itemsanity) {Create}": ITEMSANITY,
    }, lambda state: canCraftRoseQuartz(world, state) and canCraftSPDecorativeStone(world, state) and canUseSandpaper(world, state))

    # Has Zinc
    create_region(world, "Zinc", "ZincCutting", {
        "Copycat Step (Itemsanity) {Create}": ITEMSANITY,
        "Copycat Panel (Itemsanity) {Create}": ITEMSANITY,
    }, lambda state: canGetZinc(world, state) and canCraftSPDecorativeStone(world, state))

    # Has Andesite Alloy
    create_region(world, "AndesiteAlloy", "AndesiteAlloyCutting", {
        "Andesite Table Cover (Itemsanity) {Create}": ITEMSANITY,
        "Andesite Ladder (Itemsanity) {Create}": ITEMSANITY,
        "Andesite Bars (Itemsanity) {Create}": ITEMSANITY,
        "Andesite Scaffolding (Itemsanity) {Create}": ITEMSANITY,
    }, lambda state: canCraftAndesiteAlloy(world, state) and canCraftSPDecorativeStone(world, state))

    # Has Brass
    create_region(world, "Brass", "BrassCutting", {
        "Brass Table Cover (Itemsanity) {Create}": ITEMSANITY,
        "Brass Ladder (Itemsanity) {Create}": ITEMSANITY,
        "Brass Bars (Itemsanity) {Create}": ITEMSANITY,
        "Brass Scaffolding (Itemsanity) {Create}": ITEMSANITY,
    }, lambda state: canCraftBrass(world, state) and canCraftSPDecorativeStone(world, state))

    ####################################################################################################################
    # DYED ITEMS #######################################################################################################
    ####################################################################################################################

    # Regular Dye and Press
    create_region(world, "AndesiteAlloy", "RegularDyeAndPress", {
        "Red Valve Handle (Itemsanity) {Create}": DYE,
        "Yellow Valve Handle (Itemsanity) {Create}": DYE,
        "Blue Valve Handle (Itemsanity) {Create}": DYE,
        "White Valve Handle (Itemsanity) {Create}": DYE
    }, lambda state: canDyeBasic(world, state) and hasPress(world, state))

    # Black Dye and Press
    create_region(world, "AndesiteAlloy", "BlackDyeAndPress", {
        "Black Valve Handle (Itemsanity) {Create}": DYE,
        "Gray Valve Handle (Itemsanity) {Create}": DYE
    }, lambda state: canDyeBlack(world, state) and hasPress(world, state))

    # Green Dye and Press
    create_region(world, "AndesiteAlloy", "GreenDyeAndPress", {
        "Green Valve Handle (Itemsanity) {Create}": DYE_AND_EXPLORATION
    }, lambda state: hasPress(world, state) and canDyeGreen(world, state))

    # Full Dye and Press
    create_region(world, "AndesiteAlloy", "FullDyeAndPress", {
        "Orange Valve Handle (Itemsanity) {Create}": DYE,
        "Light Blue Valve Handle (Itemsanity) {Create}": DYE,
        "Purple Valve Handle (Itemsanity) {Create}": DYE,
        "Light Gray Valve Handle (Itemsanity) {Create}": DYE,
        "Brown Valve Handle (Itemsanity) {Create}": DYE_AND_EXPLORATION,
        "Pink Valve Handle (Itemsanity) {Create}": DYE,
        "Magenta Valve Handle (Itemsanity) {Create}": DYE
    }, lambda state: canDyeFull(world, state) and hasPress(world, state))

    # Lime and Cyan Dye and Press
    create_region(world, "AndesiteAlloy", "LimeAndCyanDyeAndPress", {
        "Lime Valve Handle (Itemsanity) {Create}": DYE_AND_EXPLORATION,
        "Cyan Valve Handle (Itemsanity) {Create}": DYE_AND_EXPLORATION
    }, lambda state: canDyeFull(world, state) and hasPress(world, state) and canDyeGreen(world, state))




    # Regular Dye and Storage
    create_region(world, "AndesiteAlloy", "RegularDyeAndStorageAndAlloy", {
        "Red Postbox (Itemsanity) {Create}": DYE,
        "Yellow Postbox (Itemsanity) {Create}": DYE,
        "Blue Postbox (Itemsanity) {Create}": DYE,
        "White Postbox (Itemsanity) {Create}": DYE
    }, lambda state: canDyeBasic(world, state) and canAccessChests(world, state))

    # Black Dye and Storage
    create_region(world, "AndesiteAlloy", "BlackDyeAndStorageAndAlloy", {
        "Black Postbox (Itemsanity) {Create}": DYE,
        "Gray Postbox (Itemsanity) {Create}": DYE
    }, lambda state: canDyeBlack(world, state) and canAccessChests(world, state))

    # Green Dye and Storage
    create_region(world, "AndesiteAlloy", "GreenDyeAndStorageAndAlloy", {
        "Green Postbox (Itemsanity) {Create}": DYE_AND_EXPLORATION
    }, lambda state: canAccessChests(world, state) and canDyeGreen(world, state))

    # Full Dye and Storage
    create_region(world, "AndesiteAlloy", "FullDyeAndStorageAndAlloy", {
        "Orange Postbox (Itemsanity) {Create}": DYE,
        "Light Blue Postbox (Itemsanity) {Create}": DYE,
        "Purple Postbox (Itemsanity) {Create}": DYE,
        "Light Gray Postbox (Itemsanity) {Create}": DYE,
        "Brown Postbox (Itemsanity) {Create}": DYE_AND_EXPLORATION,
        "Pink Postbox (Itemsanity) {Create}": DYE,
        "Magenta Postbox (Itemsanity) {Create}": DYE
    }, lambda state: canDyeFull(world, state) and canAccessChests(world, state))

    # Lime and Cyan Dye and Storage
    create_region(world, "AndesiteAlloy", "LimeAndCyanDyeAndStorageAndAlloy", {
        "Lime Postbox (Itemsanity) {Create}": DYE_AND_EXPLORATION,
        "Cyan Postbox (Itemsanity) {Create}": DYE_AND_EXPLORATION
    }, lambda state: canDyeFull(world, state) and canAccessChests(world, state) and canDyeGreen(world, state))


    # Regular Dye
    create_region(world, "AndesiteAlloy", "RegularDye", {
        "Red Table Cloth (Itemsanity) {Create}": DYE,
        "Yellow Table Cloth (Itemsanity) {Create}": DYE,
        "Blue Table Cloth (Itemsanity) {Create}": DYE,
        "White Table Cloth (Itemsanity) {Create}": DYE,

        "Red Seat (Itemsanity) {Create}": DYE,
        "Yellow Seat (Itemsanity) {Create}": DYE,
        "Blue Seat (Itemsanity) {Create}": DYE,
        "White Seat (Itemsanity) {Create}": DYE
    }, lambda state: canDyeBasic(world, state))

    # Black Dye
    create_region(world, "AndesiteAlloy", "BlackDye", {
        "Black Table Cloth (Itemsanity) {Create}": DYE,
        "Gray Table Cloth (Itemsanity) {Create}": DYE,

        "Black Seat (Itemsanity) {Create}": DYE,
        "Gray Seat (Itemsanity) {Create}": DYE
    }, lambda state: canDyeBlack(world, state))

    # Green Dye
    create_region(world, "AndesiteAlloy", "GreenDye", {
        "Green Table Cloth (Itemsanity) {Create}": DYE_AND_EXPLORATION,
        "Green Seat (Itemsanity) {Create}": DYE_AND_EXPLORATION,
    }, lambda state: canDyeGreen(world, state))

    # Full Dye
    create_region(world, "AndesiteAlloy", "FullDye", {
        "Orange Table Cloth (Itemsanity) {Create}": DYE,
        "Light Blue Table Cloth (Itemsanity) {Create}": DYE,
        "Purple Table Cloth (Itemsanity) {Create}": DYE,
        "Light Gray Table Cloth (Itemsanity) {Create}": DYE,
        "Brown Table Cloth (Itemsanity) {Create}": DYE_AND_EXPLORATION,
        "Pink Table Cloth (Itemsanity) {Create}": DYE,
        "Magenta Table Cloth (Itemsanity) {Create}": DYE,

        "Orange Seat (Itemsanity) {Create}": DYE,
        "Light Blue Seat (Itemsanity) {Create}": DYE,
        "Purple Seat (Itemsanity) {Create}": DYE,
        "Light Gray Seat (Itemsanity) {Create}": DYE,
        "Brown Seat (Itemsanity) {Create}": DYE_AND_EXPLORATION,
        "Pink Seat (Itemsanity) {Create}": DYE,
        "Magenta Seat (Itemsanity) {Create}": DYE
    }, lambda state: canDyeFull(world, state))

    # Lime and Cyan Dye
    create_region(world, "AndesiteAlloy", "LimeAndCyanDye", {
        "Lime Table Cloth (Itemsanity) {Create}": DYE_AND_EXPLORATION,
        "Cyan Table Cloth (Itemsanity) {Create}": DYE_AND_EXPLORATION,

        "Lime Seat (Itemsanity) {Create}": DYE_AND_EXPLORATION,
        "Cyan Seat (Itemsanity) {Create}": DYE_AND_EXPLORATION
    }, lambda state: canDyeFull(world, state) and canDyeGreen(world, state))


    # Regular Dye and Press And Storage And Gold
    create_region(world, "AndesiteAlloy", "RegularDyeAndPressAndStorageAndGold", {
        "Red Toolbox (Itemsanity) {Create}": DYE,
        "Yellow Toolbox (Itemsanity) {Create}": DYE,
        "Blue Toolbox (Itemsanity) {Create}": DYE,
        "White Toolbox (Itemsanity) {Create}": DYE
    }, lambda state: canDyeBasic(world, state) and hasPress(world, state) and canAccessChests(world, state) and canGetGold(world, state))

    # Black Dye and Press And Storage And Gold
    create_region(world, "AndesiteAlloy", "BlackDyeAndPressAndStorageAndGold", {
        "Black Toolbox (Itemsanity) {Create}": DYE,
        "Gray Toolbox (Itemsanity) {Create}": DYE
    }, lambda state: canDyeBlack(world, state) and hasPress(world, state) and canAccessChests(world, state) and canGetGold(world, state))

    # Green Dye and Press And Storage And Gold
    create_region(world, "AndesiteAlloy", "GreenDyeAndPressAndStorageAndGold", {
        "Green Toolbox (Itemsanity) {Create}": DYE_AND_EXPLORATION
    }, lambda state: hasPress(world, state) and canDyeGreen(world, state) and canAccessChests(world, state) and canGetGold(world, state))

    # Full Dye and Press And Storage And Gold
    create_region(world, "AndesiteAlloy", "FullDyeAndPressAndStorageAndGold", {
        "Orange Toolbox (Itemsanity) {Create}": DYE,
        "Light Blue Toolbox (Itemsanity) {Create}": DYE,
        "Purple Toolbox (Itemsanity) {Create}": DYE,
        "Light Gray Toolbox (Itemsanity) {Create}": DYE,
        "Brown Toolbox (Itemsanity) {Create}": DYE_AND_EXPLORATION,
        "Pink Toolbox (Itemsanity) {Create}": DYE,
        "Magenta Toolbox (Itemsanity) {Create}": DYE
    }, lambda state: canDyeFull(world, state) and hasPress(world, state) and canAccessChests(world, state) and canGetGold(world, state))

    # Lime and Cyan Dye and Press And Storage And Gold
    create_region(world, "AndesiteAlloy", "LimeAndCyanDyeAndPressAndStorageAndGold", {
        "Lime Toolbox (Itemsanity) {Create}": DYE_AND_EXPLORATION,
        "Cyan Toolbox (Itemsanity) {Create}": DYE_AND_EXPLORATION
    }, lambda state: canDyeFull(world, state) and hasPress(world, state) and canDyeGreen(world, state) and canAccessChests(world, state) and canGetGold(world, state))



def create_region(world: FabricMinecraftWorld, region_name: str, new_region_name: str, locations: dict[str, int], rule=None):
    create_locations_and_connect(world, region_name + "CreateItemsanity", new_region_name + "CreateItemsanity", locations, rule)