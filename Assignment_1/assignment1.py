import sqlite3

conn = sqlite3.connect('rpg_db.sqlite3')

curs = conn.cursor()

#Q: How many total Characters are there?

query_1 = """
SELECT count(distinct character_id) as char_count
FROM charactercreator_character_inventory
"""

answer_1 = curs.execute(query_1).fetchall()
#breakpoint()
#answer_1x = answer_1[0]["char_count"]

print(f"There are {answer_1} characters.")
#_____________________________________

#Q: How many of each specific subclass?
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
query_2e = """
SELECT count(distinct mage_ptr_id) as char_count_necro
FROM charactercreator_necromancer
"""
answer_2a = curs.execute(query_2a).fetchall()
answer_2b = curs.execute(query_2b).fetchall()
answer_2c = curs.execute(query_2c).fetchall()
answer_2d = curs.execute(query_2d).fetchall()
answer_2e = curs.execute(query_2e).fetchall()

print(f"There are {answer_2a} mages, {answer_2b} thieves, {answer_2c} clerics, {answer_2d} fighters, and {answer_2e} necromancers.")
#_____________________________________

#Q: How many total Items?

query_3 = """
SELECT count(distinct item_id) as item_count
FROM armory_item
"""
answer_3 = curs.execute(query_3).fetchall()
print(f"There are {answer_3} items.")
#_____________________________________

#Q: How many of the Items are weapons? How many are not?

#quick count on weapons armory
query_4 = """
SELECT count(distinct item_ptr_id) as weapon_count
FROM armory_weapon
"""
#subtract all items from weapons armory
query_5 = """
SELECT
	count(distinct armory_item.item_id) - count(distinct armory_weapon.item_ptr_id)
FROM armory_item, armory_weapon
"""
#answers
answer_4 = curs.execute(query_4).fetchall()
answer_5 = curs.execute(query_5).fetchall()
print(f"Out of all the items, {answer_4} are weapons and {answer_5} are not weapons.")
#_____________________________________

#Q: How many Items does each character have? (Return first 20 rows)

query_6 = """
SELECT
	character_id, count(character_id) as total_items
FROM charactercreator_character_inventory
group by character_id
LIMIT 20
"""
#answer
answer_6 = curs.execute(query_6).fetchall()
print(f"This is a list of the first 20 characters and the amount of items they have: {answer_6}")
#_____________________________________

#Q: How many Weapons does each character have? (Return first 20 rows)

query_7 = """
SELECT
	inv.character_id, count(character_id) as total_weapons
FROM charactercreator_character_inventory as inv
join armory_weapon as aw on aw.item_ptr_id = inv.item_id
GROUP by character_id
LIMIT 20
"""
#answer
answer_7 = curs.execute(query_7).fetchall()
print(f"This is a list of the first 20 characters and how many weapons they have: {answer_7}")
#_____________________________________

#Q: On average, how many items does each character have?
query_8 = """
SELECT 
	cast(count(distinct item_id)AS FLOAT) / count(distinct character_id) as Avg_items_per_char
FROM charactercreator_character_inventory as char_inv
"""
#answer
answer_8 = curs.execute(query_8).fetchall()
print(f"On average, each character has {answer_8} items.")
#_____________________________________

#Q: On average, how many weapons does each character have?
query_9 = """
SELECT
	cast(count(distinct ifnull(item_ptr_id,NULL))AS FLOAT) / count(distinct character_id) as avg_weapons_per_char
FROM charactercreator_character_inventory as inv
LEFT JOIN armory_weapon as aw on aw.item_ptr_id = inv.item_id
"""
#answer
answer_9 = curs.execute(query_9).fetchall()
print(f"On average, each character has {answer_9} weapons.")