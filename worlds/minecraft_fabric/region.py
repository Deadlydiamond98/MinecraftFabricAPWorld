from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from worlds.minecraft_fabric.vanilla_logic import *

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
        return canGoalEnderDragon(world, state)
    elif goal_id == 1: # Wither
        return canGoalWither(world, state)
    elif goal_id == 2: # Both Bosses
        return canBeatDragonAndWither(world, state)
    elif goal_id == 4: # Ruby Hunt
        return canCompleteRubyHunt(world, state)

    # Since Advancements are Locations, just make game try to reach end of game
    return canAccessVanillaEndGame(world, state)


def create_regions(world: FabricMinecraftWorld):
    # Menu Region (always available)
    create_locations_advanced(world, "Menu", {
        "Stone Age": 0,
        "Voluntary Exile": 0,
        "Monster Hunter": 0,
        "The Parrots and the Bats": 0,
        "You've Got a Friend in Me": 0,
        "Best Friends Forever": 0,
        "A Seedy Place": 0,
        "Hero of the Village": 0,
        "Postmortal": 0,
        "Getting Wood": 0,
        "Benchmarking": 0,
        "Time to Mine!": 0,
        "Time to Farm!": 0,
        "Bake Bread": 0,
        "Time to Strike!": 0,
        "Cow Tipper": 0,
        "When the Squad Hops into Town": 1,
        "Whatever Floats Your Goat!": 2,
        "Sneak 100": 2,
        "It Spreads": 2
    })

    # REQUIRES NETHER ACCESS
    create_locations_and_connect(world, "Menu", "NetherAccess", {
        "We Need to Go Deeper": 0,
        "Return to Sender": 0,
        "Those Were the Days": 0,
        "Subspace Bubble": 0,
        "A Terrible Fortress": 0,
        "Uneasy Alliance": 0,
        "Spooky Scary Skeleton": 0,
        "Into Fire": 0,
        "The Power of Books": 0,
        "With Our Powers Combined!": 1,
        "Hot Tourist Destinations": 2
    }, lambda state: canAccessNether(world, state))

    # REQUIRES END ACCESS
    create_locations_and_connect(world, "NetherAccess", "EndAccess", {
        "Free the End": 0,
        "The Next Generation": 0,
        "Remote Getaway": 0,
        "The City at the End of the Game": 0,
        "Sky's the Limit": 0,
        "Great View From Up Here": 0,
        "Eye Spy": 0,
        "The End?": 0
    }, lambda state: canAccessEnd(world, state))

    # REQUIRES STONE TOOLS
    create_locations_and_connect(world, "Menu", "HasStoneTools", {
        "Getting an Upgrade": 0
    },  lambda state: canUseStoneTools(world, state))

    # REQUIRES LEATHER ARMOR
    create_locations_and_connect(world, "Menu", "HasLeatherArmor", {
        "Light as a Rabbit": 2
    }, lambda state: canWearLeatherArmor(world, state))

    # REQUIRES SMELTING
    create_locations_and_connect(world, "HasStoneTools", "CanSmeltItems", {
        "Acquire Hardware": 0,
        "Hot Topic": 0,
        "Surge Protector": 1
    }, lambda state: canSmelt(world, state))


    # REQUIRES SHIELD
    create_locations_and_connect(world, "CanSmeltItems", "HasShield", {
        "Not Today, Thank You": 0
    }, lambda state: canUseShield(world, state))

    # REQUIRES IRON TOOLS
    create_locations_and_connect(world, "CanSmeltItems", "HasIronTools", {
        "Isn't It Iron Pick": 0,
        "Diamonds!": 0,
        "Sound of Music": 2
    }, lambda state: canUseIronTools(world, state))

    # REQUIRES IRON ARMOR
    create_locations_and_connect(world, "CanSmeltItems", "HasIronArmor", {
        "Suit Up": 0
    }, lambda state: canWearIronArmor(world, state))

    # REQUIRES DIAMOND TOOLS
    create_locations_and_connect(world, "HasIronTools", "HasDiamondTools", {
        "Ice Bucket Challenge": 0
    }, lambda state: canUseDiamondTools(world, state))

    # REQUIRES DIAMOND ARMOR
    create_locations_and_connect(world, "HasIronTools", "HasDiamondArmor", {
        "Cover Me with Diamonds": 0
    }, lambda state: canWearDiamondArmor(world, state))

    # REQUIRES ARMOR TRIMS
    create_locations_and_connect(world, "CanSmeltItems", "CanSmithItems", {
        "Crafting a New Look": 0
    }, lambda state: canGetAndUseArmorTrims(world, state))

    # REQUIRES NETHERITE TOOLS
    create_locations_and_connect(world, "CanSmithItems", "HasNetheriteTools", {
        "Serious Dedication": 1
    }, lambda state: canUseNetheriteTools(world, state))

    # REQUIRES NETHERITE TOOLS
    create_locations_and_connect(world, "CanSmithItems", "HasNetheriteArmor", {
        "Cover Me in Debris": 1
    }, lambda state: canWearNetheriteArmor(world, state))

    # REQUIRES BOW
    create_locations_and_connect(world, "Menu", "HasBow", {
        "Take Aim": 0,
        "Bullseye": 0,
        "Sniper Duel": 0
    }, lambda state: canUseBow(world, state))

    # REQUIRES CROSSBOW
    create_locations_and_connect(world, "CanSmeltItems", "HasCrossbow", {
        "Ol' Betsy": 0,
        "Who's the Pillager Now?": 0,
        "Arbalistic": 0,
        "Two Birds, One Arrow": 1
    }, lambda state: canUseCrossBow(world, state))

    # REQUIRES MINECART
    create_locations_and_connect(world, "CanSmeltItems", "HasMinecart", {
        "On A Rail": 0
    }, lambda state: canUseMinecart(world, state))

    # REQUIRES FISHING
    create_locations_and_connect(world, "Menu", "HasFishing", {
        "Fishy Business": 0,
        "A Complete Catalogue": 1
    }, lambda state: canUseFishingRod(world, state))

    # REQUIRES BRUSH
    create_locations_and_connect(world, "CanSmeltItems", "HasBrush", {
        "Respecting the Remnants": 0,
        "Careful Restoration": 0
    }, lambda state: canUseBrush(world, state))

    # REQUIRES CHESTS
    create_locations_and_connect(world, "Menu", "HasChests", {
        "When Pigs Fly": 0,
        "Overpowered": 2
    }, lambda state: canAccessChests(world, state))

    # REQUIRES TRADING
    create_locations_and_connect(world, "Menu", "HasTrading", {
        "What a Deal!": 0,
        "Star Trader": 0
    }, lambda state: canTrade(world, state))

    # REQUIRES ENCHANTING
    create_locations_and_connect(world, "HasDiamondTools", "HasEnchanting", {
        "Enchanter": 0,
        "Librarian": 0,
        "Total Beelocation": 0
    }, lambda state: canEnchant(world, state))

    # REQUIRES BUCKET
    create_locations_and_connect(world, "CanSmeltItems", "HasBucket", {
        "Birthday Song": 0,
        "Hot Stuff": 0,
        "The Lie": 0,
        "Bukkit Bukkit": 2
    }, lambda state: canUseBucket(world, state))

    # REQUIRES BREWING
    create_locations_and_connect(world, "NetherAccess", "HasBrewing", {
        "Local Brewery": 0,
        "Zombie Doctor": 0,
        "A Furious Cocktail": 1
    }, lambda state: canBrew(world, state))

    # REQUIRES BARTERING
    create_locations_and_connect(world, "NetherAccess", "HasBartering", {
        "Oh Shiny": 0
    }, lambda state: canBarter(world, state))

    # REQUIRES SLEEP
    create_locations_and_connect(world, "Menu", "HasSleep", {
        "Sweet Dreams": 0
    }, lambda state: canSleep(world, state))

    # REQUIRES SPYGLASS
    create_locations_and_connect(world, "CanSmeltItems", "HasSpyglass", {
        "Is It a Bird?": 0
    }, lambda state: canUseSpyglass(world, state))

    # REQUIRES GLASS BOTTLES
    create_locations_and_connect(world, "CanSmeltItems", "HasBottles", {
        "Sticky Situation": 0,
        "Bee Our Guest": 0
    }, lambda state: canUseBottles(world, state))

    # REQUIRES SWIMMING
    create_locations_and_connect(world, "Menu", "HasSwim", {
        "A Throwaway Joke": 0,
        "Glow and Behold!": 0,
        "The Healing Power of Friendship!": 0
    }, lambda state: canSwim(world, state))

    # REQUIRES WITHER SUMMONING
    create_locations_and_connect(world, "NetherAccess", "CanSummonWither", {
        "Withering Heights": 0
    }, lambda state: canGoalWither(world, state))

    # REQUIRES BEACON
    create_locations_and_connect(world, "CanSummonWither", "CanUseBeacon", {
        "Bring Home the Beacon": 0,
        "Beaconator": 1
    }, lambda state: canPlaceBeacon(world, state))

    # REQUIRES CRYING OBSIDIAN
    create_locations_and_connect(world, "HasBartering", "CanGetCryingObsidian", {
        "Who is Cutting Onions?": 0,
        "Not Quite \"Nine\" Lives": 0
    }, lambda state: canGetCryingObsidian(world, state))


    ####################################################################################################################
    # MULTIPLE CHECKS ##################################################################################################
    ####################################################################################################################

    # REQUIRES SWIMMING AND ENCHANTING
    create_locations_and_connect(world, "HasEnchanting", "HasSwimAndEnchanting", {
        "Very Very Frightening": 1
    }, lambda state: canSwim(world, state) and canEnchant(world, state))

    # REQUIRES SWIMMING AND BRUSH
    create_locations_and_connect(world, "HasBrush", "HasSwimAndBrush", {
        "Smells Interesting": 0,
        "Little Sniffs": 1,
        "Planting the Past": 1
    }, lambda state: canSwim(world, state) and canUseBrush(world, state))

    # REQUIRES FISHING AND SMELTING
    create_locations_and_connect(world, "CanSmeltItems", "CanSmeltItemsAndHasFishing", {
        "Delicious Fish": 0
    }, lambda state: canSmelt(world, state) and canUseFishingRod(world, state))

    # REQUIRES NETHERITE NO SMITHING
    create_locations_and_connect(world, "HasDiamondTools", "NetheriteNoSmithing", {
        "Country Lode, Take Me Home": 0
    }, lambda state: canSmelt(world, state) and canAccessNether(world, state) and canUseDiamondTools(world, state))

    # REQUIRES SHEARS AND COMPACTING
    create_locations_and_connect(world, "CanSmeltItems", "HasShearsAndCompacting", {
        "Wax On": 0,
        "Wax Off": 0
    }, lambda state: canUseShears(world, state) and canCompactResources(world, state))

    # REQUIRES BUCKET AND SWIM
    create_locations_and_connect(world, "HasBucket", "HasBucketAndSwim", {
        "Caves & Cliffs": 0,
        "Tactical Fishing": 0,
        "The Cutest Predator": 0
    }, lambda state: canUseBucket(world, state) and canSwim(world, state))

    # REQUIRES SPYGLASS AND NETHER
    create_locations_and_connect(world, "HasSpyglass", "HasSpyglassNether", {
        "Is It a Balloon?": 0
    }, lambda state: canUseSpyglass(world, state) and canAccessNether(world, state))

    # REQUIRES SPYGLASS AND END
    create_locations_and_connect(world, "HasSpyglass", "HasSpyglassEnd", {
        "Is It a Plane?": 0
    }, lambda state: canUseSpyglass(world, state) and canAccessEnd(world, state))

    # REQUIRES COMPACTING AND SMELTING
    create_locations_and_connect(world, "CanSmeltItems", "CanSmeltAndCanCompact", {
        "Hired Help": 0
    }, lambda state: canSmelt(world, state) and canCompactResources(world, state))

    # REQUIRES NETHER AND FISHING ROD AND CHESTS
    create_locations_and_connect(world, "NetherAccess", "NetherAccessAndFishingRodAndChests", {
        "This Boat Has Legs": 0,
        "Feels Like Home": 1
    }, lambda state: canAccessNether(world, state) and canUseFishingRod(world, state) and canAccessChests(world, state))

    # REQUIRES END AND SMELTING
    create_locations_and_connect(world, "EndAccess", "EndAccessAndSmelting", {
        "The End... Again...": 0
    }, lambda state: canAccessEnd(world, state) and canSmelt(world, state))

    # REQUIRES END AND GLASS BOTTLES AND SMELTING
    create_locations_and_connect(world, "EndAccessAndSmelting", "EndAccessAndGlassBottles", {
        "You Need a Mint": 0
    }, lambda state: canAccessEnd(world, state) and canSmelt(world, state) and canUseBottles(world, state))

    # REQUIRES VANILLA END GAME
    create_locations_and_connect(world, "EndAccess", "VanillaEndGame", {
        "Overkill": 0,
        "Monsters Hunted": 1,
        "Smithing with Style": 1,
        "Two by Two": 1,
        "A Balanced Diet": 1,
        "Adventuring Time": 3,
        "How Did We Get Here?": 3
    }, lambda state: canAccessVanillaEndGame(world, state))

    # REQUIRES NETHER AND CHESTS
    create_locations_and_connect(world, "NetherAccess", "NetherAccessAndChests", {
        "War Pigs": 0
    }, lambda state: canAccessNether(world, state) and canAccessChests(world, state))

    # REQUIRES NETHER + DIAMOND TOOLS OR CHESTS
    create_locations_and_connect(world, "NetherAccess", "NetherAccessGetDebree", {
        "Hidden in the Depths": 0
    }, lambda state: canAccessNether(world, state) and (canAccessChests(world, state) or canUseDiamondTools(world, state)))

    world.multiworld.completion_condition[world.player] = lambda state: get_goal_condition(world, state)

# Helper Methods #######################################################################################################

def create_locations_advanced(world: FabricMinecraftWorld, region_name: str, locations: dict[str, int]):
    location_list = []

    for location, type in locations.items():
        if type == 1 and world.options.exclude_hard_advancements:
            continue
        if type == 2 and world.options.exclude_exploration_advancements:
            continue
        elif type == 3 and world.options.exclude_unreasonable_advancements:
            continue

        location_list.append(location)

    return create_locations(world, region_name, location_list)

def create_locations(world: FabricMinecraftWorld, region_name: str, locations: list[str]):
    region = Region(region_name, world.player, world.multiworld, region_name)
    region.locations += [Location(world.player, name, location_table[name], region) for name in locations]
    world.multiworld.regions.append(region)

def connect(world, source: str, target: str, rule=None, reach: Optional[bool] = False,
            rule_to_str: Optional[str] = None, ) -> Optional[Entrance]:
    source_region = world.multiworld.get_region(source, world.player)
    target_region = world.multiworld.get_region(target, world.player)

    connection = Entrance(world.player, source + " ==> " + target, source_region)

    if rule:
        connection.access_rule = rule

    source_region.exits.append(connection)
    connection.connect(target_region)

    return connection if reach else None


def create_locations_and_connect(world: FabricMinecraftWorld, region_name: str, new_region_name: str, locations: dict[str, int], rule=None, reach: Optional[bool] = False,
            rule_to_str: Optional[str] = None, ):
    create_locations_advanced(world, new_region_name, locations)
    connect(world, region_name, new_region_name, rule)

