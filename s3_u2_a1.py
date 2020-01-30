import sqlite3

conn = sqlite3.connect('rpg_db.sqlite3')

curs = conn.cursor()

query_1 = """
SELECT count(distinct character_id) as char_count
FROM charactercreator_character_inventory
"""

answer_1 = curs.execute(query_1).fetchall()
#breakpoint()
#answer_1x = answer_1[0]["char_count"]

print(f"There are {answer_1} characters.")

#mage, thief, cleric, fighter

query_2a = """
SELECT count(distinct character_ptr_id) as char_count_mage
FROM charactercreator_mage
"""
query_2b = """
SELECT count(distinct character_ptr_id) as char_count_thief
FROM charactercreator_thief
"""
query_2c = """
SELECT count(distinct character_ptr_id) as char_count_cleric
FROM charactercreator_cleric
"""
query_2d = """
SELECT count(distinct character_ptr_id) as char_count_fighter
FROM charactercreator_fighter
"""
answer_2a = curs.execute(query_2a).fetchall()
answer_2b = curs.execute(query_2b).fetchall()
answer_2c = curs.execute(query_2c).fetchall()
answer_2d = curs.execute(query_2d).fetchall()

print(f"There are {answer_2a} mages, {answer_2b} thieves, {answer_2c} clerics, and {answer_2d} fighters.")

query_3 = """
SELECT count(distinct item_id) as item_count
FROM armory_item
"""
answer_3 = curs.execute(query_3).fetchall()
print(f"There are {answer_3} items.")

query_4 = """
SELECT count(distinct item_ptr_id) as weapon_count
FROM armory_weapon
"""
query_5 = """

"""

answer_4 = curs.execute(query_4).fetchall()
answer_5 = curs.execute(query_5).fetchall()
print(f"Out of all the items, {answer_4} are weapons and {answer_5} are not weapons.")




