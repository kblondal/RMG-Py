# Data sources
database(
    thermoLibraries=['surfaceThermoPt', 'primaryThermoLibrary', 'thermo_DFT_CCSDTF12_BAC','DFT_QCI_thermo'],
    reactionLibraries = [('Surface/CPOX_Pt/Deutschmann2006', False)],
    seedMechanisms = [],
    kineticsDepositories = ['training'],
    kineticsFamilies = ['surface','default'],
    kineticsEstimator = 'rate rules',
    bindingEnergies = { # default values for Pt(111)
                       'H':(-2.479, 'eV/molecule'),
                       'O':(-3.586, 'eV/molecule'),
                       'C':(-6.750, 'eV/molecule'),
                       'N':(-4.352, 'eV/molecule'),
                       },
)

species(
    label='CH4',
    reactive=True,
    structure=SMILES("[CH4]"),
)

species(
   label='O2',
   reactive=True,
   structure=adjacencyList(
       """
1 O u1 p2 c0 {2,S}
2 O u1 p2 c0 {1,S}
"""),
)

species(
    label='N2',
    reactive=False,
    structure=SMILES("N#N"),
)

species(
    label='vacantX',
    reactive=True,
    structure=adjacencyList("1 X u0"),
)
#----------
# Reaction systems
surfaceReactor(
    temperature=(800,'K'),
    initialPressure=(1.0, 'bar'),
    initialGasMoleFractions={
        "CH4": 0.1,
        "O2": 0.2,
        "N2": 0.7,
    },
    initialSurfaceCoverages={
        "vacantX": 1.0,
    },
    surfaceVolumeRatio=(1.e5, 'm^-1'),
    surfaceSiteDensity=(2.9e-9, 'mol/cm^2'),
    terminationConversion = { "CH4":0.99,},
    terminationTime=(0.1, 's'),
)

simulator(
    atol=1e-18,
    rtol=1e-12,
)

model(
    toleranceKeepInEdge=0.0,
    toleranceMoveToCore=1e-5,
    toleranceInterruptSimulation=0.1,
    maximumEdgeSpecies=100000,
)

options(
    units='si',
    saveRestartPeriod=None,
    generateOutputHTML=True,
    generatePlots=False, # Enable to make plots of core and edge size etc.. But takes 40% of the total runtime!
    saveEdgeSpecies=True,
    saveSimulationProfiles=True,
)
