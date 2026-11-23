# dad-joke-showdown-entry: this file IS the whole entry.
# The joke string below must stay byte-identical — it is submitted exactly as written.
JOKE = "I put a clock in my blender. Now I make smoothies in no time."

with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(JOKE)
