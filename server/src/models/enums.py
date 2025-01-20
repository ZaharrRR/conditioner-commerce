import enum


class AirConditionerType(enum.Enum):
    """Enum типов кондиционеров"""

    WALL_MOUNTED = "wall_mounted"  # Настенные кондиционеры
    PORTABLE = "portable"  # Переносные мобильные кондиционеры
    WINDOW = "window"  # Оконные кондиционеры
    CASSETTE = "cassette"  # Кассетные кондиционеры
    DUCT = "duct"  # Канальные кондиционеры
    FLOOR_CEILING = "floor_ceiling"  # Напольно-потолочные кондиционеры
    MULTI_SPLIT = "multi_split"  # Мульти-сплит системы
    VRF = "vrf"  # VRF-системы
