import FWCore.ParameterSet.Config as cms

#from Configuration.Generator.PyquenTuneZ2Settings_cff import *
from Configuration.Generator.PyquenDefaultSettings_cff import *
from Configuration.Generator.PythiaUEZ2Settings_cfi import *

generator = cms.EDFilter("PyquenGeneratorFilter",
    etaMax     = cms.double(3.0), # will this introduce bias? Should apply eta cut on D0, but should not on the parton
	partons    = cms.vint32(5), # 4 for prompt and 5 for non-prompt
	partonPt   = cms.vdouble(0),
	partonStatus = cms.vint32(2),
	particleStatus = cms.vint32(2),
	particles = cms.vint32(421),
	particlePt = cms.vdouble(15.0), # min particle pt
	filterType = cms.untracked.string("EcalGenEvtSelector"),
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
