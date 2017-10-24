def dead(reason, death_count):
    print('')
    print(reason, "Rip in peace.")
    death_count = death_count + 1
    start_game(True, False, False, )
    # "Rip in peace" = rip squared? idk...


space = "-" * 80

map_pic = """
-------------
| O | X | X |
| X | X | O |
| O | O | O |
-------------
"""
