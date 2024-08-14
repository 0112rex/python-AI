import random


class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, target):
        damage = random.randint(0, self.attack_power)
        target.health -= damage
        print(f"{self.name} attacks {target.name} for {damage} damage!")

    def defend(self):
        print(f"{self.name} is defending this turn.")

    def is_alive(self):
        return self.health > 0


def print_status(player, enemies):
    print("\nPlayer Health:", player.health)
    print("Enemies' Health:", [enemy.health for enemy in enemies])


def main():
    # 初始化玩家和敵人
    player = Character("Player", 100, 20)
    enemies = [Character(f"Enemy {i+1}", 50, 15) for i in range(3)]

    print("Welcome to the Shooting Game!\n")

    # 遊戲循環
    while player.is_alive() and any(enemy.is_alive() for enemy in enemies):
        print_status(player, enemies)

        action = input("\nChoose your action (attack/defend): ").lower()

        if action == "attack":
            target = int(input(f"Choose enemy to attack (1-{len(enemies)}): ")) - 1
            if 0 <= target < len(enemies) and enemies[target].is_alive():
                player.attack(enemies[target])
            else:
                print("Invalid target.")
        elif action == "defend":
            player.defend()
        else:
            print("Invalid action.")

        # 敵人攻擊
        for enemy in enemies:
            if enemy.is_alive():
                if action == "defend":
                    damage = max(0, random.randint(0, enemy.attack_power) - 5)
                    player.health -= damage
                    print(f"{enemy.name} attacks for {damage} damage!")
                else:
                    enemy.attack(player)

    # 遊戲結束
    if player.is_alive():
        print("\nCongratulations! You defeated all the enemies!")
    else:
        print("\nGame Over! You were defeated by the enemies.")


if __name__ == "__main__":
    main()
