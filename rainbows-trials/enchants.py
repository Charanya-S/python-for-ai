#Parent Class
class CommonEnchants:
    def unbreaking(self):
        print(f"{self.name} needs Unbreaking III")
    
    def mending(self):
        print(f"{self.name} needs Mending")

class Armour:
    def protection(self):
        print(f"{self.name} needs Protection IV")

class MeleeWeapons:
    def sharpness(self):
        print(f"{self.name} may need Sharpness V or")
    
    def smite(self):
        print(f"{self.name} may need Smite V")

class Tools:
    def efficiency(self):
        print(f"{self.name} needs Efficiency V")

#Child Class
class Helmet(CommonEnchants, Armour):
    def __init__(self, name):
        self.name = name

    def aqua_affinity(self):
        print(f"{self.name} needs Aqua Affinity")
    
    def respiration(self):
        print(f"{self.name} needs Respiration III")
    
    def show_enchants(self):
        self.unbreaking()
        self.mending()
        self.protection()
        self.aqua_affinity()
        self.respiration()

class Chestplate(CommonEnchants, Armour):
    def __init__(self, name):
        self.name = name
        
    def show_enchants(self):
        self.unbreaking()
        self.mending()
        self.protection()

class Leggings(CommonEnchants, Armour):
    def __init__(self, name):
        self.name = name
        
    def show_enchants(self):
        self.unbreaking()
        self.mending()
        self.protection()

class Boots(CommonEnchants, Armour):
    def __init__(self, name):
        self.name = name
        
    def feather_falling(self):
        print(f"{self.name} needs Feather Falling IV")
    
    def depth_strider(self):
        print(f"{self.name} needs Depth Strider III")
    
    def frost_walker(self):
        print(f"{self.name} needs Frost Walker II")
    
    def show_enchants(self):
        self.unbreaking()
        self.mending()
        self.protection()
        self.feather_falling()
        self.depth_strider()
        self.frost_walker()

class Sword(CommonEnchants, MeleeWeapons):
    def __init__(self, name):
        self.name = name
        
    def sharpness1(self):
        print(f"Sharpness V is best for {self.name} in Bedrock")
    
    def smite1(self):
        print(f"Smite V is also good for {self.name} in Bedrock but best in Java")
    
    def looting(self):
        print(f"{self.name} needs Looting III")
    
    def knockback(self):
        print(f"Knockback II is not recommended for {self.name}")
    
    def fire_aspect(self):
        print(f"Fire Aspect II is not recommended for {self.name}")
    
    def sweeping_edge(self):
        print(f"Sweeping Edge is available on in Java and {self.name} needs it")
    
    def show_enchants(self):
        self.unbreaking()
        self.mending()
        self.sharpness()
        self.smite()
        self.sharpness1()
        self.smite1()
        self.looting()
        self.knockback()
        self.fire_aspect()
        self.sweeping_edge()

class Spear(CommonEnchants, MeleeWeapons):
    def __init__(self, name):
        self.name = name
        
    def smite1(self):
        print(f"Smite V is best for {self.name}")
    
    def sharpness1(self):
        print(f"But Sparpness V is also good for {self.name}")
    
    def looting(self):
        print(f"{self.name} needs Looting III")
    
    def knockback(self):
        print(f"{self.name} needs Knockback II")
    
    def fire_aspect(self):
        print(f"Fire Aspect II is not recommended for {self.name}")
    
    def lunge(self):
        print(f"{self.name} needs Lunge III")
    
    def show_enchants(self):
        self.unbreaking()
        self.mending()
        self.sharpness()
        self.smite()
        self.sharpness1()
        self.smite1()
        self.looting()
        self.knockback()
        self.fire_aspect()
        self.lunge()

class Bow(CommonEnchants):
    def __init__(self, name):
        self.name = name
        
    def power(self):
        print(f"{self.name} needs Power V")
    
    def punch(self):
        print(f"{self.name} needs Punch II")
    
    def flame(self):
        print(f"{self.name} needs Flame")
    
    def infinity(self):
        print(f"{self.name} needs Infinity, but Infinity and Mending cannot be put together.")
    
    def show_enchants(self):
        self.unbreaking()
        self.mending()
        self.power()
        self.punch()
        self.flame()
        self.infinity()

class Crossbow(CommonEnchants):
    def __init__(self, name):
        self.name = name
        
    def quick_charge(self):
        print(f"{self.name} needs Quick Charge III")
    
    def piercing(self):
        print(f"{self.name} needs Piercing IV")
    
    def multishot(self):
        print(f"{self.name} can have Multishot but connet be put with Piercing and is good with Firework Rockets")
    
    def show_enchants(self):
        self.unbreaking()
        self.mending()
        self.quick_charge()
        self.piercing()
        self.multishot()
    
class Trident(CommonEnchants):
    def __init__(self, name):
        self.name = name
        
    def impailing(self):
        print(f"{self.name} needs Impailing V")
    
    def channeling(self):
        print(f"{self.name} needs Channeling")
    
    def loyalty(self):
        print(f"{self.name} can have either Loyaly III or")
    
    def riptide(self):
        print(f"{self.name} can have Riptide III")
    
    def show_enchants(self):
        self.unbreaking()
        self.mending()
        self.impailing()
        self.channeling()
        self.loyalty()
        self.riptide()

class Mace(CommonEnchants):
    def __init__(self, name):
        self.name = name
        
    def breach(self):
        print(f"{self.name} needs Breach IV in Multiplayer")
    
    def density(self):
        print(f"{self.name} needs Density V")
    
    def wind_burst(self):
        print(f"{self.name} needs Wind Burst II or III")
    
    def show_enchants(self):
        self.unbreaking()
        self.mending()
        self.breach()
        self.density()
        self.wind_burst()

class Axe(CommonEnchants, Tools, MeleeWeapons):
    def __init__(self, name):
        self.name = name
        
    def sharpness1(self):
        print(f"{self.name} needs Sharpness V")
    
    def smite1(self):
        print(f"Smite is not recommended for {self.name}")
    
    def silk_touch(self):
        print(f"{self.name} can have Silk Touch")
    
    def show_enchants(self):
        self.unbreaking()
        self.mending()
        self.efficiency()
        self.sharpness()
        self.smite()
        self.sharpness1()
        self.smite1()
        self.silk_touch()

class Pickaxe(CommonEnchants, Tools):
    def __init__(self, name):
        self.name = name
        
    def fortune(self):
        print(f"{self.name} needs Fortune III")
    
    def silk_touch(self):
        print(f"{self.name} can have Silk Touch on another Pickaxe")
    
    def show_enchants(self):
        self.unbreaking()
        self.mending()
        self.efficiency()
        self.fortune()
        self.silk_touch()

class Shovel(CommonEnchants, Tools):
    def __init__(self, name):
        self.name = name
        
    def silk_touch(self):
        print(f"{self.name} can have Silk Touch")
    
    def show_enchants(self):
        self.unbreaking()
        self.mending()
        self.efficiency()
        self.silk_touch()

class Hoe(CommonEnchants, Tools):
    def __init__(self, name):
        self.name = name
        
    def silk_touch(self):
        print(f"{self.name} can have Silk Touch")
    
    def show_enchants(self):
        self.unbreaking()
        self.mending()
        self.efficiency()
        self.silk_touch()

class FishingRod(CommonEnchants):
    def __init__(self, name):
        self.name = name
        
    def luck_of_the_sea(self):
        print(f"{self.name} needs Luck of the Sea III")
    
    def lure(self):
        print(f"{self.name} needs Lure III")
    
    def show_enchants(self):
        self.unbreaking()
        self.mending()
        self.luck_of_the_sea()
        self.lure()