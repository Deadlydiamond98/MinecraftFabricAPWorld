from dataclasses import dataclass

from Options import PerGameCommonOptions, Choice, Range, ItemSet, OptionSet, OptionGroup, Toggle


# GOAL CONDITION #######################################################################################################

class GoalCondition(Choice):
    """
    Your Goal Condition for your game

    ender_dragon - Goal when the Ender Dragon is defeated
    wither - Goal when the Wither is defeated
    both_bosses - Goal when the Ender Dragon and Wither is defeated
    advancements_only - Goal when you collect a certain amount of Advancements
    ruby_hunt - Goal when a certain amount of rubies are collected (McGuffin hunt)
    ("RUBY HUNT" AND "ADVANCEMENT ONLY" CURRENTLY NOT IMPLEMENTED)
    """
    option_ender_dragon = 0
    option_wither = 1
    option_both_bosses = 2
    option_advancements_only = 3
    option_ruby_hunt = 4
    default = 0
#
# class AdvancementsToGoal(Range):
#     """
#     Determines the Percentage of Advancements needed to goal the game
#     """
#     display_name = "Advancements to Goal"
#     range_start = 0
#     range_end = 100
#     default = 50
#
class ExcludeHardAdvancements(Toggle):
    """
    Makes it so hard Advancements (such as "How Did We Get Here?" will not have checks)
    """
    display_name = "Exclude Hard Advancements"
    default = True
#
# class RubyPercentage(Range):
#     """
#     The Amount of Rubies Needed in order to goal
#     """
#     display_name = "Rubies Needed"
#     range_start = 0
#     range_end = 100
#     default = 0
#
# class TotalRubyPercentage(Range):
#     """
#     Replaces a Percentage of Junk and Trap items in the pool with Rubies
#     """
#     display_name = "Ruby Fill Percentage"
#     range_start = 0
#     range_end = 100
#     default = 0

# ABILITIES ############################################################################################################

class RandomizeSwim(Toggle):
    """Removes the ability to enter water, and adds a Swim Item to the pool."""
    display_name = "Randomize Swim"
    default = False

class RandomizeSprint(Toggle):
    """Removes the ability to Sprint, and adds a Sprint Item to the pool."""
    display_name = "Randomize Sprint"
    default = False

# TRAP STUFF ###########################################################################################################

class TrapFillPercentage(Range):
    """
    Replace a percentage of junk items in the item pool with random traps
    """
    display_name = "Trap Fill Percentage"
    range_start = 0
    range_end = 100
    default = 0

class BaseTrapWeight(Choice):
    """
    Base Class for Trap Weights
    """
    option_none = 0
    option_low = 1
    option_medium = 2
    option_high = 4
    default = 2

class ReverseControlsTrapWeight(BaseTrapWeight):
    """
    Likelihood of a receiving a trap which causes WASD, Shift, Jump, Break, and Place to Swap for a short duration
    """
    display_name = "Reverse Controls Trap Weight"

class InvertedMouseTrapWeight(BaseTrapWeight):
    """
    Likelihood of a receiving a trap which causes the Mouse to Invert for a short duration
    """
    display_name = "Inverted Mouse Trap Weight"

class IceTrapWeight(BaseTrapWeight):
    """
    Likelihood of a receiving a trap which causes all blocks to become slippery for a short duration
    """
    display_name = "Ice Trap Weight"

class RandomEffectTrapWeight(BaseTrapWeight):
    """
    Likelihood of a receiving a trap which applies a random Negative Status Effect
    """
    display_name = "Random Status Effect Trap Weight"

class StunTrapWeight(BaseTrapWeight):
    """
    Likelihood of a receiving a trap that temporarily stops movement of the player
    """
    display_name = "Stun Trap Weight"

class TNTTrapWeight(BaseTrapWeight):
    """
    Likelihood of a receiving a trap that spawns a block of lit TNT on the player's position
    """
    display_name = "TNT Trap Weight"

class TeleportTrapWeight(BaseTrapWeight):
    """
    Likelihood of a receiving a trap that Teleports the player similar to Chorus Fruit
    """
    display_name = "Teleport Trap Weight"

class BeeTrapWeight(BaseTrapWeight):
    """
    Likelihood of a receiving a trap that Spawns 6 angry bees near the player
    """
    display_name = "Bee Trap Weight"

class LiteratureTrapWeight(BaseTrapWeight):
    """
    Likelihood of a receiving a trap that Opens Literature Pop-Ups
    """
    display_name = "Literature Trap Weight"


# class EnabledMods(OptionSet):
#     """List Compatible Mods here to include their checks in the game"""
#     display_name = "Mods"
#     rich_text_doc = True

@dataclass
class FMCOptions(PerGameCommonOptions):
    # Goal Related Options
    goal_condition: GoalCondition
    exclude_hard_advancements: ExcludeHardAdvancements
    # extra_rubies: ExtraRubyPercentage
    # Abilities
    randomize_swim: RandomizeSwim
    randomize_sprint: RandomizeSprint
    # Traps
    trap_fill_percentage: TrapFillPercentage
    reverseControlsTrapWeight: ReverseControlsTrapWeight
    invertedMouseTrapWeight: InvertedMouseTrapWeight
    iceTrapWeight: IceTrapWeight
    randomEffectTrapWeight: RandomEffectTrapWeight
    stunTrapWeight: StunTrapWeight
    tntTrapWeight: TNTTrapWeight
    teleportTrapWeight: TeleportTrapWeight
    beeTrapWeight: BeeTrapWeight
    literatureTrapWeight: LiteratureTrapWeight

