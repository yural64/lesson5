class Warrior(): #класс Воин
    def init (self, name, power, endurance, hair_color): #функция init (конструктор класса)
        # с указанием характеристик класа: имя, сила, выносливость, цвет волос
        self.name = name #привязываем характеристики к этому классу
        self.power = power
        self.endurance = endurance
        self.hair_color = hair_color

    #пропишем методы класса
    def sleep (self): #метод "спать"
        print(f"{self.name} лег спать")
        self.endurance += 2 #увеличили выносливость на 2

    def eat (self): #метод "кушать"
        print(f"{self.name} сел кушать")
        self.power += 1  # увеличили силу на 1

    def hit (self): #метод "бить"
        print(f"{self.name} бьет")
        self.endurance -= 6  # удар уменьшает выносливость на 6

    def walk (self): #метод "ходить"
        print(f"{self.name} гуляет")

    def info (self): #метод вывода информации и персонаже
        print(f"имя воина - {self.name}")
        print(f"цвет волос воина - {self.hair_color}")
        print(f"сила воина - {self.power}")
        print(f"выносливость воина - {self.endurance}")