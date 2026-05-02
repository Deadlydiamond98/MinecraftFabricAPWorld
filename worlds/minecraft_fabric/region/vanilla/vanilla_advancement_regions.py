from __future__ import annotations


from typing import TYPE_CHECKING, Optional

from worlds.minecraft_fabric.region.mc_regions_consts import *
from worlds.minecraft_fabric.region.regions_helper import create_locations_and_connect
from worlds.minecraft_fabric.logic.vanilla_logic import *


if TYPE_CHECKING:
   from worlds.minecraft_fabric import FabricMinecraftWorld


def create_vanilla_advancement_regions(world: FabricMinecraftWorld):
    # BASE (REQUIRES NOTHING TO GET)
    create_locations_and_connect(world, "Menu", "MenuVanillaAdvancements", {
        "Stone Age": ADVANCEMENT,
        "Voluntary Exile": ADVANCEMENT,
        "Monster Hunter": ADVANCEMENT,
        "The Parrots and the Bats": ADVANCEMENT,
        "You've Got a Friend in Me": ADVANCEMENT_EXPLORATION,
        "Best Friends Forever": ADVANCEMENT,
        "A Seedy Place": ADVANCEMENT,
        "Getting Wood": ADVANCEMENT,
        "Benchmarking": ADVANCEMENT,
        "Time to Mine!": ADVANCEMENT,
        "Time to Farm!": ADVANCEMENT,
        "Bake Bread": ADVANCEMENT,
        "Time to Strike!": ADVANCEMENT,
        "Cow Tipper": ADVANCEMENT,
        "When the Squad Hops into Town": ADVANCEMENT_HARD,
        "Whatever Floats Your Goat!": ADVANCEMENT_EXPLORATION,
        "Sneak 100": ADVANCEMENT_EXPLORATION,
        "It Spreads": ADVANCEMENT_EXPLORATION
    })

    # REQUIRES NETHER ACCESS
    create_region(world, "Menu", "NetherAccess", {
        "We Need to Go Deeper": ADVANCEMENT,
        "Return to Sender": ADVANCEMENT,
        "Those Were the Days": ADVANCEMENT,
        "Subspace Bubble": ADVANCEMENT,
        "A Terrible Fortress": ADVANCEMENT,
        "Uneasy Alliance": ADVANCEMENT_HARD,
        "Spooky Scary Skeleton": ADVANCEMENT,
        "Into Fire": ADVANCEMENT,
        "The Power of Books": ADVANCEMENT,
        "With Our Powers Combined!": ADVANCEMENT_HARD,
        "Hot Tourist Destinations": ADVANCEMENT_EXPLORATION
    }, lambda state: canAccessNether(world, state))

    # REQUIRES END ACCESS
    create_region(world, "NetherAccess", "EndAccess", {
       "Free the End": ADVANCEMENT,
       "The Next Generation": ADVANCEMENT,
       "Remote Getaway": ADVANCEMENT,
       "The City at the End of the Game": ADVANCEMENT,
       "Sky's the Limit": ADVANCEMENT,
       "Great View From Up Here": ADVANCEMENT,
       "Eye Spy": ADVANCEMENT,
       "The End?": ADVANCEMENT
    }, lambda state: canAccessEnd(world, state))

    # REQUIRES STONE TOOLS
    create_region(world, "Menu", "HasStoneTools", {
        "Getting an Upgrade": ADVANCEMENT
    }, lambda state: canUseStoneTools(world, state))

    # REQUIRES LEATHER ARMOR
    create_region(world, "Menu", "HasLeatherArmor", {
        "Light as a Rabbit": ADVANCEMENT_EXPLORATION
    }, lambda state: canWearLeatherArmor(world, state))

    # REQUIRES SMELTING
    create_region(world, "Menu", "CanSmeltItems", {
        "Hot Topic": ADVANCEMENT
    }, lambda state: canSmelt(world, state))

    # REQUIRES SMELTING
    create_region(world, "HasStoneTools", "CanGetIron", {
        "Acquire Hardware": ADVANCEMENT
    }, lambda state: canGetIron(world, state))

    # REQUIRES SHIELD
    create_region(world, "CanSmeltItems", "HasShield", {
        "Not Today, Thank You": ADVANCEMENT
    }, lambda state: canUseShield(world, state))

    # REQUIRES IRON TOOLS
    create_region(world, "CanSmeltItems", "HasIronTools", {
        "Isn't It Iron Pick": ADVANCEMENT,
        "Diamonds!": ADVANCEMENT,
        "Sound of Music": ADVANCEMENT_EXPLORATION
    }, lambda state: canUseIronTools(world, state))

    # REQUIRES IRON ARMOR
    create_region(world, "CanSmeltItems", "HasIronArmor", {
        "Suit Up": ADVANCEMENT
    }, lambda state: canWearIronArmor(world, state))

    # REQUIRES DIAMOND TOOLS
    create_region(world, "HasIronTools", "HasDiamondTools", {
        "Ice Bucket Challenge": ADVANCEMENT
    }, lambda state: canUseDiamondTools(world, state))

    # REQUIRES DIAMOND ARMOR
    create_region(world, "HasIronTools", "HasDiamondArmor", {
        "Cover Me with Diamonds": ADVANCEMENT
    }, lambda state: canWearDiamondArmor(world, state))

    # REQUIRES ARMOR TRIMS
    create_region(world, "CanSmeltItems", "CanSmithItems", {
        "Crafting a New Look": ADVANCEMENT
    }, lambda state: canGetAndUseArmorTrims(world, state))

    # REQUIRES NETHERITE TOOLS
    create_region(world, "CanSmithItems", "HasNetheriteTools", {
        "Serious Dedication": ADVANCEMENT_HARD
    }, lambda state: canUseNetheriteTools(world, state))

    # REQUIRES NETHERITE Armor
    create_region(world, "CanSmithItems", "HasNetheriteArmor", {
        "Cover Me in Debris": ADVANCEMENT_HARD
    }, lambda state: canWearNetheriteArmor(world, state))

    # REQUIRES BOW
    create_region(world, "Menu", "HasBow", {
        "Take Aim": ADVANCEMENT,
        "Bullseye": ADVANCEMENT,
        "Sniper Duel": ADVANCEMENT
    }, lambda state: canUseBow(world, state))

    # REQUIRES CROSSBOW
    create_region(world, "CanSmeltItems", "HasCrossbow", {
        "Ol' Betsy": ADVANCEMENT,
        "Who's the Pillager Now?": ADVANCEMENT
    }, lambda state: canUseCrossBow(world, state))

    # REQUIRES MINECART
    create_region(world, "CanSmeltItems", "HasMinecart", {
        "On A Rail": ADVANCEMENT
    }, lambda state: canUseMinecart(world, state))

    # REQUIRES FISHING
    create_region(world, "Menu", "HasFishing", {
        "Fishy Business": ADVANCEMENT,
        "A Complete Catalogue": ADVANCEMENT_HARD
    }, lambda state: canUseFishingRod(world, state))

    # REQUIRES BRUSH
    create_region(world, "CanSmeltItems", "HasBrush", {
        "Respecting the Remnants": ADVANCEMENT,
        "Careful Restoration": ADVANCEMENT
    }, lambda state: canUseBrush(world, state))

    # REQUIRES CHESTS
    create_region(world, "Menu", "HasChests", {
        "When Pigs Fly": ADVANCEMENT,
        "Overpowered": ADVANCEMENT_EXPLORATION
    }, lambda state: canAccessChests(world, state))

    # REQUIRES TRADING
    create_region(world, "Menu", "HasTrading", {
        "What a Deal!": ADVANCEMENT
    }, lambda state: canTrade(world, state))

    # REQUIRES ENCHANTING
    create_region(world, "HasDiamondTools", "HasEnchanting", {
        "Enchanter": ADVANCEMENT,
        "Librarian": ADVANCEMENT,
        "Total Beelocation": ADVANCEMENT,
        "Surge Protector": ADVANCEMENT_HARD
    }, lambda state: canEnchant(world, state))

    # REQUIRES BUCKET
    create_region(world, "CanSmeltItems", "HasBucket", {
        "Birthday Song": ADVANCEMENT,
        "Hot Stuff": ADVANCEMENT,
        "The Lie": ADVANCEMENT,
        "Bukkit Bukkit": ADVANCEMENT_EXPLORATION
    }, lambda state: canUseBucket(world, state))

    # REQUIRES BREWING
    create_region(world, "NetherAccess", "HasBrewing", {
        "Local Brewery": ADVANCEMENT,
        "A Furious Cocktail": ADVANCEMENT_HARD
    }, lambda state: canBrew(world, state))

    # ZOMBIE DOCTOR
    create_region(world, "HasBrewing", "CanCureZombieVillager", {
        "Zombie Doctor": ADVANCEMENT
    }, lambda state: canCureZombieVillager(world, state))

    # REQUIRES BARTERING
    create_region(world, "NetherAccess", "HasBartering", {
        "Oh Shiny": ADVANCEMENT
    }, lambda state: canBarter(world, state))

    # REQUIRES SLEEP
    create_region(world, "Menu", "HasSleep", {
        "Sweet Dreams": ADVANCEMENT
    }, lambda state: canSleep(world, state))

    # REQUIRES SPYGLASS
    create_region(world, "CanSmeltItems", "HasSpyglass", {
        "Is It a Bird?": ADVANCEMENT_EXPLORATION
    }, lambda state: canUseSpyglass(world, state))

    # REQUIRES GLASS BOTTLES
    create_region(world, "CanSmeltItems", "HasBottles", {
        "Sticky Situation": ADVANCEMENT,
        "Bee Our Guest": ADVANCEMENT
    }, lambda state: canUseBottles(world, state))

    # REQUIRES SWIMMING
    create_region(world, "Menu", "HasSwim", {
        "A Throwaway Joke": ADVANCEMENT,
        "Glow and Behold!": ADVANCEMENT,
        "The Healing Power of Friendship!": ADVANCEMENT
    }, lambda state: canSwim(world, state))

    # REQUIRES WITHER SUMMONING
    create_region(world, "NetherAccess", "CanSummonWither", {
        "Withering Heights": ADVANCEMENT
    }, lambda state: canGoalWither(world, state))

    # REQUIRES BEACON
    create_region(world, "CanSummonWither", "CanUseBeacon", {
        "Bring Home the Beacon": ADVANCEMENT,
        "Beaconator": ADVANCEMENT_HARD
    }, lambda state: canPlaceBeacon(world, state))

    # REQUIRES CRYING OBSIDIAN
    create_region(world, "HasBartering", "CanGetCryingObsidian", {
        "Who is Cutting Onions?": ADVANCEMENT,
        "Not Quite \"Nine\" Lives": ADVANCEMENT
    }, lambda state: canGetCryingObsidian(world, state))

    # REQUIRES RAIDS
    create_locations_and_connect(world, "MenuVanillaAdvancements", "CanFightRaid", {
        "Hero of the Village": ADVANCEMENT,
        "Postmortal": ADVANCEMENT_EXPLORATION
    }, lambda state: canFightRaid(world, state))

    ####################################################################################################################
    # MULTIPLE CHECKS ##################################################################################################
    ####################################################################################################################

    # REQUIRES CROSSBOW AND ENCHANTING
    create_region(world, "HasCrossbow", "HasCrossbowAndEnchanting", {
        "Arbalistic": ADVANCEMENT_HARD,
        "Two Birds, One Arrow": ADVANCEMENT_HARD
    }, lambda state: canUseCrossBow(world, state) and canEnchant(world, state))

    # REQUIRES TRADING AND BUCKETS
    create_region(world, "HasTrading", "HasTradingAndBuckets", {
        "Star Trader": ADVANCEMENT
    }, lambda state: canTrade(world, state) and canUseBucket(world, state))

    # REQUIRES SWIMMING AND ENCHANTING
    create_region(world, "HasEnchanting", "HasSwimAndEnchanting", {
        "Very Very Frightening": ADVANCEMENT_HARD
    }, lambda state: canSwim(world, state) and canEnchant(world, state))

    # REQUIRES SWIMMING AND BRUSH
    create_region(world, "HasBrush", "HasSwimAndBrush", {
        "Smells Interesting": ADVANCEMENT,
        "Little Sniffs": ADVANCEMENT_HARD,
        "Planting the Past": ADVANCEMENT_HARD
    }, lambda state: canSwim(world, state) and canUseBrush(world, state))

    # REQUIRES FISHING AND SMELTING
    create_region(world, "CanSmeltItems", "CanSmeltItemsAndHasFishing", {
        "Delicious Fish": ADVANCEMENT
    }, lambda state: canSmelt(world, state) and canUseFishingRod(world, state))

    # REQUIRES NETHERITE NO SMITHING
    create_region(world, "HasDiamondTools", "NetheriteNoSmithing", {
        "Country Lode, Take Me Home": ADVANCEMENT
    }, lambda state: canSmelt(world, state) and canAccessNether(world, state) and canUseDiamondTools(world, state))

    # REQUIRES SHEARS AND COMPACTING
    create_region(world, "CanSmeltItems", "HasShearsAndCompacting", {
        "Wax On": ADVANCEMENT,
        "Wax Off": ADVANCEMENT
    }, lambda state: canUseShears(world, state) and canCompactResources(world, state))

    # REQUIRES BUCKET AND SWIM
    create_region(world, "HasBucket", "HasBucketAndSwim", {
        "Caves & Cliffs": ADVANCEMENT,
        "Tactical Fishing": ADVANCEMENT,
        "The Cutest Predator": ADVANCEMENT
    }, lambda state: canUseBucket(world, state) and canSwim(world, state))

    # REQUIRES SPYGLASS AND NETHER
    create_region(world, "HasSpyglass", "HasSpyglassNether", {
        "Is It a Balloon?": ADVANCEMENT
    }, lambda state: canUseSpyglass(world, state) and canAccessNether(world, state))

    # REQUIRES SPYGLASS AND END
    create_region(world, "HasSpyglass", "HasSpyglassEnd", {
        "Is It a Plane?": ADVANCEMENT
    }, lambda state: canUseSpyglass(world, state) and canAccessEnd(world, state))

    # REQUIRES COMPACTING AND SMELTING
    create_region(world, "CanSmeltItems", "CanSmeltAndCanCompact", {
        "Hired Help": ADVANCEMENT
    }, lambda state: canGetIron(world, state) and canCompactResources(world, state) and canUseShears(world, state))

    # REQUIRES NETHER AND FISHING ROD AND CHESTS
    create_region(world, "NetherAccess", "NetherAccessAndFishingRodAndChests", {
        "This Boat Has Legs": ADVANCEMENT,
        "Feels Like Home": ADVANCEMENT_HARD
    }, lambda state: canAccessNether(world, state) and canUseFishingRod(world, state) and canAccessChests(world, state))

    # REQUIRES END AND SMELTING
    create_region(world, "EndAccess", "EndAccessAndSmelting", {
        "The End... Again...": ADVANCEMENT
    }, lambda state: canAccessEnd(world, state) and canSmelt(world, state))

    # REQUIRES END AND GLASS BOTTLES AND SMELTING
    create_region(world, "EndAccessAndSmelting", "EndAccessAndGlassBottles", {
        "You Need a Mint": ADVANCEMENT
    }, lambda state: canAccessEnd(world, state) and canSmelt(world, state) and canUseBottles(world, state))

    # REQUIRES VANILLA END GAME
    create_region(world, "EndAccess", "VanillaEndGame", {
        "Overkill": ADVANCEMENT,
        "Monsters Hunted": ADVANCEMENT_HARD,
        "Smithing with Style": ADVANCEMENT_UNREASONABLE,
        "Two by Two": ADVANCEMENT_HARD,
        "A Balanced Diet": ADVANCEMENT_HARD,
        "Adventuring Time": ADVANCEMENT_UNREASONABLE,
        "How Did We Get Here?": ADVANCEMENT_UNREASONABLE
    }, lambda state: canAccessVanillaEndGame(world, state))

    # REQUIRES NETHER AND CHESTS
    create_region(world, "NetherAccess", "NetherAccessAndChests", {
        "War Pigs": ADVANCEMENT
    }, lambda state: canAccessNether(world, state) and canAccessChests(world, state))

    # REQUIRES NETHER + DIAMOND TOOLS OR CHESTS
    create_region(world, "NetherAccess", "NetherAccessGetDebree", {
        "Hidden in the Depths": ADVANCEMENT
    }, lambda state: canAccessNether(world, state) and (canAccessChests(world, state) or canUseDiamondTools(world, state)))



def create_region(world: FabricMinecraftWorld, region_name: str, new_region_name: str, locations: dict[str, int], rule=None):
    create_locations_and_connect(world, region_name + "VanillaAdvancements", new_region_name + "VanillaAdvancements", locations, rule)