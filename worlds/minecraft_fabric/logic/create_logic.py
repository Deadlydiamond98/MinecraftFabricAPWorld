from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from worlds.minecraft_fabric import FabricMinecraftWorld

from vanilla_logic import *
from BaseClasses import CollectionState


########################################################################################################################
########################################################################################################################
# CREATE MOD LOGIC #####################################################################################################
########################################################################################################################
########################################################################################################################


# BASIC COMPONENTS #####################################################################################################

def canCraftAndesiteAlloy(world: FabricMinecraftWorld, state: CollectionState):
    return canCompactResources(world, state) and canSmelt(world, state)

def canCraftBrass(world: FabricMinecraftWorld, state: CollectionState):
    return hasMixer(world, state) and hasBlazeBurner(world, state)

def canCraftCardboard(world: FabricMinecraftWorld, state: CollectionState):
    return hasMixer(world, state) and canFillFluidWater(world, state) and hasPress(world, state)

def canCraftRoseQuartz(world: FabricMinecraftWorld, state: CollectionState):
    return canAccessNether(world, state) and canUseIronTools(world, state)

def canCraftElectronTube(world: FabricMinecraftWorld, state: CollectionState):
    return canCraftRoseQuartz(world, state) and hasPress(world, state)

def canCraftPercisionMechanism(world: FabricMinecraftWorld, state: CollectionState):
    return hasDeployer(world, state) and hasPress(world, state) and hasCogs(world, state)

def canCraftSturdySheet(world: FabricMinecraftWorld, state: CollectionState):
    return (hasCrusher(world, state) and hasPress(world, state) and hasSpout(world, state)
            and canUseBucket(world, state) and canGetObsidian(world, state))

def hasCogs(world: FabricMinecraftWorld, state: CollectionState):
    return canCraftAndesiteAlloy(world, state) and state.has("Cogwheel Recipes", world.player)

def hasBlazeBurner(world: FabricMinecraftWorld, state: CollectionState):
    return canAccessNether(world, state) and hasPress(world, state)

def canFillFluidWater(world: FabricMinecraftWorld, state: CollectionState):
    return canUseBucket(world, state) or hasPump(world, state) or canUseBottles(world, state)

def canMakeHeat(world: FabricMinecraftWorld, state: CollectionState):
    return (canUseFlintAndSteel(world, state) or canUseStoneTools(world, state) or canSmelt(world, state) or
            canUseBucket(world, state))

# POWER GENERATION #####################################################################################################

def hasWaterWheel(world: FabricMinecraftWorld, state: CollectionState):
    return canCraftAndesiteAlloy(world, state) and state.has("Water Wheel Recipes", world.player)

def hasWindmill(world: FabricMinecraftWorld, state: CollectionState):
    return canCraftAndesiteAlloy(world, state) and state.has("Windmill Recipes", world.player)

def hasSteamEngine(world: FabricMinecraftWorld, state: CollectionState):
    return (canCraftAndesiteAlloy(world, state) and state.has("Steam Engine Recipes", world.player)
            and canCompactResources(world, state) and canFillFluidTankWater(world, state) and canMakeHeat(world, state))

def hasMorePower(world: FabricMinecraftWorld, state: CollectionState):
    return hasWaterWheel(world, state) or hasWindmill(world, state) or hasSteamEngine(world, state)

# CRAFTING #############################################################################################################

def hasPress(world: FabricMinecraftWorld, state: CollectionState):
    return (state.has("Mechanical Press Recipes", world.player) and canCompactResources(world, state) and
            canCraftAndesiteAlloy(world, state))

def hasMixer(world: FabricMinecraftWorld, state: CollectionState):
    return (state.has("Mechanical Mixer Recipes", world.player) and canCraftAndesiteAlloy(world, state)
            and hasCogs(world, state) and hasPress(world, state))

def hasSaw(world: FabricMinecraftWorld, state: CollectionState):
    return hasPress(world, state)

def hasSpout(world: FabricMinecraftWorld, state: CollectionState):
    return canCraftDriedKelp(world, state) and canUseStoneTools(world, state)

def hasDeployer(world: FabricMinecraftWorld, state: CollectionState):
    return canCraftElectronTube(world, state) and canCraftBrass(world, state)

def canUseSpout(world: FabricMinecraftWorld, state: CollectionState):
    return hasSpout(world, state) and canFillFluidWater(world, state)

def hasMechanicalCrafter(world: FabricMinecraftWorld, state: CollectionState):
    return hasMorePower(world, state) and canCraftElectronTube(world, state) and canCraftBrass(world, state)

def hasCrusher(world: FabricMinecraftWorld, state: CollectionState):
    return hasMechanicalCrafter(world, state)

# FAN CRAFTING #########################################################################################################

def canWash(world: FabricMinecraftWorld, state: CollectionState):
    return hasPress(world, state) and canUseBucket(world, state)

def canHaunt(world: FabricMinecraftWorld, state: CollectionState):
    return hasPress(world, state) and canAccessNether(world, state)

# FLUID TANKS ##########################################################################################################

def hasFluidTank(world: FabricMinecraftWorld, state: CollectionState):
    return hasPress(world, state) and canAccessChests(world, state) and canSmelt(world, state)

def canFillFluidTankWater(world: FabricMinecraftWorld, state: CollectionState):
    return hasFluidTank(world, state) and canFillFluidWater(world, state)

def hasPump(world: FabricMinecraftWorld, state: CollectionState):
    return hasCogs(world, state) and hasPress(world, state)

# OTHER CHECKS #########################################################################################################

def canCraftDecorativeStone(world: FabricMinecraftWorld, state: CollectionState):
    return hasSaw(world, state) or canAccessMiscJobsites(world, state)