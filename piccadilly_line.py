from tube.lul import DeepTubeTrain, DeepTubeLinePlatform
from tube.core import PlatformEntrance, LoadingType

MILLION = 1000000

# Eastbound Journey
DeepTubeTrain().run_journey([
    DeepTubeLinePlatform("Heathrow Terminal 4", [
        PlatformEntrance(0.33)
    ], LoadingType.FullyLoading, 1.45 * MILLION, 6),

    DeepTubeLinePlatform("Heathrow Terminal 2+3", [
        PlatformEntrance(0.33, 0.66),
        PlatformEntrance(0.66, 0.34),
    ], LoadingType.FullyLoading, 5.37 * MILLION, 12),

    DeepTubeLinePlatform("Hatton Cross", [
        PlatformEntrance(0.4)
    ], LoadingType.FullyLoading, 2.85 * MILLION, 12),

    DeepTubeLinePlatform("Hounslow West", [
        PlatformEntrance(0.6)
    ], LoadingType.MostlyLoading, 2.78 * MILLION, 12),

    DeepTubeLinePlatform("Hounslow Central", [
        PlatformEntrance(0)
    ], LoadingType.MostlyLoading, 3 * MILLION, 12),

    DeepTubeLinePlatform("Hounslow East", [
        PlatformEntrance(0)
    ], LoadingType.MostlyLoading, 3.37 * MILLION, 12),

    DeepTubeLinePlatform("Osterley", [
        PlatformEntrance(0)
    ], LoadingType.MostlyLoading, 1.68 * MILLION, 12),

    DeepTubeLinePlatform("Boston Manor", [
        PlatformEntrance(1)
    ], LoadingType.MostlyLoading, 1.44 * MILLION, 12),

    DeepTubeLinePlatform("Northfields", [
        PlatformEntrance(0)
    ], LoadingType.MostlyLoading, 2.78 * MILLION, 15),

    DeepTubeLinePlatform("South Ealing", [
        PlatformEntrance(1)
    ], LoadingType.MostlyLoading, 1.66 * MILLION, 15),

    DeepTubeLinePlatform("Acton Town", [
        PlatformEntrance(0.75)
    ], LoadingType.MostlyLoading, 4.82 * 0.5 * MILLION, 21),

    DeepTubeLinePlatform("Hammersmith", [
        PlatformEntrance(0, 0.5),
        PlatformEntrance(1, 0.5)
    ], LoadingType.MostlyLoading, 20.29 * MILLION * 0.5, 21),
    
    DeepTubeLinePlatform("Barons' Court", [
        PlatformEntrance(0)
    ], LoadingType.MostlyLoading, 5.24 * 0.5 * MILLION, 21),

    DeepTubeLinePlatform("Earl's Court",
    [PlatformEntrance(0.33, 0.5),
    PlatformEntrance(0.66, 0.5)],
    LoadingType.Equal, 15.78 * MILLION, 21),

    DeepTubeLinePlatform("Gloucester Road",
    [PlatformEntrance(0.33)], LoadingType.Equal, 11.35 * MILLION * 0.5, 21),

    DeepTubeLinePlatform("South Kensington",
    [PlatformEntrance(0.33)], LoadingType.Equal, 26.09 * MILLION * 0.5, 21),

    DeepTubeLinePlatform("Knightsbridge",
    [PlatformEntrance(0.33)], LoadingType.Equal, 13.57 * MILLION, 21),

    DeepTubeLinePlatform("Hyde Park Corner", 
    [PlatformEntrance(0)], LoadingType.Equal, 4.16 * MILLION, 21),

    DeepTubeLinePlatform("Green Park",
    [PlatformEntrance(1, 0.66), PlatformEntrance(0.5, 0.34)], LoadingType.Equal, 28.25 * MILLION, 21),

    DeepTubeLinePlatform("Piccadilly Circus",
    [PlatformEntrance(0.5, 0.7), PlatformEntrance(0.2, 0.3)], LoadingType.Equal, 26.74 * MILLION, 21),

    DeepTubeLinePlatform("Leicester Square",
    [PlatformEntrance(0.2, 0.7), PlatformEntrance(1, 0.3)], LoadingType.Equal, 27.38 * MILLION, 21),

    DeepTubeLinePlatform("Covent Garden",
    [PlatformEntrance(0.4)], LoadingType.Equal, 12.57 * MILLION, 21),

    DeepTubeLinePlatform("Holborn",
    [PlatformEntrance(0.6)], LoadingType.Equal, 20.24 * MILLION, 21),

    DeepTubeLinePlatform("Russell Square",
    [PlatformEntrance(0.7)], LoadingType.Equal, 7.82 * MILLION, 21)
])
