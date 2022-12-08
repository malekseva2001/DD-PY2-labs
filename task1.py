class Cat:
    """ Класс описывает модель кота """
    def __init__(self, name: str, color: str, years: int):
        """
        Инициализация экземпляра класса
        :param name: кличка кота
        :param color: окрас кота
        :param years: возраст(лет)
        Example:
        >>> Cat("Вася", "рыжий", 5)
        """
        if not isinstance(name, str):
            raise TypeError(f"Не тот тип для клички. Ожидается str, а не {type(name)}")
        self.name = name
        if not isinstance(color, str):
            raise TypeError(f"Не тот тип для цвета. Ожидается str, а не {type(color)}")
        self.color = color
        if not isinstance(years, int):
            raise TypeError(f"Не тот тип для возраста. Ожидается int, а не {type(years)}")
        if years < 0:
            raise ValueError(f"Кол-во лет не может быть меньше 0")
        self.years = years

    def newname(self, name: str)-> str:
        if name in self.name:
            raise ValueError(f"Кличка у кота уже есть")
        ... # todo дать коту кличку

    def take_cat_to_home(self, name:str)->bool:
        if name not in self.name:
            raise ValueError(f"Такогго кота не существует")
        ... # todo забрать кота
    def change_year(self,years:int)->int:
        ...
        """Изменение возраста кота"""

class YoutubeChannel:

    def __init__(self, username: str, video: dict = None, title_video = str):
        """
               Инициализация экземпляра класса
               :param username: название канала
               :param video: название видео (title_video) и продолжиетльность в минутах
               :param title_video: название видео
               Example:
               >>> YoutubeChannel("ВасяGG", {"ghbrjks": 50})
               """
        self.username = username
        if video is None:
            self.video = {}
        else:
            self.video = video
        self.title_video = title_video
    """Класс описывает модель ютуб канала"""
    def open_video(self, title_video: str)->bool:
        if title_video not in self.video:
            raise ValueError("Такого видео нет на канале")
        ... # todo открыть видео

    def count_video(self)->int:
        """Считаем количество видео на канале"""
        return sum(self.video.keys())
    def delete_video(self, title_video)->bool:
        """Удаляем видео с канала"""
        if title_video not in self.video:
            ValueError("Видео нет на канале")
        else:
            self.title_video -= 1
        ... # todo удаляем видео
class Calendar:
    def __init__(self, days:int, month: (int,str), year:(int), notes:str):
        """
            Инициализация экземпляра класса
            :param days: число(день)
            :param month: название или номер месяца
            :param year: год
            Example:
            >>> Calendar(15,"Январь", 2001)
        """
        if 31 < days < 0:
            raise ValueError(f"Колличество дней не может быть меньше 0 и больше 31 ")
        if not isinstance(days, int):
            raise TypeError(f"Не тот тип для дня. Ожидается int, а не {type(days)}")
        self.days = days
        if year < 0:
            raise ValueError(f"Год не может быть меньше 0")
        if not isinstance(year, int):
            raise TypeError(f"Не тот тип для года. Ожидается int, а не {type(year)}")
        self.year = year
        if 12 < month < 0:
            raise ValueError(f"номер месяца не может быть меньше 0 больше 12")
        if not isinstance(month, (int,str)):
            raise TypeError(f"Не тот тип для месяца. Ожидается int, а не {type(month)}")
        self.month = month
        if not isinstance(notes, str):
            raise TypeError(f"Не тот тип для месяца. Ожидается int, а не {type(notes)}")
        self.notes = notes

    def change_data(self, days: int, month: (int, str), year: (int)):
        """Меняем дату"""
        ...

    def delete_notes(self, notes: str) -> bool:
        if notes in self.notes:
            ValueError("Заметки нет в расписание")
        """Удаляем заметку из календаря"""
        ...

    def create_notes(self,days: int, month: (int, str), year: (int)) -> str:
        """Создаем заметку в календаре"""
        ...
if __name__ == "__main__":
    import doctest
    doctest.testmod()
