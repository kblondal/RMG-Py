#Data sources
database(
    thermoLibraries=['primaryThermoLibrary', 'thermo_DFT_CCSDTF12_BAC','DFT_QCI_thermo'],
    reactionLibraries = [('BurkeH2O2inN2', False),('combustion_core/version5',False)],
    seedMechanisms = [],
    kineticsDepositories = ['training'],
    kineticsFamilies ='default',
    kineticsEstimator = 'rate rules',
#    bindingEnergies = { # default values for Pt(111)
#                       'H':(-0.240, 'eV/molecule'),
#                       'O':(-1.030, 'eV/molecule'),
#                       'C':(-6.750, 'eV/molecule'),
#                       'N':(0.525, 'eV/molecule'),
#                       }
)

# List of species
#species(
#    label='X',
#    reactive=True,
#    structure=adjacencyList("1 X u0"),
#)

species(
    label='CH4',
    reactive=True,
    structure=SMILES("[CH4]"),
)

species(
    label='CH3',
    reactive=True,
    structure=SMILES("[CH3]"),
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


#----------
#Reaction system
simpleReactor(
    temperature=(1500,'K'),
    pressure=(1.0,'bar'),
    initialMoleFractions={
        "CH4": 0.1,
        "CH3": 0.01,
        "O2": 0.1890,
        "N2": 0.7110,
    },
    terminationConversion={
        'CH4': 0.9,
    },
)


simulator(
    atol=1e-18,
    rtol=1e-12,
)

model(
    toleranceKeepInEdge=0.0,
    toleranceMoveToCore=1e-4,
    toleranceInterruptSimulation=0.1,
    maximumEdgeSpecies=100000
)

options(
    units='si',
    saveRestartPeriod=None,
    generateOutputHTML=True,
    generatePlots=False,
#    saveEdgeSpecies=True,
    saveSimulationProfiles=True,
)

