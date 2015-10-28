import FWCore.ParameterSet.Config as cms


from Configuration.Generator.PyquenTuneZ2Settings_cff import *

hiSignal = cms.EDFilter("PyquenGeneratorFilter",
    ptMin = cms.double(1.0),
    etaMax = cms.double(2.0),
    pdg = cms.int32(421),
    status = cms.int32(2),
    minimumCandidates = cms.int32(1),
    filterType = cms.untracked.string("MultiCandGenEvtSelector"),
    aBeamTarget = cms.double(208.0),
    comEnergy = cms.double(2760.0),
    qgpInitialTemperature = cms.double(1.0),
    doCollisionalEnLoss = cms.bool(False),
    qgpNumQuarkFlavor = cms.int32(0),
    qgpProperTimeFormation = cms.double(0.1),
    numQuarkFlavor = cms.int32(0),
    hadronFreezoutTemperature = cms.double(0.14),
    doRadiativeEnLoss = cms.bool(True),
    backgroundLabel = cms.InputTag("generator"),
    embeddingMode = cms.bool(True),
    angularSpectrumSelector = cms.int32(0),
    doIsospin = cms.bool(True),
    doQuench = cms.bool(False),
    cFlag = cms.int32(0),
    bFixed = cms.double(0.0),
    bMin = cms.double(0.0),
    bMax = cms.double(0.0),
    ExternalDecays = cms.PSet(
        EvtGen = cms.untracked.PSet(
            use_default_decay = cms.untracked.bool(False),
            use_internal_pythia = cms.untracked.bool(False),
            decay_table = cms.FileInPath('GeneratorInterface/ExternalDecays/data/DECAY_NOLONGLIFE.DEC'),
            particle_property_file = cms.FileInPath('GeneratorInterface/ExternalDecays/data/evt.pdl'),
            user_decay_file = cms.FileInPath('GeneratorInterface/ExternalDecays/data/D0_Kpi.dec'),
            list_forced_decays = cms.vstring('myD0', 'myanti-D0'),
            operates_on_particles = cms.vint32(0)
        ),
        parameterSets = cms.vstring('EvtGen')
    ),
    PythiaParameters = cms.PSet(
        pyquenPythiaDefaultBlock,
        pythiaDijet = cms.vstring('MSEL=1'),
        parameterSets = cms.vstring('pythiaUESettings',
            'pythiaDijet',
            'kinematics'),
        kinematics = cms.vstring('CKIN(3) = 0.       !(D=0 GeV) lower lim pT_hat',
            'CKIN(4) = 9999.       !(D=-1 GeV) upper lim pT_hat, if < 0 innactive')
    )
)

ProductionFilterSequence = cms.Sequence(hiSignal)
