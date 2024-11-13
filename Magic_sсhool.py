from abc import ABC, abstractmethod

# Абстрактний клас для магічних сутностей
class MagicalEntity(ABC):
    @abstractmethod
    def performSpell(self, spell):
        pass

# Клас для заклинань
class Spell:
    def __init__(self, name, spell_type, power_boost):
        self.name = name
        self.spell_type = spell_type  # тип заклинання (атакуюче, захисне, трансформаційне)
        self.power_boost = power_boost

# Клас для артефактів
class Artifact:
    def __init__(self, name, effect):
        self.name = name
        self.effect = effect

# Клас для подій
class MagicalEvent:
    def __init__(self, event_name, description):
        self.event_name = event_name
        self.description = description

    def organizeEvent(self):
        print(f"Організація події '{self.event_name}': {self.description}")
# Клас для магічних уроків
class Lesson:
    def __init__(self, name, lesson_type):
        self.name = name
        self.lesson_type = lesson_type  # Тип уроку, наприклад, зіллєваріння, трансфігурація, захист від темних мистецтв

    def conductLesson(self):
        print(f"Проводиться урок {self.lesson_type}: {self.name}")

# Клас студента з магічними здібностями
class Student(MagicalEntity):
    def __init__(self, name, power_level):
        self.name = name
        self.power_level = power_level

    def performSpell(self, spell):
        print(f"{self.name} використовує заклинання {spell.name} типу {spell.spell_type}!")
        self.power_level += spell.power_boost

# Клас професора з магічною спеціалізацією
class Professor(MagicalEntity):
    def __init__(self, name, specialty):
        self.name = name
        self.specialty = specialty

    def teachMagic(self, student):
        print(f"{self.name} навчає {student.name} магії {self.specialty}")
        student.power_level += 10

    def performSpell(self, spell):
        print(f"{self.name} використовує {spell.spell_type} заклинання {spell.name}")

# Клас для магічних істот
class MagicalCreature(MagicalEntity):
    def __init__(self, species, danger_level):
        self.species = species
        self.danger_level = danger_level

    def performSpell(self, spell):
        print(f"{self.species} піддається впливу {spell.spell_type} заклинання {spell.name}")

        # Основна школа  class MagicSchool:
        def __init__(self, name):
            self.name = name
            self.students = []
            self.professors = []
            self.artifacts = []
            self.creatures = []
            self.lessons = []

        def addStudent(self, student):
            self.students.append(student)
            print(f"{student.name} доданий до школи.")

        def addProfessor(self, professor):
            self.professors.append(professor)
            print(f"Професор {professor.name} додається до школи.")

        def addArtifact(self, artifact):
            self.artifacts.append(artifact)
            print(f"Артефакт {artifact.name} додано до школи.")

        def addCreature(self, creature):
            self.creatures.append(creature)
            print(f"Магічна істота {creature.species} додана до школи.")

        def addLesson(self, lesson):
            self.lessons.append(lesson)
            print(f"Додано урок: {lesson.name} ({lesson.lesson_type})")

        def teachMagic(self):
            for professor in self.professors:
                for student in self.students:
                    professor.teachMagic(student)

        def organizeEvent(self, event):
            print(f"Організовано подію: {event.event_name}")
            event.organizeEvent()

        def investigateMystery(self):
            print("Розслідування магічної таємниці розпочато!")

        def handleThreat(self):
            print("Протидія магічній загрозі активована!")

        def studyCreature(self, species_name):
            creature = next((c for c in self.creatures if c.species == species_name), None)
            if creature:
                print(f"Ви починаєте вивчення магічної істоти: {creature.species}")
            else:
                print("Істоту з таким ім'ям не знайдено.")

        def conductLesson(self, lesson_index):
            if 0 <= lesson_index < len(self.lessons):
                self.lessons[lesson_index].conductLesson()
            else:
                print("Невірний вибір уроку.")

# Меню для взаємодії з користувачем
def main():
    school = MagicSchool("Школа Чарів")

    # Додавання прикладів уроків
    school.addLesson(Lesson("Зіллєваріння", "Практичний"))
    school.addLesson(Lesson("Трансфігурація", "Теоретичний"))
    school.addLesson(Lesson("Захист від темних мистецтв", "Захисний"))

    while True:
        print("\n--- Меню ---")
        print("1. Додати студента")
        print("2. Додати професора")
        print("3. Додати артефакт")
        print("4. Додати магічну істоту")
        print("5. Додати урок")
        print("6. Провести урок магії")
        print("7. Вивчити магічну істоту")
        print("8. Організувати магічну подію")
        print("9. Розслідувати таємницю")
        print("10. Протидіяти загрозі")
        print("11. Вийти")

        choice = input("Оберіть опцію: ")

        if choice == "1":
            name = input("Введіть ім'я студента: ")
            if not name.strip():
                print("Ім'я студента не може бути порожнім.")
                continue
            try:
                power_level = int(input("Введіть рівень сили студента: "))
            except ValueError:
                print("Рівень сили має бути числом.")
                continue
            student = Student(name, power_level)
            school.addStudent(student)

        elif choice == "2":
            name = input("Введіть ім'я професора: ")
            if not name.strip():
                print("Ім'я професора не може бути порожнім.")
                continue
            specialty = input("Введіть спеціалізацію професора: ")
            if not specialty.strip():
                print("Спеціалізація професора не може бути порожньою.")
                continue
            professor = Professor(name, specialty)
            school.addProfessor(professor)

        elif choice == "3":
            name = input("Введіть назву артефакту: ")
            try:
                effect = int(input("Введіть силу ефекту артефакту: "))
            except ValueError:
                print("Сила ефекту має бути числом.")
                continue
            artifact = Artifact(name, effect)
            school.addArtifact(artifact)

        elif choice == "4":
            species = input("Введіть вид магічної істоти: ")
            try:
                danger_level = int(input("Введіть рівень небезпеки: "))
            except ValueError:
                print("Рівень небезпеки має бути числом.")
                continue
            creature = MagicalCreature(species, danger_level)
            school.addCreature(creature)

        elif choice == "5":
            name = input("Введіть назву уроку: ")
            lesson_type = input("Введіть тип уроку (наприклад, зіллєваріння, захист від темних мистецтв): ")
            lesson = Lesson(name, lesson_type)
            school.addLesson(lesson)

        elif choice == "6":
            # Показати список уроків
            print("\n--- Список уроків ---")
            for i, lesson in enumerate(school.lessons, start=1):
                print(f"{i}. {lesson.name} ({lesson.lesson_type})")

            try:
                lesson_choice = int(input("Оберіть номер уроку для вивчення: ")) - 1
                school.conductLesson(lesson_choice)
            except ValueError:
                print("Будь ласка, введіть правильний номер.")
            except IndexError:
                print("Невірний вибір уроку.")

        elif choice == "7":
            species_name = input("Введіть назву магічної істоти для вивчення: ")
            school.studyCreature(species_name)

        elif choice == "8":
            event_name = input("Введіть назву події: ")
            description = input("Введіть опис події: ")
            event = MagicalEvent(event_name, description)
            school.organizeEvent(event)

        elif choice == "9":
            school.investigateMystery()

        elif choice == "10":
            school.handleThreat()

        elif choice == "11":
            print("Завершення програми.")
            break

        else:
            print("Неправильний вибір, спробуйте ще раз.")

    # Запуск головного меню
    if __name__ == "__main__":
        main()