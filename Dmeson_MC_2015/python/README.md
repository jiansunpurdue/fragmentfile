*prompt*.py are fragment files for prompt D0 and Ds production

Pythia8_D0pt15p0_Pthat15_TuneCUETP8M1_5020GeV_nonprompt_cfi_evtgen130.py is sample fragment file for non-prompt D0 (better to double check fraction of non-prompt D0)

Pythia8_Dspt15p0_Pthat15_TuneCUETP8M1_5020GeV_nonprompt_cfi_evtgen130.py is sample fragment file for non-prompt Ds (better to double check fraction of non-prompt Ds)


Event level Filter efficiency from 10k inputs:
- prompt D0 filter efficiency: 1.010e-02 (Pt0), 1.300e-02 (Pt5), 7.300e-03 (Pt15), 6.400e-03 (Pt30), 5.400e-03 (Pt50), 2.700e-03 (Pt70), 2.700e-03 (Pt90)
- prompt Ds filter efficiency: 2.300e-03 (Pt0), 2.800e-03 (Pt5), 1.200e-03 (Pt15), 1.100e-03 (Pt30), 1.200e-03 (Pt50)
- non prompt D0 filter efficiency:
- non prompt Ds filter efficiency:


cmsDriver.py commands should be the same with request from other groups. like dilepton: https://twiki.cern.ch/twiki/bin/view/CMS/DileptonEmbeddingRequest

1, PbPb

git cms-merge-topic 10839 (Not in official CMSSW yet)

GEN-SIM:

cmsDriver.py fragmentfile/Dmeson_MC_2015/python/Pythia8_D0pt0p0_Pthat0_TuneCUETP8M1_5020GeV_prompt_cfi_evtgen130.py --conditions auto:run2_mc_HIon -s GEN,SIM --pileup_input das:/Hydjet_Quenched_MinBias_5020GeV_750/HiFall15-75X_mcRun2_HeavyIon_v1_75X_mcRun2_HeavyIon_v1-v1/GEN-SIM -n 10 --eventcontent RAWSIM --scenario HeavyIons --pileup HiMixGEN --datatier GEN-SIM --beamspot MatchHI --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1_HI --pileup_dasoption "--limit 0" --no_exec

Digi:

cmsDriver.py step2 --conditions auto:run2_mc_HIon --scenario HeavyIons --pileup_input das:/Hydjet_Quenched_MinBias_5020GeV/HiFall14-START71_V1-v2/GEN-SIM --pileup_dasoption --limit 0 -n -1 --eventcontent RAWSIM -s DIGI:pdigi_valid,L1,DIGI2RAW,HLT:HIon,RAW2DIGI,L1Reco --datatier GEN-SIM-DIGI-RAW --pileup HiMix --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1_HI --filein file:Pyquen_Unquenched_AllQCDPhoton30_PhotonFilter20GeV_eta24_TuneZ2_PbPb_5020GeV_cfi_py_GEN_SIM_PU.root --no_exec

Reco:

cmsDriver.py step3 --conditions auto:run2_mc_HIon -s RAW2DIGI,L1Reco,RECO -n -1 --eventcontent RECOSIM --scenario HeavyIons --datatier GEN-SIM-RECO --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1_HI --filein file:step2_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_PU.root --no_exec


2, pp

GEN-SIM:

cmsDriver.py fragmentfile/Dmeson_MC_2015/python/Pythia8_D0pt0p0_Pthat0_TuneCUETP8M1_5020GeV_prompt_cfi_evtgen130.py --conditions auto:run2_mc --eventcontent RAWSIM -s GEN,SIM --datatier GEN-SIM --beamspot NominalHICollision2015 --no_exec

# beamspot to be decided: NominalCollision2015 (pp 13 TeV) or NominalHICollision2015??

Digi:

cmsDriver.py step2 --conditions auto:run2_mc -n 10 --eventcontent RAWSIM -s DIGI:pdigi_valid,L1,DIGI2RAW,HLT:Fake,RAW2DIGI,L1Reco --datatier GEN-SIM-DIGI-RAW-HLTDEBUG --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1 --no_exec

Reco:

cmsDriver.py step3 --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1 --conditions auto:run2_mc -s RAW2DIGI,L1Reco,RECO --datatier GEN-SIM-RECO -n 10 --eventcontent RECOSIM --no_exec
