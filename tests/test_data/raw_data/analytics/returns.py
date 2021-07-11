"""Sample analytics results"""

from pandas import Timestamp

periodic_return_cum_raw = {
    "AAPL": {
        Timestamp("2020-05-04 00:00:00"): 0.0,
        Timestamp("2020-05-05 00:00:00"): 0.015008913210424524,
        Timestamp("2020-05-06 00:00:00"): 0.02548093716281219,
        Timestamp("2020-05-07 00:00:00"): 0.03608946500981691,
        Timestamp("2020-05-08 00:00:00"): 0.06075022288280252,
        Timestamp("2020-05-11 00:00:00"): 0.07744142312088043,
        Timestamp("2020-05-12 00:00:00"): 0.06512822539052299,
        Timestamp("2020-05-13 00:00:00"): 0.05226764599191358,
        Timestamp("2020-05-14 00:00:00"): 0.058732193019659595,
        Timestamp("2020-05-15 00:00:00"): 0.05247287471107209,
        Timestamp("2020-05-18 00:00:00"): 0.07727045173016323,
        Timestamp("2020-05-19 00:00:00"): 0.07104539075001703,
        Timestamp("2020-05-20 00:00:00"): 0.09187531761587509,
    },
    "RY.TO": {
        Timestamp("2020-05-04 00:00:00"): 0.0,
        Timestamp("2020-05-05 00:00:00"): -0.0030538585780689464,
        Timestamp("2020-05-06 00:00:00"): -0.006107623703093701,
        Timestamp("2020-05-07 00:00:00"): -0.01127557704684834,
        Timestamp("2020-05-08 00:00:00"): 0.0023489422657372305,
        Timestamp("2020-05-11 00:00:00"): 0.017148166343801785,
        Timestamp("2020-05-12 00:00:00"): -0.0029364815545654954,
        Timestamp("2020-05-13 00:00:00"): -0.031007813515572025,
        Timestamp("2020-05-14 00:00:00"): -0.023490730999991882,
        Timestamp("2020-05-15 00:00:00"): -0.029363507203033934,
        Timestamp("2020-05-18 00:00:00"): -0.029363507203033934,
        Timestamp("2020-05-19 00:00:00"): -0.016561000867151066,
        Timestamp("2020-05-20 00:00:00"): 0.010218436210960968,
    },
}

periodic_return_raw = {
    "AAPL": {
        Timestamp("2020-05-05 00:00:00"): 0.015008913210424524,
        Timestamp("2020-05-06 00:00:00"): 0.010317174377577842,
        Timestamp("2020-05-07 00:00:00"): 0.010344929352226861,
        Timestamp("2020-05-08 00:00:00"): 0.023801764911056233,
        Timestamp("2020-05-11 00:00:00"): 0.015735278558524524,
        Timestamp("2020-05-12 00:00:00"): -0.011428182976937595,
        Timestamp("2020-05-13 00:00:00"): -0.012074207679450222,
        Timestamp("2020-05-14 00:00:00"): 0.0061434436878957666,
        Timestamp("2020-05-15 00:00:00"): -0.005912088391999304,
        Timestamp("2020-05-18 00:00:00"): 0.02356125047488633,
        Timestamp("2020-05-19 00:00:00"): -0.0057785498248359435,
        Timestamp("2020-05-20 00:00:00"): 0.019448220444953757,
    },
    "RY.TO": {
        Timestamp("2020-05-05 00:00:00"): -0.0030538585780689464,
        Timestamp("2020-05-06 00:00:00"): -0.0030631194586592247,
        Timestamp("2020-05-07 00:00:00"): -0.0051997112232711196,
        Timestamp("2020-05-08 00:00:00"): 0.013779895586974122,
        Timestamp("2020-05-11 00:00:00"): 0.014764543018933152,
        Timestamp("2020-05-12 00:00:00"): -0.01974603952791132,
        Timestamp("2020-05-13 00:00:00"): -0.028154005679371097,
        Timestamp("2020-05-14 00:00:00"): 0.007757629649061126,
        Timestamp("2020-05-15 00:00:00"): -0.006014050649059466,
        Timestamp("2020-05-18 00:00:00"): 0.0,
        Timestamp("2020-05-19 00:00:00"): 0.013189805278175148,
        Timestamp("2020-05-20 00:00:00"): 0.02723039975201802,
    },
}

weighted_return_raw = {
    Timestamp("2020-05-05 00:00:00"): 0.0025751179419302417,
    Timestamp("2020-05-06 00:00:00"): 0.0011450002718261989,
    Timestamp("2020-05-07 00:00:00"): -0.00025879111192143606,
    Timestamp("2020-05-08 00:00:00"): 0.016986796836035826,
    Timestamp("2020-05-11 00:00:00"): 0.01507537100431188,
    Timestamp("2020-05-12 00:00:00"): -0.017067353298721718,
    Timestamp("2020-05-13 00:00:00"): -0.022917881371074193,
    Timestamp("2020-05-14 00:00:00"): 0.007232564354207712,
    Timestamp("2020-05-15 00:00:00"): -0.005980881888380351,
    Timestamp("2020-05-18 00:00:00"): 0.007785490609402548,
    Timestamp("2020-05-19 00:00:00"): 0.007001031175416956,
    Timestamp("2020-05-20 00:00:00"): 0.02470431273518519,
}

weighted_cum_return_raw = {
    Timestamp("2020-05-04 00:00:00"): 0.0,
    Timestamp("2020-05-05 00:00:00"): 0.002575117941930216,
    Timestamp("2020-05-06 00:00:00"): 0.003723066724500068,
    Timestamp("2020-05-07 00:00:00"): 0.0034633121160012603,
    Timestamp("2020-05-08 00:00:00"): 0.02050893953133137,
    Timestamp("2020-05-11 00:00:00"): 0.035893490407983064,
    Timestamp("2020-05-12 00:00:00"): 0.018213530227344066,
    Timestamp("2020-05-13 00:00:00"): -0.005121766668828909,
    Timestamp("2020-05-14 00:00:00"): 0.0020737541783393265,
    Timestamp("2020-05-15 00:00:00"): -0.003919530588847198,
    Timestamp("2020-05-18 00:00:00"): 0.003835444551962608,
    Timestamp("2020-05-19 00:00:00"): 0.010863327794259359,
    Timestamp("2020-05-20 00:00:00"): 0.035836011576618754,
}
