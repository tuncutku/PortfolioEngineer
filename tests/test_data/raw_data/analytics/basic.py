"""Basic analytics raw data"""

from numpy import nan
from pandas import Timestamp

yearly_return_raw = {
    "AAPL": {
        Timestamp("2020-12-31 00:00:00", freq="A-DEC"): 0.7344120177281452,
        Timestamp("2021-12-31 00:00:00", freq="A-DEC"): 0.02912771667435976,
    },
    "TSLA": {
        Timestamp("2020-12-31 00:00:00", freq="A-DEC"): 3.523525531475361,
        Timestamp("2021-12-31 00:00:00", freq="A-DEC"): -0.039678604274095974,
    },
}

monthly_return_raw = {
    "AAPL": {
        Timestamp("2020-02-28 00:00:00", freq="BM"): -0.11226352548157748,
        Timestamp("2020-03-31 00:00:00", freq="BM"): -0.06976151880748505,
        Timestamp("2020-04-30 00:00:00", freq="BM"): 0.15537382215190387,
        Timestamp("2020-05-29 00:00:00", freq="BM"): 0.08509427558200522,
        Timestamp("2020-06-30 00:00:00", freq="BM"): 0.14738615049673665,
        Timestamp("2020-07-31 00:00:00", freq="BM"): 0.1651316011103472,
        Timestamp("2020-08-31 00:00:00", freq="BM"): 0.21656933868122263,
        Timestamp("2020-09-30 00:00:00", freq="BM"): -0.10252634781131098,
        Timestamp("2020-10-30 00:00:00", freq="BM"): -0.06001209662630502,
        Timestamp("2020-11-30 00:00:00", freq="BM"): 0.09549325202363956,
        Timestamp("2020-12-31 00:00:00", freq="BM"): 0.11457367838683052,
        Timestamp("2021-01-29 00:00:00", freq="BM"): -0.005501557230603971,
        Timestamp("2021-02-26 00:00:00", freq="BM"): -0.07971200095028386,
        Timestamp("2021-03-31 00:00:00", freq="BM"): 0.007339583685219697,
        Timestamp("2021-04-30 00:00:00", freq="BM"): 0.076217821405548,
        Timestamp("2021-05-31 00:00:00", freq="BM"): -0.050497084325397124,
        Timestamp("2021-06-30 00:00:00", freq="BM"): 0.09236814421361728,
    },
    "TSLA": {
        Timestamp("2020-02-28 00:00:00", freq="BM"): -0.14360251793494627,
        Timestamp("2020-03-31 00:00:00", freq="BM"): -0.21555713856432057,
        Timestamp("2020-04-30 00:00:00", freq="BM"): 0.49213742868736676,
        Timestamp("2020-05-29 00:00:00", freq="BM"): 0.06793876578829305,
        Timestamp("2020-06-30 00:00:00", freq="BM"): 0.2931856623666733,
        Timestamp("2020-07-31 00:00:00", freq="BM"): 0.3250108843981534,
        Timestamp("2020-08-31 00:00:00", freq="BM"): 0.7414520719546438,
        Timestamp("2020-09-30 00:00:00", freq="BM"): -0.13908732649680444,
        Timestamp("2020-10-30 00:00:00", freq="BM"): -0.09549894009019932,
        Timestamp("2020-11-30 00:00:00", freq="BM"): 0.4627357053060901,
        Timestamp("2020-12-31 00:00:00", freq="BM"): 0.24325231371211364,
        Timestamp("2021-01-29 00:00:00", freq="BM"): 0.12450585757436805,
        Timestamp("2021-02-26 00:00:00", freq="BM"): -0.1487404697229392,
        Timestamp("2021-03-31 00:00:00", freq="BM"): -0.011206524536223506,
        Timestamp("2021-04-30 00:00:00", freq="BM"): 0.06214724629947077,
        Timestamp("2021-05-31 00:00:00", freq="BM"): -0.11871339570429329,
        Timestamp("2021-06-30 00:00:00", freq="BM"): 0.08389049400972515,
    },
}

weekly_return_raw = {
    "AAPL": {
        Timestamp("2020-02-07 00:00:00", freq="W-FRI"): 0.03929736115761773,
        Timestamp("2020-02-14 00:00:00", freq="W-FRI"): 0.015373537977568352,
        Timestamp("2020-02-21 00:00:00", freq="W-FRI"): -0.03662123623288338,
        Timestamp("2020-02-28 00:00:00", freq="W-FRI"): -0.12678471334370411,
        Timestamp("2020-03-06 00:00:00", freq="W-FRI"): 0.05732379420584155,
        Timestamp("2020-03-13 00:00:00", freq="W-FRI"): -0.038266069077983134,
        Timestamp("2020-03-20 00:00:00", freq="W-FRI"): -0.17530658977392777,
        Timestamp("2020-03-27 00:00:00", freq="W-FRI"): 0.08070136773494752,
        Timestamp("2020-04-03 00:00:00", freq="W-FRI"): -0.025550924775691763,
        Timestamp("2020-04-10 00:00:00", freq="W-FRI"): 0.11010289144884844,
        Timestamp("2020-04-17 00:00:00", freq="W-FRI"): 0.05526342047266097,
        Timestamp("2020-04-24 00:00:00", freq="W-FRI"): 0.0006010946938743711,
        Timestamp("2020-05-01 00:00:00", freq="W-FRI"): 0.021557278282707815,
        Timestamp("2020-05-08 00:00:00", freq="W-FRI"): 0.0757583911843076,
        Timestamp("2020-05-15 00:00:00", freq="W-FRI"): -0.007803296189026532,
        Timestamp("2020-05-22 00:00:00", freq="W-FRI"): 0.03633308388801226,
        Timestamp("2020-05-29 00:00:00", freq="W-FRI"): -0.0029790592970668772,
        Timestamp("2020-06-05 00:00:00", freq="W-FRI"): 0.04264953573116137,
        Timestamp("2020-06-12 00:00:00", freq="W-FRI"): 0.02202089177924904,
        Timestamp("2020-06-19 00:00:00", freq="W-FRI"): 0.03223153258859468,
        Timestamp("2020-06-26 00:00:00", freq="W-FRI"): 0.011180341504460456,
        Timestamp("2020-07-03 00:00:00", freq="W-FRI"): 0.02963547694386648,
        Timestamp("2020-07-10 00:00:00", freq="W-FRI"): 0.05374760121272759,
        Timestamp("2020-07-17 00:00:00", freq="W-FRI"): 0.004248223134010631,
        Timestamp("2020-07-24 00:00:00", freq="W-FRI"): -0.03854040076920062,
        Timestamp("2020-07-31 00:00:00", freq="W-FRI"): 0.14733042046411549,
        Timestamp("2020-08-07 00:00:00", freq="W-FRI"): 0.04755172451928669,
        Timestamp("2020-08-14 00:00:00", freq="W-FRI"): 0.034154509273066846,
        Timestamp("2020-08-21 00:00:00", freq="W-FRI"): 0.08234884595157266,
        Timestamp("2020-08-28 00:00:00", freq="W-FRI"): 0.0035177355505944252,
        Timestamp("2020-09-04 00:00:00", freq="W-FRI"): -0.030827508397846315,
        Timestamp("2020-09-11 00:00:00", freq="W-FRI"): -0.07407406468379119,
        Timestamp("2020-09-18 00:00:00", freq="W-FRI"): -0.046071488274110006,
        Timestamp("2020-09-25 00:00:00", freq="W-FRI"): 0.05091723516577029,
        Timestamp("2020-10-02 00:00:00", freq="W-FRI"): 0.006590747551609599,
        Timestamp("2020-10-09 00:00:00", freq="W-FRI"): 0.0349495357889551,
        Timestamp("2020-10-16 00:00:00", freq="W-FRI"): 0.01752583320136636,
        Timestamp("2020-10-23 00:00:00", freq="W-FRI"): -0.033439673851286655,
        Timestamp("2020-10-30 00:00:00", freq="W-FRI"): -0.053720497063302286,
        Timestamp("2020-11-06 00:00:00", freq="W-FRI"): 0.09218059051510408,
        Timestamp("2020-11-13 00:00:00", freq="W-FRI"): 0.004802357380200295,
        Timestamp("2020-11-20 00:00:00", freq="W-FRI"): -0.016099301649302622,
        Timestamp("2020-11-27 00:00:00", freq="W-FRI"): -0.006391690456701404,
        Timestamp("2020-12-04 00:00:00", freq="W-FRI"): 0.048546288428391815,
        Timestamp("2020-12-11 00:00:00", freq="W-FRI"): 0.0013087482659273064,
        Timestamp("2020-12-18 00:00:00", freq="W-FRI"): 0.034719407696341076,
        Timestamp("2020-12-25 00:00:00", freq="W-FRI"): 0.04192317221292319,
        Timestamp("2021-01-01 00:00:00", freq="W-FRI"): 0.005455829598467243,
        Timestamp("2021-01-08 00:00:00", freq="W-FRI"): -0.004823336782309506,
        Timestamp("2021-01-15 00:00:00", freq="W-FRI"): -0.03718285234632068,
        Timestamp("2021-01-22 00:00:00", freq="W-FRI"): 0.09383361909068189,
        Timestamp("2021-01-29 00:00:00", freq="W-FRI"): -0.05112535843182564,
        Timestamp("2021-02-05 00:00:00", freq="W-FRI"): 0.03792330078797446,
        Timestamp("2021-02-12 00:00:00", freq="W-FRI"): -0.010163838969634575,
        Timestamp("2021-02-19 00:00:00", freq="W-FRI"): -0.04062930048267033,
        Timestamp("2021-02-26 00:00:00", freq="W-FRI"): -0.06629704987614049,
        Timestamp("2021-03-05 00:00:00", freq="W-FRI"): 0.0013194183592952768,
        Timestamp("2021-03-12 00:00:00", freq="W-FRI"): -0.0032119664333112308,
        Timestamp("2021-03-19 00:00:00", freq="W-FRI"): -0.008592927940238249,
        Timestamp("2021-03-26 00:00:00", freq="W-FRI"): 0.01016753435842821,
        Timestamp("2021-04-02 00:00:00", freq="W-FRI"): 0.014767756240630314,
        Timestamp("2021-04-09 00:00:00", freq="W-FRI"): 0.08130085038893342,
        Timestamp("2021-04-16 00:00:00", freq="W-FRI"): 0.008721821550931486,
        Timestamp("2021-04-23 00:00:00", freq="W-FRI"): 0.0011926081535982291,
        Timestamp("2021-04-30 00:00:00", freq="W-FRI"): -0.021292420267074896,
        Timestamp("2021-05-07 00:00:00", freq="W-FRI"): -0.007826174309833678,
        Timestamp("2021-05-14 00:00:00", freq="W-FRI"): -0.021196602590537017,
        Timestamp("2021-05-21 00:00:00", freq="W-FRI"): -0.01584932672761641,
        Timestamp("2021-05-28 00:00:00", freq="W-FRI"): -0.006537508513347001,
        Timestamp("2021-06-04 00:00:00", freq="W-FRI"): 0.010272038945729145,
        Timestamp("2021-06-11 00:00:00", freq="W-FRI"): 0.011597419108357876,
        Timestamp("2021-06-18 00:00:00", freq="W-FRI"): 0.02442095231259911,
        Timestamp("2021-06-25 00:00:00", freq="W-FRI"): 0.020312691707095265,
        Timestamp("2021-07-02 00:00:00", freq="W-FRI"): 0.022612835196710535,
    },
    "TSLA": {
        Timestamp("2020-02-07 00:00:00", freq="W-FRI"): -0.04093590760842358,
        Timestamp("2020-02-14 00:00:00", freq="W-FRI"): 0.06945872980630585,
        Timestamp("2020-02-21 00:00:00", freq="W-FRI"): 0.12620777133425376,
        Timestamp("2020-02-28 00:00:00", freq="W-FRI"): -0.25861260008499876,
        Timestamp("2020-03-06 00:00:00", freq="W-FRI"): 0.05312947469807172,
        Timestamp("2020-03-13 00:00:00", freq="W-FRI"): -0.2229772121345418,
        Timestamp("2020-03-20 00:00:00", freq="W-FRI"): -0.21786617155111732,
        Timestamp("2020-03-27 00:00:00", freq="W-FRI"): 0.20309692434723292,
        Timestamp("2020-04-03 00:00:00", freq="W-FRI"): -0.06678204600404969,
        Timestamp("2020-04-10 00:00:00", freq="W-FRI"): 0.19372512849301793,
        Timestamp("2020-04-17 00:00:00", freq="W-FRI"): 0.31568937072872894,
        Timestamp("2020-04-24 00:00:00", freq="W-FRI"): -0.03812227979736049,
        Timestamp("2020-05-01 00:00:00", freq="W-FRI"): -0.03286210612323226,
        Timestamp("2020-05-08 00:00:00", freq="W-FRI"): 0.16839669368263266,
        Timestamp("2020-05-15 00:00:00", freq="W-FRI"): -0.024712619812738756,
        Timestamp("2020-05-22 00:00:00", freq="W-FRI"): 0.022160538148357167,
        Timestamp("2020-05-29 00:00:00", freq="W-FRI"): 0.02218191633331812,
        Timestamp("2020-06-05 00:00:00", freq="W-FRI"): 0.060670681342393395,
        Timestamp("2020-06-12 00:00:00", freq="W-FRI"): 0.05602599055883317,
        Timestamp("2020-06-19 00:00:00", freq="W-FRI"): 0.07016076970025531,
        Timestamp("2020-06-26 00:00:00", freq="W-FRI"): -0.04112296398291437,
        Timestamp("2020-07-03 00:00:00", freq="W-FRI"): 0.25936189534976894,
        Timestamp("2020-07-10 00:00:00", freq="W-FRI"): 0.2779855357998171,
        Timestamp("2020-07-17 00:00:00", freq="W-FRI"): -0.02836239153185338,
        Timestamp("2020-07-24 00:00:00", freq="W-FRI"): -0.05586206861493692,
        Timestamp("2020-07-31 00:00:00", freq="W-FRI"): 0.009710706490563492,
        Timestamp("2020-08-07 00:00:00", freq="W-FRI"): 0.015341440937889583,
        Timestamp("2020-08-14 00:00:00", freq="W-FRI"): 0.1362970144362472,
        Timestamp("2020-08-21 00:00:00", freq="W-FRI"): 0.24187775054254002,
        Timestamp("2020-08-28 00:00:00", freq="W-FRI"): 0.07971782725527654,
        Timestamp("2020-09-04 00:00:00", freq="W-FRI"): -0.05502843081820452,
        Timestamp("2020-09-11 00:00:00", freq="W-FRI"): -0.10900747108701703,
        Timestamp("2020-09-18 00:00:00", freq="W-FRI"): 0.18627922421224952,
        Timestamp("2020-09-25 00:00:00", freq="W-FRI"): -0.07872893370828227,
        Timestamp("2020-10-02 00:00:00", freq="W-FRI"): 0.019025875361307065,
        Timestamp("2020-10-09 00:00:00", freq="W-FRI"): 0.04555639458657601,
        Timestamp("2020-10-16 00:00:00", freq="W-FRI"): 0.013064547068512233,
        Timestamp("2020-10-23 00:00:00", freq="W-FRI"): -0.043305224289651,
        Timestamp("2020-10-30 00:00:00", freq="W-FRI"): -0.07747900996023849,
        Timestamp("2020-11-06 00:00:00", freq="W-FRI"): 0.10800433650969166,
        Timestamp("2020-11-13 00:00:00", freq="W-FRI"): -0.0498895490127409,
        Timestamp("2020-11-20 00:00:00", freq="W-FRI"): 0.19855565569537914,
        Timestamp("2020-11-27 00:00:00", freq="W-FRI"): 0.1963808486157046,
        Timestamp("2020-12-04 00:00:00", freq="W-FRI"): 0.022671346695436467,
        Timestamp("2020-12-11 00:00:00", freq="W-FRI"): 0.018279267843007485,
        Timestamp("2020-12-18 00:00:00", freq="W-FRI"): 0.13936295861668424,
        Timestamp("2020-12-25 00:00:00", freq="W-FRI"): -0.047812921537769615,
        Timestamp("2021-01-01 00:00:00", freq="W-FRI"): 0.06633718978384939,
        Timestamp("2021-01-08 00:00:00", freq="W-FRI"): 0.2470702181522313,
        Timestamp("2021-01-15 00:00:00", freq="W-FRI"): -0.06120320582639438,
        Timestamp("2021-01-22 00:00:00", freq="W-FRI"): 0.0247894380866156,
        Timestamp("2021-01-29 00:00:00", freq="W-FRI"): -0.06273030382767342,
        Timestamp("2021-02-05 00:00:00", freq="W-FRI"): 0.07397319446610884,
        Timestamp("2021-02-12 00:00:00", freq="W-FRI"): -0.04237117465839535,
        Timestamp("2021-02-19 00:00:00", freq="W-FRI"): -0.04266530354916609,
        Timestamp("2021-02-26 00:00:00", freq="W-FRI"): -0.13541531991039002,
        Timestamp("2021-03-05 00:00:00", freq="W-FRI"): -0.11480383092963553,
        Timestamp("2021-03-12 00:00:00", freq="W-FRI"): 0.16018056075991205,
        Timestamp("2021-03-19 00:00:00", freq="W-FRI"): -0.056016009752533846,
        Timestamp("2021-03-26 00:00:00", freq="W-FRI"): -0.05521702538541329,
        Timestamp("2021-04-02 00:00:00", freq="W-FRI"): 0.06956405504814311,
        Timestamp("2021-04-09 00:00:00", freq="W-FRI"): 0.0230752089629771,
        Timestamp("2021-04-16 00:00:00", freq="W-FRI"): 0.09270037510719153,
        Timestamp("2021-04-23 00:00:00", freq="W-FRI"): -0.014031204509099893,
        Timestamp("2021-04-30 00:00:00", freq="W-FRI"): -0.027364986707657968,
        Timestamp("2021-05-07 00:00:00", freq="W-FRI"): -0.05225249097407714,
        Timestamp("2021-05-14 00:00:00", freq="W-FRI"): -0.1228936530227096,
        Timestamp("2021-05-21 00:00:00", freq="W-FRI"): -0.015023545118657,
        Timestamp("2021-05-28 00:00:00", freq="W-FRI"): 0.07633240161065236,
        Timestamp("2021-06-04 00:00:00", freq="W-FRI"): -0.04185724086952203,
        Timestamp("2021-06-11 00:00:00", freq="W-FRI"): 0.018095362785008673,
        Timestamp("2021-06-18 00:00:00", freq="W-FRI"): 0.022003939378958393,
        Timestamp("2021-06-25 00:00:00", freq="W-FRI"): 0.07790665599588587,
        Timestamp("2021-07-02 00:00:00", freq="W-FRI"): 0.008632604276303635,
    },
}

yearly_value_raw = {
    "AAPL": {
        Timestamp("2020-12-31 00:00:00", freq="BA-DEC"): 132.26734924316406,
        Timestamp("2021-12-31 00:00:00", freq="BA-DEC"): 136.3300018310547,
    },
    "TSLA": {
        Timestamp("2020-12-31 00:00:00", freq="BA-DEC"): 705.6699829101562,
        Timestamp("2021-12-31 00:00:00", freq="BA-DEC"): 680.760009765625,
    },
}


monthly_value_raw = {
    "AAPL": {
        Timestamp("2020-02-28 00:00:00", freq="BM"): 67.6993408203125,
        Timestamp("2020-03-31 00:00:00", freq="BM"): 62.976531982421875,
        Timestamp("2020-04-30 00:00:00", freq="BM"): 72.76143646240234,
        Timestamp("2020-05-29 00:00:00", freq="BM"): 78.95301818847656,
        Timestamp("2020-06-30 00:00:00", freq="BM"): 90.589599609375,
        Timestamp("2020-07-31 00:00:00", freq="BM"): 105.5488052368164,
        Timestamp("2020-08-31 00:00:00", freq="BM"): 128.40744018554688,
        Timestamp("2020-09-30 00:00:00", freq="BM"): 115.24229431152344,
        Timestamp("2020-10-30 00:00:00", freq="BM"): 108.32636260986328,
        Timestamp("2020-11-30 00:00:00", freq="BM"): 118.6707992553711,
        Timestamp("2020-12-31 00:00:00", freq="BM"): 132.26734924316406,
        Timestamp("2021-01-29 00:00:00", freq="BM"): 131.5396728515625,
        Timestamp("2021-02-26 00:00:00", freq="BM"): 121.05438232421875,
        Timestamp("2021-03-31 00:00:00", freq="BM"): 121.94287109375,
        Timestamp("2021-04-30 00:00:00", freq="BM"): 131.23709106445312,
        Timestamp("2021-05-31 00:00:00", freq="BM"): 124.61000061035156,
        Timestamp("2021-06-30 00:00:00", freq="BM"): 136.3300018310547,
    },
    "TSLA": {
        Timestamp("2020-02-28 00:00:00", freq="BM"): 133.59800720214844,
        Timestamp("2020-03-31 00:00:00", freq="BM"): 104.80000305175781,
        Timestamp("2020-04-30 00:00:00", freq="BM"): 156.37600708007812,
        Timestamp("2020-05-29 00:00:00", freq="BM"): 167.0,
        Timestamp("2020-06-30 00:00:00", freq="BM"): 215.96200561523438,
        Timestamp("2020-07-31 00:00:00", freq="BM"): 286.1520080566406,
        Timestamp("2020-08-31 00:00:00", freq="BM"): 498.32000732421875,
        Timestamp("2020-09-30 00:00:00", freq="BM"): 429.010009765625,
        Timestamp("2020-10-30 00:00:00", freq="BM"): 388.0400085449219,
        Timestamp("2020-11-30 00:00:00", freq="BM"): 567.5999755859375,
        Timestamp("2020-12-31 00:00:00", freq="BM"): 705.6699829101562,
        Timestamp("2021-01-29 00:00:00", freq="BM"): 793.530029296875,
        Timestamp("2021-02-26 00:00:00", freq="BM"): 675.5,
        Timestamp("2021-03-31 00:00:00", freq="BM"): 667.9299926757812,
        Timestamp("2021-04-30 00:00:00", freq="BM"): 709.4400024414062,
        Timestamp("2021-05-31 00:00:00", freq="BM"): 625.219970703125,
        Timestamp("2021-06-30 00:00:00", freq="BM"): 680.760009765625,
    },
}

weekly_value_raw = {
    "AAPL": {
        Timestamp("2020-02-07 00:00:00", freq="W-FRI"): 79.2574691772461,
        Timestamp("2020-02-14 00:00:00", freq="W-FRI"): 80.47593688964844,
        Timestamp("2020-02-21 00:00:00", freq="W-FRI"): 77.52880859375,
        Timestamp("2020-02-28 00:00:00", freq="W-FRI"): 67.6993408203125,
        Timestamp("2020-03-06 00:00:00", freq="W-FRI"): 71.58012390136719,
        Timestamp("2020-03-13 00:00:00", freq="W-FRI"): 68.84103393554688,
        Timestamp("2020-03-20 00:00:00", freq="W-FRI"): 56.77274703979492,
        Timestamp("2020-03-27 00:00:00", freq="W-FRI"): 61.35438537597656,
        Timestamp("2020-04-03 00:00:00", freq="W-FRI"): 59.78672409057617,
        Timestamp("2020-04-10 00:00:00", freq="W-FRI"): 66.36941528320312,
        Timestamp("2020-04-17 00:00:00", freq="W-FRI"): 70.03721618652344,
        Timestamp("2020-04-24 00:00:00", freq="W-FRI"): 70.07931518554688,
        Timestamp("2020-05-01 00:00:00", freq="W-FRI"): 71.59003448486328,
        Timestamp("2020-05-08 00:00:00", freq="W-FRI"): 77.01358032226562,
        Timestamp("2020-05-15 00:00:00", freq="W-FRI"): 76.4126205444336,
        Timestamp("2020-05-22 00:00:00", freq="W-FRI"): 79.18892669677734,
        Timestamp("2020-05-29 00:00:00", freq="W-FRI"): 78.95301818847656,
        Timestamp("2020-06-05 00:00:00", freq="W-FRI"): 82.32032775878906,
        Timestamp("2020-06-12 00:00:00", freq="W-FRI"): 84.13309478759766,
        Timestamp("2020-06-19 00:00:00", freq="W-FRI"): 86.84483337402344,
        Timestamp("2020-06-26 00:00:00", freq="W-FRI"): 87.81578826904297,
        Timestamp("2020-07-03 00:00:00", freq="W-FRI"): 90.41825103759766,
        Timestamp("2020-07-10 00:00:00", freq="W-FRI"): 95.27801513671875,
        Timestamp("2020-07-17 00:00:00", freq="W-FRI"): 95.68277740478516,
        Timestamp("2020-07-24 00:00:00", freq="W-FRI"): 91.99512481689453,
        Timestamp("2020-07-31 00:00:00", freq="W-FRI"): 105.5488052368164,
        Timestamp("2020-08-07 00:00:00", freq="W-FRI"): 110.56783294677734,
        Timestamp("2020-08-14 00:00:00", freq="W-FRI"): 114.34422302246094,
        Timestamp("2020-08-21 00:00:00", freq="W-FRI"): 123.76033782958984,
        Timestamp("2020-08-28 00:00:00", freq="W-FRI"): 124.19569396972656,
        Timestamp("2020-09-04 00:00:00", freq="W-FRI"): 120.36705017089844,
        Timestamp("2020-09-11 00:00:00", freq="W-FRI"): 111.45097351074219,
        Timestamp("2020-09-18 00:00:00", freq="W-FRI"): 106.3162612915039,
        Timestamp("2020-09-25 00:00:00", freq="W-FRI"): 111.7295913696289,
        Timestamp("2020-10-02 00:00:00", freq="W-FRI"): 112.46597290039062,
        Timestamp("2020-10-09 00:00:00", freq="W-FRI"): 116.3966064453125,
        Timestamp("2020-10-16 00:00:00", freq="W-FRI"): 118.43655395507812,
        Timestamp("2020-10-23 00:00:00", freq="W-FRI"): 114.47607421875,
        Timestamp("2020-10-30 00:00:00", freq="W-FRI"): 108.32636260986328,
        Timestamp("2020-11-06 00:00:00", freq="W-FRI"): 118.31195068359375,
        Timestamp("2020-11-13 00:00:00", freq="W-FRI"): 118.880126953125,
        Timestamp("2020-11-20 00:00:00", freq="W-FRI"): 116.96623992919922,
        Timestamp("2020-11-27 00:00:00", freq="W-FRI"): 116.2186279296875,
        Timestamp("2020-12-04 00:00:00", freq="W-FRI"): 121.86061096191406,
        Timestamp("2020-12-11 00:00:00", freq="W-FRI"): 122.02009582519531,
        Timestamp("2020-12-18 00:00:00", freq="W-FRI"): 126.25656127929688,
        Timestamp("2020-12-25 00:00:00", freq="W-FRI"): 131.5496368408203,
        Timestamp("2021-01-01 00:00:00", freq="W-FRI"): 132.26734924316406,
        Timestamp("2021-01-08 00:00:00", freq="W-FRI"): 131.62937927246094,
        Timestamp("2021-01-15 00:00:00", freq="W-FRI"): 126.73502349853516,
        Timestamp("2021-01-22 00:00:00", freq="W-FRI"): 138.6270294189453,
        Timestamp("2021-01-29 00:00:00", freq="W-FRI"): 131.5396728515625,
        Timestamp("2021-02-05 00:00:00", freq="W-FRI"): 136.52809143066406,
        Timestamp("2021-02-12 00:00:00", freq="W-FRI"): 135.14044189453125,
        Timestamp("2021-02-19 00:00:00", freq="W-FRI"): 129.6497802734375,
        Timestamp("2021-02-26 00:00:00", freq="W-FRI"): 121.05438232421875,
        Timestamp("2021-03-05 00:00:00", freq="W-FRI"): 121.21410369873047,
        Timestamp("2021-03-12 00:00:00", freq="W-FRI"): 120.82476806640625,
        Timestamp("2021-03-19 00:00:00", freq="W-FRI"): 119.78652954101562,
        Timestamp("2021-03-26 00:00:00", freq="W-FRI"): 121.00446319580078,
        Timestamp("2021-04-02 00:00:00", freq="W-FRI"): 122.79142761230469,
        Timestamp("2021-04-09 00:00:00", freq="W-FRI"): 132.77447509765625,
        Timestamp("2021-04-16 00:00:00", freq="W-FRI"): 133.93251037597656,
        Timestamp("2021-04-23 00:00:00", freq="W-FRI"): 134.0922393798828,
        Timestamp("2021-04-30 00:00:00", freq="W-FRI"): 131.23709106445312,
        Timestamp("2021-05-07 00:00:00", freq="W-FRI"): 130.2100067138672,
        Timestamp("2021-05-14 00:00:00", freq="W-FRI"): 127.44999694824219,
        Timestamp("2021-05-21 00:00:00", freq="W-FRI"): 125.43000030517578,
        Timestamp("2021-05-28 00:00:00", freq="W-FRI"): 124.61000061035156,
        Timestamp("2021-06-04 00:00:00", freq="W-FRI"): 125.88999938964844,
        Timestamp("2021-06-11 00:00:00", freq="W-FRI"): 127.3499984741211,
        Timestamp("2021-06-18 00:00:00", freq="W-FRI"): 130.4600067138672,
        Timestamp("2021-06-25 00:00:00", freq="W-FRI"): 133.11000061035156,
        Timestamp("2021-07-02 00:00:00", freq="W-FRI"): 136.3300018310547,
    },
    "TSLA": {
        Timestamp("2020-02-07 00:00:00", freq="W-FRI"): 149.61399841308594,
        Timestamp("2020-02-14 00:00:00", freq="W-FRI"): 160.00599670410156,
        Timestamp("2020-02-21 00:00:00", freq="W-FRI"): 180.1999969482422,
        Timestamp("2020-02-28 00:00:00", freq="W-FRI"): 133.59800720214844,
        Timestamp("2020-03-06 00:00:00", freq="W-FRI"): 140.6959991455078,
        Timestamp("2020-03-13 00:00:00", freq="W-FRI"): 109.3239974975586,
        Timestamp("2020-03-20 00:00:00", freq="W-FRI"): 85.50599670410156,
        Timestamp("2020-03-27 00:00:00", freq="W-FRI"): 102.87200164794922,
        Timestamp("2020-04-03 00:00:00", freq="W-FRI"): 96.00199890136719,
        Timestamp("2020-04-10 00:00:00", freq="W-FRI"): 114.5999984741211,
        Timestamp("2020-04-17 00:00:00", freq="W-FRI"): 150.7779998779297,
        Timestamp("2020-04-24 00:00:00", freq="W-FRI"): 145.02999877929688,
        Timestamp("2020-05-01 00:00:00", freq="W-FRI"): 140.26400756835938,
        Timestamp("2020-05-08 00:00:00", freq="W-FRI"): 163.88400268554688,
        Timestamp("2020-05-15 00:00:00", freq="W-FRI"): 159.83399963378906,
        Timestamp("2020-05-22 00:00:00", freq="W-FRI"): 163.37600708007812,
        Timestamp("2020-05-29 00:00:00", freq="W-FRI"): 167.0,
        Timestamp("2020-06-05 00:00:00", freq="W-FRI"): 177.1320037841797,
        Timestamp("2020-06-12 00:00:00", freq="W-FRI"): 187.05599975585938,
        Timestamp("2020-06-19 00:00:00", freq="W-FRI"): 200.17999267578125,
        Timestamp("2020-06-26 00:00:00", freq="W-FRI"): 191.947998046875,
        Timestamp("2020-07-03 00:00:00", freq="W-FRI"): 241.73199462890625,
        Timestamp("2020-07-10 00:00:00", freq="W-FRI"): 308.92999267578125,
        Timestamp("2020-07-17 00:00:00", freq="W-FRI"): 300.1679992675781,
        Timestamp("2020-07-24 00:00:00", freq="W-FRI"): 283.3999938964844,
        Timestamp("2020-07-31 00:00:00", freq="W-FRI"): 286.1520080566406,
        Timestamp("2020-08-07 00:00:00", freq="W-FRI"): 290.5419921875,
        Timestamp("2020-08-14 00:00:00", freq="W-FRI"): 330.1419982910156,
        Timestamp("2020-08-21 00:00:00", freq="W-FRI"): 409.9960021972656,
        Timestamp("2020-08-28 00:00:00", freq="W-FRI"): 442.67999267578125,
        Timestamp("2020-09-04 00:00:00", freq="W-FRI"): 418.32000732421875,
        Timestamp("2020-09-11 00:00:00", freq="W-FRI"): 372.7200012207031,
        Timestamp("2020-09-18 00:00:00", freq="W-FRI"): 442.1499938964844,
        Timestamp("2020-09-25 00:00:00", freq="W-FRI"): 407.3399963378906,
        Timestamp("2020-10-02 00:00:00", freq="W-FRI"): 415.0899963378906,
        Timestamp("2020-10-09 00:00:00", freq="W-FRI"): 434.0,
        Timestamp("2020-10-16 00:00:00", freq="W-FRI"): 439.6700134277344,
        Timestamp("2020-10-23 00:00:00", freq="W-FRI"): 420.6300048828125,
        Timestamp("2020-10-30 00:00:00", freq="W-FRI"): 388.0400085449219,
        Timestamp("2020-11-06 00:00:00", freq="W-FRI"): 429.95001220703125,
        Timestamp("2020-11-13 00:00:00", freq="W-FRI"): 408.5,
        Timestamp("2020-11-20 00:00:00", freq="W-FRI"): 489.6099853515625,
        Timestamp("2020-11-27 00:00:00", freq="W-FRI"): 585.760009765625,
        Timestamp("2020-12-04 00:00:00", freq="W-FRI"): 599.0399780273438,
        Timestamp("2020-12-11 00:00:00", freq="W-FRI"): 609.989990234375,
        Timestamp("2020-12-18 00:00:00", freq="W-FRI"): 695.0,
        Timestamp("2020-12-25 00:00:00", freq="W-FRI"): 661.77001953125,
        Timestamp("2021-01-01 00:00:00", freq="W-FRI"): 705.6699829101562,
        Timestamp("2021-01-08 00:00:00", freq="W-FRI"): 880.02001953125,
        Timestamp("2021-01-15 00:00:00", freq="W-FRI"): 826.1599731445312,
        Timestamp("2021-01-22 00:00:00", freq="W-FRI"): 846.6400146484375,
        Timestamp("2021-01-29 00:00:00", freq="W-FRI"): 793.530029296875,
        Timestamp("2021-02-05 00:00:00", freq="W-FRI"): 852.22998046875,
        Timestamp("2021-02-12 00:00:00", freq="W-FRI"): 816.1199951171875,
        Timestamp("2021-02-19 00:00:00", freq="W-FRI"): 781.2999877929688,
        Timestamp("2021-02-26 00:00:00", freq="W-FRI"): 675.5,
        Timestamp("2021-03-05 00:00:00", freq="W-FRI"): 597.9500122070312,
        Timestamp("2021-03-12 00:00:00", freq="W-FRI"): 693.72998046875,
        Timestamp("2021-03-19 00:00:00", freq="W-FRI"): 654.8699951171875,
        Timestamp("2021-03-26 00:00:00", freq="W-FRI"): 618.7100219726562,
        Timestamp("2021-04-02 00:00:00", freq="W-FRI"): 661.75,
        Timestamp("2021-04-09 00:00:00", freq="W-FRI"): 677.02001953125,
        Timestamp("2021-04-16 00:00:00", freq="W-FRI"): 739.780029296875,
        Timestamp("2021-04-23 00:00:00", freq="W-FRI"): 729.4000244140625,
        Timestamp("2021-04-30 00:00:00", freq="W-FRI"): 709.4400024414062,
        Timestamp("2021-05-07 00:00:00", freq="W-FRI"): 672.3699951171875,
        Timestamp("2021-05-14 00:00:00", freq="W-FRI"): 589.739990234375,
        Timestamp("2021-05-21 00:00:00", freq="W-FRI"): 580.8800048828125,
        Timestamp("2021-05-28 00:00:00", freq="W-FRI"): 625.219970703125,
        Timestamp("2021-06-04 00:00:00", freq="W-FRI"): 599.0499877929688,
        Timestamp("2021-06-11 00:00:00", freq="W-FRI"): 609.8900146484375,
        Timestamp("2021-06-18 00:00:00", freq="W-FRI"): 623.3099975585938,
        Timestamp("2021-06-25 00:00:00", freq="W-FRI"): 671.8699951171875,
        Timestamp("2021-07-02 00:00:00", freq="W-FRI"): 680.760009765625,
    },
}

outliers = {
    "AAPL": {
        Timestamp("2020-05-11 00:00:00"): nan,
        Timestamp("2020-05-20 00:00:00"): 79.27335357666016,
    },
    "RY.TO": {
        Timestamp("2020-05-11 00:00:00"): 83.03875732421875,
        Timestamp("2020-05-20 00:00:00"): nan,
    },
}

non_outliers = {
    "AAPL": {
        Timestamp("2020-05-04 00:00:00"): 72.60293579101562,
        Timestamp("2020-05-05 00:00:00"): 73.692626953125,
        Timestamp("2020-05-06 00:00:00"): 74.45292663574219,
        Timestamp("2020-05-07 00:00:00"): 75.22313690185547,
        Timestamp("2020-05-08 00:00:00"): 77.01358032226562,
        Timestamp("2020-05-11 00:00:00"): 78.22541046142578,
        Timestamp("2020-05-12 00:00:00"): 77.33143615722656,
        Timestamp("2020-05-13 00:00:00"): 76.39772033691406,
        Timestamp("2020-05-14 00:00:00"): 76.8670654296875,
        Timestamp("2020-05-15 00:00:00"): 76.4126205444336,
        Timestamp("2020-05-18 00:00:00"): 78.21299743652344,
        Timestamp("2020-05-19 00:00:00"): 77.76103973388672,
        Timestamp("2020-05-20 00:00:00"): nan,
    },
    "RY.TO": {
        Timestamp("2020-05-04 00:00:00"): 81.63880157470703,
        Timestamp("2020-05-05 00:00:00"): 81.38948822021484,
        Timestamp("2020-05-06 00:00:00"): 81.14018249511719,
        Timestamp("2020-05-07 00:00:00"): 80.71827697753906,
        Timestamp("2020-05-08 00:00:00"): 81.83056640625,
        Timestamp("2020-05-11 00:00:00"): nan,
        Timestamp("2020-05-12 00:00:00"): 81.3990707397461,
        Timestamp("2020-05-13 00:00:00"): 79.10736083984375,
        Timestamp("2020-05-14 00:00:00"): 79.7210464477539,
        Timestamp("2020-05-15 00:00:00"): 79.2416000366211,
        Timestamp("2020-05-18 00:00:00"): 79.2416000366211,
        Timestamp("2020-05-19 00:00:00"): 80.28678131103516,
        Timestamp("2020-05-20 00:00:00"): 82.4730224609375,
    },
}


compsum_raw = {
    "AAPL": {
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

comp_raw = {"AAPL": 0.09187531761587509, "RY.TO": 0.010218436210960968}