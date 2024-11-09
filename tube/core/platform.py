import math
from enum import Enum


class LoadingType(Enum):
    FullyLoading = 0
    MostlyLoading = 0.3
    Equal = 0.5
    MostlyEmptying = 0.7
    FullyEmptying = 1


class PlatformEntrance:
    def __init__(self, platform_position: float,
                 passenger_proportion: float = 1):
        if platform_position < 0 or platform_position > 1:
            raise ValueError

        if passenger_proportion < 0 or passenger_proportion > 1:
            raise ValueError

        self._platform_position: float = platform_position
        self._passenger_proportion: float = passenger_proportion

    @property
    def passenger_proportion(self):
        return self._passenger_proportion

    @property
    def platform_position(self):
        return self._platform_position


class Platform:
    def __init__(self, name: str, num_sections: int,
                 entrances: list[PlatformEntrance], loading_type: LoadingType):
        self._name: str = name
        self._num_sections: int = num_sections

        if sum(x.passenger_proportion for x in entrances) != 1:
            raise ValueError

        self._entrances: list[PlatformEntrance] = entrances
        self._loading_type: LoadingType = loading_type
        self.empty_platform()

    def prepare_platform(self, num_passengers: int):
        num_passengers = num_passengers * (1 - self._loading_type.value)
        for entrance in self._entrances:
            passengers_per_entrance = num_passengers * entrance.passenger_proportion

            # find the platform section of the entrance
            entrance_section = min(
                math.floor(
                    self._num_sections *
                    entrance.platform_position),
                self._num_sections -
                1)

            # find the maximum distance to walk (in platform sections) from the
            # entrance
            max_walk_distance = max(
                entrance_section, self._num_sections - 1 - entrance_section)

            distribution_proportions = [1 +
                                        max_walk_distance -
                                        abs(entrance_section -
                                            i) for i in range(self._num_sections)]
            total_distribution_blocks = sum(distribution_proportions)
            new_train = [
                self._sections[x] +
                round(
                    num_passengers *
                    entrance.passenger_proportion *
                    distribution_proportions[x] /
                    total_distribution_blocks) for x in range(
                    self._num_sections)]
            self._sections = new_train

    def empty_platform(self):
        self._sections = [0] * self._num_sections

    @property
    def sections(self):
        return self._sections

    @property
    def loading_type(self):
        return self._loading_type

    @property
    def name(self):
        return self._name

    def __repr__(self):
        return str(self._sections)
