class Teammate:
    teammates = []
    """это список наших тиммейтов"""

    def __init__(self, skill: int, adequacy: bool):
        """
        Создание и подготовка к работе объекта "Тиммейт".

        :param skill: Уровень скилла тиммейта (от 0 до 10).
        :param adequacy: Адекватность тиммейта (True/False).
        :raises TypeError: Если аргументы имеют неправильный тип.
        :raises ValueError: Если уровень скилла выходит за пределы 0–10.

        Примеры:
        >>> teammate = Teammate(5, True)
        """
        if not isinstance(skill, int):
            raise TypeError("Уровень скилла должен быть типа int")
        if skill < 0 or skill > 10:
            raise ValueError("Уровень скилла должен быть числом в диапазоне от 0 до 10")
        self.skill = skill

        if not isinstance(adequacy, bool):
            raise TypeError("Адекватность должна быть типа bool")
        self.adequacy = adequacy

        Teammate.teammates.append(self)
        """здесь добавляем тиммейтов в созданный нами список"""

    def workoutTeammate_1(self, skillup: int) -> None:
        """
        Улучшение скиллов тиммейта.

        :param skillup: На сколько пунктов за тренировку увеличится скилл.
        :raises TypeError: Если добавляемое значение не является числом.
        :raises ValueError: Если добавляемое значение выходит за рамки допустимых границ (0–10).

        Примеры:
        >>> teammate = Teammate(5, True)
        >>> teammate.workoutTeammate_1(3)
        """
        if not isinstance(skillup, int):
            raise TypeError("Добавляемый уровень скилла должен быть типа int")
        if skillup + self.skill > 10 or skillup < 0:
            raise ValueError("Добавляемый уровень скилла должен быть положительным числом и не превышать 10")

        self.skill += skillup

    def count_high_skill_teammates(self, threshold: int = 7) -> int:
        """
        Подсчитывает количество тиммейтов с уровнем скилла выше заданного порога.

        :param threshold: Порог, выше которого считается уровень скилла (по умолчанию 7).
        :return: Количество тиммейтов, у которых skill выше порога.
                Примеры:
        >>> t1 = 8, True
        >>> t2 = 6, True
        """
        return sum(1 for teammate in Teammate.teammates if teammate.skill > threshold)

    def count_adequate_high_skill_teammates(self, threshold: int = 7) -> int:
        """
        Подсчитывает количество адекватных тиммейтов с уровнем скилла выше заданного порога.

        :param threshold: Порог, выше которого считается уровень скилла (по умолчанию 7).
        :return: Количество адекватных тиммейтов, у которых skill выше порога.
                Примеры:
        >>> t1 = 8, True
        >>> t2 = 6, True
        >>> t3 = 9, False
        """
        return sum(1 for teammate in self.teammates if teammate.skill > threshold and teammate.adequacy)


class Patient:
    patients = []
    """это список наших пациентов"""

    def __init__(self, age: int, condition: bool):
        """
        Создание и подготовка к работе объекта "Пациент".

        :param age: Возраст пациента (от 0 до 120).
        :param condition: Тяжесть состояния пациента (True - тяжелое, False - легкое).
        :raises TypeError: Если аргументы имеют неправильный тип.
        :raises ValueError: Если возраст выходит за пределы 0–120.

        Примеры:
        >>> patient = Patient(25, False)
        """
        if not isinstance(age, int):
            raise TypeError("Возраст должен быть типа int")
        if age < 0 or age > 120:
            raise ValueError("Возраст должен быть числом в диапазоне от 0 до 120")
        self.age = age

        if not isinstance(condition, bool):
            raise TypeError("Тяжесть состояния должна быть типа bool")
        self.condition = condition

        Patient.patients.append(self)

    def count_elderly_patients(self, threshold: int = 60) -> int:
        """
        Подсчитывает количество пациентов старше заданного возраста.

        :param threshold: Возрастной порог (по умолчанию 60 лет).
        :return: Количество пациентов старше порога.
                Примеры:
        >>> p1 = 70, True
        >>> p2 = 50, False
        """
        return sum(1 for patient in self.patients if patient.age > threshold)

    def count_critical_elderly_patients(self, threshold: int = 60) -> int:
        """
        Подсчитывает количество тяжелобольных пациентов старше заданного возраста.

        :param threshold: Возрастной порог (по умолчанию 60 лет).
        :return: Количество тяжелобольных пациентов старше порога.
        >>> p1 = 70, True
        >>> p2 = 50, True
        >>> p3 = 65, True
        """
        return sum(1 for patient in self.patients if patient.age > threshold and patient.condition)


class FemaleStudent:
    female_students = []
    """это список наших студенточек"""

    def __init__(self, age: int, average: float):
        """
        Создание и подготовка к работе объекта "Студентка".

        :param age: Возраст студентки (от 16 до 30).
        :param average: Средний балл студентки (от 2.0 до 5.0).
        :raises TypeError: Если аргументы имеют неправильный тип.
        :raises ValueError: Если значения не входят в допустимые диапазоны.

        Примеры:
        >>> student = FemaleStudent(20, 3.5)
        """
        if not isinstance(age, int):
            raise TypeError("Возраст должен быть типа int")
        if age < 16 or age > 30:
            raise ValueError("Возраст должен быть числом в диапазоне от 16 до 30")
        self.age = age

        if not isinstance(average, float):
            raise TypeError("Средний балл должен быть типа float")
        if average < 2.0 or average > 5.0:
            raise ValueError("Средний балл должен быть числом в диапазоне от 2.0 до 5.0")
        self.average = average

        FemaleStudent.female_students.append(self)

    def count_high_average_students(self, threshold: float = 3.5) -> int:
        """
        Подсчитывает количество студенток с высоким средним баллом.

        :param threshold: Порог среднего балла (по умолчанию 3.5).
        :return: Количество студенток с баллом выше порога.
        Примеры:
        >>> s1 = 20, 3.8
        >>> s2 = 22, 3.2
        """
        return sum(1 for student in self.female_students if student.average > threshold)

    def count_high_average_young_students(self, age_threshold: int = 25,
                                          average_threshold: float = 3.5) -> int:
        """
        Подсчитывает количество студенток младше заданного возраста и с высоким средним баллом.

        :param age_threshold: Возрастной порог (по умолчанию 25).
        :param average_threshold: Порог среднего балла (по умолчанию 3.5).
        :return: Количество студенток, младше возраста и с средним баллом выше порога.
        >>> s1 = 20, 3.8
        >>> s2 = 22, 3.2
        >>> s3 = 26, 3.9
        """
        return sum(1 for student in self.female_students if
                   student.age < age_threshold and student.average > average_threshold)
