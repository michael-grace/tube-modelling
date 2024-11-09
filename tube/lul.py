import tube.core

class DeepTubeLinePlatform(tube.core.Platform):
    def __init__(self, name: str, entrances: list[tube.core.PlatformEntrance], loading_type: tube.core.LoadingType, yearly_passengers: int, trains_per_hour: int):
        self._yearly_passengers: int = yearly_passengers
        self._trains_per_hour: int = trains_per_hour

        super().__init__(name, 6 * 6, entrances, loading_type)

    @property
    def passengers_per_train(self):
        return self._yearly_passengers / (365 * 18 * self._trains_per_hour * 2)

class DeepTubeTrain(tube.core.Train):
    def __init__(self):
        super().__init__(6 * 6)

    def __repr__(self):
        return "|-_---__---__---_-|  " * 6 + "\n" + \
       "--".join([f"| {self._sections[i * 6]}  {self._sections[i * 6 + 1]}  {self._sections[i*6+2]} {self._sections[i*6+3]}  {self._sections[i*6+4]}  {self._sections[i*6+5]} |" for i in range(6)]) + " BACK \n" + \
        "|_-___--___--___-_|  " * 6

    def run_journey(self, platforms: list[DeepTubeLinePlatform]):
        for platform in platforms:
            platform.prepare_platform(platform.passengers_per_train)
            self.empty_train(platform.passengers_per_train, platform.loading_type)
            self.fill_train(platform)
            platform.empty_platform()
            print(platform.name + ":\n" + str(self) + "\n")

