class GameCharacter:
    def __init__(self, job, life):
        self.job = job
        self.life = life

    def info(self):
        print(self.job)
        print(self.life)

human1 = GameCharacter("전사", 100)
print(human1.job)
print(human1.life)

human1.info()

human2 = GameCharacter("마법사", 50)
human2.info()
