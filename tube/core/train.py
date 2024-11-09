from tube.core.platform import Platform, LoadingType

class Train:
    def __init__(self, num_sections: int):
        self._num_sections: int = num_sections
        self._sections: list[int] = [0] * num_sections

    def empty_train(self, num_people_leaving: int, loading_type: LoadingType):
        num_people_on_train = sum(self._sections)

        try:
            leaving_prob = num_people_leaving * loading_type.value / num_people_on_train
        except ZeroDivisionError:
            leaving_prob = 0
        
        new_train = [round(x * (1-leaving_prob)) for x in self._sections]
        self._sections = new_train

    def fill_train(self, platform: Platform):
        new_train = [self._sections[x] + platform.sections[x] for x in range(self._num_sections)]
        self._sections = new_train
        platform.empty_platform()

    def __repr__(self):
        return str(self._sections)