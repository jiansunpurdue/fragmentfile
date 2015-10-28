1, PbPb

git cms-merge-topic 10839

GEN-SIM:

cmsDriver.py fragmentfile/Dmeson_MC_2015/python/Pyquen_D0pt15p0_Pthat15_TuneZ2_Unquenched_5020GeV_prompt_cfi_v3.py --conditions auto:run2_mc_HIon -s GEN,SIM --pileup_input das:/Hydjet_Quenched_MinBias_5020GeV_750/HiFall15-75X_mcRun2_HeavyIon_v1_75X_mcRun2_HeavyIon_v1-v1/GEN-SIM -n 10 --eventcontent RAWSIM --scenario HeavyIons --pileup HiMixGEN --datatier GEN-SIM --beamspot MatchHI --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1_HI --pileup_dasoption "--limit 0" --no_exec

Digi:

cmsDriver.py step2 --conditions auto:run2_mc_HIon --scenario HeavyIons --pileup_input das:/Hydjet_Quenched_MinBias_5020GeV/HiFall14-START71_V1-v2/GEN-SIM --pileup_dasoption --limit 0 -n -1 --eventcontent RAWSIM -s DIGI:pdigi_valid,L1,DIGI2RAW,HLT:HIon,RAW2DIGI,L1Reco --datatier GEN-SIM-DIGI-RAW --pileup HiMix --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1_HI --filein file:Pyquen_Unquenched_AllQCDPhoton30_PhotonFilter20GeV_eta24_TuneZ2_PbPb_5020GeV_cfi_py_GEN_SIM_PU.root --no_exec

Reco:

cmsDriver.py step3 --conditions auto:run2_mc_HIon -s RAW2DIGI,L1Reco,RECO -n -1 --eventcontent RECOSIM --scenario HeavyIons --datatier GEN-SIM-RECO --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1_HI --filein file:step2_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_PU.root --no_exec


2, pp

GEN-SIM:

cmsDriver.py fragmentfile/inclusiveD/python/Pythia_D0pt35p0_Pthat35_TuneZ2_5020GeV_cfi.py --conditions auto:run2_mc --eventcontent RAWSIM -s GEN,SIM --datatier GEN-SIM --beamspot NominalHICollision2015 --no_exec

# beamspot to be decided: NominalCollision2015 (pp 13 TeV) or NominalHICollision2015??? MatchHI does not work because it looks for "mix"

Digi:

cmsDriver.py step2 --conditions auto:run2_mc -n 10 --eventcontent RAWSIM -s DIGI:pdigi_valid,L1,DIGI2RAW,HLT:Fake,RAW2DIGI,L1Reco --datatier GEN-SIM-DIGI-RAW-HLTDEBUG --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1 --no_exec

Reco:

cmsDriver.py step3 --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1 --conditions auto:run2_mc -s RAW2DIGI,L1Reco,RECO --datatier GEN-SIM-RECO -n 10 --eventcontent RECOSIM --no_exec
