from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from worlds.minecraft_fabric.region_checks import *

if TYPE_CHECKING:
    from worlds.minecraft_fabric import FabricMinecraftWorld

from BaseClasses import Region, Location, CollectionState, Entrance
from worlds.minecraft_fabric.locations import location_table


########################################################################################################################
# Create Regions #######################################################################################################
########################################################################################################################

def get_goal_condition(world, state):
    goal_id = world.options.goal_condition.value

    # I wish Python had Switch Case Statements :,(
    if goal_id == 0: # Ender Dragon
        return canAccessEnd(world, state)
    elif goal_id == 1: # Wither
        return canSummonWither(world, state)
    elif goal_id == 2: # Both Bosses
        return canAccessEnd(world, state) and canSummonWither(world, state)
    elif goal_id == 4: # Ruby Hunt
        return canCompleteRubyHunt(world, state)

    # Since Advancements are Locations, just make game try to reach end of game
    return canAccessVanillaEndGame(world, state)


def create_regions(world: FabricMinecraftWorld):
    # Menu Region (always available)
    create_locations_advanced(world, "Menu", [
        "Stone Age",
        "Voluntary Exile",
        "Monster Hunter",
        "The Parrots and the Bats",
        "You've Got a Friend in Me",
        "Best Friends Forever",
        "A Seedy Place",
        "Hero of the Village",
        "Postmortal",
        "Getting Wood",
        "Benchmarking",
        "Time to Mine!",
        "Time to Farm!",
        "Bake Bread",
        "Time to Strike!",
        "Cow Tipper"
    ], [
        "When the Squad Hops into Town"
    ], [
        "Whatever Floats Your Goat!",
        "Sneak 100",
        "It Spreads"
    ])

    # REQUIRES NETHER ACCESS
    create_locations_and_connect(world, "Menu", "NetherAccess", [
        "We Need to Go Deeper",
        "Return to Sender",
        "Those Were the Days",
        "Subspace Bubble",
        "A Terrible Fortress",
        "Uneasy Alliance",
        "Spooky Scary Skeleton",
        "Into Fire",
        "The Power of Books"
    ], [
        "With Our Powers Combined!"
    ], [
        "Hot Tourist Destinations"
    ], lambda state: canAccessNether(world, state))

    # REQUIRES END ACCESS
    create_locations_and_connect(world, "NetherAccess", "EndAccess", [
        "Free the End",
        "The Next Generation",
        "Remote Getaway",
        "The City at the End of the Game",
        "Sky's the Limit",
        "Great View From Up Here",
        "Eye Spy",
        "The End?"
    ], [], [], lambda state: canAccessEnd(world, state))

    # REQUIRES STONE TOOLS
    create_locations_and_connect(world, "Menu", "HasStoneTools", [
        "Getting an Upgrade"
    ], [], [],  lambda state: canUseStoneTools(world, state))

    # REQUIRES LEATHER ARMOR
    create_locations_and_connect(world, "Menu", "HasLeatherArmor", [
        "Light as a Rabbit"
    ], [], [], lambda state: canWearLeatherArmor(world, state))

    # REQUIRES SMELTING
    create_locations_and_connect(world, "HasStoneTools", "CanSmeltItems", [
        "Acquire Hardware",
        "Hot Topic"
    ], [
        "Surge Protector"
    ], [], lambda state: canSmelt(world, state))


    # REQUIRES SHIELD
    create_locations_and_connect(world, "CanSmeltItems", "HasShield", [
        "Not Today, Thank You"
    ], [], [], lambda state: canUseShield(world, state))

    # REQUIRES IRON TOOLS
    create_locations_and_connect(world, "CanSmeltItems", "HasIronTools", [
        "Isn't It Iron Pick",
        "Diamonds!"
    ], [], [
        "Sound of Music"
    ], lambda state: canUseIronTools(world, state))

    # REQUIRES IRON ARMOR
    create_locations_and_connect(world, "CanSmeltItems", "HasIronArmor", [
        "Suit Up"
    ], [], [], lambda state: canWearIronArmor(world, state))

    # REQUIRES DIAMOND TOOLS
    create_locations_and_connect(world, "HasIronTools", "HasDiamondTools", [
        "Ice Bucket Challenge"
    ], [], [], lambda state: canUseDiamondTools(world, state))

    # REQUIRES DIAMOND ARMOR
    create_locations_and_connect(world, "HasIronTools", "HasDiamondArmor", [
        "Cover Me with Diamonds"
    ], [], [], lambda state: canWearDiamondArmor(world, state))

    # REQUIRES SMITHING
    create_locations_and_connect(world, "CanSmeltItems", "CanSmithItems", [
        "Crafting a New Look"
    ], [], [], lambda state: canSmith(world, state))

    # REQUIRES NETHERITE TOOLS
    create_locations_and_connect(world, "CanSmithItems", "HasNetheriteTools", [
        "Serious Dedication"
    ], [], [], lambda state: canUseNetheriteTools(world, state))

    # REQUIRES NETHERITE TOOLS
    create_locations_and_connect(world, "CanSmithItems", "HasNetheriteArmor", [
        "Cover Me in Debris"
    ], [], [], lambda state: canWearNetheriteArmor(world, state))

    # REQUIRES BOW
    create_locations_and_connect(world, "Menu", "HasBow", [
        "Take Aim",
        "Bullseye"
    ], [
        "Sniper Duel"
    ], [], lambda state: canUseBow(world, state))

    # REQUIRES CROSSBOW
    create_locations_and_connect(world, "CanSmeltItems", "HasCrossbow", [
        "Ol' Betsy",
        "Who's the Pillager Now?",
        "Arbalistic"
    ], [
        "Two Birds, One Arrow",
    ], [], lambda state: canUseCrossBow(world, state))

    # REQUIRES MINECART
    create_locations_and_connect(world, "CanSmeltItems", "HasMinecart", [
        "On A Rail"
    ], [], [], lambda state: canUseMinecart(world, state))

    # REQUIRES FISHING
    create_locations_and_connect(world, "Menu", "HasFishing", [
        "Fishy Business"
    ], [
        "A Complete Catalogue"
    ], [], lambda state: canUseFishingRod(world, state))

    # REQUIRES BRUSH
    create_locations_and_connect(world, "CanSmeltItems", "HasBrush", [
        "Respecting the Remnants",
        "Careful Restoration"
    ], [], [], lambda state: canUseBrush(world, state))

    # REQUIRES CHESTS
    create_locations_and_connect(world, "Menu", "HasChests", [
        "When Pigs Fly"
    ], [], [
        "Overpowered"
    ], lambda state: canAccessChests(world, state))

    # REQUIRES TRADING
    create_locations_and_connect(world, "Menu", "HasTrading", [
        "What a Deal!",
        "Star Trader"
    ], [], [], lambda state: canTrade(world, state))

    # REQUIRES ENCHANTING
    create_locations_and_connect(world, "HasDiamondTools", "HasEnchanting", [
        "Enchanter",
        "Librarian",
        "Total Beelocation"
    ], [], [], lambda state: canEnchant(world, state))

    # REQUIRES BUCKET
    create_locations_and_connect(world, "CanSmeltItems", "HasBucket", [
        "Birthday Song",
        "Hot Stuff",
        "The Lie"
    ], [], [
        "Bukkit Bukkit"
    ], lambda state: canUseBucket(world, state))

    # REQUIRES BREWING
    create_locations_and_connect(world, "NetherAccess", "HasBrewing", [
        "Local Brewery",
        "Zombie Doctor"
    ], [
        "A Furious Cocktail"
    ], [], lambda state: canBrew(world, state))

    # REQUIRES BARTERING
    create_locations_and_connect(world, "NetherAccess", "HasBartering", [
        "Oh Shiny"
    ], [], [], lambda state: canBarter(world, state))

    # REQUIRES SLEEP
    create_locations_and_connect(world, "Menu", "HasSleep", [
        "Sweet Dreams"
    ], [], [], lambda state: canSleep(world, state))

    # REQUIRES SPYGLASS
    create_locations_and_connect(world, "CanSmeltItems", "HasSpyglass", [
        "Is It a Bird?"
    ], [], [], lambda state: canUseSpyglass(world, state))

    # REQUIRES GLASS BOTTLES
    create_locations_and_connect(world, "CanSmeltItems", "HasBottles", [
        "Sticky Situation",
        "Bee Our Guest"
    ], [], [], lambda state: canUseBottles(world, state))

    # REQUIRES SWIMMING
    create_locations_and_connect(world, "Menu", "HasSwim", [
        "A Throwaway Joke",
        "Glow and Behold!",
        "The Healing Power of Friendship!"
    ], [], [], lambda state: canSwim(world, state))

    # REQUIRES WITHER SUMMONING
    create_locations_and_connect(world, "NetherAccess", "CanSummonWither", [
        "Withering Heights"
    ], [], [], lambda state: canSummonWither(world, state))

    # REQUIRES BEACON
    create_locations_and_connect(world, "CanSummonWither", "CanUseBeacon", [
        "Bring Home the Beacon"
    ], [
        "Beaconator"
    ], [], lambda state: canPlaceBeacon(world, state))

    # REQUIRES CRYING OBSIDIAN
    create_locations_and_connect(world, "HasBartering", "CanGetCryingObsidian", [
        "Who is Cutting Onions?",
        "Not Quite \"Nine\" Lives"
    ], [], [], lambda state: canGetCryingObsidian(world, state))


    ####################################################################################################################
    # MULTIPLE CHECKS ##################################################################################################
    ####################################################################################################################

    # REQUIRES SWIMMING AND ENCHANTING
    create_locations_and_connect(world, "HasEnchanting", "HasSwimAndEnchanting", [
    ], [
        "Very Very Frightening"
    ], [], lambda state: canSwim(world, state) and canEnchant(world, state))

    # REQUIRES SWIMMING AND BRUSH
    create_locations_and_connect(world, "HasBrush", "HasSwimAndBrush", [
        "Smells Interesting"
    ], [
        "Little Sniffs",
        "Planting the Past"
    ], [], lambda state: canSwim(world, state) and canUseBrush(world, state))

    # REQUIRES FISHING AND SMELTING
    create_locations_and_connect(world, "CanSmeltItems", "CanSmeltItemsAndHasFishing", [
        "Delicious Fish"
    ], [], [], lambda state: canSmelt(world, state) and canUseFishingRod(world, state))

    # REQUIRES NETHERITE NO SMITHING
    create_locations_and_connect(world, "HasDiamondTools", "NetheriteNoSmithing", [
        "Country Lode, Take Me Home"
    ], [], [], lambda state: canSmelt(world, state) and canAccessNether(world, state) and canUseDiamondTools(world, state))

    # REQUIRES SHEARS AND COMPACTING
    create_locations_and_connect(world, "CanSmeltItems", "HasShearsAndCompacting", [
        "Wax On",
        "Wax Off"
    ], [], [], lambda state: canUseShears(world, state) and canCompactResources(world, state))

    # REQUIRES BUCKET AND SWIM
    create_locations_and_connect(world, "HasBucket", "HasBucketAndSwim", [
        "Caves & Cliffs",
        "Tactical Fishing",
        "The Cutest Predator"
    ], [], [], lambda state: canUseBucket(world, state) and canSwim(world, state))

    # REQUIRES SPYGLASS AND NETHER
    create_locations_and_connect(world, "HasSpyglass", "HasSpyglassNether", [
        "Is It a Balloon?"
    ], [], [], lambda state: canUseSpyglass(world, state) and canAccessNether(world, state))

    # REQUIRES SPYGLASS AND END
    create_locations_and_connect(world, "HasSpyglass", "HasSpyglassEnd", [
        "Is It a Plane?"
    ], [], [], lambda state: canUseSpyglass(world, state) and canAccessEnd(world, state))

    # REQUIRES COMPACTING AND SMELTING
    create_locations_and_connect(world, "CanSmeltItems", "CanSmeltAndCanCompact", [
        "Hired Help"
    ], [], [], lambda state: canSmelt(world, state) and canCompactResources(world, state))

    # REQUIRES NETHER AND FISHING ROD
    create_locations_and_connect(world, "NetherAccess", "NetherAccessAndFishingRod", [
        "This Boat Has Legs",
        "Feels Like Home"
    ], [], [], lambda state: canAccessNether(world, state) and canUseFishingRod(world, state))

    # REQUIRES END AND SMELTING
    create_locations_and_connect(world, "EndAccess", "EndAccessAndSmelting", [
        "The End... Again..."
    ], [], [], lambda state: canAccessEnd(world, state) and canSmelt(world, state))

    # REQUIRES END AND GLASS BOTTLES AND SMELTING
    create_locations_and_connect(world, "EndAccessAndSmelting", "EndAccessAndGlassBottles", [
        "You Need a Mint"
    ], [], [], lambda state: canAccessEnd(world, state) and canSmelt(world, state) and canUseBottles(world, state))

    # REQUIRES VANILLA END GAME
    create_locations_and_connect(world, "EndAccess", "VanillaEndGame", [
        "Overkill"
    ], [
        "Monsters Hunted",
        "How Did We Get Here?",
        "Smithing with Style",
        "Adventuring Time",
        "Two by Two",
        "A Balanced Diet"
    ], [], lambda state: canAccessVanillaEndGame(world, state))

    # REQUIRES NETHER AND CHESTS
    create_locations_and_connect(world, "NetherAccess", "NetherAccessAndChests", [
        "War Pigs"
    ], [], [], lambda state: canAccessNether(world, state) and canAccessChests(world, state))

    world.multiworld.completion_condition[world.player] = lambda state: get_goal_condition(world, state)

# Helper Methods #######################################################################################################

def create_locations_advanced(world: FabricMinecraftWorld, region_name: str, locations: list[str], hard_locations: list[str], exploration_locations: list[str]):
    location_list = locations

    if not world.options.exclude_hard_advancements:
        location_list += hard_locations

    if not world.options.exclude_exploration_advancements:
        location_list += exploration_locations

    return create_locations(world, region_name, location_list)

def create_locations(world: FabricMinecraftWorld, region_name: str, locations: list[str]):
    region = Region(region_name, world.player, world.multiworld, region_name)
    region.locations += [Location(world.player, name, location_table[name], region) for name in locations]
    world.multiworld.regions.append(region)

def connect(world, source: str, target: str, rule=None, reach: Optional[bool] = False,
            rule_to_str: Optional[str] = None, ) -> Optional[Entrance]:
    source_region = world.multiworld.get_region(source, world.player)
    target_region = world.multiworld.get_region(target, world.player)

    connection = Entrance(world.player, source + " -> " + target, source_region)

    if rule:
        connection.access_rule = rule

    source_region.exits.append(connection)
    connection.connect(target_region)

    return connection if reach else None

def create_locations_and_connect(world: FabricMinecraftWorld, region_name: str, new_region_name: str, locations: list[str], hard_locations: list[str], exploration_locations: list[str], rule=None, reach: Optional[bool] = False,
            rule_to_str: Optional[str] = None, ):
    create_locations_advanced(world, new_region_name, locations, hard_locations, exploration_locations)
    connect(world, region_name, new_region_name, rule)
