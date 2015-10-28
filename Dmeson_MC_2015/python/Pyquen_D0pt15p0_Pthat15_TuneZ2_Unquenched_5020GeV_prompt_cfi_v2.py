#not sure if work or not, if work, will also need filter efficiency
import FWCore.ParameterSet.Config as cms

#from Configuration.Generator.PyquenTuneZ2Settings_cff import *
from Configuration.Generator.PyquenDefaultSettings_cff import *
from Configuration.Generator.PythiaUEZ2Settings_cfi import *

generator = cms.EDFilter("PyquenGeneratorFilter",
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


partonfilter = cms.EDFilter("PythiaFilter",
    ParticleID = cms.untracked.int32(4) # 4 for prompt D0 and 5 for non-prompt D0
)
##or
#partonfilter = cms.EDFilter("MCSingleParticleFilter",
#                       MaxEta     = cms.untracked.vdouble(3.0, 3.0),
#                       MinEta     = cms.untracked.vdouble(-3.0, -3.0),
#                       MinPt      = cms.untracked.vdouble(0.0, 0.0),
#                       ParticleID = cms.untracked.vint32(4, -4)
#                       )
#
D0filter = cms.EDFilter("MCSingleParticleFilter",
    MaxEta = cms.untracked.vdouble(2.4, 2.4),
    MinEta = cms.untracked.vdouble(-2.4, -2.4),
    MinPt = cms.untracked.vdouble(15.0, 15.0), #min pt
    ParticleID = cms.untracked.vint32(421, -421)
)

ProductionFilterSequence = cms.Sequence(generator*partonfilter*D0filter)
