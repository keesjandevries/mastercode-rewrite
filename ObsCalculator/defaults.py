predictor_defaults={
    'SoftSUSY':
        {   'SMinputs':
                {   'alpha_em_inv'  : 1.27908953e2, #MC-old
                    'G_Fermi'       : 1.16639e-5,   #MC-old
                    'alpha_s'       : 1.187e-01,    #MC-old
                    'MZ'            : 9.11876e1,    #MC-old
                    'mt'            : 174.3,        #arbitrary, from web
                    'mb'            : 4.2,          #MC-old
                    'mtau'          : 1.77703,      #MC-old
                },
        },

    'FeynHiggs':
        {   'mssmpart'      :4, 
            'fieldren'      :0, 
            'tanbren'       :0, 
            'higgsmix'      :2,
            'p2approx'      :0, 
            'looplevel'     :2, 
            'tl_running_mt' :1, 
            'tl_bot_resum'  :1,
        },

    'LSP scattering':
        {   'SigmaPiN'      : 50. , 
            'SigmaPiNerr'   : 14. ,
        },

    'SUSY-POPE' :
        {   'flags': 
                {   'LoopOption'    : 5,
                    'IterOpt'       : 1,
                    'Observables'   : 1,
                    'HiggsOpt'      : 1,
                    'Verbose'       : 1,
                    'SMObsOpt'      : 1
                },
            'non_slha_inputs' : 
                {   'DeltaAlfa5had' : 0.02749,
                    'DeltaAlfaQED'  : 0.031497637,
                    'ZWidthexp'     : 2.4952,
                    'MB'            : 4.8,
                    'M2phase'       : 0.,
                    'M1phase'       : 0., 
                    'MUEPhase'      : 0.,
                    'Atphase'       : 0., 
                    'Abphase'       : 0.,
                    'Atauphase'     : 0., 
                },
         },

}
