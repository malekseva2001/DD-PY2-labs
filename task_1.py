class SocialMedia:
    """ Базовый класс социальные сети. """

    def __init__(self, name: str, domain: str):
        """
        Инициализация экземпляра класса
        :param name: название площадки
        :param domain: адресс сайта
        """
        self._name = name
        self._domain = domain

    @property
    def name(self) -> str:
        return self._name

    @property
    def domain(self) -> str:
        return self._domain

    def __str__(self):
        return f"Социальная сеть {self.name}. Адрес сайта {self.domain}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, domain={self.domain!r})"

    def __eq__(self, other):
        return self.domain == other.domain

    def get_domain(self) -> str:
        """Функция возвращает домен экземпляра"""
        return self._domain



class VK(SocialMedia):
    """ Дочерний класс социальные сети VK. """

    def __init__(self, name: str, domain: str, subscribes: int):
        """
        Инициализация экземпляра класса
        :param name: название площадки
        :param domain: адресс сайта
        :param subscribes: кол-во подписчиков
        """
        super().__init__(name, domain)
        self.subscribes = subscribes

    @property
    def subscribes(self) -> int:
        return self._subscribes

    @subscribes.setter
    def subscribes(self,  subscribes: int) -> None:
        if not isinstance(subscribes, int):
            raise TypeError
        if subscribes < 0:
            raise ValueError
        self._subscribes = subscribes

    def __str__(self):
        return f"Социальная сеть {self.name}. Адрес сайта {self.domain}. Кол-во подписчиков {self._subscribes}."

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, domain={self.domain!r}, subscribes={self.subscribes!r})"

    def domain_for_vk(self):
        """Создание ссылки web-сайта
           Перегружаем метод get_domain для добавлемя к нему приставки www
        """
        ad_domain = super().get_domain()
        return f"www.{ad_domain}"

if __name__ == "__main__":
    BOOKS_DATABASE = [
        {
            "name": "VK",
            "domain": "vk.com",
            "subscribes": 222,
        },
        {
            "name": "test_name_2",
            "domain": "domain.com",
        }
    ]
    list_examination = [
        SocialMedia(name=book_dict["name"], domain=book_dict["domain"]) for book_dict in BOOKS_DATABASE
    ]

    for book in list_examination:
        print(book)  # проверяем метод __str__

    print(list_examination)  # проверяем метод __repr__

    print(VK("vk", "vk.com", 222)) # проверяем метод __str__
    print(repr(VK("vk", "vk.com", 222))) # проверяем метод __repr__

    sm1=VK("vko", "vk.ru", 555) # проверяем метод __eq__
    sm2=VK("vk", "vk.com", 888)
    print(sm1==sm2)

    print(SocialMedia.get_domain(sm1)) # проверяем метод get_domain
    print(VK.get_domain(sm2))

    print(VK.domain_for_vk(sm2))
    pass
