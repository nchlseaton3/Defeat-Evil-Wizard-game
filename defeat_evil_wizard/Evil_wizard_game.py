# Base Character class
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  

    def attack(self, opponent):
        opponent.health -= self.attack_power
        print(f"{self.name} attacks {opponent.name} for {self.attack_power} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)

# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)

# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)

    def regenerate(self):
        self.health += 5
        print(f"{self.name} regenerates 5 health! Current health: {self.health}")

# Create Archer class
class Jinzo(Character):
    def __init__(self, name):
        super().__init__(name, health=120, attack_power=20)
        self.hidden = False  # Used for Tanuki-Gakure

    def throw_shuriken(self, opponent):
        """Launches a quick double shuriken attack."""
        damage = self.attack_power * 2
        opponent.health -= damage
        print(f"{self.name} throws shurikens from the shadows for {damage} damage!")

    def tanuki_gakure(self):
        """Hides in shadows to avoid next attack."""
        self.hidden = True
        print(f"{self.name} uses Tanuki-Gakure and disappears into the shadows!")

    def take_damage(self, amount):
        """Overrides the normal damage logic."""
        if self.hidden:
            print(f"{self.name} evades the attack from the shadows!")
            self.hidden = False
        else:
            self.health -= amount
            print(f"{self.name} takes {amount} damage. Health is now {self.health}.")

    def heal(self):
        """Heals a small amount — ninja meditation."""
        heal_amount = 10
        self.health += heal_amount
        if self.health > self.max_health:
            self.health = self.max_health
        print(f"{self.name} meditates in silence and heals {heal_amount} HP. Health: {self.health}/{self.max_health}")


class MikeTyson(Character):
    def __init__(self, name):
        super().__init__(name, health=200, attack_power=50)
        self.defending = False

    def super_uppercut(self, opponent):
        """A devastating uppercut with bonus power."""
        damage = self.attack_power + 30
        opponent.health -= damage
        print(f"{self.name} unleashes a SUPER UPPERCUT for {damage} damage!")

    def peek_a_boo(self):
        """Defensive move to reduce damage."""
        self.defending = True
        print(f"{self.name} uses the Peek-A-Boo defense stance!")

    def take_damage(self, amount):
        """Takes reduced damage if defending."""
        if self.defending:
            reduced = amount // 2
            self.health -= reduced
            self.defending = False
            print(f"{self.name} blocks some of the attack using Peek-A-Boo! Taking only {reduced} damage.")
        else:
            self.health -= amount
            print(f"{self.name} takes {amount} damage. Health is now {self.health}.")



def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Jinzo") #Potential Class Add on
    print("4. Mike Tyson")  #Potential Class Add on

    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Jinzo(name)
    elif class_choice == '4':
        return MikeTyson(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)

def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. View Stats")

        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard)
        
        elif choice == '2':
            if isinstance(player, Jinzo):
                ability = input("Choose ability: 1. Throw Shurikens 2. Tanuki-Gakure ")
                if ability == '1':
                    player.throw_shuriken(wizard)
                else:
                    player.tanuki_gakure() 

            elif isinstance(player, MikeTyson):
                ability = input("Choose ability: 1. Super Uppercut 2. Peek-A-Boo ")   
                if ability == '1':
                    player.super_uppercut(wizard)
                else:
                    player.peek_a_boo()

            else:
                print("Your class doesn't have special abilities yet.")    

        elif choice == '3':
            if hasattr(player, "heal"):
                player.heal()
            else:
                print(f"{player.name} cannot heal!")
        
        elif choice == '4':
            player.display_stats()
        else:
            print("Invalid choice. Try again.")

        #Wizards turn
        if wizard.health > 0:
            wizard.regenerate()
            print("\n---Wizards Turn ---")
            if hasattr(player, "take_damage"):
                player.take_damage(wizard.attack_power)
            else:
                wizard.attack(player) 
        if player.health <= 0:
            print (f"{player.name} has been defeated!")
            break
        if wizard.health <= 0:
            print(f"{wizard.name} has been defeated by {player.name}!")           

        
       

def main():
    player = create_character()
    wizard = EvilWizard("The Dark Wizard")
    battle(player, wizard)

if __name__ == "__main__":
    main()
