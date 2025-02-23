class ElectronicDevice:
    """
    Общий класс для электронных устройств
    """
    def __init__(self, devices_ip: str, memory: int):
        """
        Инициализация атрибутов класса
        :param devices_ip: ip адрес устройства
        :param memory: объем внутренней памяти
        """
        self.devices_ip = devices_ip
        self.memory = memory

    def __repr__(self):
        return f"{self.__class__.__name__}(ip: {self.devices_ip})"

    def __str__(self):
        return f"Device IP = {self.devices_ip}"

    def power_on(self) -> None:
        """
        Включение устройства
        :return: None
        """
        ...

    def change_ip(self, new_ip: str) -> None:
        """
        Данный метод изменяет ip устройства
        :param new_ip: новый ip адрес
        :return: None
        """
        self.devices_ip = new_ip

    def download_app(self) -> None:
        """
        Скачивание приложения во внутреннюю память
        :return: None
        """
        ...


class Phone(ElectronicDevice):
    """
    Наследованный класс - Телефон
    """
    def __init__(self, devices_ip: str, memory: int, phone_name: str):
        """
        Инициализация атрибутов класса
        :param devices_ip: ip адрес устройства
        :param memory: объем внутренней памяти
        :param phone_name: название модели телефона
        """
        super().__init__(devices_ip, memory)

        self.memory = memory
        self.phone_name = phone_name

    def __repr__(self):
        return f"{self.__class__.__name__}(ip: {self.devices_ip}, memory: {self.memory}, phone_name: {self.phone_name})"

    def call_to_person(self) -> None:
        """
        Метод, выполняющий функцию звонка другому человеку
        :return: None
        """
        ...

    def download_app(self) -> None:
        """
        Скачивает приложение без выбора пути установки файла
        :return: None
        """
        ...


class Computer(ElectronicDevice):
    def __init__(self, devices_ip: str, memory: int, cpu_speed: int, gpu_speed: int):
        """
        Инициализация атрибутов класса
        :param devices_ip: ip адрес устройства
        :param memory: объем внутренней памяти
        :param cpu_speed: скорость вычислительного процессора
        :param gpu_speed: скорость графического процессора
        """
        super().__init__(devices_ip, memory)

        self.memory = memory
        self.cpu_speed = cpu_speed
        self.gpu_speed = gpu_speed

    def __repr__(self):
        return f"{self.__class__.__name__}(ip: {self.devices_ip}, memory: {self.memory}," \
               f" cpu_speed: {self.cpu_speed}, gpu_speed: {self.gpu_speed})"

    def play_rdr2(self) -> None:
        """
        Играю в Red Dead Redemption 2
        :return: None
        """
        ...

    def download_app(self) -> None:
        """
        Скачивает приложение учитывая выбор пути установки
        :return: None
        """
        ...


if __name__ == "__main__":
    # Write your solution here
    l = [('1.1.1.1', 50), ('2.2.2.2', 100), ('192.168.0.255', 150)]
    print(list(ElectronicDevice(i[0], i[1]) for i in l))
    print(ElectronicDevice(l[2][0], l[2][1]))