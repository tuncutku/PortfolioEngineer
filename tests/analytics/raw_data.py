"""Raw data for portfolio"""

from pandas import Timestamp

raw_portfolio = {
    "AAPL": {
        Timestamp("2021-01-05 00:00:00", freq="B"): 0.01236365781646609,
        Timestamp("2021-01-06 00:00:00", freq="B"): -0.0336614742422493,
        Timestamp("2021-01-07 00:00:00", freq="B"): 0.034123218444531256,
        Timestamp("2021-01-08 00:00:00", freq="B"): 0.008631183057217884,
        Timestamp("2021-01-11 00:00:00", freq="B"): -0.023248696996061358,
        Timestamp("2021-01-12 00:00:00", freq="B"): -0.0013956467043150234,
        Timestamp("2021-01-13 00:00:00", freq="B"): 0.016226744502986445,
        Timestamp("2021-01-14 00:00:00", freq="B"): -0.015127036041214903,
        Timestamp("2021-01-15 00:00:00", freq="B"): -0.013730715152414641,
        Timestamp("2021-01-18 00:00:00", freq="B"): 0.0,
        Timestamp("2021-01-19 00:00:00", freq="B"): 0.005427104182289311,
        Timestamp("2021-01-20 00:00:00", freq="B"): 0.03285619910414472,
        Timestamp("2021-01-21 00:00:00", freq="B"): 0.03665823139912039,
        Timestamp("2021-01-22 00:00:00", freq="B"): 0.016073765530416617,
        Timestamp("2021-01-25 00:00:00", freq="B"): 0.02768382632583255,
        Timestamp("2021-01-26 00:00:00", freq="B"): 0.0016793592948236569,
        Timestamp("2021-01-27 00:00:00", freq="B"): -0.007683766320895624,
        Timestamp("2021-01-28 00:00:00", freq="B"): -0.03498524686651039,
        Timestamp("2021-01-29 00:00:00", freq="B"): -0.037420735011012285,
        Timestamp("2021-02-01 00:00:00", freq="B"): 0.016520117425273373,
        Timestamp("2021-02-02 00:00:00", freq="B"): 0.006336767549112388,
        Timestamp("2021-02-03 00:00:00", freq="B"): -0.007778240754778953,
        Timestamp("2021-02-04 00:00:00", freq="B"): 0.025757702181440134,
        Timestamp("2021-02-05 00:00:00", freq="B"): -0.00309812088618866,
        Timestamp("2021-02-08 00:00:00", freq="B"): 0.001096918453850959,
        Timestamp("2021-02-09 00:00:00", freq="B"): -0.006573740213881685,
        Timestamp("2021-02-10 00:00:00", freq="B"): -0.004558518260409206,
        Timestamp("2021-02-11 00:00:00", freq="B"): -0.0019202631746458865,
        Timestamp("2021-02-12 00:00:00", freq="B"): 0.0017758999378882923,
        Timestamp("2021-02-15 00:00:00", freq="B"): 0.0,
        Timestamp("2021-02-16 00:00:00", freq="B"): -0.016103804523960097,
        Timestamp("2021-02-17 00:00:00", freq="B"): -0.017644030740257666,
        Timestamp("2021-02-18 00:00:00", freq="B"): -0.008636560613165423,
        Timestamp("2021-02-19 00:00:00", freq="B"): 0.0012336013512141975,
        Timestamp("2021-02-22 00:00:00", freq="B"): -0.02979903269877937,
        Timestamp("2021-02-23 00:00:00", freq="B"): -0.0011111379061732318,
        Timestamp("2021-02-24 00:00:00", freq="B"): -0.004052149733117183,
        Timestamp("2021-02-25 00:00:00", freq="B"): -0.03478258586472138,
        Timestamp("2021-02-26 00:00:00", freq="B"): 0.0022316161627791153,
        Timestamp("2021-03-01 00:00:00", freq="B"): 0.05385125628483256,
        Timestamp("2021-03-02 00:00:00", freq="B"): -0.020893703589195955,
        Timestamp("2021-03-03 00:00:00", freq="B"): -0.024456570443776915,
        Timestamp("2021-03-04 00:00:00", freq="B"): -0.015811884214734118,
        Timestamp("2021-03-05 00:00:00", freq="B"): 0.010738389813667704,
        Timestamp("2021-03-08 00:00:00", freq="B"): -0.04167351918087281,
        Timestamp("2021-03-09 00:00:00", freq="B"): 0.04064968402734803,
        Timestamp("2021-03-10 00:00:00", freq="B"): -0.009166613941022694,
        Timestamp("2021-03-11 00:00:00", freq="B"): 0.016502627892926114,
        Timestamp("2021-03-12 00:00:00", freq="B"): -0.007625438041590105,
        Timestamp("2021-03-15 00:00:00", freq="B"): 0.024456758885001983,
        Timestamp("2021-03-16 00:00:00", freq="B"): 0.01274294453729885,
        Timestamp("2021-03-17 00:00:00", freq="B"): -0.006450540925908577,
        Timestamp("2021-03-18 00:00:00", freq="B"): -0.033905135532936836,
        Timestamp("2021-03-19 00:00:00", freq="B"): -0.004480202695944957,
        Timestamp("2021-03-22 00:00:00", freq="B"): 0.02833572279490193,
        Timestamp("2021-03-23 00:00:00", freq="B"): -0.006888733457077745,
        Timestamp("2021-03-24 00:00:00", freq="B"): -0.019993516689839175,
        Timestamp("2021-03-25 00:00:00", freq="B"): 0.004163544502227667,
        Timestamp("2021-03-26 00:00:00", freq="B"): 0.005141421785979761,
        Timestamp("2021-03-29 00:00:00", freq="B"): 0.001484980649218759,
        Timestamp("2021-03-30 00:00:00", freq="B"): -0.01227445978070607,
        Timestamp("2021-03-31 00:00:00", freq="B"): 0.018765671865784928,
        Timestamp("2021-04-01 00:00:00", freq="B"): 0.006958601474931436,
        Timestamp("2021-04-02 00:00:00", freq="B"): 0.0,
        Timestamp("2021-04-05 00:00:00", freq="B"): 0.023577325823064044,
        Timestamp("2021-04-06 00:00:00", freq="B"): 0.002462226747362184,
        Timestamp("2021-04-07 00:00:00", freq="B"): 0.013390366431693668,
        Timestamp("2021-04-08 00:00:00", freq="B"): 0.019233787804121327,
        Timestamp("2021-04-09 00:00:00", freq="B"): 0.02025157975661651,
        Timestamp("2021-04-12 00:00:00", freq="B"): -0.013233024380530978,
        Timestamp("2021-04-13 00:00:00", freq="B"): 0.024306483396833167,
        Timestamp("2021-04-14 00:00:00", freq="B"): -0.017853069953940537,
        Timestamp("2021-04-15 00:00:00", freq="B"): 0.018707907122020195,
        Timestamp("2021-04-16 00:00:00", freq="B"): -0.0025278606987256813,
        Timestamp("2021-04-19 00:00:00", freq="B"): 0.005068419845577488,
        Timestamp("2021-04-20 00:00:00", freq="B"): -0.012829829085842626,
        Timestamp("2021-04-21 00:00:00", freq="B"): 0.002929731635616273,
        Timestamp("2021-04-22 00:00:00", freq="B"): -0.01168526684487703,
        Timestamp("2021-04-23 00:00:00", freq="B"): 0.018038472979764908,
        Timestamp("2021-04-26 00:00:00", freq="B"): 0.0029779860832057636,
        Timestamp("2021-04-27 00:00:00", freq="B"): -0.0024496489147131095,
        Timestamp("2021-04-28 00:00:00", freq="B"): -0.0060271361227907105,
        Timestamp("2021-04-29 00:00:00", freq="B"): -0.0007486494972714919,
        Timestamp("2021-04-30 00:00:00", freq="B"): -0.015133293049751861,
        Timestamp("2021-05-03 00:00:00", freq="B"): 0.008215292073591618,
        Timestamp("2021-05-04 00:00:00", freq="B"): -0.035385477682524535,
        Timestamp("2021-05-05 00:00:00", freq="B"): 0.0019555065243814784,
        Timestamp("2021-05-06 00:00:00", freq="B"): 0.012802405146462803,
        Timestamp("2021-05-07 00:00:00", freq="B"): 0.0053274582196922715,
        Timestamp("2021-05-10 00:00:00", freq="B"): -0.025804581020968165,
        Timestamp("2021-05-11 00:00:00", freq="B"): -0.007410245597279208,
        Timestamp("2021-05-12 00:00:00", freq="B"): -0.024938485320373682,
        Timestamp("2021-05-13 00:00:00", freq="B"): 0.01791968650522091,
        Timestamp("2021-05-14 00:00:00", freq="B"): 0.019844746402187363,
        Timestamp("2021-05-17 00:00:00", freq="B"): -0.009258558159151553,
        Timestamp("2021-05-18 00:00:00", freq="B"): -0.01124569541709608,
        Timestamp("2021-05-19 00:00:00", freq="B"): -0.0012815288847675133,
        Timestamp("2021-05-20 00:00:00", freq="B"): 0.0210120548433419,
        Timestamp("2021-05-21 00:00:00", freq="B"): -0.014767061349629906,
        Timestamp("2021-05-24 00:00:00", freq="B"): 0.01331415177336237,
        Timestamp("2021-05-25 00:00:00", freq="B"): -0.0015734930800931357,
        Timestamp("2021-05-26 00:00:00", freq="B"): -0.0003940835327033154,
        Timestamp("2021-05-27 00:00:00", freq="B"): -0.01237681239210009,
        Timestamp("2021-05-28 00:00:00", freq="B"): -0.005347968002701098,
        Timestamp("2021-05-31 00:00:00", freq="B"): 0.0,
        Timestamp("2021-06-01 00:00:00", freq="B"): -0.0026483206740457454,
        Timestamp("2021-06-02 00:00:00", freq="B"): 0.006276137765536927,
        Timestamp("2021-06-03 00:00:00", freq="B"): -0.01215408171675536,
        Timestamp("2021-06-04 00:00:00", freq="B"): 0.019022153754008286,
        Timestamp("2021-06-07 00:00:00", freq="B"): 7.944904484835646e-05,
        Timestamp("2021-06-08 00:00:00", freq="B"): 0.006671915106366555,
        Timestamp("2021-06-09 00:00:00", freq="B"): 0.0030771896399954812,
        Timestamp("2021-06-10 00:00:00", freq="B"): -0.008023257246628335,
        Timestamp("2021-06-11 00:00:00", freq="B"): 0.009832616792656568,
        Timestamp("2021-06-14 00:00:00", freq="B"): 0.024577899132341763,
        Timestamp("2021-06-15 00:00:00", freq="B"): -0.006437665195967779,
        Timestamp("2021-06-16 00:00:00", freq="B"): 0.003933928670150966,
        Timestamp("2021-06-17 00:00:00", freq="B"): 0.01260081603898211,
        Timestamp("2021-06-18 00:00:00", freq="B"): -0.010091757161469483,
        Timestamp("2021-06-21 00:00:00", freq="B"): 0.014103958329331201,
        Timestamp("2021-06-22 00:00:00", freq="B"): 0.012698323592580829,
        Timestamp("2021-06-23 00:00:00", freq="B"): -0.002089792648359956,
        Timestamp("2021-06-24 00:00:00", freq="B"): -0.0021690342556995867,
        Timestamp("2021-06-25 00:00:00", freq="B"): -0.002248662612178265,
        Timestamp("2021-06-28 00:00:00", freq="B"): 0.012545969225230325,
        Timestamp("2021-06-29 00:00:00", freq="B"): 0.011500241277281997,
        Timestamp("2021-06-30 00:00:00", freq="B"): 0.004621149476463637,
        Timestamp("2021-07-01 00:00:00", freq="B"): 0.002263460510446791,
        Timestamp("2021-07-02 00:00:00", freq="B"): 0.019596402806337343,
        Timestamp("2021-07-05 00:00:00", freq="B"): 0.0,
        Timestamp("2021-07-06 00:00:00", freq="B"): 0.014718469232031683,
        Timestamp("2021-07-07 00:00:00", freq="B"): 0.017955239463629313,
        Timestamp("2021-07-08 00:00:00", freq="B"): -0.00919974977712279,
        Timestamp("2021-07-09 00:00:00", freq="B"): 0.013055014689011823,
        Timestamp("2021-07-12 00:00:00", freq="B"): -0.004203691312132607,
        Timestamp("2021-07-13 00:00:00", freq="B"): 0.007889244520682404,
        Timestamp("2021-07-14 00:00:00", freq="B"): 0.02410049794425917,
        Timestamp("2021-07-15 00:00:00", freq="B"): -0.0044920779777114506,
        Timestamp("2021-07-16 00:00:00", freq="B"): -0.014076038561466442,
        Timestamp("2021-07-19 00:00:00", freq="B"): -0.026914350722410108,
        Timestamp("2021-07-20 00:00:00", freq="B"): 0.025973978604830972,
        Timestamp("2021-07-21 00:00:00", freq="B"): -0.00513166530684539,
        Timestamp("2021-07-22 00:00:00", freq="B"): 0.009628595983111943,
        Timestamp("2021-07-23 00:00:00", freq="B"): 0.011989121296750005,
        Timestamp("2021-07-26 00:00:00", freq="B"): 0.0028945231803072513,
        Timestamp("2021-07-27 00:00:00", freq="B"): -0.01490040311389118,
        Timestamp("2021-07-28 00:00:00", freq="B"): -0.012195958718198896,
        Timestamp("2021-07-29 00:00:00", freq="B"): 0.004552346610352087,
        Timestamp("2021-07-30 00:00:00", freq="B"): 0.0015105372459283117,
        Timestamp("2021-08-02 00:00:00", freq="B"): -0.002330907574611518,
        Timestamp("2021-08-03 00:00:00", freq="B"): 0.012644221095817754,
        Timestamp("2021-08-04 00:00:00", freq="B"): -0.0027822436255675598,
        Timestamp("2021-08-05 00:00:00", freq="B"): 0.0007485356861631765,
        Timestamp("2021-08-06 00:00:00", freq="B"): -0.004767072771041492,
        Timestamp("2021-08-09 00:00:00", freq="B"): -0.0003421585600564825,
        Timestamp("2021-08-10 00:00:00", freq="B"): -0.00335403002709167,
    },
    "FB": {
        Timestamp("2021-01-05 00:00:00", freq="B"): 0.007548147396700955,
        Timestamp("2021-01-06 00:00:00", freq="B"): -0.028268825433079403,
        Timestamp("2021-01-07 00:00:00", freq="B"): 0.02062205281276075,
        Timestamp("2021-01-08 00:00:00", freq="B"): -0.004353586934106368,
        Timestamp("2021-01-11 00:00:00", freq="B"): -0.040101695603447784,
        Timestamp("2021-01-12 00:00:00", freq="B"): -0.022387478905098068,
        Timestamp("2021-01-13 00:00:00", freq="B"): 0.0021904618255585984,
        Timestamp("2021-01-14 00:00:00", freq="B"): -0.023843586133178274,
        Timestamp("2021-01-15 00:00:00", freq="B"): 0.023286114781451817,
        Timestamp("2021-01-18 00:00:00", freq="B"): 0.0,
        Timestamp("2021-01-19 00:00:00", freq="B"): 0.03874922608813414,
        Timestamp("2021-01-20 00:00:00", freq="B"): 0.024435100473659377,
        Timestamp("2021-01-21 00:00:00", freq="B"): 0.020150979174047068,
        Timestamp("2021-01-22 00:00:00", freq="B"): 0.005973558514971389,
        Timestamp("2021-01-25 00:00:00", freq="B"): 0.0127869208219491,
        Timestamp("2021-01-26 00:00:00", freq="B"): 0.014531771826308049,
        Timestamp("2021-01-27 00:00:00", freq="B"): -0.035135520558169264,
        Timestamp("2021-01-28 00:00:00", freq="B"): -0.026236548335831,
        Timestamp("2021-01-29 00:00:00", freq="B"): -0.025169861991450437,
        Timestamp("2021-02-01 00:00:00", freq="B"): 0.014245435623595037,
        Timestamp("2021-02-02 00:00:00", freq="B"): 0.019350317230917513,
        Timestamp("2021-02-03 00:00:00", freq="B"): -0.0016099771506649097,
        Timestamp("2021-02-04 00:00:00", freq="B"): -0.0006000512498472999,
        Timestamp("2021-02-05 00:00:00", freq="B"): 0.0060415622655267676,
        Timestamp("2021-02-08 00:00:00", freq="B"): -0.005669599017700588,
        Timestamp("2021-02-09 00:00:00", freq="B"): 0.010766095653574448,
        Timestamp("2021-02-10 00:00:00", freq="B"): 0.008981194286593164,
        Timestamp("2021-02-11 00:00:00", freq="B"): -0.005443706533749926,
        Timestamp("2021-02-12 00:00:00", freq="B"): 0.00040676558158225795,
        Timestamp("2021-02-15 00:00:00", freq="B"): 0.0,
        Timestamp("2021-02-16 00:00:00", freq="B"): 0.012828100631065098,
        Timestamp("2021-02-17 00:00:00", freq="B"): -0.0014599915855829648,
        Timestamp("2021-02-18 00:00:00", freq="B"): -0.015279425974600302,
        Timestamp("2021-02-19 00:00:00", freq="B"): -0.029065728735573892,
        Timestamp("2021-02-22 00:00:00", freq="B"): -0.004702595954308997,
        Timestamp("2021-02-23 00:00:00", freq="B"): 0.021242265833873786,
        Timestamp("2021-02-24 00:00:00", freq="B"): -0.005830090567856994,
        Timestamp("2021-02-25 00:00:00", freq="B"): -0.03639663730485598,
        Timestamp("2021-02-26 00:00:00", freq="B"): 0.011504152686383273,
        Timestamp("2021-03-01 00:00:00", freq="B"): 0.028297526135755646,
        Timestamp("2021-03-02 00:00:00", freq="B"): -0.02230947710697828,
        Timestamp("2021-03-03 00:00:00", freq="B"): -0.013860989721585448,
        Timestamp("2021-03-04 00:00:00", freq="B"): 0.008731102753822828,
        Timestamp("2021-03-05 00:00:00", freq="B"): 0.025772332531186715,
        Timestamp("2021-03-08 00:00:00", freq="B"): -0.03394127918168366,
        Timestamp("2021-03-09 00:00:00", freq="B"): 0.0408522689104156,
        Timestamp("2021-03-10 00:00:00", freq="B"): -0.0031609707562259004,
        Timestamp("2021-03-11 00:00:00", freq="B"): 0.033899627003529664,
        Timestamp("2021-03-12 00:00:00", freq="B"): -0.020008802718814445,
        Timestamp("2021-03-15 00:00:00", freq="B"): 0.019932959110196435,
        Timestamp("2021-03-16 00:00:00", freq="B"): 0.02020090878281966,
        Timestamp("2021-03-17 00:00:00", freq="B"): 0.016936447318112613,
        Timestamp("2021-03-18 00:00:00", freq="B"): -0.01897825591740776,
        Timestamp("2021-03-19 00:00:00", freq="B"): 0.04123892913551419,
        Timestamp("2021-03-22 00:00:00", freq="B"): 0.011823182125919596,
        Timestamp("2021-03-23 00:00:00", freq="B"): -0.009913482242281946,
        Timestamp("2021-03-24 00:00:00", freq="B"): -0.02921236655450743,
        Timestamp("2021-03-25 00:00:00", freq="B"): -0.012050840850416522,
        Timestamp("2021-03-26 00:00:00", freq="B"): 0.015354807093514333,
        Timestamp("2021-03-29 00:00:00", freq="B"): 0.02755995552727586,
        Timestamp("2021-03-30 00:00:00", freq="B"): -0.00969674456088876,
        Timestamp("2021-03-31 00:00:00", freq="B"): 0.022673606872558594,
        Timestamp("2021-04-01 00:00:00", freq="B"): 0.0140223573148055,
        Timestamp("2021-04-02 00:00:00", freq="B"): 0.0,
        Timestamp("2021-04-05 00:00:00", freq="B"): 0.03431996207833832,
        Timestamp("2021-04-06 00:00:00", freq="B"): -0.008578530526913486,
        Timestamp("2021-04-07 00:00:00", freq="B"): 0.02230126805485466,
        Timestamp("2021-04-08 00:00:00", freq="B"): -0.00022360128090193054,
        Timestamp("2021-04-09 00:00:00", freq="B"): -0.0017890153288877553,
        Timestamp("2021-04-12 00:00:00", freq="B"): -0.0029443222662588475,
        Timestamp("2021-04-13 00:00:00", freq="B"): -0.005713547956843645,
        Timestamp("2021-04-14 00:00:00", freq="B"): -0.02240444932403407,
        Timestamp("2021-04-15 00:00:00", freq="B"): 0.016511458553155167,
        Timestamp("2021-04-16 00:00:00", freq="B"): -0.00532783642848178,
        Timestamp("2021-04-19 00:00:00", freq="B"): -0.0128682557177352,
        Timestamp("2021-04-20 00:00:00", freq="B"): 0.001356550011106794,
        Timestamp("2021-04-21 00:00:00", freq="B"): -0.0038988689891890083,
        Timestamp("2021-04-22 00:00:00", freq="B"): -0.01641958465846627,
        Timestamp("2021-04-23 00:00:00", freq="B"): 0.015547066099911522,
        Timestamp("2021-04-26 00:00:00", freq="B"): 0.006342787603821343,
        Timestamp("2021-04-27 00:00:00", freq="B"): 0.0017489399562840013,
        Timestamp("2021-04-28 00:00:00", freq="B"): 0.011628285713768616,
        Timestamp("2021-04-29 00:00:00", freq="B"): 0.07297298344746861,
        Timestamp("2021-04-30 00:00:00", freq="B"): -0.013444275020690233,
        Timestamp("2021-05-03 00:00:00", freq="B"): -0.007690414984818705,
        Timestamp("2021-05-04 00:00:00", freq="B"): -0.013082030492792995,
        Timestamp("2021-05-05 00:00:00", freq="B"): -0.010491256726885112,
        Timestamp("2021-05-06 00:00:00", freq="B"): 0.015872008680004823,
        Timestamp("2021-05-07 00:00:00", freq="B"): -0.00293732414748038,
        Timestamp("2021-05-10 00:00:00", freq="B"): -0.041086830585638556,
        Timestamp("2021-05-11 00:00:00", freq="B"): 0.00183023680870531,
        Timestamp("2021-05-12 00:00:00", freq="B"): -0.012984083131105773,
        Timestamp("2021-05-13 00:00:00", freq="B"): 0.008957270143771012,
        Timestamp("2021-05-14 00:00:00", freq="B"): 0.03498654371393495,
        Timestamp("2021-05-17 00:00:00", freq="B"): -0.001519310573586341,
        Timestamp("2021-05-18 00:00:00", freq="B"): -0.017434857506433477,
        Timestamp("2021-05-19 00:00:00", freq="B"): 0.01171120461634989,
        Timestamp("2021-05-20 00:00:00", freq="B"): 0.016008128678514533,
        Timestamp("2021-05-21 00:00:00", freq="B"): -0.007469867470124125,
        Timestamp("2021-05-24 00:00:00", freq="B"): 0.026562924468441773,
        Timestamp("2021-05-25 00:00:00", freq="B"): 0.009734170023039335,
        Timestamp("2021-05-26 00:00:00", freq="B"): -0.0003966102670108773,
        Timestamp("2021-05-27 00:00:00", freq="B"): 0.0155343840597022,
        Timestamp("2021-05-28 00:00:00", freq="B"): -0.012081108981733646,
        Timestamp("2021-05-31 00:00:00", freq="B"): 0.0,
        Timestamp("2021-06-01 00:00:00", freq="B"): 0.0012167854565034997,
        Timestamp("2021-06-02 00:00:00", freq="B"): 6.0732881765002134e-05,
        Timestamp("2021-06-03 00:00:00", freq="B"): -0.009448535346291309,
        Timestamp("2021-06-04 00:00:00", freq="B"): 0.013219229068937688,
        Timestamp("2021-06-07 00:00:00", freq="B"): 0.018858726664584324,
        Timestamp("2021-06-08 00:00:00", freq="B"): -0.0086160615965849,
        Timestamp("2021-06-09 00:00:00", freq="B"): -0.010279287793901304,
        Timestamp("2021-06-10 00:00:00", freq="B"): 0.006691874201599113,
        Timestamp("2021-06-11 00:00:00", freq="B"): -0.00360940179358471,
        Timestamp("2021-06-14 00:00:00", freq="B"): 0.016633396986087456,
        Timestamp("2021-06-15 00:00:00", freq="B"): -5.935509197363409e-05,
        Timestamp("2021-06-16 00:00:00", freq="B"): -0.016837456355558666,
        Timestamp("2021-06-17 00:00:00", freq="B"): 0.016400940599211156,
        Timestamp("2021-06-18 00:00:00", freq="B"): -0.020356024797855365,
        Timestamp("2021-06-21 00:00:00", freq="B"): 0.007977931364425261,
        Timestamp("2021-06-22 00:00:00", freq="B"): 0.0202834574048405,
        Timestamp("2021-06-23 00:00:00", freq="B"): 0.004601355526680839,
        Timestamp("2021-06-24 00:00:00", freq="B"): 0.0076044404290758205,
        Timestamp("2021-06-25 00:00:00", freq="B"): -0.005274193126706406,
        Timestamp("2021-06-28 00:00:00", freq="B"): 0.04180220797188494,
        Timestamp("2021-06-29 00:00:00", freq="B"): -0.010544370277644433,
        Timestamp("2021-06-30 00:00:00", freq="B"): -0.01187877751386468,
        Timestamp("2021-07-01 00:00:00", freq="B"): 0.01921147898398079,
        Timestamp("2021-07-02 00:00:00", freq="B"): 0.0008747355901133069,
        Timestamp("2021-07-05 00:00:00", freq="B"): 0.0,
        Timestamp("2021-07-06 00:00:00", freq="B"): -0.005413062761931098,
        Timestamp("2021-07-07 00:00:00", freq="B"): -0.006491321936747729,
        Timestamp("2021-07-08 00:00:00", freq="B"): -0.01380922843090071,
        Timestamp("2021-07-09 00:00:00", freq="B"): 0.013800143542541221,
        Timestamp("2021-07-12 00:00:00", freq="B"): 0.00781916023452256,
        Timestamp("2021-07-13 00:00:00", freq="B"): -0.003029808905661069,
        Timestamp("2021-07-14 00:00:00", freq="B"): -0.012667191631306696,
        Timestamp("2021-07-15 00:00:00", freq="B"): -0.009118929273101761,
        Timestamp("2021-07-16 00:00:00", freq="B"): -0.009580177306017013,
        Timestamp("2021-07-19 00:00:00", freq="B"): -0.012340225729531196,
        Timestamp("2021-07-20 00:00:00", freq="B"): 0.01397830919852927,
        Timestamp("2021-07-21 00:00:00", freq="B"): 0.013375892042483128,
        Timestamp("2021-07-22 00:00:00", freq="B"): 0.014325712092225329,
        Timestamp("2021-07-23 00:00:00", freq="B"): 0.05296280068968917,
        Timestamp("2021-07-26 00:00:00", freq="B"): 0.007220267850562845,
        Timestamp("2021-07-27 00:00:00", freq="B"): -0.012484546000010366,
        Timestamp("2021-07-28 00:00:00", freq="B"): 0.01487181223188938,
        Timestamp("2021-07-29 00:00:00", freq="B"): -0.040077131118732345,
        Timestamp("2021-07-30 00:00:00", freq="B"): -0.005637473459365716,
        Timestamp("2021-08-02 00:00:00", freq="B"): -0.012208744695397233,
        Timestamp("2021-08-03 00:00:00", freq="B"): -0.0020173943686030427,
        Timestamp("2021-08-04 00:00:00", freq="B"): 0.021865457826242052,
        Timestamp("2021-08-05 00:00:00", freq="B"): 0.01128381712206794,
        Timestamp("2021-08-06 00:00:00", freq="B"): 0.001487749795040294,
        Timestamp("2021-08-09 00:00:00", freq="B"): -0.005226883340262223,
        Timestamp("2021-08-10 00:00:00", freq="B"): -0.0013273429611833087,
    },
    "PBW": {
        Timestamp("2021-01-05 00:00:00", freq="B"): 0.027068687572521455,
        Timestamp("2021-01-06 00:00:00", freq="B"): 0.0618082410652705,
        Timestamp("2021-01-07 00:00:00", freq="B"): 0.07684839506212948,
        Timestamp("2021-01-08 00:00:00", freq="B"): 0.002460863891951215,
        Timestamp("2021-01-11 00:00:00", freq="B"): 0.004664050663451658,
        Timestamp("2021-01-12 00:00:00", freq="B"): 0.04007171012841915,
        Timestamp("2021-01-13 00:00:00", freq="B"): -0.012137841301218755,
        Timestamp("2021-01-14 00:00:00", freq="B"): -0.0003963384763387978,
        Timestamp("2021-01-15 00:00:00", freq="B"): -0.05606660786175777,
        Timestamp("2021-01-18 00:00:00", freq="B"): 0.0,
        Timestamp("2021-01-19 00:00:00", freq="B"): 0.058472618074178584,
        Timestamp("2021-01-20 00:00:00", freq="B"): -0.003174856103031698,
        Timestamp("2021-01-21 00:00:00", freq="B"): 0.03519388939115631,
        Timestamp("2021-01-22 00:00:00", freq="B"): 0.009922349037393197,
        Timestamp("2021-01-25 00:00:00", freq="B"): -0.03191166400218681,
        Timestamp("2021-01-26 00:00:00", freq="B"): 0.03123286838835071,
        Timestamp("2021-01-27 00:00:00", freq="B"): -0.04737571340919333,
        Timestamp("2021-01-28 00:00:00", freq="B"): -0.010170620002080244,
        Timestamp("2021-01-29 00:00:00", freq="B"): -0.03325240339475499,
        Timestamp("2021-02-01 00:00:00", freq="B"): 0.03648836818276324,
        Timestamp("2021-02-02 00:00:00", freq="B"): 0.017359792301435473,
        Timestamp("2021-02-03 00:00:00", freq="B"): 0.0243650640071722,
        Timestamp("2021-02-04 00:00:00", freq="B"): 0.0075927276423159995,
        Timestamp("2021-02-05 00:00:00", freq="B"): -0.0013840304451345764,
        Timestamp("2021-02-08 00:00:00", freq="B"): 0.027719916831281166,
        Timestamp("2021-02-09 00:00:00", freq="B"): 0.018955712364603805,
        Timestamp("2021-02-10 00:00:00", freq="B"): -0.019191177978571505,
        Timestamp("2021-02-11 00:00:00", freq="B"): -0.009745946388735605,
        Timestamp("2021-02-12 00:00:00", freq="B"): 0.005905072396510169,
        Timestamp("2021-02-15 00:00:00", freq="B"): 0.0,
        Timestamp("2021-02-16 00:00:00", freq="B"): -0.029126202394275436,
        Timestamp("2021-02-17 00:00:00", freq="B"): -0.03651166548065532,
        Timestamp("2021-02-18 00:00:00", freq="B"): -0.05865314185583259,
        Timestamp("2021-02-19 00:00:00", freq="B"): 0.027863302831604875,
        Timestamp("2021-02-22 00:00:00", freq="B"): -0.057542033601904685,
        Timestamp("2021-02-23 00:00:00", freq="B"): -0.04226216907193303,
        Timestamp("2021-02-24 00:00:00", freq="B"): 0.05214186273154753,
        Timestamp("2021-02-25 00:00:00", freq="B"): -0.06601877547975266,
        Timestamp("2021-02-26 00:00:00", freq="B"): 0.013030850449724518,
        Timestamp("2021-03-01 00:00:00", freq="B"): 0.051915614727344295,
        Timestamp("2021-03-02 00:00:00", freq="B"): -0.039588259772035395,
        Timestamp("2021-03-03 00:00:00", freq="B"): -0.061646943647349794,
        Timestamp("2021-03-04 00:00:00", freq="B"): -0.06374459764129203,
        Timestamp("2021-03-05 00:00:00", freq="B"): -0.01970610219983937,
        Timestamp("2021-03-08 00:00:00", freq="B"): -0.03041896399011712,
        Timestamp("2021-03-09 00:00:00", freq="B"): 0.09565587749277471,
        Timestamp("2021-03-10 00:00:00", freq="B"): 0.014417290284073347,
        Timestamp("2021-03-11 00:00:00", freq="B"): 0.07155554943815834,
        Timestamp("2021-03-12 00:00:00", freq="B"): -0.0041448454378045785,
        Timestamp("2021-03-15 00:00:00", freq="B"): 0.0024047150018327024,
        Timestamp("2021-03-16 00:00:00", freq="B"): -0.03829108717703111,
        Timestamp("2021-03-17 00:00:00", freq="B"): 0.0035497800299399973,
        Timestamp("2021-03-18 00:00:00", freq="B"): -0.06061182116618791,
        Timestamp("2021-03-19 00:00:00", freq="B"): 0.029513582104240932,
        Timestamp("2021-03-22 00:00:00", freq="B"): 0.0017124829844348266,
        Timestamp("2021-03-23 00:00:00", freq="B"): -0.05059786422025614,
        Timestamp("2021-03-24 00:00:00", freq="B"): -0.05797858444520909,
        Timestamp("2021-03-25 00:00:00", freq="B"): 0.01679555081252726,
        Timestamp("2021-03-26 00:00:00", freq="B"): 0.01869156547120232,
        Timestamp("2021-03-29 00:00:00", freq="B"): -0.04992526234093764,
        Timestamp("2021-03-30 00:00:00", freq="B"): 0.05827535768060166,
        Timestamp("2021-03-31 00:00:00", freq="B"): 0.04392569761489851,
        Timestamp("2021-04-01 00:00:00", freq="B"): 0.00874071435681767,
        Timestamp("2021-04-02 00:00:00", freq="B"): 0.0,
        Timestamp("2021-04-05 00:00:00", freq="B"): -0.023879124378910377,
        Timestamp("2021-04-06 00:00:00", freq="B"): 0.021366664723725615,
        Timestamp("2021-04-07 00:00:00", freq="B"): -0.045578532086850476,
        Timestamp("2021-04-08 00:00:00", freq="B"): 0.013871199098776765,
        Timestamp("2021-04-09 00:00:00", freq="B"): -0.015456938281009025,
        Timestamp("2021-04-12 00:00:00", freq="B"): -0.03150521772599901,
        Timestamp("2021-04-13 00:00:00", freq="B"): 0.0015334433459017749,
        Timestamp("2021-04-14 00:00:00", freq="B"): -0.00798341995203955,
        Timestamp("2021-04-15 00:00:00", freq="B"): -0.039245919585911726,
        Timestamp("2021-04-16 00:00:00", freq="B"): 0.00872058107706608,
        Timestamp("2021-04-19 00:00:00", freq="B"): -0.031168258285452444,
        Timestamp("2021-04-20 00:00:00", freq="B"): -0.021721267807053635,
        Timestamp("2021-04-21 00:00:00", freq="B"): 0.04752758409215252,
        Timestamp("2021-04-22 00:00:00", freq="B"): 0.010884578459289918,
        Timestamp("2021-04-23 00:00:00", freq="B"): 0.032415229083477826,
        Timestamp("2021-04-26 00:00:00", freq="B"): 0.029201921118230167,
        Timestamp("2021-04-27 00:00:00", freq="B"): -0.009386671411408254,
        Timestamp("2021-04-28 00:00:00", freq="B"): -0.008291236008971747,
        Timestamp("2021-04-29 00:00:00", freq="B"): -0.021063976875045576,
        Timestamp("2021-04-30 00:00:00", freq="B"): -0.025177493239403548,
        Timestamp("2021-05-03 00:00:00", freq="B"): -0.022414406426846223,
        Timestamp("2021-05-04 00:00:00", freq="B"): -0.031540960662165274,
        Timestamp("2021-05-05 00:00:00", freq="B"): -0.014060814607129046,
        Timestamp("2021-05-06 00:00:00", freq="B"): -0.027059958217770297,
        Timestamp("2021-05-07 00:00:00", freq="B"): 0.013405163439117684,
        Timestamp("2021-05-10 00:00:00", freq="B"): -0.056620116937158294,
        Timestamp("2021-05-11 00:00:00", freq="B"): 0.012056134751157854,
        Timestamp("2021-05-12 00:00:00", freq="B"): -0.0554189834983394,
        Timestamp("2021-05-13 00:00:00", freq="B"): -0.015764101939066744,
        Timestamp("2021-05-14 00:00:00", freq="B"): 0.04902498752866857,
        Timestamp("2021-05-17 00:00:00", freq="B"): 0.0030536753617700363,
        Timestamp("2021-05-18 00:00:00", freq="B"): 0.02647259507087929,
        Timestamp("2021-05-19 00:00:00", freq="B"): 0.004513177964609039,
        Timestamp("2021-05-20 00:00:00", freq="B"): 0.014890880102090831,
        Timestamp("2021-05-21 00:00:00", freq="B"): 0.004806467622785471,
        Timestamp("2021-05-24 00:00:00", freq="B"): -0.002391738000132926,
        Timestamp("2021-05-25 00:00:00", freq="B"): -0.01047323884860707,
        Timestamp("2021-05-26 00:00:00", freq="B"): 0.04437651812144505,
        Timestamp("2021-05-27 00:00:00", freq="B"): 0.02161164861507281,
        Timestamp("2021-05-28 00:00:00", freq="B"): -0.006931992489670802,
        Timestamp("2021-05-31 00:00:00", freq="B"): 0.0,
        Timestamp("2021-06-01 00:00:00", freq="B"): 0.018413838392405513,
        Timestamp("2021-06-02 00:00:00", freq="B"): 0.016426404537206674,
        Timestamp("2021-06-03 00:00:00", freq="B"): -0.007557322005846245,
        Timestamp("2021-06-04 00:00:00", freq="B"): 0.012066506431301915,
        Timestamp("2021-06-07 00:00:00", freq="B"): 0.021877573839380382,
        Timestamp("2021-06-08 00:00:00", freq="B"): 0.020729483456552567,
        Timestamp("2021-06-09 00:00:00", freq="B"): -0.008767074013567244,
        Timestamp("2021-06-10 00:00:00", freq="B"): -0.012427179375945063,
        Timestamp("2021-06-11 00:00:00", freq="B"): 0.013830593125221613,
        Timestamp("2021-06-14 00:00:00", freq="B"): -0.0032427585522408764,
        Timestamp("2021-06-15 00:00:00", freq="B"): -0.028270132741843534,
        Timestamp("2021-06-16 00:00:00", freq="B"): 0.01731705632215008,
        Timestamp("2021-06-17 00:00:00", freq="B"): 0.006581844272725679,
        Timestamp("2021-06-18 00:00:00", freq="B"): -0.010484744192979845,
        Timestamp("2021-06-21 00:00:00", freq="B"): -0.009644191450604134,
        Timestamp("2021-06-22 00:00:00", freq="B"): 0.00703819802975536,
        Timestamp("2021-06-23 00:00:00", freq="B"): 0.026924822490700162,
        Timestamp("2021-06-24 00:00:00", freq="B"): 0.0029008383822142214,
        Timestamp("2021-06-25 00:00:00", freq="B"): 0.007676075715778774,
        Timestamp("2021-06-28 00:00:00", freq="B"): 0.04316621719667846,
        Timestamp("2021-06-29 00:00:00", freq="B"): -0.000529108090735253,
        Timestamp("2021-06-30 00:00:00", freq="B"): -0.013235916642161727,
        Timestamp("2021-07-01 00:00:00", freq="B"): -0.01030152440522003,
        Timestamp("2021-07-02 00:00:00", freq="B"): -0.01929964592761335,
        Timestamp("2021-07-05 00:00:00", freq="B"): 0.0,
        Timestamp("2021-07-06 00:00:00", freq="B"): -0.00641231864266445,
        Timestamp("2021-07-07 00:00:00", freq="B"): -0.024924951871655,
        Timestamp("2021-07-08 00:00:00", freq="B"): -0.011069195728757864,
        Timestamp("2021-07-09 00:00:00", freq="B"): 0.01153934869307216,
        Timestamp("2021-07-12 00:00:00", freq="B"): 0.016541146334322354,
        Timestamp("2021-07-13 00:00:00", freq="B"): -0.026820776268413615,
        Timestamp("2021-07-14 00:00:00", freq="B"): -0.04750925609533363,
        Timestamp("2021-07-15 00:00:00", freq="B"): -0.0018159991361973438,
        Timestamp("2021-07-16 00:00:00", freq="B"): -0.024378345436418924,
        Timestamp("2021-07-19 00:00:00", freq="B"): -0.014172045686831392,
        Timestamp("2021-07-20 00:00:00", freq="B"): 0.03543502459589698,
        Timestamp("2021-07-21 00:00:00", freq="B"): 0.045670441750395474,
        Timestamp("2021-07-22 00:00:00", freq="B"): -0.02247845669061288,
        Timestamp("2021-07-23 00:00:00", freq="B"): -0.02835693130899697,
        Timestamp("2021-07-26 00:00:00", freq="B"): -0.005518142989536234,
        Timestamp("2021-07-27 00:00:00", freq="B"): -0.02663373703273364,
        Timestamp("2021-07-28 00:00:00", freq="B"): 0.04877119780910544,
        Timestamp("2021-07-29 00:00:00", freq="B"): 0.0077303947647184845,
        Timestamp("2021-07-30 00:00:00", freq="B"): 0.002876637455251796,
        Timestamp("2021-08-02 00:00:00", freq="B"): -0.005856314981388389,
        Timestamp("2021-08-03 00:00:00", freq="B"): 0.0020437384986968787,
        Timestamp("2021-08-04 00:00:00", freq="B"): -0.01619674263749682,
        Timestamp("2021-08-05 00:00:00", freq="B"): 0.01085365109327352,
        Timestamp("2021-08-06 00:00:00", freq="B"): -0.004343112715676001,
        Timestamp("2021-08-09 00:00:00", freq="B"): 0.029565036683586454,
        Timestamp("2021-08-10 00:00:00", freq="B"): 0.019771687431333618,
    },
}
