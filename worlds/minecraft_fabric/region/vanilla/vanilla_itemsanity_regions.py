from __future__ import annotations


from typing import TYPE_CHECKING, Optional

from worlds.minecraft_fabric.region.mc_regions_consts import *
from worlds.minecraft_fabric.region.regions_helper import create_locations_and_connect
from worlds.minecraft_fabric.logic.vanilla_logic import *



if TYPE_CHECKING:
   from worlds.minecraft_fabric import FabricMinecraftWorld

def create_vanilla_itemsanity_regions(world: FabricMinecraftWorld):
    create_locations_and_connect(world, "Menu", "MenuVanillaItemsanity", {
        "Dirt (Itemsanity)": ITEMSANITY,
        "Coarse Dirt (Itemsanity)": ITEMSANITY,
        "Rooted Dirt (Itemsanity)": ITEMSANITY,
        "Oak Planks (Itemsanity)": ITEMSANITY,
        "Spruce Planks (Itemsanity)": ITEMSANITY,
        "Birch Planks (Itemsanity)": ITEMSANITY,
        "Acacia Planks (Itemsanity)": ITEMSANITY,
        "Oak Sapling (Itemsanity)": ITEMSANITY,
        "Spruce Sapling (Itemsanity)": ITEMSANITY,
        "Birch Sapling (Itemsanity)": ITEMSANITY,
        "Acacia Sapling (Itemsanity)": ITEMSANITY,
        "Sand (Itemsanity)": ITEMSANITY,
        "Gravel (Itemsanity)": ITEMSANITY,
        "Oak Log (Itemsanity)": ITEMSANITY,
        "Spruce Log (Itemsanity)": ITEMSANITY,
        "Birch Log (Itemsanity)": ITEMSANITY,
        "Acacia Log (Itemsanity)": ITEMSANITY,
        "Stripped Oak Log (Itemsanity)": ITEMSANITY,
        "Stripped Spruce Log (Itemsanity)": ITEMSANITY,
        "Stripped Birch Log (Itemsanity)": ITEMSANITY,
        "Stripped Acacia Log (Itemsanity)": ITEMSANITY,
        "Stripped Oak Wood (Itemsanity)": ITEMSANITY,
        "Stripped Spruce Wood (Itemsanity)": ITEMSANITY,
        "Stripped Birch Wood (Itemsanity)": ITEMSANITY,
        "Stripped Acacia Wood (Itemsanity)": ITEMSANITY,
        "Oak Wood (Itemsanity)": ITEMSANITY,
        "Spruce Wood (Itemsanity)": ITEMSANITY,
        "Birch Wood (Itemsanity)": ITEMSANITY,
        "Acacia Wood (Itemsanity)": ITEMSANITY,
        "Sandstone (Itemsanity)": ITEMSANITY,
        "Chiseled Sandstone (Itemsanity)": ITEMSANITY,
        "Cut Sandstone (Itemsanity)": ITEMSANITY,
        "Dandelion (Itemsanity)": FLOWER,
        "Poppy (Itemsanity)": FLOWER,
        "Allium (Itemsanity)": FLOWER,
        "Azure Bluet (Itemsanity)": FLOWER,
        "Red Tulip (Itemsanity)": FLOWER,
        "Orange Tulip (Itemsanity)": FLOWER,
        "White Tulip (Itemsanity)": FLOWER,
        "Pink Tulip (Itemsanity)": FLOWER,
        "Oxeye Daisy (Itemsanity)": FLOWER,
        "Cornflower (Itemsanity)": FLOWER,
        "Lily of the Valley (Itemsanity)": FLOWER,
        "Brown Mushroom (Itemsanity)": ITEMSANITY,
        "Red Mushroom (Itemsanity)": ITEMSANITY,
        "Sugar Cane (Itemsanity)": ITEMSANITY,
        "Oak Slab (Itemsanity)": SLAB,
        "Spruce Slab (Itemsanity)": SLAB,
        "Birch Slab (Itemsanity)": SLAB,
        "Acacia Slab (Itemsanity)": SLAB,
        "Chiseled Bookshelf (Itemsanity)": ITEMSANITY,
        "Torch (Itemsanity)": ITEMSANITY,
        "Crafting Table (Itemsanity)": ITEMSANITY,
        "Ladder (Itemsanity)": ITEMSANITY,
        "Granite (Itemsanity)": ITEMSANITY,
        "Polished Granite (Itemsanity)": ITEMSANITY,
        "Diorite (Itemsanity)": ITEMSANITY,
        "Polished Diorite (Itemsanity)": ITEMSANITY,
        "Andesite (Itemsanity)": ITEMSANITY,
        "Polished Andesite (Itemsanity)": ITEMSANITY,
        "Cobbled Deepslate (Itemsanity)": ITEMSANITY,
        "Polished Deepslate (Itemsanity)": ITEMSANITY,
        "Calcite (Itemsanity)": ITEMSANITY,
        "Tuff (Itemsanity)": ITEMSANITY,
        "Dripstone Block (Itemsanity)": ITEMSANITY,
        "Cobblestone (Itemsanity)": ITEMSANITY,
        "Block of Amethyst (Itemsanity)": ITEMSANITY,
        "Moss Carpet (Itemsanity)": ITEMSANITY,
        "Moss Block (Itemsanity)": ITEMSANITY,
        "Big Dripleaf (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Spore Blossom (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Azalea (Itemsanity)": ITEMSANITY,
        "Flowering Azalea (Itemsanity)": ITEMSANITY,
        "Sandstone Slab (Itemsanity)": SLAB,
        "Cut Sandstone Slab (Itemsanity)": SLAB,
        "Cobblestone Slab (Itemsanity)": SLAB,
        "Cobblestone Stairs (Itemsanity)": STAIR,
        "Snow (Itemsanity)": ITEMSANITY,
        "Snow Block (Itemsanity)": ITEMSANITY,
        "Clay (Itemsanity)": ITEMSANITY,
        "Oak Fence (Itemsanity)": WALL,
        "Spruce Fence (Itemsanity)": WALL,
        "Birch Fence (Itemsanity)": WALL,
        "Acacia Fence (Itemsanity)": WALL,
        "Pumpkin (Itemsanity)": ITEMSANITY,
        "Deepslate Bricks (Itemsanity)": ITEMSANITY,
        "Deepslate Tiles (Itemsanity)": ITEMSANITY,
        "Chiseled Deepslate (Itemsanity)": ITEMSANITY,
        "Melon (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Sandstone Stairs (Itemsanity)": STAIR,
        "Oak Stairs (Itemsanity)": STAIR,
        "Spruce Stairs (Itemsanity)": STAIR,
        "Birch Stairs (Itemsanity)": STAIR,
        "Acacia Stairs (Itemsanity)": STAIR,
        "Cobblestone Wall (Itemsanity)": WALL,
        "Granite Wall (Itemsanity)": WALL,
        "Andesite Wall (Itemsanity)": WALL,
        "Sandstone Wall (Itemsanity)": WALL,
        "Diorite Wall (Itemsanity)": WALL,
        "Cobbled Deepslate Wall (Itemsanity)": WALL,
        "Polished Deepslate Wall (Itemsanity)": WALL,
        "Deepslate Brick Wall (Itemsanity)": WALL,
        "Deepslate Tile Wall (Itemsanity)": WALL,
        "Hay Bale (Itemsanity)": ITEMSANITY,
        "Lilac (Itemsanity)": FLOWER,
        "Rose Bush (Itemsanity)": FLOWER,
        "Peony (Itemsanity)": FLOWER,
        "Bone Block (Itemsanity)": ITEMSANITY,
        "Polished Granite Stairs (Itemsanity)": STAIR,
        "Polished Diorite Stairs (Itemsanity)": STAIR,
        "Granite Stairs (Itemsanity)": STAIR,
        "Andesite Stairs (Itemsanity)": STAIR,
        "Polished Andesite Stairs (Itemsanity)": STAIR,
        "Diorite Stairs (Itemsanity)": STAIR,
        "Cobbled Deepslate Stairs (Itemsanity)": STAIR,
        "Polished Deepslate Stairs (Itemsanity)": STAIR,
        "Deepslate Brick Stairs (Itemsanity)": STAIR,
        "Deepslate Tile Stairs (Itemsanity)": STAIR,
        "Polished Granite Slab (Itemsanity)": SLAB,
        "Polished Diorite Slab (Itemsanity)": SLAB,
        "Granite Slab (Itemsanity)": SLAB,
        "Andesite Slab (Itemsanity)": SLAB,
        "Polished Andesite Slab (Itemsanity)": SLAB,
        "Diorite Slab (Itemsanity)": SLAB,
        "Cobbled Deepslate Slab (Itemsanity)": SLAB,
        "Polished Deepslate Slab (Itemsanity)": SLAB,
        "Deepslate Brick Slab (Itemsanity)": SLAB,
        "Deepslate Tile Slab (Itemsanity)": SLAB,
        "Scaffolding (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Lever (Itemsanity)": ITEMSANITY,
        "Oak Button (Itemsanity)": ITEMSANITY,
        "Spruce Button (Itemsanity)": ITEMSANITY,
        "Birch Button (Itemsanity)": ITEMSANITY,
        "Acacia Button (Itemsanity)": ITEMSANITY,
        "Oak Pressure Plate (Itemsanity)": ITEMSANITY,
        "Spruce Pressure Plate (Itemsanity)": ITEMSANITY,
        "Birch Pressure Plate (Itemsanity)": ITEMSANITY,
        "Acacia Pressure Plate (Itemsanity)": ITEMSANITY,
        "Oak Door (Itemsanity)": ITEMSANITY,
        "Spruce Door (Itemsanity)": ITEMSANITY,
        "Birch Door (Itemsanity)": ITEMSANITY,
        "Acacia Door (Itemsanity)": ITEMSANITY,
        "Oak Trapdoor (Itemsanity)": ITEMSANITY,
        "Spruce Trapdoor (Itemsanity)": ITEMSANITY,
        "Birch Trapdoor (Itemsanity)": ITEMSANITY,
        "Acacia Trapdoor (Itemsanity)": ITEMSANITY,
        "Oak Fence Gate (Itemsanity)": WALL,
        "Spruce Fence Gate (Itemsanity)": WALL,
        "Birch Fence Gate (Itemsanity)": WALL,
        "Acacia Fence Gate (Itemsanity)": WALL,
        "Oak Boat (Itemsanity)": ITEMSANITY,
        "Spruce Boat (Itemsanity)": ITEMSANITY,
        "Birch Boat (Itemsanity)": ITEMSANITY,
        "Acacia Boat (Itemsanity)": ITEMSANITY,
        "Apple (Itemsanity)": ITEMSANITY,
        "Arrow (Itemsanity)": ITEMSANITY,
        "Coal (Itemsanity)": ITEMSANITY,
        "Amethyst Shard (Itemsanity)": ITEMSANITY,
        "Wooden Sword (Itemsanity)": ITEMSANITY,
        "Wooden Shovel (Itemsanity)": ITEMSANITY,
        "Wooden Pickaxe (Itemsanity)": ITEMSANITY,
        "Wooden Axe (Itemsanity)": ITEMSANITY,
        "Wooden Hoe (Itemsanity)": ITEMSANITY,
        "Stick (Itemsanity)": ITEMSANITY,
        "Bowl (Itemsanity)": ITEMSANITY,
        "Mushroom Stew (Itemsanity)": ITEMSANITY,
        "String (Itemsanity)": ITEMSANITY,
        "Feather (Itemsanity)": ITEMSANITY,
        "Gunpowder (Itemsanity)": ITEMSANITY,
        "Wheat Seeds (Itemsanity)": ITEMSANITY,
        "Wheat (Itemsanity)": ITEMSANITY,
        "Bread (Itemsanity)": ITEMSANITY,
        "Flint (Itemsanity)": ITEMSANITY,
        "Raw Porkchop (Itemsanity)": ITEMSANITY,
        "Painting (Itemsanity)": ITEMSANITY,
        "Oak Sign (Itemsanity)": ITEMSANITY,
        "Spruce Sign (Itemsanity)": ITEMSANITY,
        "Birch Sign (Itemsanity)": ITEMSANITY,
        "Acacia Sign (Itemsanity)": ITEMSANITY,
        "Snowball (Itemsanity)": ITEMSANITY,
        "Leather (Itemsanity)": ITEMSANITY,
        "Paper (Itemsanity)": ITEMSANITY,
        "Book (Itemsanity)": ITEMSANITY,
        "Egg (Itemsanity)": ITEMSANITY,
        "Bone Meal (Itemsanity)": ITEMSANITY,
        "Bone (Itemsanity)": ITEMSANITY,
        "Sugar (Itemsanity)": ITEMSANITY,
        "Cookie (Itemsanity)": ITEMSANITY,
        "Melon Slice (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Pumpkin Seeds (Itemsanity)": ITEMSANITY,
        "Melon Seeds (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Raw Beef (Itemsanity)": ITEMSANITY,
        "Raw Chicken (Itemsanity)": ITEMSANITY,
        "Rotten Flesh (Itemsanity)": ITEMSANITY,
        "Ender Pearl (Itemsanity)": ITEMSANITY,
        "Spider Eye (Itemsanity)": ITEMSANITY,
        "Fermented Spider Eye (Itemsanity)": ITEMSANITY,
        "Item Frame (Itemsanity)": ITEMSANITY,
        "Carrot (Itemsanity)": ITEMSANITY,
        "Potato (Itemsanity)": ITEMSANITY,
        "Poisonous Potato (Itemsanity)": ITEMSANITY,
        "Pumpkin Pie (Itemsanity)": ITEMSANITY,
        "Raw Rabbit (Itemsanity)": ITEMSANITY,
        "Rabbit's Foot (Itemsanity)": ITEMSANITY,
        "Rabbit Hide (Itemsanity)": ITEMSANITY,
        "Leather Horse Armor (Itemsanity)": ITEMSANITY,
        "Raw Mutton (Itemsanity)": ITEMSANITY,
        "Beetroot (Itemsanity)": ITEMSANITY,
        "Beetroot Seeds (Itemsanity)": ITEMSANITY,
        "Beetroot Soup (Itemsanity)": ITEMSANITY,
        "Phantom Membrane (Itemsanity)": ITEMSANITY,
        "Composter (Itemsanity)": ITEMSANITY,
        "Glow Berries (Itemsanity)": ITEMSANITY,
        "Pointed Dripstone (Itemsanity)": ITEMSANITY,
        "Firework Rocket (Itemsanity)": ITEMSANITY,
        "Lead (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Suspicious Stew (Itemsanity)": ITEMSANITY,
        "Flower Charge Banner Pattern (Itemsanity)": ITEMSANITY,
        "Music Disc Blocks (Itemsanity)": DISCS,
        "Music Disc Chirp (Itemsanity)": DISCS,
        "Music Disc Far (Itemsanity)": DISCS,
        "Music Disc Mall (Itemsanity)": DISCS,
        "Music Disc Mellohi (Itemsanity)": DISCS,
        "Music Disc Stal (Itemsanity)": DISCS,
        "Music Disc Strad (Itemsanity)": DISCS,
        "Music Disc Ward (Itemsanity)": DISCS,
        "Music Disc 11 (Itemsanity)": DISCS,
        "Music Disc Wait (Itemsanity)": DISCS,

        "Bell (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Slimeball (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Slime Block (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Pink Petals (Itemsanity)": FLOWER_AND_EXPLORATION,
        "Blue Orchid (Itemsanity)": FLOWER_AND_EXPLORATION,
        "Cactus (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Sunflower (Itemsanity)": FLOWER_AND_EXPLORATION,
        "Sweet Berries (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Cocoa Beans (Itemsanity)": ITEMSANITY_EXPLORATION,

        "Bamboo Sign (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Bamboo Raft (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Bamboo Fence Gate (Itemsanity)": WALL_AND_EXPLORATION,
        "Bamboo Trapdoor (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Bamboo Door (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Bamboo Pressure Plate (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Bamboo Button (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Bamboo Stairs (Itemsanity)": STAIR_AND_EXPLORATION,
        "Bamboo Mosaic Stairs (Itemsanity)": STAIR_AND_EXPLORATION,
        "Bamboo Fence (Itemsanity)": WALL_AND_EXPLORATION,
        "Bamboo Slab (Itemsanity)": SLAB_AND_EXPLORATION,
        "Bamboo Mosaic Slab (Itemsanity)": SLAB_AND_EXPLORATION,
        "Bamboo (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Block of Stripped Bamboo (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Block of Bamboo (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Bamboo Planks (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Bamboo Mosaic (Itemsanity)": ITEMSANITY_EXPLORATION,

        "Jungle Sign (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Jungle Boat (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Jungle Fence Gate (Itemsanity)": WALL_AND_EXPLORATION,
        "Jungle Trapdoor (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Jungle Door (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Jungle Pressure Plate (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Jungle Button (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Jungle Stairs (Itemsanity)": STAIR_AND_EXPLORATION,
        "Jungle Fence (Itemsanity)": WALL_AND_EXPLORATION,
        "Jungle Slab (Itemsanity)": SLAB_AND_EXPLORATION,
        "Jungle Wood (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Stripped Jungle Wood (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Stripped Jungle Log (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Jungle Log (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Jungle Planks (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Jungle Sapling (Itemsanity)": ITEMSANITY_EXPLORATION,

        "Dark Oak Sign (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Dark Oak Boat (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Dark Oak Fence Gate (Itemsanity)": WALL_AND_EXPLORATION,
        "Dark Oak Trapdoor (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Dark Oak Door (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Dark Oak Pressure Plate (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Dark Oak Button (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Dark Oak Stairs (Itemsanity)": STAIR_AND_EXPLORATION,
        "Dark Oak Fence (Itemsanity)": WALL_AND_EXPLORATION,
        "Dark Oak Slab (Itemsanity)": SLAB_AND_EXPLORATION,
        "Dark Oak Wood (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Stripped Dark Oak Wood (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Stripped Dark Oak Log (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Dark Oak Log (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Dark Oak Planks (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Dark Oak Sapling (Itemsanity)": ITEMSANITY_EXPLORATION,

        "Mangrove Sign (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Mangrove Boat (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Mangrove Fence Gate (Itemsanity)": WALL_AND_EXPLORATION,
        "Mangrove Trapdoor (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Mangrove Door (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Mangrove Pressure Plate (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Mangrove Button (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Mangrove Stairs (Itemsanity)": STAIR_AND_EXPLORATION,
        "Mangrove Fence (Itemsanity)": WALL_AND_EXPLORATION,
        "Mangrove Slab (Itemsanity)": SLAB_AND_EXPLORATION,
        "Mangrove Wood (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Stripped Mangrove Wood (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Stripped Mangrove Log (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Mangrove Log (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Mangrove Planks (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Mangrove Propagule (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Mangrove Roots (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Muddy Mangrove Roots (Itemsanity)": ITEMSANITY_EXPLORATION,

        "Cherry Sign (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Cherry Boat (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Cherry Fence Gate (Itemsanity)": WALL_AND_EXPLORATION,
        "Cherry Trapdoor (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Cherry Door (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Cherry Pressure Plate (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Cherry Button (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Cherry Stairs (Itemsanity)": STAIR_AND_EXPLORATION,
        "Cherry Fence (Itemsanity)": WALL_AND_EXPLORATION,
        "Cherry Slab (Itemsanity)": SLAB_AND_EXPLORATION,
        "Cherry Wood (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Stripped Cherry Wood (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Stripped Cherry Log (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Cherry Log (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Cherry Planks (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Cherry Sapling (Itemsanity)": ITEMSANITY_EXPLORATION
    })

    # REQUIRES NETHER ACCESS
    create_region(world, "Menu", "NetherAccess", {
        "Crimson Planks (Itemsanity)": ITEMSANITY,
        "Warped Planks (Itemsanity)": ITEMSANITY,
        "Crimson Stem (Itemsanity)": ITEMSANITY,
        "Warped Stem (Itemsanity)": ITEMSANITY,
        "Stripped Crimson Stem (Itemsanity)": ITEMSANITY,
        "Stripped Warped Stem (Itemsanity)": ITEMSANITY,
        "Stripped Crimson Hyphae (Itemsanity)": ITEMSANITY,
        "Stripped Warped Hyphae (Itemsanity)": ITEMSANITY,
        "Crimson Hyphae (Itemsanity)": ITEMSANITY,
        "Warped Hyphae (Itemsanity)": ITEMSANITY,
        "Crimson Fungus (Itemsanity)": ITEMSANITY,
        "Warped Fungus (Itemsanity)": ITEMSANITY,
        "Crimson Roots (Itemsanity)": ITEMSANITY,
        "Warped Roots (Itemsanity)": ITEMSANITY,
        "Weeping Vines (Itemsanity)": ITEMSANITY,
        "Twisting Vines (Itemsanity)": ITEMSANITY,
        "Crimson Slab (Itemsanity)": SLAB,
        "Warped Slab (Itemsanity)": SLAB,
        "Quartz Slab (Itemsanity)": SLAB,
        "Crimson Fence (Itemsanity)": WALL,
        "Warped Fence (Itemsanity)": WALL,
        "Netherrack (Itemsanity)": ITEMSANITY,
        "Soul Sand (Itemsanity)": ITEMSANITY,
        "Soul Soil (Itemsanity)": ITEMSANITY,
        "Basalt (Itemsanity)": ITEMSANITY,
        "Polished Basalt (Itemsanity)": ITEMSANITY,
        "Soul Torch (Itemsanity)": ITEMSANITY,
        "Glowstone (Itemsanity)": ITEMSANITY,
        "Crimson Stairs (Itemsanity)": STAIR,
        "Warped Stairs (Itemsanity)": STAIR,
        "Blackstone Wall (Itemsanity)": WALL,
        "Polished Blackstone Wall (Itemsanity)": WALL,
        "Polished Blackstone Brick Wall (Itemsanity)": WALL,
        "Chiseled Quartz Block (Itemsanity)": ITEMSANITY,
        "Block of Quartz (Itemsanity)": ITEMSANITY,
        "Quartz Bricks (Itemsanity)": ITEMSANITY,
        "Quartz Pillar (Itemsanity)": ITEMSANITY,
        "Quartz Stairs (Itemsanity)": STAIR,
        "Nether Wart Block (Itemsanity)": ITEMSANITY,
        "Warped Wart Block (Itemsanity)": ITEMSANITY,
        "Polished Blackstone Button (Itemsanity)": ITEMSANITY,
        "Crimson Button (Itemsanity)": ITEMSANITY,
        "Warped Button (Itemsanity)": ITEMSANITY,
        "Polished Blackstone Pressure Plate (Itemsanity)": ITEMSANITY,
        "Crimson Pressure Plate (Itemsanity)": ITEMSANITY,
        "Warped Pressure Plate (Itemsanity)": ITEMSANITY,
        "Crimson Door (Itemsanity)": ITEMSANITY,
        "Warped Door (Itemsanity)": ITEMSANITY,
        "Crimson Trapdoor (Itemsanity)": ITEMSANITY,
        "Warped Trapdoor (Itemsanity)": ITEMSANITY,
        "Crimson Fence Gate (Itemsanity)": WALL,
        "Warped Fence Gate (Itemsanity)": WALL,
        "Nether Quartz (Itemsanity)": ITEMSANITY,
        "Crimson Sign (Itemsanity)": ITEMSANITY,
        "Warped Sign (Itemsanity)": ITEMSANITY,
        "Clay Ball (Itemsanity)": ITEMSANITY,
        "Glowstone Dust (Itemsanity)": ITEMSANITY,
        "Blaze Rod (Itemsanity)": ITEMSANITY,
        "Ghast Tear (Itemsanity)": ITEMSANITY,
        "Nether Wart (Itemsanity)": ITEMSANITY,
        "Blaze Powder (Itemsanity)": ITEMSANITY,
        "Magma Cream (Itemsanity)": ITEMSANITY,
        "Fire Charge (Itemsanity)": ITEMSANITY,
        "Spectral Arrow (Itemsanity)": ITEMSANITY,
        "Soul Campfire (Itemsanity)": ITEMSANITY,
        "Shroomlight (Itemsanity)": ITEMSANITY,
        "Blackstone (Itemsanity)": ITEMSANITY,
        "Blackstone Slab (Itemsanity)": SLAB,
        "Blackstone Stairs (Itemsanity)": STAIR,
        "Gilded Blackstone (Itemsanity)": ITEMSANITY,
        "Polished Blackstone (Itemsanity)": ITEMSANITY,
        "Polished Blackstone Slab (Itemsanity)": SLAB,
        "Polished Blackstone Stairs (Itemsanity)": STAIR,
        "Chiseled Polished Blackstone (Itemsanity)": ITEMSANITY,
        "Polished Blackstone Bricks (Itemsanity)": ITEMSANITY,
        "Polished Blackstone Brick Slab (Itemsanity)": SLAB,
        "Polished Blackstone Brick Stairs (Itemsanity)": STAIR,
        "Wither Skeleton Skull (Itemsanity)": ITEMSANITY,
        "Skull Charge Banner Pattern (Itemsanity)": ITEMSANITY,

        "Ochre Froglight (Itemsanity)": ITEMSANITY_HARD,
        "Verdant Froglight (Itemsanity)": ITEMSANITY_HARD,
        "Pearlescent Froglight (Itemsanity)": ITEMSANITY_HARD
    }, lambda state: canAccessNether(world, state))

    # REQUIRES END ACCESS
    create_region(world, "NetherAccess", "EndAccess", {
        "Dragon Egg (Itemsanity)": ITEMSANITY,
        "End Stone (Itemsanity)": ITEMSANITY,
        "End Stone Bricks (Itemsanity)": ITEMSANITY,
        "End Stone Brick Wall (Itemsanity)": WALL,
        "End Stone Brick Stairs (Itemsanity)": STAIR,
        "End Stone Brick Slab (Itemsanity)": SLAB,
        "Elytra (Itemsanity)": ITEMSANITY,
        "Dragon Head (Itemsanity)": ITEMSANITY,
        "Eye of Ender (Itemsanity)": ITEMSANITY,
        "End Crystal (Itemsanity)": ITEMSANITY,
        "Chorus Fruit (Itemsanity)": ITEMSANITY,
        "Shulker Shell (Itemsanity)": ITEMSANITY
    }, lambda state: canAccessEnd(world, state))

    # REQUIRES STONE TOOLS
    create_region(world, "Menu", "HasStoneTools", {
        "Lapis Lazuli (Itemsanity)": ITEMSANITY,
        "Raw Iron (Itemsanity)": ITEMSANITY,
        "Raw Copper (Itemsanity)": ITEMSANITY,
        "Stone Shovel (Itemsanity)": ITEMSANITY,
        "Stone Pickaxe (Itemsanity)": ITEMSANITY,
        "Stone Hoe (Itemsanity)": ITEMSANITY
    }, lambda state: canUseStoneTools(world, state))

    # REQUIRES STONE TOOLS
    create_region(world, "Menu", "HasStoneWeapons", {
        "Stone Sword (Itemsanity)": ITEMSANITY,
        "Stone Axe (Itemsanity)": ITEMSANITY
    }, lambda state: canUseStoneWeapons(world, state))

    # REQUIRES LEATHER ARMOR
    create_region(world, "Menu", "HasLeatherArmor", {
        "Leather Cap (Itemsanity)": ITEMSANITY,
        "Leather Tunic (Itemsanity)": ITEMSANITY,
        "Leather Pants (Itemsanity)": ITEMSANITY,
        "Leather Boots (Itemsanity)": ITEMSANITY
    }, lambda state: canWearLeatherArmor(world, state))

    # REQUIRES SMELTING
    create_region(world, "HasStoneTools", "CanSmeltItems", {
        "Glass (Itemsanity)": ITEMSANITY,
        "Tinted Glass (Itemsanity)": ITEMSANITY,
        "Smooth Stone Slab (Itemsanity)": SLAB,
        "Brick Slab (Itemsanity)": SLAB,
        "Bricks (Itemsanity)": ITEMSANITY,
        "Smooth Sandstone (Itemsanity)": ITEMSANITY,
        "Smooth Stone (Itemsanity)": ITEMSANITY,
        "Decorated Pot (Itemsanity)": ITEMSANITY,
        "Furnace (Itemsanity)": ITEMSANITY,
        "Cracked Stone Bricks (Itemsanity)": ITEMSANITY,
        "Iron Bars (Itemsanity)": ITEMSANITY,
        "Glass Pane (Itemsanity)": ITEMSANITY,
        "Brick Stairs (Itemsanity)": STAIR,
        "Smooth Basalt (Itemsanity)": ITEMSANITY,
        "Brick Wall (Itemsanity)": WALL,
        "Terracotta (Itemsanity)": ITEMSANITY,
        "Smooth Sandstone Stairs (Itemsanity)": STAIR,
        "Smooth Sandstone Slab (Itemsanity)": SLAB,
        "Tripwire Hook (Itemsanity)": ITEMSANITY,
        "Heavy Weighted Pressure Plate (Itemsanity)": ITEMSANITY,
        "Iron Door (Itemsanity)": ITEMSANITY,
        "Iron Trapdoor (Itemsanity)": ITEMSANITY,
        "Charcoal (Itemsanity)": ITEMSANITY,
        "Iron Ingot (Itemsanity)": ITEMSANITY,
        "Copper Ingot (Itemsanity)": ITEMSANITY,
        "Cooked Porkchop (Itemsanity)": ITEMSANITY,
        "Brick (Itemsanity)": ITEMSANITY,
        "Steak (Itemsanity)": ITEMSANITY,
        "Cooked Chicken (Itemsanity)": ITEMSANITY,
        "Cauldron (Itemsanity)": ITEMSANITY,
        "Flower Pot (Itemsanity)": ITEMSANITY,
        "Baked Potato (Itemsanity)": ITEMSANITY,
        "Cooked Rabbit (Itemsanity)": ITEMSANITY,
        "Rabbit Stew (Itemsanity)": ITEMSANITY,
        "Armor Stand (Itemsanity)": ITEMSANITY,
        "Cooked Mutton (Itemsanity)": ITEMSANITY,
        "Campfire (Itemsanity)": ITEMSANITY,
        "Cracked Deepslate Bricks (Itemsanity)": ITEMSANITY,
        "Cracked Deepslate Tiles (Itemsanity)": ITEMSANITY
    }, lambda state: canSmelt(world, state))

    # REQUIRES SMELTING (x2)
    create_region(world, "CanSmeltItems", "CanSmeltItemsBetter", {
        "Smoker (Itemsanity)": ITEMSANITY,
        "Blast Furnace (Itemsanity)": ITEMSANITY
    }, lambda state: canSmeltBetter(world, state))

    # REQUIRES SHIELD
    create_region(world, "CanSmeltItems", "HasShield", {
        "Shield (Itemsanity)": ITEMSANITY
    }, lambda state: canUseShield(world, state))

    # REQUIRES IRON TOOLS
    create_region(world, "CanSmeltItems", "HasIronTools", {
        "Jukebox (Itemsanity)": ITEMSANITY,
        "Redstone Dust (Itemsanity)": ITEMSANITY,
        "Redstone Torch (Itemsanity)": ITEMSANITY,
        "Redstone Repeater (Itemsanity)": ITEMSANITY,
        "Piston (Itemsanity)": ITEMSANITY,
        "Dropper (Itemsanity)": ITEMSANITY,
        "Target (Itemsanity)": ITEMSANITY,
        "Lightning Rod (Itemsanity)": ITEMSANITY,
        "Note Block (Itemsanity)": ITEMSANITY,
        "Diamond (Itemsanity)": ITEMSANITY,
        "Emerald (Itemsanity)": ITEMSANITY,
        "Raw Gold (Itemsanity)": ITEMSANITY,
        "Golden Shovel (Itemsanity)": ITEMSANITY,
        "Golden Pickaxe (Itemsanity)": ITEMSANITY,
        "Golden Hoe (Itemsanity)": ITEMSANITY,
        "Iron Shovel (Itemsanity)": ITEMSANITY,
        "Iron Pickaxe (Itemsanity)": ITEMSANITY,
        "Iron Hoe (Itemsanity)": ITEMSANITY,
        "Compass (Itemsanity)": ITEMSANITY,
        "Clock (Itemsanity)": ITEMSANITY,
        "Map (Itemsanity)": ITEMSANITY,

        "Sticky Piston (Itemsanity)": ITEMSANITY_EXPLORATION
    }, lambda state: canUseIronTools(world, state))

    # CAN GET GOLD
    create_region(world, "Menu", "CanGetGold", {
        "Gold Ingot (Itemsanity)": ITEMSANITY,
        "Golden Apple (Itemsanity)": ITEMSANITY,
        "Light Weighted Pressure Plate (Itemsanity)": ITEMSANITY
    }, lambda state: canGetGold(world, state))

    # CAN GET GOLD Nugget
    create_region(world, "Menu", "CanGetGoldNugget", {
        "Gold Nugget (Itemsanity)": ITEMSANITY,
        "Glistering Melon Slice (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Golden Carrot (Itemsanity)": ITEMSANITY
    }, lambda state: canGetGoldNugget(world, state))

    # REQUIRES IRON WEAPONS
    create_region(world, "CanSmeltItems", "HasIronWeapons", {
        "Iron Axe (Itemsanity)": ITEMSANITY,
        "Iron Sword (Itemsanity)": ITEMSANITY
    }, lambda state: canUseIronWeapons(world, state))

    # REQUIRES IRON WEAPONS AND GOLD
    create_region(world, "HasIronWeapons", "HasIronWeaponsAndGold", {
        "Golden Sword (Itemsanity)": ITEMSANITY,
        "Golden Axe (Itemsanity)": ITEMSANITY
    }, lambda state: canUseIronWeapons(world, state) and canGetGold(world, state))

    # REQUIRES IRON ARMOR
    create_region(world, "CanSmeltItems", "HasIronArmor", {
        "Iron Helmet (Itemsanity)": ITEMSANITY,
        "Iron Chestplate (Itemsanity)": ITEMSANITY,
        "Iron Leggings (Itemsanity)": ITEMSANITY,
        "Iron Boots (Itemsanity)": ITEMSANITY
    }, lambda state: canWearIronArmor(world, state))

    # REQUIRES GOLD ARMOR
    create_region(world, "CanSmeltItems", "HasGoldArmor", {
        "Golden Helmet (Itemsanity)": ITEMSANITY,
        "Golden Chestplate (Itemsanity)": ITEMSANITY,
        "Golden Leggings (Itemsanity)": ITEMSANITY,
        "Golden Boots (Itemsanity)": ITEMSANITY
    }, lambda state: canWearGoldArmor(world, state))

    # REQUIRES DIAMOND TOOLS
    create_region(world, "HasIronTools", "HasDiamondTools", {
        "Obsidian (Itemsanity)": ITEMSANITY,
        "Diamond Shovel (Itemsanity)": ITEMSANITY,
        "Diamond Pickaxe (Itemsanity)": ITEMSANITY,
        "Diamond Hoe (Itemsanity)": ITEMSANITY
    }, lambda state: canUseDiamondTools(world, state))

    # REQUIRES DIAMOND WEAPONS
    create_region(world, "HasIronTools", "HasDiamondWeapons", {
        "Diamond Sword (Itemsanity)": ITEMSANITY,
        "Diamond Axe (Itemsanity)": ITEMSANITY
    }, lambda state: canUseDiamondWeapons(world, state))

    # REQUIRES DIAMOND ARMOR
    create_region(world, "HasIronTools", "HasDiamondArmor", {
        "Diamond Helmet (Itemsanity)": ITEMSANITY,
        "Diamond Chestplate (Itemsanity)": ITEMSANITY,
        "Diamond Leggings (Itemsanity)": ITEMSANITY,
        "Diamond Boots (Itemsanity)": ITEMSANITY
    }, lambda state: canWearDiamondArmor(world, state))

    # REQUIRES ARMOR TRIMS
    create_region(world, "CanSmeltItems", "CanSmithItems", {
        "Smithing Table (Itemsanity)": ITEMSANITY
    }, lambda state: canGetAndUseArmorTrims(world, state))

    # REQUIRES NETHERITE TOOLS
    create_region(world, "CanSmithItems", "HasNetheriteTools", {
        "Netherite Shovel (Itemsanity)": NETHERITE,
        "Netherite Pickaxe (Itemsanity)": NETHERITE,
        "Netherite Hoe (Itemsanity)": NETHERITE
    }, lambda state: canUseNetheriteTools(world, state))

    # REQUIRES NETHERITE WEAPONS
    create_region(world, "CanSmithItems", "HasNetheriteWeapons", {
        "Netherite Sword (Itemsanity)": NETHERITE,
        "Netherite Axe (Itemsanity)": NETHERITE
    }, lambda state: canUseNetheriteWeapons(world, state))

    # REQUIRES NETHERITE Armor
    create_region(world, "CanSmithItems", "HasNetheriteArmor", {
        "Netherite Helmet (Itemsanity)": NETHERITE,
        "Netherite Chestplate (Itemsanity)": NETHERITE,
        "Netherite Leggings (Itemsanity)": NETHERITE,
        "Netherite Boots (Itemsanity)": NETHERITE
    }, lambda state: canWearNetheriteArmor(world, state))

    # REQUIRES BOW
    create_region(world, "Menu", "HasBow", {
        "Bow (Itemsanity)": ITEMSANITY
    }, lambda state: canUseBow(world, state))

    # REQUIRES CROSSBOW
    create_region(world, "CanSmeltItems", "HasCrossbow", {
        "Crossbow (Itemsanity)": ITEMSANITY
    }, lambda state: canUseCrossBow(world, state))

    # REQUIRES MINECART
    create_region(world, "CanSmeltItems", "HasMinecart", {
        "Rail (Itemsanity)": ITEMSANITY,
        "Minecart (Itemsanity)": ITEMSANITY,
        "Minecart with TNT (Itemsanity)": ITEMSANITY,
        "Minecart with Furnace (Itemsanity)": ITEMSANITY
    }, lambda state: canUseMinecart(world, state))

    # REQUIRES FISHING
    create_region(world, "Menu", "HasFishing", {
        "Carrot on a Stick (Itemsanity)": ITEMSANITY,
        "Fishing Rod (Itemsanity)": ITEMSANITY
    }, lambda state: canUseFishingRod(world, state))

    # REQUIRES BRUSH
    create_region(world, "CanSmeltItems", "HasBrush", {
        "Brush (Itemsanity)": ITEMSANITY,

        "Music Disc Relic (Itemsanity)": DISCS,
        "Archer Pottery Sherd (Itemsanity)": SHERD,
        "Miner Pottery Sherd (Itemsanity)": SHERD,
        "Prize Pottery Sherd (Itemsanity)": SHERD,
        "Skull Pottery Sherd (Itemsanity)": SHERD,

        "Wayfinder Armor Trim (Itemsanity)": TRIM,
        "Shaper Armor Trim (Itemsanity)": TRIM,
        "Raiser Armor Trim (Itemsanity)": TRIM,
        "Host Armor Trim (Itemsanity)": TRIM,
        "Arms Up Pottery Sherd (Itemsanity)": SHERD,
        "Brewer Pottery Sherd (Itemsanity)": SHERD,
        "Burn Pottery Sherd (Itemsanity)": SHERD,
        "Danger Pottery Sherd (Itemsanity)": SHERD,
        "Friend Pottery Sherd (Itemsanity)": SHERD,
        "Heart Pottery Sherd (Itemsanity)": SHERD,
        "Heartbreak Pottery Sherd (Itemsanity)": SHERD,
        "Howl Pottery Sherd (Itemsanity)": SHERD,
        "Sheaf Pottery Sherd (Itemsanity)": SHERD
    }, lambda state: canUseBrush(world, state))

    # REQUIRES FLINT AND STEEL
    create_region(world, "CanSmeltItems", "HasFlintAndSteel", {
        "Flint and Steel (Itemsanity)": ITEMSANITY
    }, lambda state: canUseFlintAndSteel(world, state))

    # REQUIRES CHESTS
    create_region(world, "Menu", "HasChests", {
        "Chest (Itemsanity)": ITEMSANITY,
        "Saddle (Itemsanity)": ITEMSANITY,
        "Oak Boat with Chest (Itemsanity)": ITEMSANITY,
        "Spruce Boat with Chest (Itemsanity)": ITEMSANITY,
        "Birch Boat with Chest (Itemsanity)": ITEMSANITY,
        "Jungle Boat with Chest (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Acacia Boat with Chest (Itemsanity)": ITEMSANITY,
        "Cherry Boat with Chest (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Dark Oak Boat with Chest (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Mangrove Boat with Chest (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Bamboo Raft with Chest (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Iron Horse Armor (Itemsanity)": ITEMSANITY,
        "Golden Horse Armor (Itemsanity)": ITEMSANITY,
        "Diamond Horse Armor (Itemsanity)": ITEMSANITY,
        "Name Tag (Itemsanity)": ITEMSANITY,
        "Barrel (Itemsanity)": ITEMSANITY,
        "Music Disc 13 (Itemsanity)": DISCS,
        "Music Disc Cat (Itemsanity)": DISCS,

        "Enchanted Golden Apple (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Thing Banner Pattern (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Tall Grass (Itemsanity)": ITEMSANITY_UNREASONABLE,
        "Large Fern (Itemsanity)": ITEMSANITY_UNREASONABLE,
        "Echo Shard (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Goat Horn (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Music Disc 5 (Itemsanity)": DISCS,
        "Disc 5 Fragment (Itemsanity)": DISCS,
        "Music Disc Otherside (Itemsanity)": DISCS,
        "Sentry Armor Trim (Itemsanity)": TRIM,
        "Dune Armor Trim (Itemsanity)": TRIM,
        "Vex Armor Trim (Itemsanity)": TRIM,

        "Wild Armor Trim (Itemsanity)": TRIM,
        "Ward Armor Trim (Itemsanity)": TRIM,
        "Silence Armor Trim (Itemsanity)": TRIM,
    }, lambda state: canAccessChests(world, state))

    # REQUIRES ENCHANTING
    create_region(world, "HasDiamondTools", "HasEnchanting", {
        "Grass Block (Itemsanity)": ITEMSANITY,
        "Podzol (Itemsanity)": ITEMSANITY,
        "Coal Ore (Itemsanity)": ITEMSANITY,
        "Iron Ore (Itemsanity)": ITEMSANITY,
        "Deepslate Iron Ore (Itemsanity)": ITEMSANITY,
        "Copper Ore (Itemsanity)": ITEMSANITY,
        "Deepslate Copper Ore (Itemsanity)": ITEMSANITY,
        "Gold Ore (Itemsanity)": ITEMSANITY,
        "Deepslate Gold Ore (Itemsanity)": ITEMSANITY,
        "Redstone Ore (Itemsanity)": ITEMSANITY,
        "Deepslate Redstone Ore (Itemsanity)": ITEMSANITY,
        "Emerald Ore (Itemsanity)": ITEMSANITY,
        "Lapis Lazuli Ore (Itemsanity)": ITEMSANITY,
        "Deepslate Lapis Lazuli Ore (Itemsanity)": ITEMSANITY,
        "Deepslate Diamond Ore (Itemsanity)": ITEMSANITY,
        "Bookshelf (Itemsanity)": ITEMSANITY,
        "Ice (Itemsanity)": ITEMSANITY,
        "Brown Mushroom Block (Itemsanity)": ITEMSANITY,
        "Red Mushroom Block (Itemsanity)": ITEMSANITY,
        "Mushroom Stem (Itemsanity)": ITEMSANITY,
        "Sculk (Itemsanity)": ITEMSANITY,
        "Sculk Vein (Itemsanity)": ITEMSANITY,
        "Sculk Catalyst (Itemsanity)": ITEMSANITY,
        "Sculk Shrieker (Itemsanity)": ITEMSANITY,
        "Enchanting Table (Itemsanity)": ITEMSANITY,
        "Anvil (Itemsanity)": ITEMSANITY,
        "Chipped Anvil (Itemsanity)": ITEMSANITY,
        "Damaged Anvil (Itemsanity)": ITEMSANITY,
        "Packed Ice (Itemsanity)": ITEMSANITY,
        "Blue Ice (Itemsanity)": ITEMSANITY,
        "Lectern (Itemsanity)": ITEMSANITY,
        "Sculk Sensor (Itemsanity)": ITEMSANITY,
        "Calibrated Sculk Sensor (Itemsanity)": ITEMSANITY,
        "Bee Nest (Itemsanity)": ITEMSANITY,
        "Small Amethyst Bud (Itemsanity)": ITEMSANITY,
        "Medium Amethyst Bud (Itemsanity)": ITEMSANITY,
        "Large Amethyst Bud (Itemsanity)": ITEMSANITY,
        "Amethyst Cluster (Itemsanity)": ITEMSANITY,

        "Deepslate Coal Ore (Itemsanity)": RARE_ORE,
        "Deepslate Emerald Ore (Itemsanity)": RARE_ORE,
        "Diamond Ore (Itemsanity)": RARE_ORE
    }, lambda state: canEnchant(world, state))

    # REQUIRES BUCKET
    create_region(world, "CanSmeltItems", "HasBucket", {
        "Bucket (Itemsanity)": ITEMSANITY,
        "Water Bucket (Itemsanity)": ITEMSANITY,
        "Lava Bucket (Itemsanity)": ITEMSANITY,
        "Milk Bucket (Itemsanity)": ITEMSANITY,
        "Cake (Itemsanity)": ITEMSANITY,

        "Suspicious Sand (Itemsanity)": ITEMSANITY_HARD,
        "Suspicious Gravel (Itemsanity)": ITEMSANITY_HARD,

        "Powder Snow Bucket (Itemsanity)": ITEMSANITY_EXPLORATION
    }, lambda state: canUseBucket(world, state))

    # REQUIRES TNT
    create_region(world, "Menu", "HasTNT", {
        "TNT (Itemsanity)": ITEMSANITY,
    }, lambda state: hasTNT(world, state))

    # REQUIRES SMOOTH STONE OBTAINING
    create_region(world, "Menu", "CanGetSmoothStone", {
        "Stone (Itemsanity)": ITEMSANITY,
        "Stone Slab (Itemsanity)": SLAB,
        "Stone Brick Slab (Itemsanity)": SLAB,
        "Chiseled Stone Bricks (Itemsanity)": ITEMSANITY,
        "Stone Bricks (Itemsanity)": ITEMSANITY,
        "Stone Brick Stairs (Itemsanity)": STAIR,
        "Stone Brick Wall (Itemsanity)": WALL,
        "Stone Stairs (Itemsanity)": STAIR,
        "Stone Button (Itemsanity)": ITEMSANITY,
        "Stone Pressure Plate (Itemsanity)": ITEMSANITY,
        "Deepslate (Itemsanity)": ITEMSANITY
    }, lambda state: canUseBucket(world, state))

    # REQUIRES BREWING
    create_region(world, "NetherAccess", "HasBrewing", {
        "Brewing Stand (Itemsanity)": ITEMSANITY
    }, lambda state: canBrew(world, state))

    # REQUIRES SPYGLASS
    create_region(world, "CanSmeltItems", "HasSpyglass", {
        "Spyglass (Itemsanity)": ITEMSANITY
    }, lambda state: canUseSpyglass(world, state))

    # REQUIRES GLASS BOTTLES
    create_region(world, "CanSmeltItems", "HasBottles", {
        "Honey Block (Itemsanity)": ITEMSANITY,
        "Glass Bottle (Itemsanity)": ITEMSANITY,
        "Honey Bottle (Itemsanity)": ITEMSANITY,

        "Mud Brick Wall (Itemsanity)": WALL,
        "Mud Brick Stairs (Itemsanity)": STAIR,
        "Packed Mud (Itemsanity)": ITEMSANITY,
        "Mud Bricks (Itemsanity)": ITEMSANITY,
        "Mud (Itemsanity)": ITEMSANITY,
        "Mud Brick Slab (Itemsanity)": SLAB,
    }, lambda state: canUseBottles(world, state))

    # REQUIRES SWIMMING
    create_region(world, "Menu", "HasSwim", {
        "Sea Pickle (Itemsanity)": ITEMSANITY,
        "Kelp (Itemsanity)": ITEMSANITY,
        "Ink Sac (Itemsanity)": ITEMSANITY,
        "Glow Ink Sac (Itemsanity)": ITEMSANITY,
        "Book and Quill (Itemsanity)": ITEMSANITY,
        "Glow Item Frame (Itemsanity)": ITEMSANITY,
        "Trident (Itemsanity)": ITEMSANITY,
        "Nautilus Shell (Itemsanity)": ITEMSANITY,

        "Lily Pad (Itemsanity)": ITEMSANITY_EXPLORATION,

        "Dark Prismarine Slab (Itemsanity)": SLAB_AND_EXPLORATION,
        "Dark Prismarine (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Dark Prismarine Stairs (Itemsanity)": STAIR_AND_EXPLORATION,

        "Sea Lantern (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Sponge (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Wet Sponge (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Tide Armor Trim (Itemsanity)": TRIM
    }, lambda state: canSwim(world, state))

    # REQUIRES PRISMARINE
    create_region(world, "Menu", "CanGetPrismarine", {
        "Prismarine Shard (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Prismarine Crystals (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Prismarine Slab (Itemsanity)": SLAB_AND_EXPLORATION,
        "Prismarine Brick Slab (Itemsanity)": SLAB_AND_EXPLORATION,
        "Prismarine Wall (Itemsanity)": WALL_AND_EXPLORATION,
        "Prismarine (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Prismarine Bricks (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Prismarine Stairs (Itemsanity)": STAIR_AND_EXPLORATION,
        "Prismarine Brick Stairs (Itemsanity)": STAIR_AND_EXPLORATION
    }, lambda  state: canGetPrismarine(world, state))

    # REQUIRES WITHER SUMMONING
    create_region(world, "NetherAccess", "CanSummonWither", {
        "Wither Rose (Itemsanity)": ITEMSANITY,
        "Nether Star (Itemsanity)": ITEMSANITY
    }, lambda state: canGoalWither(world, state))

    # REQUIRES BEACON
    create_region(world, "CanSummonWither", "CanUseBeacon", {
        "Beacon (Itemsanity)": ITEMSANITY
    }, lambda state: canPlaceBeacon(world, state))

    # REQUIRES CRYING OBSIDIAN
    create_region(world, "NetherAccess", "CanGetCryingObsidian", {
        "Crying Obsidian (Itemsanity)": ITEMSANITY,
        "Respawn Anchor (Itemsanity)": ITEMSANITY
    }, lambda state: canGetCryingObsidian(world, state))

    # REQUIRES SHEARS
    create_region(world, "CanSmeltItems", "HasShears", {
        "Grass (Itemsanity)": ITEMSANITY,
        "Fern (Itemsanity)": ITEMSANITY,
        "Dead Bush (Itemsanity)": ITEMSANITY,
        "Small Dripleaf (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Mossy Cobblestone (Itemsanity)": ITEMSANITY,
        "Mossy Stone Bricks (Itemsanity)": ITEMSANITY,
        "Vines (Itemsanity)": ITEMSANITY,
        "Glow Lichen (Itemsanity)": ITEMSANITY,
        "Mossy Cobblestone Wall (Itemsanity)": WALL,
        "Mossy Stone Brick Wall (Itemsanity)": WALL,
        "Mossy Stone Brick Stairs (Itemsanity)": STAIR,
        "Mossy Cobblestone Stairs (Itemsanity)": STAIR,
        "Mossy Stone Brick Slab (Itemsanity)": SLAB,
        "Mossy Cobblestone Slab (Itemsanity)": SLAB,
        "Shears (Itemsanity)": ITEMSANITY,
        "Honeycomb (Itemsanity)": ITEMSANITY,
        "Beehive (Itemsanity)": ITEMSANITY,
        "Honeycomb Block (Itemsanity)": ITEMSANITY,
        "Hanging Roots (Itemsanity)": ITEMSANITY,
        "Candle (Itemsanity)": ITEMSANITY,
        "Carved Pumpkin (Itemsanity)": ITEMSANITY,
        "Jack o'Lantern (Itemsanity)": ITEMSANITY,
    }, lambda state: canUseShears(world, state))

    # REQUIRES MISC CRAFTING
    create_region(world, "CanSmeltItems", "CanCraftMiscStations", {
        "Loom (Itemsanity)": ITEMSANITY,
        "Cartography Table (Itemsanity)": ITEMSANITY,
        "Fletching Table (Itemsanity)": ITEMSANITY,
        "Grindstone (Itemsanity)": ITEMSANITY,
        "Stonecutter (Itemsanity)": ITEMSANITY
    }, lambda state: canAccessMiscJobsites(world, state))

    # REQUIRES TRADING
    create_region(world, "Menu", "HasTrading", {
        "Chainmail Helmet (Itemsanity)": ITEMSANITY_HARD,
        "Chainmail Chestplate (Itemsanity)": ITEMSANITY_HARD,
        "Chainmail Leggings (Itemsanity)": ITEMSANITY_HARD,
        "Chainmail Boots (Itemsanity)": ITEMSANITY_HARD,
        "Globe Banner Pattern (Itemsanity)": ITEMSANITY_HARD,

        "Bottle o' Enchanting (Itemsanity)": ITEMSANITY_EXPLORATION
    }, lambda state: canTrade(world, state))

    # REQUIRES RAIDS
    create_region(world, "Menu", "CanFightRaids", {
        "Totem of Undying (Itemsanity)": ITEMSANITY_EXPLORATION
    }, lambda state: canFightRaid(world, state))


    ####################################################################################################################
    # MULTIPLE CHECKS ##################################################################################################
    ####################################################################################################################

    # REQUIRES SWIMMING AND ENCHANTING
    create_region(world, "HasEnchanting", "HasSwimAndEnchanting", {
        "Tube Coral Block (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Brain Coral Block (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Bubble Coral Block (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Fire Coral Block (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Horn Coral Block (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Tube Coral (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Brain Coral (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Bubble Coral (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Fire Coral (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Horn Coral (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Dead Brain Coral (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Dead Bubble Coral (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Dead Fire Coral (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Dead Horn Coral (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Dead Tube Coral (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Tube Coral Fan (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Brain Coral Fan (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Bubble Coral Fan (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Fire Coral Fan (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Horn Coral Fan (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Dead Tube Coral Fan (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Dead Brain Coral Fan (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Dead Bubble Coral Fan (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Dead Fire Coral Fan (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Dead Horn Coral Fan (Itemsanity)": ITEMSANITY_EXPLORATION,

        "Zombie Head (Itemsanity)": MOB_HEADS,
        "Skeleton Skull (Itemsanity)": MOB_HEADS,
        "Creeper Head (Itemsanity)": MOB_HEADS,
        "Piglin Head (Itemsanity)": MOB_HEADS,
        "Creeper Charge Banner Pattern (Itemsanity)": MOB_HEADS,

        "Mycelium (Itemsanity)": ITEMSANITY_EXPLORATION
    }, lambda state: canSwim(world, state) and canEnchant(world, state))

    # REQUIRES SWIMMING AND BRUSH
    create_region(world, "HasBrush", "HasSwimAndBrush", {
        "Sniffer Egg (Itemsanity)": ITEMSANITY,
        "Torchflower Seeds (Itemsanity)": FLOWER_AND_HARD,
        "Pitcher Pod (Itemsanity)": FLOWER_AND_HARD,
        "Torchflower (Itemsanity)": FLOWER_AND_HARD,
        "Pitcher Plant (Itemsanity)": FLOWER_AND_HARD,

        "Angler Pottery Sherd (Itemsanity)": SHERD,
        "Shelter Pottery Sherd (Itemsanity)": SHERD,
        "Snort Pottery Sherd (Itemsanity)": SHERD,
        "Blade Pottery Sherd (Itemsanity)": SHERD,
        "Explorer Pottery Sherd (Itemsanity)": SHERD,
        "Mourner Pottery Sherd (Itemsanity)": SHERD,
        "Plenty Pottery Sherd (Itemsanity)": SHERD
    }, lambda state: canSwim(world, state) and canUseBrush(world, state))

    # REQUIRES SWIMMING AND SHEARS
    create_region(world, "HasShears", "HasSwimAndShears", {
        "Seagrass (Itemsanity)": ITEMSANITY,
        "Scute (Itemsanity)": ITEMSANITY_HARD,
        "Turtle Shell (Itemsanity)": ITEMSANITY_UNREASONABLE
    }, lambda state: canUseShears(world, state) and canSwim(world, state))

    # REQUIRES SWIMMING AND CHESTS
    create_region(world, "HasSwim", "HasSwimAndChests", {
        "Heart of the Sea (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Conduit (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Coast Armor Trim (Itemsanity)": TRIM
    }, lambda state: canAccessChests(world, state) and canSwim(world, state))

    # REQUIRES EYES OF ENDER AND CHESTS
    create_region(world, "HasChests", "HasChestsAndEyesOfEnder", {
        "Eye Armor Trim (Itemsanity)": TRIM
    }, lambda state: canAccessChests(world, state) and canGetEyesOfEnder(world, state))

    # REQUIRES SWIMMING AND SMELTING
    create_region(world, "CanSmeltItems", "HasSwimAndSmelting", {
        "Dried Kelp Block (Itemsanity)": ITEMSANITY,
        "Dried Kelp (Itemsanity)": ITEMSANITY
    }, lambda state: canSmelt(world, state) and canSwim(world, state))

    # REQUIRES SWIMMING AND STONE TOOLS
    create_region(world, "HasStoneTools", "HasSwimAndStoneTools", {
        "Dead Tube Coral Block (Itemsanity)": ITEMSANITY,
        "Dead Brain Coral Block (Itemsanity)": ITEMSANITY,
        "Dead Bubble Coral Block (Itemsanity)": ITEMSANITY,
        "Dead Fire Coral Block (Itemsanity)": ITEMSANITY,
        "Dead Horn Coral Block (Itemsanity)": ITEMSANITY
    }, lambda state: canSmelt(world, state) and canSwim(world, state))

    # REQUIRES SHEARS AND COMPACTING
    create_region(world, "CanSmeltItems", "HasShearsAndCompacting", {
        "Waxed Block of Copper (Itemsanity)": ITEMSANITY,
        "Waxed Exposed Copper (Itemsanity)": ITEMSANITY,
        "Waxed Weathered Copper (Itemsanity)": ITEMSANITY,
        "Waxed Oxidized Copper (Itemsanity)": ITEMSANITY,
        "Waxed Cut Copper (Itemsanity)": ITEMSANITY,
        "Waxed Exposed Cut Copper (Itemsanity)": ITEMSANITY,
        "Waxed Weathered Cut Copper (Itemsanity)": ITEMSANITY,
        "Waxed Oxidized Cut Copper (Itemsanity)": ITEMSANITY,
        "Waxed Cut Copper Stairs (Itemsanity)": STAIR,
        "Waxed Exposed Cut Copper Stairs (Itemsanity)": STAIR,
        "Waxed Weathered Cut Copper Stairs (Itemsanity)": STAIR,
        "Waxed Oxidized Cut Copper Stairs (Itemsanity)": STAIR,
        "Waxed Cut Copper Slab (Itemsanity)": SLAB,
        "Waxed Exposed Cut Copper Slab (Itemsanity)": SLAB,
        "Waxed Weathered Cut Copper Slab (Itemsanity)": SLAB,
        "Waxed Oxidized Cut Copper Slab (Itemsanity)": SLAB
    }, lambda state: canUseShears(world, state) and canCompactResources(world, state))

    # REQUIRES BUCKET AND SWIM
    create_region(world, "HasBucket", "HasBucketAndSwim", {
        "Bucket of Pufferfish (Itemsanity)": ITEMSANITY,
        "Bucket of Salmon (Itemsanity)": ITEMSANITY,
        "Bucket of Cod (Itemsanity)": ITEMSANITY,
        "Bucket of Tropical Fish (Itemsanity)": ITEMSANITY,
        "Bucket of Axolotl (Itemsanity)": ITEMSANITY,

        "Bucket of Tadpole (Itemsanity)": ITEMSANITY_EXPLORATION
    }, lambda state: canUseBucket(world, state) and canSwim(world, state))

    # REQUIRES COMPACTING AND SMELTING
    create_region(world, "CanSmeltItems", "CanSmeltAndCanCompact", {
        "Block of Iron (Itemsanity)": ITEMSANITY,
        "Block of Copper (Itemsanity)": ITEMSANITY,
        "Exposed Copper (Itemsanity)": ITEMSANITY,
        "Weathered Copper (Itemsanity)": ITEMSANITY,
        "Oxidized Copper (Itemsanity)": ITEMSANITY,
        "Cut Copper (Itemsanity)": ITEMSANITY,
        "Exposed Cut Copper (Itemsanity)": ITEMSANITY,
        "Weathered Cut Copper (Itemsanity)": ITEMSANITY,
        "Oxidized Cut Copper (Itemsanity)": ITEMSANITY,
        "Cut Copper Stairs (Itemsanity)": STAIR,
        "Exposed Cut Copper Stairs (Itemsanity)": STAIR,
        "Weathered Cut Copper Stairs (Itemsanity)": STAIR,
        "Oxidized Cut Copper Stairs (Itemsanity)": STAIR,
        "Cut Copper Slab (Itemsanity)": SLAB,
        "Exposed Cut Copper Slab (Itemsanity)": SLAB,
        "Weathered Cut Copper Slab (Itemsanity)": SLAB,
        "Oxidized Cut Copper Slab (Itemsanity)": SLAB,
        "Iron Nugget (Itemsanity)": ITEMSANITY,
    }, lambda state: canSmelt(world, state) and canCompactResources(world, state))

    # REQUIRES COMPACTING AND STONE TOOLS
    create_region(world, "HasStoneTools", "CanCompactAndStoneTools", {
        "Block of Coal (Itemsanity)": ITEMSANITY,
        "Block of Raw Iron (Itemsanity)": ITEMSANITY,
        "Block of Raw Copper (Itemsanity)": ITEMSANITY,
        "Block of Lapis Lazuli (Itemsanity)": ITEMSANITY
    }, lambda state: canCompactResources(world, state))

    # REQUIRES COMPACTING AND IRON TOOLS
    create_region(world, "HasIronTools", "CanCompactAndIronTools", {
        "Block of Raw Gold (Itemsanity)": ITEMSANITY,
        "Block of Diamond (Itemsanity)": ITEMSANITY,
        "Block of Emerald (Itemsanity)": ITEMSANITY,
        "Block of Redstone (Itemsanity)": ITEMSANITY
    }, lambda state: canCompactResources(world, state))

    # REQUIRES COMPACTING AND DIAMOND TOOLS
    create_region(world, "CanCompactAndIronTools", "CanCompactAndDiamondTools", {
        "Block of Netherite (Itemsanity)": ITEMSANITY
    }, lambda state: canCompactResources(world, state) and canGetNetherite(world, state))

    # REQUIRES COMPACTING AND IRON TOOLS AND SMELTING
    create_region(world, "HasIronTools", "CanCompactAndIronToolsAndSmelting", {
        "Block of Gold (Itemsanity)": ITEMSANITY
    }, lambda state: canCompactResources(world, state) and canSmelt(world, state) and canUseIronTools(world, state))

    # REQUIRES NETHER AND FISHING ROD
    create_region(world, "NetherAccess", "NetherAccessAndFishing", {
        "Warped Fungus on a Stick (Itemsanity)": ITEMSANITY
    }, lambda state: canAccessNether(world, state) and canUseFishingRod(world, state))

    # REQUIRES END AND SMELTING
    create_region(world, "EndAccess", "EndAccessAndSmelting", {
        "Purpur Slab (Itemsanity)": SLAB,
        "Purpur Block (Itemsanity)": ITEMSANITY,
        "Purpur Pillar (Itemsanity)": ITEMSANITY,
        "Purpur Stairs (Itemsanity)": STAIR,
        "Popped Chorus Fruit (Itemsanity)": ITEMSANITY
    }, lambda state: canAccessEnd(world, state) and canSmelt(world, state))

    # REQUIRES END AND GLASS BOTTLES AND SMELTING
    create_region(world, "EndAccessAndSmelting", "EndAccessAndGlassBottles", {
        "Dragon's Breath (Itemsanity)": ITEMSANITY
    }, lambda state: canAccessEnd(world, state) and canSmelt(world, state) and canUseBottles(world, state))

    # REQUIRES VANILLA END GAME
    create_region(world, "EndAccess", "VanillaEndGame", {
        "End Rod (Itemsanity)": ITEMSANITY
    }, lambda state: canAccessVanillaEndGame(world, state))

    # REQUIRES NETHER + DIAMOND TOOLS OR CHESTS
    create_region(world, "NetherAccess", "NetherAccessGetDebree", {
        "Ancient Debris (Itemsanity)": ITEMSANITY
    }, lambda state: canGetNetherite(world, state))

    # REQUIRES NETHER + DIAMOND TOOLS OR CHESTS + Smelting
    create_region(world, "NetherAccessGetDebree", "NetherAccessGetDebreeScrap", {
        "Netherite Scrap (Itemsanity)": ITEMSANITY,
        "Netherite Ingot (Itemsanity)": ITEMSANITY,
        "Lodestone (Itemsanity)": ITEMSANITY
    }, lambda state: canGetNetherite(world, state) and canSmelt(world, state))

    # REQUIRES NETHER AND ENCHANTING
    create_region(world, "NetherAccess", "NetherAccessAndEnchanting", {
        "Crimson Nylium (Itemsanity)": ITEMSANITY,
        "Warped Nylium (Itemsanity)": ITEMSANITY,
        "Nether Gold Ore (Itemsanity)": ITEMSANITY,
        "Nether Quartz Ore (Itemsanity)": ITEMSANITY
    }, lambda state: canAccessNether(world, state) and canEnchant(world, state))

    # REQUIRES NETHER AND SMELTING
    create_region(world, "NetherAccess", "NetherAccessAndSmelting", {
        "Nether Brick Slab (Itemsanity)": SLAB,
        "Smooth Quartz Block (Itemsanity)": ITEMSANITY,
        "Nether Bricks (Itemsanity)": ITEMSANITY,
        "Cracked Nether Bricks (Itemsanity)": ITEMSANITY,
        "Chiseled Nether Bricks (Itemsanity)": ITEMSANITY,
        "Nether Brick Fence (Itemsanity)": WALL,
        "Nether Brick Stairs (Itemsanity)": STAIR,
        "Nether Brick Wall (Itemsanity)": WALL,
        "Red Nether Brick Wall (Itemsanity)": WALL,
        "Smooth Quartz Stairs (Itemsanity)": STAIR,
        "Red Nether Brick Stairs (Itemsanity)": STAIR,
        "Smooth Quartz Slab (Itemsanity)": SLAB,
        "Red Nether Brick Slab (Itemsanity)": SLAB,
        "Daylight Detector (Itemsanity)": ITEMSANITY,
        "Red Nether Bricks (Itemsanity)": ITEMSANITY,
        "Nether Brick (Itemsanity)": ITEMSANITY,
        "Cracked Polished Blackstone Bricks (Itemsanity)": ITEMSANITY
    }, lambda state: canAccessNether(world, state) and canSmelt(world, state))

    # REQUIRES NETHER AND SMELTING AND IRON TOOLS
    create_region(world, "NetherAccessAndSmelting", "NetherAccessAndSmeltingAndIronTools", {
        "Redstone Comparator (Itemsanity)": ITEMSANITY,
        "Observer (Itemsanity)": ITEMSANITY,
        "Redstone Lamp (Itemsanity)": ITEMSANITY
    }, lambda state: canAccessNether(world, state) and canSmelt(world, state) and canUseIronTools(world, state))

    # REQUIRES SHEARS OR ENCHANTING
    create_region(world, "Menu", "ShearsOrEnchanting", {
        "Oak Leaves (Itemsanity)": ITEMSANITY,
        "Spruce Leaves (Itemsanity)": ITEMSANITY,
        "Birch Leaves (Itemsanity)": ITEMSANITY,
        "Jungle Leaves (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Acacia Leaves (Itemsanity)": ITEMSANITY,
        "Cherry Leaves (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Dark Oak Leaves (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Mangrove Leaves (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Azalea Leaves (Itemsanity)": ITEMSANITY,
        "Flowering Azalea Leaves (Itemsanity)": ITEMSANITY,
        "Cobweb (Itemsanity)": ITEMSANITY_EXPLORATION
    }, lambda state: canUseShears(world, state) or canEnchant(world, state))

    # REQUIRES END AND BOW
    create_region(world, "EndAccess", "EndAccessAndBow", {
        "Chorus Flower (Itemsanity)": ITEMSANITY
    }, lambda state: canAccessEnd(world, state) and canUseBow(world, state))

    # REQUIRES DIAMOND TOOLS AND EYES OF ENDER
    create_region(world, "HasDiamondTools", "HasDiamondToolsAndEyesOfEnder", {
        "Ender Chest (Itemsanity)": ITEMSANITY
    }, lambda state: canGetObsidian(world, state) and canGetEyesOfEnder(world, state))

    # REQUIRES SWIM OR NETHER ACCESS
    create_region(world, "Menu", "NetherAccessOrSwim", {
        "Magma Block (Itemsanity)": ITEMSANITY
    }, lambda state: canSwim(world, state) or canAccessNether(world, state))

    # REQUIRES CHESTS AND END ACCESS
    create_region(world, "EndAccess", "EndAccessAndChests", {
        "Shulker Box (Itemsanity)": ITEMSANITY,
        "Spire Armor Trim (Itemsanity)": TRIM
    }, lambda state: canAccessChests(world, state) and canAccessEnd(world, state))

    # REQUIRES CHESTS AND SMELTING
    create_region(world, "CanSmeltItems", "CanSmeltItemsAndUseChests", {
        "Hopper (Itemsanity)": ITEMSANITY,
        "Trapped Chest (Itemsanity)": ITEMSANITY
    }, lambda state: canAccessChests(world, state) and canSmelt(world, state))

    # REQUIRES BOW AND IRON TOOLS
    create_region(world, "HasIronTools", "HasIronToolsAndBow", {
        "Dispenser (Itemsanity)": ITEMSANITY
    }, lambda state: canUseIronTools(world, state) and canUseBow(world, state))

    # REQUIRES MINECART AND IRON TOOLS
    create_region(world, "HasMinecart", "HasMinecartAndIronTools", {
        "Powered Rail (Itemsanity)": ITEMSANITY,
        "Detector Rail (Itemsanity)": ITEMSANITY,
        "Activator Rail (Itemsanity)": ITEMSANITY
    }, lambda state: canUseMinecart(world, state) and canUseIronTools(world, state))


    # REQUIRES CHESTS AND IRON TOOLS
    create_region(world, "HasIronTools", "HasIronToolsAndChests", {
        "Recovery Compass (Itemsanity)": ITEMSANITY_EXPLORATION
    }, lambda state: canAccessChests(world, state) and canUseIronTools(world, state))

    # REQUIRES MINECART AND CHESTS
    create_region(world, "HasMinecart", "HasMinecartAndChests", {
        "Minecart with Chest (Itemsanity)": ITEMSANITY,
        "Minecart with Hopper (Itemsanity)": ITEMSANITY
    }, lambda state: canUseMinecart(world, state) and canAccessChests(world, state))

    # REQUIRES FISHING OR SWIM
    create_region(world, "Menu", "HasSwimOrFishing", {
        "Raw Cod (Itemsanity)": ITEMSANITY,
        "Raw Salmon (Itemsanity)": ITEMSANITY,
        "Tropical Fish (Itemsanity)": ITEMSANITY,
        "Pufferfish (Itemsanity)": ITEMSANITY
    }, lambda state: canSwim(world, state) or canUseFishingRod(world, state))

    # REQUIRES FISHING OR SWIM + SMELTING
    create_region(world, "Menu", "HasSwimOrFishingAndSmelting", {
        "Cooked Cod (Itemsanity)": ITEMSANITY,
        "Cooked Salmon (Itemsanity)": ITEMSANITY
    }, lambda state: canSmelt(world, state) and (canSwim(world, state) or canUseFishingRod(world, state)))

    # REQUIRES SHEARS AND NETHER
    create_region(world, "NetherAccess", "NetherAccessAndShears", {
        "Nether Sprouts (Itemsanity)": ITEMSANITY
    }, lambda state: canAccessNether(world, state) and canUseShears(world, state))

    # Regular Dye
    create_region(world, "Menu", "RegularDye", {
        "Red Wool (Itemsanity)": DYE,
        "Red Carpet (Itemsanity)": DYE,
        "Red Concrete (Itemsanity)": DYE,
        "Red Concrete Powder (Itemsanity)": DYE,
        "Red Dye (Itemsanity)": ITEMSANITY,
        "Red Banner (Itemsanity)": DYE,

        "Yellow Wool (Itemsanity)": DYE,
        "Yellow Carpet (Itemsanity)": DYE,
        "Yellow Concrete (Itemsanity)": DYE,
        "Yellow Concrete Powder (Itemsanity)": DYE,
        "Yellow Dye (Itemsanity)": ITEMSANITY,
        "Yellow Banner (Itemsanity)": DYE,

        "Blue Wool (Itemsanity)": DYE,
        "Blue Carpet (Itemsanity)": DYE,
        "Blue Concrete (Itemsanity)": DYE,
        "Blue Concrete Powder (Itemsanity)": DYE,
        "Blue Dye (Itemsanity)": ITEMSANITY,
        "Blue Banner (Itemsanity)": DYE,

        "White Wool (Itemsanity)": DYE,
        "White Carpet (Itemsanity)": DYE,
        "White Concrete (Itemsanity)": DYE,
        "White Concrete Powder (Itemsanity)": DYE,
        "White Dye (Itemsanity)": ITEMSANITY,
        "White Banner (Itemsanity)": DYE,

        "Firework Star (Itemsanity)": ITEMSANITY
    }, lambda state: canDyeBasic(world, state))

    # Regular Dye and Smelt
    create_region(world, "RegularDye", "RegularDyeAndSmelt", {
        "Red Terracotta (Itemsanity)": DYE,
        "Red Stained Glass (Itemsanity)": DYE,
        "Red Stained Glass Pane (Itemsanity)": DYE,
        "Red Glazed Terracotta (Itemsanity)": DYE,

        "Yellow Terracotta (Itemsanity)": DYE,
        "Yellow Stained Glass (Itemsanity)": DYE,
        "Yellow Stained Glass Pane (Itemsanity)": DYE,
        "Yellow Glazed Terracotta (Itemsanity)": DYE,

        "Blue Terracotta (Itemsanity)": DYE,
        "Blue Stained Glass (Itemsanity)": DYE,
        "Blue Stained Glass Pane (Itemsanity)": DYE,
        "Blue Glazed Terracotta (Itemsanity)": DYE,

        "White Terracotta (Itemsanity)": DYE,
        "White Stained Glass (Itemsanity)": DYE,
        "White Stained Glass Pane (Itemsanity)": DYE,
        "White Glazed Terracotta (Itemsanity)": DYE
    }, lambda state: canDyeBasic(world, state) and canSmelt(world, state))

    # Regular Dye and Shears
    create_region(world, "RegularDye", "RegularDyeAndShears", {
        "Red Candle (Itemsanity)": DYE,
        "Yellow Candle (Itemsanity)": DYE,
        "Blue Candle (Itemsanity)": DYE,
        "White Candle (Itemsanity)": DYE
    }, lambda state: canDyeBasic(world, state) and canUseShears(world, state))

    # Regular Dye and Sleep
    create_region(world, "RegularDye", "RegularDyeAndSleep", {
        "Red Bed (Itemsanity)": DYE,
        "Yellow Bed (Itemsanity)": DYE,
        "Blue Bed (Itemsanity)": DYE,
        "White Bed (Itemsanity)": DYE
    }, lambda state: canDyeBasic(world, state) and canSleep(world, state))

    # Regular Dye and End and Chests
    create_region(world, "RegularDye", "RegularDyeAndShulker", {
        "Red Shulker Box (Itemsanity)": DYE,
        "Yellow Shulker Box (Itemsanity)": DYE,
        "Blue Shulker Box (Itemsanity)": DYE,
        "White Shulker Box (Itemsanity)": DYE
    }, lambda state: canDyeBasic(world, state) and canAccessChests(world, state) and canAccessEnd(world, state))

    # Black Dye
    create_region(world, "RegularDye", "BlackDye", {
        "Black Wool (Itemsanity)": DYE,
        "Black Carpet (Itemsanity)": DYE,
        "Black Concrete (Itemsanity)": DYE,
        "Black Concrete Powder (Itemsanity)": DYE,
        "Black Dye (Itemsanity)": ITEMSANITY,
        "Black Banner (Itemsanity)": DYE,

        "Gray Wool (Itemsanity)": DYE,
        "Gray Carpet (Itemsanity)": DYE,
        "Gray Concrete (Itemsanity)": DYE,
        "Gray Concrete Powder (Itemsanity)": DYE,
        "Gray Dye (Itemsanity)": ITEMSANITY,
        "Gray Banner (Itemsanity)": DYE
    }, lambda state: canDyeBlack(world, state))

    # Black Dye and Smelt
    create_region(world, "RegularDye", "BlackDyeAndSmelt", {
        "Black Terracotta (Itemsanity)": DYE,
        "Black Stained Glass (Itemsanity)": DYE,
        "Black Stained Glass Pane (Itemsanity)": DYE,
        "Black Glazed Terracotta (Itemsanity)": DYE,

        "Gray Terracotta (Itemsanity)": DYE,
        "Gray Stained Glass (Itemsanity)": DYE,
        "Gray Stained Glass Pane (Itemsanity)": DYE,
        "Gray Glazed Terracotta (Itemsanity)": DYE
    }, lambda state: canDyeBlack(world, state) and canSmelt(world, state))

    # Black Dye and Shears
    create_region(world, "RegularDye", "BlackDyeAndShears", {
        "Black Candle (Itemsanity)": DYE,
        "Gray Candle (Itemsanity)": DYE
    }, lambda state: canDyeBlack(world, state) and canUseShears(world, state))

    # Black Dye and Sleep
    create_region(world, "RegularDye", "BlackDyeAndSleep", {
        "Black Bed (Itemsanity)": DYE,
        "Gray Bed (Itemsanity)": DYE
    }, lambda state: canDyeBlack(world, state) and canSleep(world, state))

    # Black Dye and End and Chests
    create_region(world, "RegularDye", "BlackDyeAndShulker", {
        "Black Shulker Box (Itemsanity)": DYE,
        "Gray Shulker Box (Itemsanity)": DYE
    }, lambda state: canDyeBlack(world, state) and canAccessChests(world, state) and canAccessEnd(world, state))

    # Green Dye and Smelt
    create_region(world, "RegularDye", "GreenDyeAndSmelt", {
        "Green Terracotta (Itemsanity)": DYE_AND_EXPLORATION,
        "Green Stained Glass (Itemsanity)": DYE_AND_EXPLORATION,
        "Green Stained Glass Pane (Itemsanity)": DYE_AND_EXPLORATION,
        "Green Glazed Terracotta (Itemsanity)": DYE_AND_EXPLORATION,
        "Green Wool (Itemsanity)": DYE_AND_EXPLORATION,
        "Green Carpet (Itemsanity)": DYE_AND_EXPLORATION,
        "Green Concrete (Itemsanity)": DYE_AND_EXPLORATION,
        "Green Concrete Powder (Itemsanity)": DYE_AND_EXPLORATION,
        "Green Dye (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Green Banner (Itemsanity)": DYE_AND_EXPLORATION
    }, lambda state: canDyeGreen(world, state))

    # Green Dye and Shears
    create_region(world, "RegularDye", "GreenDyeAndShears", {
        "Green Candle (Itemsanity)": DYE_AND_EXPLORATION
    }, lambda state: canUseShears(world, state) and canDyeGreen(world, state))

    # Green Dye and Sleep
    create_region(world, "RegularDye", "GreenDyeAndSleep", {
        "Green Bed (Itemsanity)": DYE_AND_EXPLORATION
    }, lambda state: canSleep(world, state) and canDyeGreen(world, state))

    # Green Dye and End and Chests
    create_region(world, "RegularDye", "GreenDyeAndShulker", {
        "Green Shulker Box (Itemsanity)": DYE_AND_EXPLORATION
    }, lambda state: canAccessChests(world, state) and canAccessEnd(world, state) and canDyeGreen(world, state))

    # Full Dye
    create_region(world, "RegularDye", "FullDye", {
        "Orange Wool (Itemsanity)": DYE,
        "Orange Carpet (Itemsanity)": DYE,
        "Orange Concrete (Itemsanity)": DYE,
        "Orange Concrete Powder (Itemsanity)": DYE,
        "Orange Dye (Itemsanity)": ITEMSANITY,
        "Orange Banner (Itemsanity)": DYE,

        "Light Blue Wool (Itemsanity)": DYE,
        "Light Blue Carpet (Itemsanity)": DYE,
        "Light Blue Concrete (Itemsanity)": DYE,
        "Light Blue Concrete Powder (Itemsanity)": DYE,
        "Light Blue Dye (Itemsanity)": ITEMSANITY,
        "Light Blue Banner (Itemsanity)": DYE,

        "Purple Wool (Itemsanity)": DYE,
        "Purple Carpet (Itemsanity)": DYE,
        "Purple Concrete (Itemsanity)": DYE,
        "Purple Concrete Powder (Itemsanity)": DYE,
        "Purple Dye (Itemsanity)": ITEMSANITY,
        "Purple Banner (Itemsanity)": DYE,

        "Pink Wool (Itemsanity)": DYE,
        "Pink Carpet (Itemsanity)": DYE,
        "Pink Concrete (Itemsanity)": DYE,
        "Pink Concrete Powder (Itemsanity)": DYE,
        "Pink Dye (Itemsanity)": ITEMSANITY,
        "Pink Banner (Itemsanity)": DYE,

        "Magenta Wool (Itemsanity)": DYE,
        "Magenta Carpet (Itemsanity)": DYE,
        "Magenta Concrete (Itemsanity)": DYE,
        "Magenta Concrete Powder (Itemsanity)": DYE,
        "Magenta Dye (Itemsanity)": ITEMSANITY,
        "Magenta Banner (Itemsanity)": DYE,

        "Light Gray Wool (Itemsanity)": DYE,
        "Light Gray Carpet (Itemsanity)": DYE,
        "Light Gray Concrete (Itemsanity)": DYE,
        "Light Gray Concrete Powder (Itemsanity)": DYE,
        "Light Gray Dye (Itemsanity)": ITEMSANITY,
        "Light Gray Banner (Itemsanity)": DYE,

        "Brown Wool (Itemsanity)": DYE_AND_EXPLORATION,
        "Brown Carpet (Itemsanity)": DYE_AND_EXPLORATION,
        "Brown Concrete (Itemsanity)": DYE_AND_EXPLORATION,
        "Brown Concrete Powder (Itemsanity)": DYE_AND_EXPLORATION,
        "Brown Dye (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Brown Banner (Itemsanity)": DYE_AND_EXPLORATION
    }, lambda state: canDyeFull(world, state))

    # Full Dye and Smelt
    create_region(world, "RegularDye", "FullDyeAndSmelt", {
        "Orange Terracotta (Itemsanity)": DYE,
        "Orange Stained Glass (Itemsanity)": DYE,
        "Orange Stained Glass Pane (Itemsanity)": DYE,
        "Orange Glazed Terracotta (Itemsanity)": DYE,

        "Light Blue Terracotta (Itemsanity)": DYE,
        "Light Blue Stained Glass (Itemsanity)": DYE,
        "Light Blue Stained Glass Pane (Itemsanity)": DYE,
        "Light Blue Glazed Terracotta (Itemsanity)": DYE,

        "Purple Terracotta (Itemsanity)": DYE,
        "Purple Stained Glass (Itemsanity)": DYE,
        "Purple Stained Glass Pane (Itemsanity)": DYE,
        "Purple Glazed Terracotta (Itemsanity)": DYE,

        "Light Gray Terracotta (Itemsanity)": DYE,
        "Light Gray Stained Glass (Itemsanity)": DYE,
        "Light Gray Stained Glass Pane (Itemsanity)": DYE,
        "Light Gray Glazed Terracotta (Itemsanity)": DYE,

        "Brown Terracotta (Itemsanity)": DYE_AND_EXPLORATION,
        "Brown Stained Glass (Itemsanity)": DYE_AND_EXPLORATION,
        "Brown Stained Glass Pane (Itemsanity)": DYE_AND_EXPLORATION,
        "Brown Glazed Terracotta (Itemsanity)": DYE_AND_EXPLORATION,

        "Pink Terracotta (Itemsanity)": DYE,
        "Pink Stained Glass (Itemsanity)": DYE,
        "Pink Stained Glass Pane (Itemsanity)": DYE,
        "Pink Glazed Terracotta (Itemsanity)": DYE,

        "Magenta Terracotta (Itemsanity)": DYE,
        "Magenta Stained Glass (Itemsanity)": DYE,
        "Magenta Stained Glass Pane (Itemsanity)": DYE,
        "Magenta Glazed Terracotta (Itemsanity)": DYE
    }, lambda state: canDyeFull(world, state) and canSmelt(world, state))

    # Full Dye and Shears
    create_region(world, "RegularDye", "FullDyeAndShears", {
        "Orange Candle (Itemsanity)": DYE,
        "Light Blue Candle (Itemsanity)": DYE,
        "Purple Candle (Itemsanity)": DYE,
        "Light Gray Candle (Itemsanity)": DYE,
        "Brown Candle (Itemsanity)": DYE_AND_EXPLORATION,
        "Pink Candle (Itemsanity)": DYE,
        "Magenta Candle (Itemsanity)": DYE
    }, lambda state: canDyeFull(world, state) and canUseShears(world, state))

    # Full Dye and Sleep
    create_region(world, "RegularDye", "FullDyeAndSleep", {
        "Orange Bed (Itemsanity)": DYE,
        "Light Blue Bed (Itemsanity)": DYE,
        "Purple Bed (Itemsanity)": DYE,
        "Light Gray Bed (Itemsanity)": DYE,
        "Brown Bed (Itemsanity)": DYE_AND_EXPLORATION,
        "Pink Bed (Itemsanity)": DYE,
        "Magenta Bed (Itemsanity)": DYE
    }, lambda state: canDyeFull(world, state) and canSleep(world, state))

    # Full Dye and End and Chests
    create_region(world, "RegularDye", "FullDyeAndShulker", {
        "Orange Shulker Box (Itemsanity)": DYE,
        "Light Blue Shulker Box (Itemsanity)": DYE,
        "Purple Shulker Box (Itemsanity)": DYE,
        "Light Gray Shulker Box (Itemsanity)": DYE,
        "Brown Shulker Box (Itemsanity)": DYE_AND_EXPLORATION,
        "Pink Shulker Box (Itemsanity)": DYE,
        "Magenta Shulker Box (Itemsanity)": DYE
    }, lambda state: canDyeFull(world, state) and canAccessChests(world, state) and canAccessEnd(world, state))

    # Lime and Cyan Dye and Smelt
    create_region(world, "RegularDye", "LimeAndCyanDyeAndSmelt", {
        "Lime Terracotta (Itemsanity)": DYE_AND_EXPLORATION,
        "Lime Stained Glass (Itemsanity)": DYE_AND_EXPLORATION,
        "Lime Stained Glass Pane (Itemsanity)": DYE_AND_EXPLORATION,
        "Lime Glazed Terracotta (Itemsanity)": DYE_AND_EXPLORATION,
        "Lime Wool (Itemsanity)": DYE_AND_EXPLORATION,
        "Lime Carpet (Itemsanity)": DYE_AND_EXPLORATION,
        "Lime Concrete (Itemsanity)": DYE_AND_EXPLORATION,
        "Lime Concrete Powder (Itemsanity)": DYE_AND_EXPLORATION,
        "Lime Dye (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Lime Banner (Itemsanity)": DYE_AND_EXPLORATION,

        "Cyan Terracotta (Itemsanity)": DYE_AND_EXPLORATION,
        "Cyan Stained Glass (Itemsanity)": DYE_AND_EXPLORATION,
        "Cyan Stained Glass Pane (Itemsanity)": DYE_AND_EXPLORATION,
        "Cyan Glazed Terracotta (Itemsanity)": DYE_AND_EXPLORATION,
        "Cyan Wool (Itemsanity)": DYE_AND_EXPLORATION,
        "Cyan Carpet (Itemsanity)": DYE_AND_EXPLORATION,
        "Cyan Concrete (Itemsanity)": DYE_AND_EXPLORATION,
        "Cyan Concrete Powder (Itemsanity)": DYE_AND_EXPLORATION,
        "Cyan Dye (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Cyan Banner (Itemsanity)": DYE_AND_EXPLORATION
    }, lambda state: canDyeFull(world, state) and canDyeGreen(world, state))

    # Lime and Cyan Dye and Shears
    create_region(world, "RegularDye", "LimeAndCyanDyeAndShears", {
        "Lime Candle (Itemsanity)": DYE_AND_EXPLORATION,
        "Cyan Candle (Itemsanity)": DYE_AND_EXPLORATION
    }, lambda state: canDyeFull(world, state) and canUseShears(world, state) and canDyeGreen(world, state))

    # Lime and Cyan Dye and Sleep
    create_region(world, "RegularDye", "LimeAndCyanDyeAndSleep", {
        "Lime Bed (Itemsanity)": DYE_AND_EXPLORATION,
        "Cyan Bed (Itemsanity)": DYE_AND_EXPLORATION
    }, lambda state: canDyeFull(world, state) and canSleep(world, state) and canDyeGreen(world, state))

    # Lime and Cyan Dye and End and Chests
    create_region(world, "RegularDye", "LimeAndCyanDyeAndShulker", {
        "Lime Shulker Box (Itemsanity)": DYE_AND_EXPLORATION,
        "Cyan Shulker Box (Itemsanity)": DYE_AND_EXPLORATION
    }, lambda state: canDyeFull(world, state) and canAccessChests(world, state) and canAccessEnd(world, state) and canDyeGreen(world, state))

    # Can Smelt and Compact
    create_region(world, "CanSmeltItems", "CanSmeltItemsAndCompact", {
        "Lantern (Itemsanity)": ITEMSANITY,
        "Chain (Itemsanity)": ITEMSANITY,
        "Oak Hanging Sign (Itemsanity)": ITEMSANITY,
        "Spruce Hanging Sign (Itemsanity)": ITEMSANITY,
        "Birch Hanging Sign (Itemsanity)": ITEMSANITY,
        "Jungle Hanging Sign (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Acacia Hanging Sign (Itemsanity)": ITEMSANITY,
        "Cherry Hanging Sign (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Dark Oak Hanging Sign (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Mangrove Hanging Sign (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Bamboo Hanging Sign (Itemsanity)": ITEMSANITY_EXPLORATION
    }, lambda state: canCompactResources(world, state) and canSmelt(world, state))

    # Can Smelt and Compact and Has Nether
    create_region(world, "CanSmeltItemsAndCompact", "CanSmeltItemsAndCompactAndNether", {
        "Crimson Hanging Sign (Itemsanity)": ITEMSANITY,
        "Warped Hanging Sign (Itemsanity)": ITEMSANITY,
        "Soul Lantern (Itemsanity)": ITEMSANITY
    }, lambda state: canCompactResources(world, state) and canSmelt(world, state) and canAccessNether(world, state))

    # Can Shear and Enchant
    create_region(world, "HasEnchanting", "HasEnchantingAndShears", {
        "Turtle Egg (Itemsanity)": ITEMSANITY
    }, lambda state: canEnchant(world, state) and canUseShears(world, state))

    # Can Use Chests and Access Nether
    create_region(world, "NetherAccess", "NetherAccessAndChests", {
        "Netherite Smithing Template (Itemsanity)": NETHERITE,
        "Snout Banner Pattern (Itemsanity)": ITEMSANITY_EXPLORATION,
        "Music Disc Pigstep (Itemsanity)": DISCS,
        "Snout Armor Trim (Itemsanity)": TRIM,
        "Rib Armor Trim (Itemsanity)": TRIM
    }, lambda state: canAccessChests(world, state) and canAccessNether(world, state))

    if "create" in world.options.enabled_mods.value:
        create_region(world, "Menu", "RedSand", {
            "Red Sandstone (Itemsanity)": ITEMSANITY,
            "Chiseled Red Sandstone (Itemsanity)": ITEMSANITY,
            "Cut Red Sandstone (Itemsanity)": ITEMSANITY,
            "Red Sandstone Stairs (Itemsanity)": STAIR,
            "Red Sandstone Wall (Itemsanity)": WALL,
            "Red Sand (Itemsanity)": ITEMSANITY,
            "Red Sandstone Slab (Itemsanity)": SLAB,
            "Cut Red Sandstone Slab (Itemsanity)": SLAB,
        }, lambda state: canCraftAndesiteAlloyCreate(world, state) and hasCogsCreate(world, state))

        # REQUIRES SMELTING
        create_region(world, "RedSand", "CanSmeltItemsRedSand", {
            "Smooth Red Sandstone (Itemsanity)": ITEMSANITY,
            "Smooth Red Sandstone Stairs (Itemsanity)": STAIR,
            "Smooth Red Sandstone Slab (Itemsanity)": SLAB,
        }, lambda state: canCraftAndesiteAlloyCreate(world, state) and hasCogsCreate(world, state) and canSmelt(world, state))
    else:
        create_region(world, "Menu", "RedSand", {
            "Red Sandstone (Itemsanity)": ITEMSANITY_EXPLORATION,
            "Chiseled Red Sandstone (Itemsanity)": ITEMSANITY_EXPLORATION,
            "Cut Red Sandstone (Itemsanity)": ITEMSANITY_EXPLORATION,
            "Red Sandstone Stairs (Itemsanity)": STAIR_AND_EXPLORATION,
            "Red Sandstone Wall (Itemsanity)": WALL_AND_EXPLORATION,
            "Red Sand (Itemsanity)": ITEMSANITY_EXPLORATION,
            "Red Sandstone Slab (Itemsanity)": SLAB_AND_EXPLORATION,
            "Cut Red Sandstone Slab (Itemsanity)": SLAB_AND_EXPLORATION,
        })

        # REQUIRES SMELTING
        create_region(world, "RedSand", "CanSmeltItemsRedSand", {
            "Smooth Red Sandstone (Itemsanity)": ITEMSANITY_EXPLORATION,
            "Smooth Red Sandstone Stairs (Itemsanity)": STAIR_AND_EXPLORATION,
            "Smooth Red Sandstone Slab (Itemsanity)": SLAB_AND_EXPLORATION,
        }, lambda state: canSmelt(world, state))




def create_region(world: FabricMinecraftWorld, region_name: str, new_region_name: str, locations: dict[str, int], rule=None):
    create_locations_and_connect(world, region_name + "VanillaItemsanity", new_region_name + "VanillaItemsanity", locations, rule)