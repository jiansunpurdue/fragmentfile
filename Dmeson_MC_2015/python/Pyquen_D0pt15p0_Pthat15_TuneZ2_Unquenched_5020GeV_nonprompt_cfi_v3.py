import FWCore.ParameterSet.Config as cms

#from Configuration.Generator.PyquenTuneZ2Settings_cff import *
from Configuration.Generator.PyquenDefaultSettings_cff import *
from Configuration.Generator.PythiaUEZ2Settings_cfi import *

generator = cms.EDFilter("PyquenGeneratorFilter",
    partons      = cms.vint32(5), # 4 for prompt and 5 for non-prompt
    partonStatus = cms.vint32(2),
    partonEtaMax = cms.vdouble(999.),
    partonPtMin  = cms.vdouble(0.),
    hadrons      = cms.vint32(421),
    hadronStatus = cms.vint32(2),
    hadronEtaMax = cms.vdouble(2.4),
    hadronEtaMin = cms.vdouble(-2.4),
    hadronPMin   = cms.vdouble(0.0), #momentum cut, just cut on pt
    hadronPtMax  = cms.vdouble(999.),
    hadronPtMin  = cms.vdouble(15.), #D0 pt cut
    decays      = cms.int32(211), # does not cut on daughters of D0, but needed by the filter
    decayStatus = cms.int32(1),
    decayEtaMax = cms.double(999.),
    decayEtaMin = cms.double(-999.),
    decayPMin   = cms.double(0.0),
    decayPtMax  = cms.double(999.),
    decayPtMin  = cms.double(0.),
    decayNtrig  = cms.int32(1),
    filterType = cms.untracked.string("PartonHadronDecayGenEvtSelector"), #just filter on parton and D0
    aBeamTarget = cms.double(208.0),
    comEnergy = cms.double(5020.0),
    qgpInitialTemperature = cms.double(1.0),
    doCollisionalEnLoss = cms.bool(False),
    qgpNumQuarkFlavor = cms.int32(0),
    qgpProperTimeFormation = cms.double(0.1),
    numQuarkFlavor = cms.int32(0),
    hadronFreezoutTemperature = cms.double(0.14),
    doRadiativeEnLoss = cms.bool(True),
    backgroundLabel = cms.InputTag("generator"),
    embeddingMode = cms.bool(False),
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
        kinematics = cms.vstring('CKIN(3) = 15.       !(D=0 GeV) lower lim pT_hat', #min pthat
            'CKIN(4) = 9999.       !(D=-1 GeV) upper lim pT_hat, if < 0 innactive')
    )
)

ProductionFilterSequence = cms.Sequence(generator)
