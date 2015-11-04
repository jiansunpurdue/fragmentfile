*_prompt_*.py are fragment files for prompt D0 and Ds production
*_nonprompt_*.py are fragment files for non-prompt D0 and Ds production

Event level Filter efficiency:
- prompt D0 filter efficiency: 9.600e-03 (Pt0), 1.176e-02 (Pt5), 6.720e-03 (Pt15), 5.760e-03 (Pt30), 4.540e-03 (Pt50), 3.240e-03 (Pt70), 3.580e-03 (Pt90)
- prompt Ds filter efficiency: 1.920e-03 (Pt0), 2.480e-03 (Pt5), 1.180e-03 (Pt15), 1.300e-03 (Pt30), 8.200e-04 (Pt50)
- non prompt D0 filter efficiency: 2.422e-04 (Pt0), 1.419e-03 (Pt5), 1.067e-03 (Pt15), 9.560e-04 (Pt30), 6.531e-04 (Pt50), 5.188e-04 (Pt70), 4.281e-04 (Pt90)
- non prompt Ds filter efficiency: 1.116e-04 (Pt0), 5.590e-04 (Pt5), 5.651e-04 (Pt15), 3.011e-04 (Pt30), 2.116e-04 (Pt50)


cmsDriver.py commands should be the same with request from other groups. like dilepton: https://twiki.cern.ch/twiki/bin/view/CMS/DileptonEmbeddingRequest

1, PbPb

cmsrel CMSSW_7_5_4

cd CMSSW_7_5_4/src

git clone https://github.com/jiansunpurdue/fragmentfile

scram b -j8


GEN-SIM:

cmsDriver.py fragmentfile/Dmeson_MC_2015/python/Pythia8_D0pt15p0_Pthat15_TuneCUETP8M1_5020GeV_prompt_cfi_evtgen130.py --conditions auto:run2_mc_HIon -s GEN,SIM --pileup_input das:/Hydjet_Quenched_MinBias_5020GeV_750/HiFall15-75X_mcRun2_HeavyIon_v1_75X_mcRun2_HeavyIon_v1-v1/GEN-SIM -n 20000 --eventcontent RAWSIM --scenario HeavyIons --pileup HiMixGEN --datatier GEN-SIM --beamspot MatchHI --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1_HI --pileup_dasoption "--limit 0" --no_exec

Digi:

cmsDriver.py step2 --conditions auto:run2_mc_HIon --scenario HeavyIons --pileup_input das:/Hydjet_Quenched_MinBias_5020GeV_750/HiFall15-75X_mcRun2_HeavyIon_v1_75X_mcRun2_HeavyIon_v1-v1/GEN-SIM --pileup_dasoption "--limit 0" -n -1 --eventcontent RAWSIM -s DIGI:pdigi_valid,L1,DIGI2RAW,HLT:HIon,RAW2DIGI,L1Reco --datatier GEN-SIM-DIGI-RAW --pileup HiMix --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1_HI --filein file:Pyquen_Unquenched_AllQCDPhoton30_PhotonFilter20GeV_eta24_TuneZ2_PbPb_5020GeV_cfi_py_GEN_SIM_PU.root --no_exec

Reco:

cmsDriver.py step3 --conditions auto:run2_mc_HIon -s RAW2DIGI,L1Reco,RECO -n -1 --eventcontent RECOSIM --scenario HeavyIons --datatier GEN-SIM-RECO --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1_HI --filein file:step2_DIGI_L1_DIGI2RAW_HLT_RAW2DIGI_L1Reco_PU.root --no_exec


2, pp

GEN-SIM:

cmsDriver.py fragmentfile/Dmeson_MC_2015/python/Pythia8_D0pt15p0_Pthat15_TuneCUETP8M1_5020GeV_prompt_cfi_evtgen130.py -n 20000 --conditions auto:run2_mc --eventcontent RAWSIM -s GEN,SIM --datatier GEN-SIM --beamspot NominalHICollision2015 --no_exec

Digi:

cmsDriver.py step2 --conditions auto:run2_mc -n 10 --eventcontent RAWSIM -s DIGI:pdigi_valid,L1,DIGI2RAW,HLT:Fake,RAW2DIGI,L1Reco --datatier GEN-SIM-DIGI-RAW-HLTDEBUG --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1 --no_exec

Reco:

cmsDriver.py step3 --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1 --conditions auto:run2_mc -s RAW2DIGI,L1Reco,RECO --datatier GEN-SIM-RECO -n 10 --eventcontent RECOSIM --no_exec
