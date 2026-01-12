from dataclasses import dataclass

from Options import Toggle, PerGameCommonOptions


class TestToggle(Toggle):
    """This is a Test Toggle"""
    display_name = "Test Toggle"

@dataclass
class FMCOptions(PerGameCommonOptions):
    test_toggle: TestToggle

