from nose.tools import *
from castleontheweb.map import *

# castle_map = """
# --------------------
# | A |    TR      B |
# |   |         |    |
# |-  ------------  --
# |         |        |
# |  BR     |    DR  |
# |                  |
# --------     -------
#        |  H  |
# """

def test_room():
    gold = Room("GoldRoom",
                """ This room has gold in it that you can collect.
                There's a door to the north.""")
    assert_equal(gold.name, "GoldRoom")
    assert_equal(gold.paths, {})


def test_room_paths():
    center = Room("Center", "Test room in the center.")
    north = Room("North", "Test room in the north.")
    south = Room("South", "Test room in the south.")

    center.add_paths({'north': north, 'south': south})
    assert_equal(center.go('north'), north)
    assert_equal(center.go('south'), south)


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

def test_castle_game_map():
    assert_equal(hallway.go("left"), bedroom)
    assert_equal(hallway.go("right"), dining_room)

    assert_equal(bedroom.go("back"), hallway)
    assert_equal(bedroom.go("forward"), armory)
    assert_equal(bedroom.go("door"), armory)

    assert_equal(armory.go("back"), bedroom)
    assert_equal(armory.go("door"), bedroom)
    assert_equal(armory.go("bomb"), death_scene)

    assert_equal(dining_room.go("forward"), barracks)
    assert_equal(dining_room.go("door"), barracks)
    assert_equal(dining_room.go("back"), hallway)

    assert_equal(barracks.go("back"), dining_room)
    assert_equal(barracks.go("attack"), death_scene)
    assert_equal(barracks.go("door"), treasure_room)
    assert_equal(barracks.go("left"), treasure_room)








