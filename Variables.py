#This file contains a dictionary with all the id's of observables
#used in MC++. Functions should only ever have deal with these id's
#Data from e.g. a point has the structure {id:value, ...}
#examples of id's are
#1) ('slha',('block',(indices),slhalib_nr)))
#2) ('BPhysics','Bsmm')
#
#1) completely defines the slha handles. Note that we have to be
# very careful with the slhalib_nr. We need a script that compares
# the id's. It is important that the slha id can directly be used in
# the slha class, and set
#2) (predictor, specification) is a reasonable way to do this

# in order to get the names of the predictors
from ObsCalculator.interfaces import softsusy
from ObsCalculator.interfaces import feynhiggs, micromegas, superiso, bphysics, lspscat
from ObsCalculator.interfaces import susypope

#for short names corresponding to slha: do use the slha lib comments 
def get_ids():
    ids={
        'Mh0'       :(feynhiggs.name,   'mh'),
        'ssiKO'     :(lspscat.name,'s3out'),
        'bsmmBP'    :(bphysics.name,'Psll'),
        
        # SLHA variables
        # Straight from slhafile.suggested_ids_dict()
        'invAlfaMZ' : ('slha', ('SMINPUTS', (1,), 7)),
        'GF'        : ('slha', ('SMINPUTS', (2,), 8)),
        'AlfasMZ'   : ('slha', ('SMINPUTS', (3,), 9)),
        'MZ'        : ('slha', ('SMINPUTS', (4,), 10)),
        'Mb'        : ('slha', ('SMINPUTS', (5,), 22)),
        'Mt'        : ('slha', ('SMINPUTS', (6,), 21)),
        'Mtau'      : ('slha', ('SMINPUTS', (7,), 20)),
        'M0'        : ('slha', ('MINPAR', (1,), 23)),
        'M12'       : ('slha', ('MINPAR', (2,), 24)),
        'MINPARTB'  : ('slha', ('MINPAR', (3,), 25)),
        'signMUE'   : ('slha', ('MINPAR', (4,), 26)),
        'A'         : ('slha', ('MINPAR', (5,), 27)),
        'Q'         : ('slha', ('EXTPAR', (0,), 29)),
        'MSf(1,1,1)': ('slha', ('MASS', (1000012,), 110)),
        'MSf(1,2,1)': ('slha', ('MASS', (1000011,), 112)),
        'MSf(2,2,1)': ('slha', ('MASS', (2000011,), 113)),
        'MSf(1,3,1)': ('slha', ('MASS', (1000002,), 114)),
        'MSf(2,3,1)': ('slha', ('MASS', (2000002,), 115)),
        'MSf(1,4,1)': ('slha', ('MASS', (1000001,), 116)),
        'MSf(2,4,1)': ('slha', ('MASS', (2000001,), 117)),
        'MSf(1,1,2)': ('slha', ('MASS', (1000014,), 118)),
        'MSf(1,2,2)': ('slha', ('MASS', (1000013,), 120)),
        'MSf(2,2,2)': ('slha', ('MASS', (2000013,), 121)),
        'MSf(1,3,2)': ('slha', ('MASS', (1000004,), 122)),
        'MSf(2,3,2)': ('slha', ('MASS', (2000004,), 123)),
        'MSf(1,4,2)': ('slha', ('MASS', (1000003,), 124)),
        'MSf(2,4,2)': ('slha', ('MASS', (2000003,), 125)),
        'MSf(1,1,3)': ('slha', ('MASS', (1000016,), 126)),
        'MSf(1,2,3)': ('slha', ('MASS', (1000015,), 128)),
        'MSf(2,2,3)': ('slha', ('MASS', (2000015,), 129)),
        'MSf(1,3,3)': ('slha', ('MASS', (1000006,), 130)),
        'MSf(2,3,3)': ('slha', ('MASS', (2000006,), 131)),
        'MSf(1,4,3)': ('slha', ('MASS', (1000005,), 132)),
        'MSf(2,4,3)': ('slha', ('MASS', (2000005,), 133)),
        'MW'        : ('slha', ('MASS', (24,), 135)),
        'Mh0'       : ('slha', ('MASS', (25,), 136)),
        'MHH'       : ('slha', ('MASS', (35,), 137)),
        'MA0'       : ('slha', ('MASS', (36,), 138)),
        'MHp'       : ('slha', ('MASS', (37,), 139)),
        'MNeu(1)'   : ('slha', ('MASS', (1000022,), 142)),
        'MNeu(2)'   : ('slha', ('MASS', (1000023,), 143)),
        'MNeu(3)'   : ('slha', ('MASS', (1000025,), 144)),
        'MNeu(4)'   : ('slha', ('MASS', (1000035,), 145)),
        'MCha(1)'   : ('slha', ('MASS', (1000024,), 147)),
        'MCha(2)'   : ('slha', ('MASS', (1000037,), 148)),
        'MGl'       : ('slha', ('MASS', (1000021,), 149)),
        'ZNeu(1,1)' : ('slha', ('NMIX', (1, 1), 156)),
        'ZNeu(1,2)' : ('slha', ('NMIX', (1, 2), 160)),
        'ZNeu(1,3)' : ('slha', ('NMIX', (1, 3), 164)),
        'ZNeu(1,4)' : ('slha', ('NMIX', (1, 4), 168)),
        'ZNeu(2,1)' : ('slha', ('NMIX', (2, 1), 157)),
        'ZNeu(2,2)' : ('slha', ('NMIX', (2, 2), 161)),
        'ZNeu(2,3)' : ('slha', ('NMIX', (2, 3), 165)),
        'ZNeu(2,4)' : ('slha', ('NMIX', (2, 4), 169)),
        'ZNeu(3,1)' : ('slha', ('NMIX', (3, 1), 158)),
        'ZNeu(3,2)' : ('slha', ('NMIX', (3, 2), 162)),
        'ZNeu(3,3)' : ('slha', ('NMIX', (3, 3), 166)),
        'ZNeu(3,4)' : ('slha', ('NMIX', (3, 4), 170)),
        'ZNeu(4,1)' : ('slha', ('NMIX', (4, 1), 159)),
        'ZNeu(4,2)' : ('slha', ('NMIX', (4, 2), 163)),
        'ZNeu(4,3)' : ('slha', ('NMIX', (4, 3), 167)),
        'ZNeu(4,4)' : ('slha', ('NMIX', (4, 4), 171)),
        'UCha(1,1)' : ('slha', ('UMIX', (1, 1), 172)),
        'UCha(1,2)' : ('slha', ('UMIX', (1, 2), 174)),
        'UCha(2,1)' : ('slha', ('UMIX', (2, 1), 173)),
        'UCha(2,2)' : ('slha', ('UMIX', (2, 2), 175)),
        'VCha(1,1)' : ('slha', ('VMIX', (1, 1), 176)),
        'VCha(1,2)' : ('slha', ('VMIX', (1, 2), 178)),
        'VCha(2,1)' : ('slha', ('VMIX', (2, 1), 177)),
        'VCha(2,2)' : ('slha', ('VMIX', (2, 2), 179)),
        'STAUMIXUSf(1,1)': ('slha', ('STAUMIX', (1, 1), 180)),
        'STAUMIXUSf(1,2)': ('slha', ('STAUMIX', (1, 2), 182)),
        'STAUMIXUSf(2,1)': ('slha', ('STAUMIX', (2, 1), 181)),
        'STAUMIXUSf(2,2)': ('slha', ('STAUMIX', (2, 2), 183)),
        'STOPMIXUSf(1,1)': ('slha', ('STOPMIX', (1, 1), 184)),
        'STOPMIXUSf(1,2)': ('slha', ('STOPMIX', (1, 2), 186)),
        'STOPMIXUSf(2,1)': ('slha', ('STOPMIX', (2, 1), 185)),
        'STOPMIXUSf(2,2)': ('slha', ('STOPMIX', (2, 2), 187)),
        'SBOTMIXUSf(1,1)': ('slha', ('SBOTMIX', (1, 1), 188)),
        'SBOTMIXUSf(1,2)': ('slha', ('SBOTMIX', (1, 2), 190)),
        'SBOTMIXUSf(2,1)': ('slha', ('SBOTMIX', (2, 1), 189)),
        'SBOTMIXUSf(2,2)': ('slha', ('SBOTMIX', (2, 2), 191)),
        'Alpha': ('slha', ('ALPHA', (), 192)),
        'MUE': ('slha', ('HMIX', (1,), 195)),
        'HMIXTB': ('slha', ('HMIX', (2,), 196)),
        'VEV': ('slha', ('HMIX', (3,), 197)),
        'MA02': ('slha', ('HMIX', (4,), 198)),
        'g1': ('slha', ('GAUGE', (1,), 200)),
        'g2': ('slha', ('GAUGE', (2,), 201)),
        'g3': ('slha', ('GAUGE', (3,), 202)),
        'M1': ('slha', ('MSOFT', (1,), 204)),
        'M2': ('slha', ('MSOFT', (2,), 205)),
        'M3': ('slha', ('MSOFT', (3,), 206)),
        'MHd2': ('slha', ('MSOFT', (21,), 208)),
        'MHu2': ('slha', ('MSOFT', (22,), 207)),
        'MSL(1)': ('slha', ('MSOFT', (31,), 209)),
        'MSL(2)': ('slha', ('MSOFT', (32,), 210)),
        'MSL(3)': ('slha', ('MSOFT', (33,), 211)),
        'MSE(1)': ('slha', ('MSOFT', (34,), 212)),
        'MSE(2)': ('slha', ('MSOFT', (35,), 213)),
        'MSE(3)': ('slha', ('MSOFT', (36,), 214)),
        'MSQ(1)': ('slha', ('MSOFT', (41,), 215)),
        'MSQ(2)': ('slha', ('MSOFT', (42,), 216)),
        'MSQ(3)': ('slha', ('MSOFT', (43,), 217)),
        'MSU(1)': ('slha', ('MSOFT', (44,), 218)),
        'MSU(2)': ('slha', ('MSOFT', (45,), 219)),
        'MSU(3)': ('slha', ('MSOFT', (46,), 220)),
        'MSD(1)': ('slha', ('MSOFT', (47,), 221)),
        'MSD(2)': ('slha', ('MSOFT', (48,), 222)),
        'MSD(3)': ('slha', ('MSOFT', (49,), 223)),
        'AEAf(1,1)': ('slha', ('AE', (1, 1), 225)),
        'AEAf(2,2)': ('slha', ('AE', (2, 2), 229)),
        'AEAf(3,3)': ('slha', ('AE', (3, 3), 233)),
        'AUAf(1,1)': ('slha', ('AU', (1, 1), 235)),
        'AUAf(2,2)': ('slha', ('AU', (2, 2), 239)),
        'AUAf(3,3)': ('slha', ('AU', (3, 3), 243)),
        'ADAf(1,1)': ('slha', ('AD', (1, 1), 245)),
        'ADAf(2,2)': ('slha', ('AD', (2, 2), 249)),
        'ADAf(3,3)': ('slha', ('AD', (3, 3), 253)),
        'YEYf(3,3)': ('slha', ('YE', (3, 3), 266)),
        'YUYf(3,3)': ('slha', ('YU', (3, 3), 276)),
        'YDYf(3,3)': ('slha', ('YD', (3, 3), 286)),
        'UH(1,1)': ('slha', ('CVHMIX', (1, 1), 1205)),
        'UH(1,2)': ('slha', ('CVHMIX', (1, 2), 1209)),
        'UH(1,3)': ('slha', ('CVHMIX', (1, 3), 1213)),
        'UH(2,1)': ('slha', ('CVHMIX', (2, 1), 1206)),
        'UH(2,2)': ('slha', ('CVHMIX', (2, 2), 1210)),
        'UH(2,3)': ('slha', ('CVHMIX', (2, 3), 1214)),
        'UH(3,1)': ('slha', ('CVHMIX', (3, 1), 1207)),
        'UH(3,2)': ('slha', ('CVHMIX', (3, 2), 1211)),
        'UH(3,3)': ('slha', ('CVHMIX', (3, 3), 1215)),
        'DeltaRho': ('slha', ('PRECOBS', (1,), 1264)),
        'MWSM': ('slha', ('PRECOBS', (3,), 1266)),
        'SW2effSM': ('slha', ('PRECOBS', (5,), 1268)),
        'gminus2mu': ('slha', ('PRECOBS', (11,), 1269)),
        'EDMeTh': ('slha', ('PRECOBS', (21,), 1270)),
        'EDMn': ('slha', ('PRECOBS', (22,), 1271)),
        'EDMHg': ('slha', ('PRECOBS', (23,), 1272)),
        }
    return ids
#        'AlfasMZ'   : ('slha', ('SMINPUTS', (3,), 9)),
#        'GF'        : ('slha', ('SMINPUTS', (2,), 8)),
#        'MZ'        : ('slha', ('SMINPUTS', (4,), 10)),
#        'Mb'        : ('slha', ('SMINPUTS', (5,), 22)),
#        'Mt'        : ('slha', ('SMINPUTS', (6,), 21)),
#        'Mtau'      : ('slha', ('SMINPUTS', (7,), 20)),
#        'invAlfaMZ' : ('slha', ('SMINPUTS', (1,), 7)),
#
#        'm0'        : ('slha', ('MINPAR', (1,), 23)),
#        'm12'       : ('slha', ('MINPAR', (2,), 24)),
#        'tanb'      : ('slha', ('MINPAR', (3,), 25)),
#        'signMUE'   : ('slha', ('MINPAR', (4,), 26)),
#        'A0'        : ('slha', ('MINPAR', (5,), 27)),
#
#        'Q'         : ('slha', ('EXTPAR', (0,), 29)),
#
#        'MA0'       : ('slha', ('MASS', (36,), 138)),
#        'MCha(1)'   : ('slha', ('MASS', (1000024,), 147)),
#        'MCha(2)'   : ('slha', ('MASS', (1000037,), 148)),
#        'MGl'       : ('slha', ('MASS', (1000021,), 149)),
#        'MHH'       : ('slha', ('MASS', (35,), 137)),
#        'MHp'       : ('slha', ('MASS', (37,), 139)),
#        'MNeu(1)'   : ('slha', ('MASS', (1000022,), 142)),
#        'MNeu(2)'   : ('slha', ('MASS', (1000023,), 143)),
#        'MNeu(3)'   : ('slha', ('MASS', (1000025,), 144)),
#        'MNeu(4)'   : ('slha', ('MASS', (1000035,), 145)),
#        'MSf(1,1,1)': ('slha', ('MASS', (1000012,), 110)),
#        'MSf(1,1,2)': ('slha', ('MASS', (1000014,), 118)),
#        'MSf(1,1,3)': ('slha', ('MASS', (1000016,), 126)),
#        'MSf(1,2,1)': ('slha', ('MASS', (1000011,), 112)),
#        'MSf(1,2,2)': ('slha', ('MASS', (1000013,), 120)),
#        'MSf(1,2,3)': ('slha', ('MASS', (1000015,), 128)),
#        'MSf(1,3,1)': ('slha', ('MASS', (1000002,), 114)),
#        'MSf(1,3,2)': ('slha', ('MASS', (1000004,), 122)),
#        'MSf(1,3,3)': ('slha', ('MASS', (1000006,), 130)),
#        'MSf(1,4,1)': ('slha', ('MASS', (1000001,), 116)),
#        'MSf(1,4,2)': ('slha', ('MASS', (1000003,), 124)),
#        'MSf(1,4,3)': ('slha', ('MASS', (1000005,), 132)),
#        'MSf(2,2,1)': ('slha', ('MASS', (2000011,), 113)),
#        'MSf(2,2,2)': ('slha', ('MASS', (2000013,), 121)),
#        'MSf(2,2,3)': ('slha', ('MASS', (2000015,), 129)),
#        'MSf(2,3,1)': ('slha', ('MASS', (2000002,), 115)),
#        'MSf(2,3,2)': ('slha', ('MASS', (2000004,), 123)),
#        'MSf(2,3,3)': ('slha', ('MASS', (2000006,), 131)),
#        'MSf(2,4,1)': ('slha', ('MASS', (2000001,), 117)),
#        'MSf(2,4,2)': ('slha', ('MASS', (2000003,), 125)),
#        'MSf(2,4,3)': ('slha', ('MASS', (2000005,), 133)),
#        'MW'        : ('slha', ('MASS', (24,), 135)),
#        'Mh0'       : ('slha', ('MASS', (25,), 136)),
#        'M1'        : ('slha', ('MSOFT', (1,), 204)),
#        'M2'        : ('slha', ('MSOFT', (2,), 205)),
#        'M3'        : ('slha', ('MSOFT', (3,), 206)),
#        'MHu2'      : ('slha', ('MSOFT', (22,), 207)),
#        'MHd2'      : ('slha', ('MSOFT', (21,), 208)),
#        'MSD(1)'    : ('slha', ('MSOFT', (47,), 221)),
#        'MSD(2)'    : ('slha', ('MSOFT', (48,), 222)),
#        'MSD(3)'    : ('slha', ('MSOFT', (49,), 223)),
#        'MSE(1)'    : ('slha', ('MSOFT', (34,), 212)),
#        'MSE(2)'    : ('slha', ('MSOFT', (35,), 213)),
#        'MSE(3)'    : ('slha', ('MSOFT', (36,), 214)),
#        'MSL(1)'    : ('slha', ('MSOFT', (31,), 209)),
#        'MSL(2)'    : ('slha', ('MSOFT', (32,), 210)),
#        'MSL(3)'    : ('slha', ('MSOFT', (33,), 211)),
#        'MSQ(1)'    : ('slha', ('MSOFT', (41,), 215)),
#        'MSQ(2)'    : ('slha', ('MSOFT', (42,), 216)),
#        'MSQ(3)'    : ('slha', ('MSOFT', (43,), 217)),
#        'MSU(1)'    : ('slha', ('MSOFT', (44,), 218)),
#        'MSU(2)'    : ('slha', ('MSOFT', (45,), 219)),
#        'MSU(3)'    : ('slha', ('MSOFT', (46,), 220)),
#        'Ae(1,1)'   : ('slha', ('AE', (1, 1), 225)),
#        'Ae(2,2)'   : ('slha', ('AE', (2, 2), 229)),
#        'Ae(3,3)'   : ('slha', ('AE', (3, 3), 233)),
#        'Au(1,1)'   : ('slha', ('AU', (1, 1), 235)),
#        'Au(2,2)'   : ('slha', ('AU', (2, 2), 239)),
#        'Au(3,3)'   : ('slha', ('AU', (3, 3), 243)),
#        'Ad(1,1)'   : ('slha', ('AD', (1, 1), 245)),
#        'Ad(2,2)'   : ('slha', ('AD', (2, 2), 249)),
#        'Ad(3,3)'   : ('slha', ('AD', (3, 3), 253)),
#        'Alpha'     : ('slha', ('ALPHA', (), 192)),
#        'MUE'       : ('slha', ('HMIX', (1,), 195)),
#        'TB'        : ('slha', ('HMIX', (2,), 196)),
#        'VEV'       : ('slha', ('HMIX', (3,), 197)),
#        'MA02'      : ('slha', ('HMIX', (4,), 198)),
#        'UCha(1,2)' : ('slha', ('UMIX', (1, 2), 174)),
#        'UCha(2,1)' : ('slha', ('UMIX', (2, 1), 173)),
#        'UH(1,1)'   : ('slha', ('CVHMIX', (1, 1), 1205)),
#        'UH(2,2)'   : ('slha', ('CVHMIX', (2, 2), 1210)),
#        'UH(2,3)'   : ('slha', ('CVHMIX', (2, 3), 1214)),
#        'UH(3,1)'   : ('slha', ('CVHMIX', (3, 1), 1207)),
#        'UH(3,3)'   : ('slha', ('CVHMIX', (3, 3), 1215)),
#        'UStop(1,1)': ('slha', ('STOPMIX', (1, 1), 184)),
#        'UStop(2,2)': ('slha', ('STOPMIX', (2, 2), 187)),
#        'USbot(1,2)': ('slha', ('SBOTMIX', (1, 2), 190)),
#        'USbot(2,1)': ('slha', ('SBOTMIX', (2, 1), 189)),
#        'UStau(1,1)': ('slha', ('STAUMIX', (1, 1), 180)),
#        'UStau(2,2)': ('slha', ('STAUMIX', (2, 2), 183)),
#        'VCha(1,2)' : ('slha', ('VMIX', (1, 2), 178)),
#        'VCha(2,1)' : ('slha', ('VMIX', (2, 1), 177)),
#        'YUf(3,3)'  : ('slha', ('YU', (3, 3), 276)),
#        'YDf(3,3)'  : ('slha', ('YD', (3, 3), 286)),
#        'YEf(3,3)'  : ('slha', ('YE', (3, 3), 266)),
#        'ZNeu(1,1)' : ('slha', ('NMIX', (1, 1), 156)),
#        'ZNeu(1,2)' : ('slha', ('NMIX', (1, 2), 160)),
#        'ZNeu(1,3)' : ('slha', ('NMIX', (1, 3), 164)),
#        'ZNeu(1,4)' : ('slha', ('NMIX', (1, 4), 168)),
#        'ZNeu(2,1)' : ('slha', ('NMIX', (2, 1), 157)),
#        'ZNeu(2,2)' : ('slha', ('NMIX', (2, 2), 161)),
#        'ZNeu(2,3)' : ('slha', ('NMIX', (2, 3), 165)),
#        'ZNeu(2,4)' : ('slha', ('NMIX', (2, 4), 169)),
#        'ZNeu(3,1)' : ('slha', ('NMIX', (3, 1), 158)),
#        'ZNeu(3,2)' : ('slha', ('NMIX', (3, 2), 162)),
#        'ZNeu(3,3)' : ('slha', ('NMIX', (3, 3), 166)),
#        'ZNeu(3,4)' : ('slha', ('NMIX', (3, 4), 170)),
#        'ZNeu(4,1)' : ('slha', ('NMIX', (4, 1), 159)),
#        'ZNeu(4,2)' : ('slha', ('NMIX', (4, 2), 163)),
#        'ZNeu(4,3)' : ('slha', ('NMIX', (4, 3), 167)),
#        'ZNeu(4,4)' : ('slha', ('NMIX', (4, 4), 171)),
#        'g1'        : ('slha', ('GAUGE', (1,), 200)),
#        'g2'        : ('slha', ('GAUGE', (2,), 201)),
#        'g3'        : ('slha', ('GAUGE', (3,), 202)),
#        'gminus2mu' : ('slha', ('PRECOBS', (11,), 1269)),
#        'DeltaRho'  : ('slha', ('PRECOBS', (1,), 1264)),
#        'SW2effSM'  : ('slha', ('PRECOBS', (5,), 1268)),
#        'MWSM'      : ('slha', ('PRECOBS', (3,), 1266)),