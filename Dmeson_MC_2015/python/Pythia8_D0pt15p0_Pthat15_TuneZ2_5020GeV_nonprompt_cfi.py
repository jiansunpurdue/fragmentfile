import FWCore.ParameterSet.Config as cms


process.generator = cms.EDFilter("Pythia8GeneratorFilter",
    PythiaParameters = cms.PSet(
        parameterSets = cms.vstring('pythia8CommonSettings', 
            'pythia8CUEP8M1Settings', 
            'processParameters'),
        processParameters = cms.vstring('HardQCD:all = on', 
            'PhaseSpace:pTHatMin = 15.', #min pthat 
            'PhaseSpace:pTHatMax = 9999.'),
        pythia8CUEP8M1Settings = cms.vstring('Tune:pp 14', 
            'Tune:ee 7', 
            'MultipartonInteractions:pT0Ref=2.4024', 
            'MultipartonInteractions:ecmPow=0.25208', 
            'MultipartonInteractions:expPow=1.6'),
        pythia8CommonSettings = cms.vstring('Tune:preferLHAPDF = 2', 
            'Main:timesAllowErrors = 10000', 
            'Check:epTolErr = 0.01', 
            'Beams:setProductionScalesFromLHEF = off', 
            'SLHA:keepSM = on', 
            'SLHA:minMassSM = 1000.', 
            'ParticleDecays:limitTau0 = on', 
            'ParticleDecays:tau0Max = 10', 
            'ParticleDecays:allowPhotonRadiation = on')
    ),
    comEnergy = cms.double(5020.0),
    filterEfficiency = cms.untracked.double(1.0),
    maxEventsToPrint = cms.untracked.int32(0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    pythiaPylistVerbosity = cms.untracked.int32(0)
)

configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('PYTHIA 8 (unquenched) D0 (pt > 15 GeV) in NN (pt-hat > 15 GeV) at sqrt(s) = 5.02 TeV')
    )

partonfilter = cms.EDFilter("PythiaFilter",
    ParticleID = cms.untracked.int32(5) # 4 for prompt D0 and 5 for non-prompt D0
)
##or
#partonfilter = cms.EDFilter("MCSingleParticleFilter",
#                       MaxEta     = cms.untracked.vdouble(999.0, 999.0),
#                       MinEta     = cms.untracked.vdouble(-999.0, -999.0),
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

