#! /usr/bin/env python
import pprint, argparse
bpp = pprint.PrettyPrinter(indent=4, depth=3)

def parse_args():
    parser = argparse.ArgumentParser(description='Converts parameter dictionary to mc-old afterburner input')
    parser.add_argument('--input_pars', '-p', dest='input_pars', action='store', type=str , help='Define paremters')
    return parser.parse_args()

if __name__=="__main__" :
    args = parse_args()
    pars=eval(args.input_pars)
    print('\nCORDINATES\n==========\n')
    print('../bin/AfterBurner.exe 0 {m0} {m12} {A0} {tanb} {mu} {mtop} {mz} {gamma_z} {alpha_had}'.format(
        m0          = pars['SoftSUSY'][('MINPAR','M0')] ,
        m12         = pars['SoftSUSY'][('MINPAR','M12')],
        A0          = pars['SoftSUSY'][('MINPAR','A')],
        tanb        = pars['SoftSUSY'][('MINPAR','TB')],
        mu          = 1. ,
        mtop        = pars['SoftSUSY'][('SMINPUTS','Mt')],
        mz          = pars['mc_slha_update'][('SMINPUTS', 'MZ')],
        gamma_z     = 2.4952,
        alpha_had   = pars['SUSY-POPE']['non_slha_inputs']['DeltaAlfa5had'],
        ))
        
