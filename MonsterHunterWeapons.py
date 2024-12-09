from collections import deque

class CraftingHashTable:
    def __init__(self, size=64):
        self.size = size
        self.table = [[] for _ in range(size)]
        self.num_items = 0
        self.load_factor_threshold = 0.7
        self.upgrade_paths = {}
   
    def _hash(self, key):
        hash_value = 0
        for char in str(key):
            hash_value = (hash_value * 31 + ord(char)) % self.size
        return hash_value
   
    def _resize(self):
        old_table = self.table
        self.size *= 2
        self.table = [[] for _ in range(self.size)]
        self.num_items = 0
       
        for bucket in old_table:
            for key, value in bucket:
                self.insert(key, value)
   
    def insert(self, item, materials):
        if self.num_items / self.size >= self.load_factor_threshold:
            self._resize()
           
        hash_value = self._hash(item)
       
        for i, (existing_item, _) in enumerate(self.table[hash_value]):
            if existing_item == item:
                self.table[hash_value][i] = (item, materials)
                return
       
        self.table[hash_value].append((item, materials))
        self.num_items += 1
   
    def get_materials(self, item):
        hash_value = self._hash(item)
       
        for existing_item, materials in self.table[hash_value]:
            if existing_item == item:
                return materials
        return None
   
    def remove(self, item):
        hash_value = self._hash(item)
       
        for i, (existing_item, _) in enumerate(self.table[hash_value]):
            if existing_item == item:
                self.table[hash_value].pop(i)
                self.num_items -= 1
                return True
        return False

    def add_upgrade_path(self, base_item, upgraded_item):
        self.upgrade_paths[base_item] = upgraded_item

    def get_upgrade(self, item):
        return self.upgrade_paths.get(item)
   
    def display_all_recipes(self):
        recipes = []
        for bucket in self.table:
            for item, materials in bucket:
                recipes.append((item, materials))
        return recipes

    def display_upgrade_path(self):
        for item, materials in self.display_all_recipes():
            upgrade = self.get_upgrade(item)
            if upgrade:
                print(f"{item}: {materials} -> Upgrades to: {upgrade}")
            else:
                print(f"{item}: {materials}")

def insert_with_quantities(self, item, materials_dict):
    if self.num_items / self.size >= self.load_factor_threshold:
        self._resize()

    hash_value = self._hash(item)
    materials_list = [f"{qty} {material}" for material, qty in materials_dict.items()]

    for i, (existing_item, _) in enumerate(self.table[hash_value]):
        if existing_item == item:
            self.table[hash_value][i] = (item, materials_list)
            return

    self.table[hash_value].append((item, materials_list))
    self.num_items += 1

CraftingHashTable.insert_with_quantities = insert_with_quantities
crafting_table = CraftingHashTable()

class CraftingHistory:
    def __init__(self, max_size=10):
        self.stack = []
        self.max_size = max_size

    def add_craft(self, item):
        if len(self._stack) >= self._max_size:
            self._stack.pop(0)
        self._stack.append(item)

    def undo_last_craft(self):
        if self._stack:
            return self._stack.pop()
        return None
   
    def peek_last_craft(self):
        return self._stack[-1] if self._stack else None

class CraftingQueue:
    def __init__(self):
        self._queue = deque()

    def add_to_queue(self, item):
        self._queue.append(item)

    def remove_from_queue(self, item):
        self.queue.pop(item)

    def next_to_craft(self):
        return self._queue.popleft() if self._queue else None
   
    def peek_queue(self):
        return self._queue[0] if self._queue else None

crafting_table.insert_with_quantities("Defender Rally Horn I", {"Iron Ore": 1})
crafting_table.insert_with_quantities("Defender Rally Horn II", {"Anjanath Scale": 1})
crafting_table.add_upgrade_path("Defender Rally Horn I", "Defender Rally Horn II")
crafting_table.insert_with_quantities("Defender Rally Horn III", {"Commendation": 1})
crafting_table.add_upgrade_path("Defender Rally Horn II", "Defender Rally Horn III")
crafting_table.insert_with_quantities("Defender Rally Horn IV", {"Pink Rathian Scale+": 1})
crafting_table.add_upgrade_path("Defender Rally Horn III", "Defender Rally Horn IV")
crafting_table.insert_with_quantities("Defender Rally Horn V", {"Immortal Dragonscale": 1})
crafting_table.add_upgrade_path("Defender Rally Horn IV", "Defender Rally Horn V")
crafting_table.insert_with_quantities("Metal Bagpipe I", {"Iron Ore": 1})
crafting_table.insert_with_quantities("Metal Bagpipe II", {"Iron Ore": 1})
crafting_table.add_upgrade_path("Metal Bagpipe I", "Metal Bagpipe II")
crafting_table.insert_with_quantities("Metal Bagpipe III", {"Earth Crystal": 2, "Machalite Ore": 2, "Iron Ore": 5})
crafting_table.add_upgrade_path("Metal Bagpipe II", "Metal Bagpipe III")
crafting_table.insert_with_quantities("Kula Duda I", {"Kulu-Ya-Ku Beak": 1, "Kulu-Ya-Ku Hide": 2, "Kulu-Ya-Ku Scale": 3})
crafting_table.add_upgrade_path("Metal Bagpipe II", "Kula Duda I")
crafting_table.insert_with_quantities("Kula Duda II", {"Radobaan Scale": 3, "Kulu-Ya-Ku Beak": 2, "Kulu-Ya-Ku Plume": 2, "Boulder Bone": 3})
crafting_table.add_upgrade_path("Kula Duda I", "Kula Duda II")
crafting_table.insert_with_quantities("Kula Duda III", {"Odogaron Claw": 2, "Kulu-Ya-Ku Beak": 2, "Kulu-Ya-Ku Plume": 4, "Warped Bone": 3})
crafting_table.add_upgrade_path("Kula Duda II", "Kula Duda III")
crafting_table.insert_with_quantities("Dancing Duval I", {"Kulu-Ya-Ku Beak+": 3, "Kulu-Ya-Ku Hide+": 4, "Kulu-Ya-Ku Scale+": 6})
crafting_table.add_upgrade_path("Kula Duda III", "Dancing Duval I")
crafting_table.insert_with_quantities("Dancing Duval II", {"Odogaron Claw+": 2, "Kulu-Ya-Ku Beak+": 4, "Kulu-Ya-Ku Plume+": 3, "Brutal Bone": 3})
crafting_table.add_upgrade_path("Dancing Duval I", "Dancing Duval II")
crafting_table.insert_with_quantities("Dancing Duval III", {"Nergigante Talon": 2, "Kulu-Ya-Ku Beak+": 5, "Kulu-Ya-Ku Plume+": 4, "Bird Wyvern Gem": 1})
crafting_table.add_upgrade_path("Dancing Duval II", "Dancing Duval III")
crafting_table.insert_with_quantities("Taghrid Al-Nasr I", {"Large Kulu-Ya-Ku Beak": 1, "Kulu-Ya-Ku Thickhide": 2, "Kulu-Ya-Ku Shard": 3, "Thick Bone": 2})
crafting_table.add_upgrade_path("Dancing Duval III", "Taghrid Al-Nasr I")
crafting_table.insert_with_quantities("Taghrid Al-Nasr II", {"Nargacuga Hardfang": 2, "Large Kulu-Ya-Ku Beak": 2, "Large Kulu-Ya-Ku Plume": 3, "Monster Slogbone": 3})
crafting_table.add_upgrade_path("Taghrid Al-Nasr I", "Taghrid Al-Nasr II")
crafting_table.insert_with_quantities("Aqua Bagpipe I", {"Earth Crystal": 3, "Jyuratodus Shell": 1, "Jyuratodus Scale": 3, "Aqua Sac": 1})
crafting_table.add_upgrade_path("Metal Bagpipe II", "Aqua Bagpipe I")
crafting_table.insert_with_quantities("Aqua Bagpipe II", {"Dragonite Ore": 5, "Jyuratodus Fin": 3, "Jyuratodus Fang": 2, "Gajau Skin": 3})
crafting_table.add_upgrade_path("Aqua Bagpipe I", "Aqua Bagpipe II")
crafting_table.insert_with_quantities("Aqua Bagpipe III", {"Monster Bone+": 2, "Jyuratodus Fang": 4, "Coral Crystal": 3, "Gajau Whisker": 3})
crafting_table.add_upgrade_path("Aqua Bagpipe II", "Aqua Bagpipe III")
crafting_table.insert_with_quantities("Water Tamtam I", {"Carbalite Ore": 5, "Jyuratodus Carapace": 2, "Jyuratodus Scale+": 3, "Gajau Scale": 5})
crafting_table.add_upgrade_path("Aqua Bagpipe III", "Water Tamtam I")
crafting_table.insert_with_quantities("Water Tamtam II", {"Fucium Ore": 5, "Jyuratodus Fin+": 4, "Torrent Sac": 3, "Grand Gajau Whisker": 3})
crafting_table.add_upgrade_path("Water Tamtam I", "Water Tamtam II")
crafting_table.insert_with_quantities("Water Tamtam III", {"Elder Dragon Bone": 4, "Jyuratodus Fin+": 6, "Jyuratodus Fang+": 5, "Wyvern Gem": 1})
crafting_table.add_upgrade_path("Water Tamtam II", "Water Tamtam III")
crafting_table.insert_with_quantities("Water Tamtam IV", {"Jyuratodus Grandfin": 1, "Jyuratodus Hardfang": 1, "Jyuratodus Shard": 3, "Gajau Thickhide": 2})
crafting_table.add_upgrade_path("Water Tamtam III", "Water Tamtam IV")
crafting_table.insert_with_quantities("Laguna Drum I", {"Coral Pukei-Pukei Shard": 3, "Coral Pukei-Pukei Fellwing": 2, "Flood Sac": 2, "Bathycite Ore": 2})
crafting_table.add_upgrade_path("Water Tamtam IV", "Laguna Drum I")
crafting_table.insert_with_quantities("Laguna Drum II", {"Acidic Glavenus Hardfang": 2, "Monster Solidbone": 3, "Large Coral Pukei-Pukei Sac": 1, "Coral Pukei-Pukei Lash": 1})
crafting_table.add_upgrade_path("Laguna Drum I", "Laguna Drum II")
crafting_table.insert_with_quantities("Hidden Harmonic", {"Nargacuga Hardfang": 2, "Nargacuga Shard": 3, "Nargacuga Tailspear": 2, "Meldspar Ore": 1})
crafting_table.add_upgrade_path("Water Tamtam IV", "Hidden Harmonic")
crafting_table.insert_with_quantities("Hidden Harmonic+", {"Fulgur Anjanath Hardfang": 3, "Nargacuga Cutwing+": 4, "Nargacuga Lash": 1, "Nargacuga Mantle": 1})
crafting_table.add_upgrade_path("Hidden Harmonic", "Hidden Harmonic+")
crafting_table.insert_with_quantities("Cry In The Night", {"Shadowpierce Fang": 2, "Nargacuga Cutwing+": 4, "Nargacuga Hardfang": 4, "Purecrystal": 1})
crafting_table.add_upgrade_path("Hidden Harmonic+", "Cry In The Night")
crafting_table.insert_with_quantities("Glacial Bagpipe I", {"Legiana Claw": 3, "Legiana Scale": 4, "Frost Sac": 2})
crafting_table.add_upgrade_path("Aqua Bagpipe II", "Glacial Bagpipe I")
crafting_table.insert_with_quantities("Glacial Bagpipe II", {"Paolumu Wing": 4, "Legiana Claw": 4, "Legiana Tail Webbing": 3, "Legiana Plate": 1})
crafting_table.add_upgrade_path("Glacial Bagpipe I", "Glacial Bagpipe II")
crafting_table.insert_with_quantities("Sectored", {"Legiana Claw+": 3, "Legiana Scale": 5, "Legiana Wing": 3, "Freezer Sac": 2})
crafting_table.add_upgrade_path("Glacial Bagpipe II", "Sectored")
crafting_table.insert_with_quantities("Legia Sectored", {"Daora Claw+": 2, "Legiana Claw+": 5, "Legiana Hide+": 3, "Legiana Gem": 1})
crafting_table.add_upgrade_path("Sectored", "Legia Sectored")
crafting_table.insert_with_quantities("Legia Sectored+", {"Legiana Hardclaw": 3, "Legiana Shard": 4, "Legiana Tail Webbing+": 1, "Frozen Bone": 4})
crafting_table.add_upgrade_path("Legia Sectored", "Legia Sectored+")
crafting_table.insert_with_quantities("Hoarcry Sectored", {"Obsidian Icetalon": 2, "Rimed Hide": 5, "Stark Wing": 2, "Cryo Sac": 4})
crafting_table.add_upgrade_path("Legia Sectored+", "Hoarcry Sectored")
crafting_table.insert_with_quantities("Lilim Glacia", {"Velkhana Hardclaw": 2, "Obsidian Icetalon": 4, "Stark Wing": 2, "Legiana Mantle": 1})
crafting_table.add_upgrade_path("Hoarcry Sectored", "Lilim Glacia")
crafting_table.insert_with_quantities("Valkyrie Chordmaker", {"Rathian Spike": 3, "Rathian Scale": 5, "Rathian Shell": 4, "Poison Sac": 3})
crafting_table.add_upgrade_path("Kula Duda I", "Valkyrie Chordmaker")
crafting_table.insert_with_quantities("Queen Chordmaker", {"Rathian Spike+": 3, "Rathian Scale+": 5, "Rathian Carapace": 4, "Rathian Plate": 1})
crafting_table.add_upgrade_path("Valkyrie Chordmaker", "Queen Chordmaker")
crafting_table.insert_with_quantities("Coral Chordmaker", {"Rathian Spike+": 4, "Pink Rathian Scale+": 5, "Pink Rathian Carapace": 4, "Wyvern Gem": 1})
crafting_table.add_upgrade_path("Queen Chordmaker", "Coral Chordmaker")
crafting_table.insert_with_quantities("Royal Chordmaker", {"Elder Dragon Blood": 3, "Rathian Spike+": 5, "Pink Rathian Scale+": 6, "Rathian Ruby": 1})
crafting_table.add_upgrade_path("Coral Chordmaker", "Royal Chordmaker")
crafting_table.insert_with_quantities("Royal Chordmaker+", {"Rathian Surspike": 3, "Rathian Shard": 5, "Rathian Cortex": 4})
crafting_table.add_upgrade_path("Royal Chordmaker", "Royal Chordmaker+")
crafting_table.insert_with_quantities("Regal Flute", {"Monster Solidbone": 5, "Pink Rathian Shard": 4, "Pink Rathian Cortex": 3, "Rathian Mantle": 1})
crafting_table.add_upgrade_path("Royal Chordmaker+", "Roegal Flute")
crafting_table.insert_with_quantities("Gold Chordmaker", {"Gold Rathian Surspike": 3, "Gold Rathian Shard": 5, "Gold Rathian Cortex": 4, "Rath Gleam": 1})
crafting_table.add_upgrade_path("Royal Chordmaker+", "Gold Chordmaker")
crafting_table.insert_with_quantities("Striped Dragonga", {"Tigrex Hardclaw": 3, "Tigrex Shard": 4, "Monster Slogbone": 3, "Thick Bone": 5})
crafting_table.add_upgrade_path("Taghrid Al-Nasr II", "Striped Dragonga")
crafting_table.insert_with_quantities("Striped Dragonga+", {"Blackcurl Stouthorn": 2, "Tigrex Hardfang": 4, "Tigrex Lash": 1, "Tigrex Mantle": 1})
crafting_table.add_upgrade_path("Striped Dragonga", "Striped Dragonga+")
crafting_table.insert_with_quantities("Tigrex Horn", {"Daora Hardclaw": 2, "Tigrex Hardfang": 2, "Tigrex Cortex": 4, "Pure Dragon Blood": 5})
crafting_table.add_upgrade_path("Striped Dragonga+", "Tigrex Horn")
crafting_table.insert_with_quantities("Accursed Wail", {"Brute Tigrex Hardclaw": 3, "Brute Tigrex Shard": 5, "Brute Tigrex Hardfang": 2, "Large Wyvern Gem": 1})
crafting_table.add_upgrade_path("Tigrex Horn", "Accursed Wail")
crafting_table.insert_with_quantities("Ogrebite", {"Tempered Ebonjaw": 5, "Brute Tigrex Hardclaw": 4, "Brute Tigrex Hardfang": 3, "Tigrex Mantle": 1})
crafting_table.add_upgrade_path("Accursed Wail", "Ogrebite")
crafting_table.insert_with_quantities("Thunder Gaida I", {"Dragonite Ore": 5, "Tobi-Kadachi Electrode": 1, "Tobi-Kadachi Claw": 2, "Electro Sac": 1})
crafting_table.add_upgrade_path("Metal Bagpipe III", "Thunder Gaida I")
crafting_table.insert_with_quantities("Thunder Gaida II", {"Monster Bone+": 2, "Tobi-Kadachi Electrode": 2, "Tobi-Kadachi Membrane": 2, "Coral Crystal": 3})
crafting_table.add_upgrade_path("Thunder Gaida I", "Thunder Gaida II")
crafting_table.insert_with_quantities("Lightning Drum I", {"Carbalite Ore": 5, "Tobi-Kadachi Scale+": 4, "Tobi-Kadachi Pelt+": 3, "Vespoid Innerwing": 3})
crafting_table.add_upgrade_path("Thunder Gaida II", "Lightning Drum I")
crafting_table.insert_with_quantities("Lightning Drum II", {"Fucium Ore": 5, "Tobi-Kadachi Electrode+": 2, "Tobi-Kadachi Membrane": 4, "Thunder Sac": 3})
crafting_table.add_upgrade_path("Lightning Drum I", "Lightning Drum II")
crafting_table.insert_with_quantities("Lightning Drum III", {"Elder Dragon Blood": 3, "Tobi-Kadachi Electrode+": 4, "Tobi-Kadachi Claw+": 6, "Wyvern Gem": 1})
crafting_table.add_upgrade_path("Lightning Drum II", "Lightning Drum III")
crafting_table.insert_with_quantities("Lightning IV", {"Tobi-Kadachi Hardclaw+": 1, "Tobi-Kadachi Shard": 2, "Tobi-Kadachi Thickfur": 2, "Lightning Sac": 1})
crafting_table.add_upgrade_path("Lightning Drum III", "Lightning Drum IV")
crafting_table.insert_with_quantities("Usurper's Growl", {"Zinogre Hardclaw": 3, "Zinogre Deathly Shocker": 2, "Zinogre Cortex": 5, "Lightning Sac": 3})
crafting_table.add_upgrade_path("Lightning Drum IV", "Usurper's Growl")
crafting_table.insert_with_quantities("Usurper's Growl+", {"Zinogre Hardhorn": 3, "Zinogre Electrofur+": 4, "Fulgurbug": 5, "Zinogre Skymerald": 1})
crafting_table.add_upgrade_path("Usurper's Growl", "Usurper's Growl+")
crafting_table.insert_with_quantities("Despot's Thunderclap", {"Spiritvein Solidbone": 5, "Zinogre Hardhorn": 2, "Zinogre Deathly Shocker": 5, "Large Elder Dragon Gem": 1})
crafting_table.add_upgrade_path("Usurper's Growl+", "Despot's Thunderclap")
crafting_table.insert_with_quantities("Great Bagpipe I", {"Dragonite Ore": 2, "Machalite Ore": 5, "Monster Bone M": 2})
crafting_table.add_upgrade_path("Metal Bagpipe III", "Great Bagpipe I")
crafting_table.insert_with_quantities("Great Bagpipe II", {"Monster Bone+": 2, "Dragonite Ore": 5, "Coral Crystal": 2, "Machalite Ore": 10})
crafting_table.add_upgrade_path("Great Bagpipe I", "Great Bagpipe II")
crafting_table.insert_with_quantities("Great Bagpipe III", {"Carbalite Ore": 8, "Dragonite Ore": 5, "Dragonvein Crystal": 2})
crafting_table.add_upgrade_path("Great Bagpipe II", "Great Bagpipe III")
crafting_table.insert_with_quantities("Fortissimo I", {"Fucium Ore": 8, "Carbalite Ore": 5, "Dragonite Ore": 10, "Dragonvein Crystal": 3})
crafting_table.add_upgrade_path("Great Bagpipe III", "Fortissimo I")
crafting_table.insert_with_quantities("Fortissimo II", {"Elder Dragon Blood": 2, "Fucium Ore": 13, "Carbalite Ore": 20, "Firecell Stone": 1})
crafting_table.add_upgrade_path("Fortissimo I", "Fortissimo II")
crafting_table.insert_with_quantities("Nergal Groove", {"Nergigante Talon": 3, "Nergigante Regrowth Plate": 4, "Nergigante Tail": 2, "Nergigante Carapace": 2})
crafting_table.add_upgrade_path("Fortissimo II", "Nergal Groove")
crafting_table.insert_with_quantities("Desolation's Overture", {"Xeno'jiiva Horn": 2, "Nergigante Horn+": 5, "Nergigante Talon": 5, "Nergigante Gem": 1})
crafting_table.add_upgrade_path("Nergal Groove", "Desolation's Overture")
crafting_table.insert_with_quantities("Ruinous Desolation", {"Annihilating Greathorn": 3, "Nergigante Hardclaw": 4, "Eternal Regrowth": 5, "Large Elder Dragon Gem": 1})
crafting_table.add_upgrade_path("Desolation's Overture", "Ruinous Desolation")
crafting_table.insert_with_quantities("Sforzando I", {"Eltalite Ore": 6, "Carbalite Ore": 10, "Spiritvein Crystal": 2, "Purecrystal": 1})
crafting_table.add_upgrade_path("Fortissimo II", "Sforzando I")
crafting_table.insert_with_quantities("Sforzando II", {"Monster Slogbone": 3, "Eltalite Ore": 4, "Meldspar Ore": 2, "Bathycite Ore": 2})
crafting_table.add_upgrade_path("Sforzando I", "Sforzando II")
crafting_table.insert_with_quantities("Sforzando III", {"Pure Dragon Blood": 3, "Eltalite Ore": 6, "Meldspar Ore": 3, "Purecrystal": 1})
crafting_table.add_upgrade_path("Sforzando II", "Sforzando III")
crafting_table.insert_with_quantities("Raven Shamisen", {"Garuga Shard": 3, "Garuga Silverpelt": 4, "Garuga Auricle": 2, "Fey Wyvern Gem": 1})
crafting_table.add_upgrade_path("Sforzando II", "Raven Shamisen")
crafting_table.insert_with_quantities("Wolf Shamisen", {"Scratched Shell": 3, "Garuga Fellwing": 2, "Fancy Beak": 3, "Large Wyvern Gem": 1})
crafting_table.add_upgrade_path("Raven Shamisen", "Wolf Shamisen")
crafting_table.insert_with_quantities("Devil's Maestro", {"Deviljho Scale": 6, "Deviljho Talon": 2, "Deviljho Tallfang": 3, "Deviljho Saliva": 2})
crafting_table.insert_with_quantities("Deep Vero", {"Elder Dragon Blood": 5, "Deviljho Scalp": 2, "Deviljho Tallfang": 5, "Deviljho Gem": 1})
crafting_table.add_upgrade_path("Devil's Maestro", "Deep Vero")
crafting_table.insert_with_quantities("Fate's Dirge", {"Vile Fang": 3, "Deviljho Ripper": 2, "Black Blood": 3, "Deviljho Crook": 1})
crafting_table.add_upgrade_path("Deep Vero", "Fate's Dirge")
crafting_table.insert_with_quantities("Denden Daiko", {"Rajang Hardhorn": 1, "Rajang Hardclaw": 1, "Rajang Hardfang": 2, "Rajang Wildpelt": 2})
crafting_table.insert_with_quantities("Denden Doomsounder", {"Tempered Glimmerpelt": 3, "Rajang Hardhorn": 3, "Rajang Hardfang": 7, "Gold Rajang Pelt+": 3})
crafting_table.add_upgrade_path("Denden Daiko", "Denden Doomsounder")
crafting_table.insert_with_quantities("Demonlord Wardrum", {"Ghoulish Gold Gorer": 3, "Rajang Apoplexy": 2, "Gold Rajang Pelt+": 5, "Rajang Heart": 1})
crafting_table.insert_with_quantities("Brimstren Drakesong", {"Stygian Zinogre Hardhorn": 1, "Stygian Zinogre Hardclaw": 1, "Stygian Zinogre Dragonlocks": 2, "Stygian Zinogre Dragonhold": 2})
crafting_table.insert_with_quantities("Stygian Tristitia", {"Tempered Dragonhold": 3, "Stygian Zinogre Hardhorn": 2, "Stygian Zinogre Hardclaw": 5, "Stygian Zinogre Skymerald": 1})
crafting_table.add_upgrade_path("Brimstren Drakesong", "Stygian Tristitia")
crafting_table.insert_with_quantities("Lightbreak Timbre", {"Brach Obliterator": 3, "Brach Warhead": 1, "Indestructible Ebonshell": 4, "Immortal Reactor": 1})
crafting_table.insert_with_quantities("Alatreon Harmony", {"Alatreon Mantle": 3, "Skyswayer": 1, "Alatreon Riptalon": 3, "Large Elder Dragon Gem": 1})
crafting_table.insert_with_quantities("Alatreon Revival", {"Alatreon Direwing": 1, "Skyswayer": 2, "Alatreon Riptalon": 2, "Azure Dragonsphire": 1})
crafting_table.add_upgrade_path("Alatreon Harmony", "Alatreon Revival")
crafting_table.insert_with_quantities("Fatalis Menace", {"Fatalis Shard": 3, "Fatalis Hardhorn": 1, "Fatalis Pectus": 1, "Fatalis Evil Eye": 1})
crafting_table.insert_with_quantities("Fatalis Menace Wailer", {"Large Elder Dragon Gem": 1, "Fatalis Pectus": 2, "Fatalis Hardhorn": 2, "Fatalis Evil Eye": 1})
crafting_table.add_upgrade_path("Fatalis Menace", "Fatalis Menace Wailer")
crafting_table.insert_with_quantities("Guild Palace Bard", {"Fest Ticket": 2, "Amber Hardfang": 2, "Gracium": 5, "Purecrystal": 1})
crafting_table.insert_with_quantities("Royal Song Symphony", {"Hero King Coin": 1, "Namielle Hardclaw": 3, "Large Elder Dragon Bone": 5, "Pure Dragon Blood": 3})
crafting_table.add_upgrade_path("Guild Palace Bard", "Royal Song Symphony")

print("\nAll Recipes:")
for item, materials in crafting_table.display_all_recipes():
    print(f"{item}: {materials}")

print("\nRecipe Tree:")
crafting_table.display_upgrade_path()
