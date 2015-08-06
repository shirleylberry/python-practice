from nose.tools import *
from bin.app import app
from tests.tools import assert_response
from castlecrawler.map import Room
from castlecrawler.bedroom import Bedroom
from castlecrawler.armory import Armory

def test_room():
    gold = Room("GoldRoom",
        """ This room has gold in it that you can collect.
        There's a door to the north.""")
    assert_equal(gold.name, "GoldRoom")
    assert_equal(gold.paths, {})

def test_room_paths():
    center = Room("Center", "Test room in the center.")
    north = Room("North", "Test room in the north.")
    # # player = Player("Shirley", [])
    # # south = Armory(player)
    # south = Hallway()
    # center.add_paths({'north': north, 'south': south})
    # assert_equal(center.go('north'), north)
    # assert_equal(center.go('south'), south)

def test_map():
    start = Room("Start", "You can go west and down a hole.")
    west = Room("Trees", "There are trees here, you can go east.")
    down = Room("Dungeon", "It's dark down here, you can go up.")

    start.add_paths({'west': west, 'down': down})
    west.add_paths({'east': start})
    down.add_paths({'up': start})

    assert_equal(start.go('west'), west)
    assert_equal(start.go('west').go('east'), start)
    assert_equal(start.go('down').go('up'), start)