import struct
from typing import Any

SS0: list = [
    696885672,
    92635524,
    382128852,
    331600848,
    340021332,
    487395612,
    747413676,
    621093156,
    491606364,
    54739776,
    403181592,
    504238620,
    289493328,
    1020063996,
    181060296,
    591618912,
    671621160,
    71581764,
    536879136,
    495817116,
    549511392,
    583197408,
    147374280,
    386339604,
    629514660,
    261063564,
    50529024,
    994800504,
    999011256,
    318968592,
    314757840,
    785310444,
    809529456,
    210534540,
    1057960764,
    680042664,
    839004720,
    500027868,
    919007988,
    876900468,
    751624428,
    361075092,
    185271048,
    390550356,
    474763356,
    457921368,
    1032696252,
    16843008,
    604250148,
    470552604,
    860058480,
    411603096,
    268439568,
    214745292,
    851636976,
    432656856,
    738992172,
    667411428,
    843215472,
    58950528,
    462132120,
    297914832,
    109478532,
    164217288,
    541089888,
    272650320,
    595829664,
    734782440,
    218956044,
    914797236,
    512660124,
    256852812,
    931640244,
    441078360,
    113689284,
    944271480,
    646357668,
    302125584,
    797942700,
    365285844,
    557932896,
    63161280,
    881111220,
    21053760,
    306336336,
    1028485500,
    227377548,
    134742024,
    521081628,
    428446104,
    0,
    420024600,
    67371012,
    323179344,
    935850996,
    566354400,
    1036907004,
    910586484,
    789521196,
    654779172,
    813740208,
    193692552,
    235799052,
    730571688,
    578986656,
    776888940,
    327390096,
    223166796,
    692674920,
    1011642492,
    151585032,
    168428040,
    1066382268,
    802153452,
    868479984,
    96846276,
    126321540,
    335810580,
    1053750012,
    608460900,
    516870876,
    772678188,
    189481800,
    436867608,
    101057028,
    553722144,
    726360936,
    642146916,
    33686016,
    902164980,
    310547088,
    176849544,
    202113036,
    864269232,
    1045328508,
    281071824,
    977957496,
    122110788,
    377918100,
    633725412,
    637936164,
    8421504,
    764256684,
    533713884,
    562143648,
    805318704,
    923218740,
    781099692,
    906375732,
    352653588,
    570565152,
    940060728,
    885321972,
    663200676,
    88424772,
    206323788,
    25264512,
    701096424,
    75792516,
    394761108,
    889532724,
    197903304,
    248431308,
    1007431740,
    826372464,
    285282576,
    130532292,
    160006536,
    893743476,
    1003222008,
    449499864,
    952692984,
    344232084,
    424235352,
    42107520,
    80003268,
    1070593020,
    155795784,
    956903736,
    658989924,
    12632256,
    265274316,
    398971860,
    948482232,
    252642060,
    244220556,
    37896768,
    587408160,
    293704080,
    743202924,
    466342872,
    612671652,
    872689716,
    834793968,
    138952776,
    46318272,
    793731948,
    1024274748,
    755835180,
    4210752,
    1049539260,
    1041117756,
    1015853244,
    29475264,
    713728680,
    982168248,
    240009804,
    356864340,
    990589752,
    483184860,
    675831912,
    1062171516,
    478974108,
    415813848,
    172638792,
    373707348,
    927429492,
    545300640,
    768467436,
    105267780,
    897954228,
    722150184,
    625303908,
    986379000,
    600040416,
    965325240,
    830583216,
    529503132,
    508449372,
    969535992,
    650568420,
    847426224,
    822161712,
    717939432,
    760045932,
    525292380,
    616882404,
    817950960,
    231588300,
    143163528,
    369496596,
    973746744,
    407392344,
    348442836,
    574775904,
    688464168,
    117900036,
    855847728,
    684253416,
    453710616,
    84214020,
    961114488,
    276861072,
    709517928,
    705307176,
    445289112,
]

SS1: list = [
    943196208,
    3894986976,
    741149985,
    2753988258,
    3423588291,
    3693006546,
    2956166067,
    3090712752,
    2888798115,
    1612726368,
    1410680145,
    3288844227,
    1141130304,
    1815039843,
    1747667811,
    1478183763,
    3221472195,
    1612857954,
    808649523,
    3023406513,
    673777953,
    2686484640,
    3760374498,
    2754054051,
    3490956243,
    2417066385,
    269549841,
    67503618,
    471600144,
    3158084784,
    875955762,
    1208699715,
    3962556387,
    2282260608,
    1814842464,
    2821228704,
    337053459,
    3288646848,
    336987666,
    4097098992,
    3221406402,
    1141196097,
    3760308705,
    3558262482,
    1010765619,
    1010634033,
    2349764226,
    2551744656,
    673712160,
    1276005954,
    4097230578,
    1010699826,
    2753922465,
    4164536817,
    202181889,
    3693072339,
    3625502928,
    673909539,
    1680229986,
    2017086066,
    606537507,
    741281571,
    4029792753,
    1882342002,
    1073889858,
    3558130896,
    1073824065,
    3221274816,
    1882407795,
    1680295779,
    2888600736,
    2282457987,
    4097296371,
    2888666529,
    2147516544,
    471797523,
    3356150466,
    741084192,
    2821360290,
    875824176,
    3490890450,
    134941443,
    3962490594,
    3895052769,
    1545424209,
    2484372624,
    404228112,
    4164471024,
    1410811731,
    2888732322,
    134744064,
    3288712641,
    269681427,
    3423456705,
    2215020162,
    3090778545,
    4232040435,
    2084392305,
    3221340609,
    808517937,
    4097164785,
    2282392194,
    1747602018,
    2956034481,
    3490824657,
    538968096,
    3558328275,
    131586,
    539099682,
    67372032,
    1747470432,
    1882276209,
    67569411,
    3625700307,
    2619182481,
    2551810449,
    1612792161,
    3158216370,
    3827746530,
    1478052177,
    3692940753,
    1343308113,
    2417000592,
    3692874960,
    2551876242,
    2686682019,
    2821426083,
    3490758864,
    2147582337,
    202313475,
    1141327683,
    404359698,
    3760440291,
    3962359008,
    2349698433,
    3158282163,
    2484504210,
    2017151859,
    1545358416,
    2686616226,
    2686550433,
    1612923747,
    539165475,
    1275940161,
    3356018880,
    2619248274,
    2619116688,
    943327794,
    202116096,
    741215778,
    3090844338,
    1814974050,
    2619314067,
    1478117970,
    4029858546,
    2417132178,
    4029924339,
    1208568129,
    2016954480,
    3423390912,
    336921873,
    4164668403,
    1882210416,
    1949648241,
    2084523891,
    875889969,
    269484048,
    197379,
    1680098400,
    1814908257,
    3288778434,
    1949582448,
    3558196689,
    3023340720,
    3895118562,
    134809857,
    1949714034,
    404293905,
    4231974642,
    1073758272,
    269615634,
    3760242912,
    3158150577,
    67437825,
    4164602610,
    65793,
    4029726960,
    673843746,
    1545490002,
    2821294497,
    1410745938,
    1073955651,
    2214954369,
    336856080,
    2282326401,
    2551942035,
    2955968688,
    3827680737,
    1208502336,
    2017020273,
    2484570003,
    4231843056,
    471731730,
    2147648130,
    539033889,
    2349632640,
    404425491,
    1545555795,
    1949779827,
    1410614352,
    2956100274,
    471665937,
    606405921,
    1276071747,
    0,
    1141261890,
    3962424801,
    1477986384,
    1343373906,
    3895184355,
    2084458098,
    3625634514,
    3356084673,
    4231908849,
    808452144,
    2484438417,
    1680164193,
    1010568240,
    3023472306,
    3827614944,
    3090910131,
    2084326512,
    202247682,
    1343242320,
    943262001,
    606471714,
    808583730,
    2214888576,
    1747536225,
    2417197971,
    876021555,
    3827812323,
    606340128,
    2753856672,
    3356216259,
    1343439699,
    134875650,
    2215085955,
    3625568721,
    1275874368,
    2147713923,
    2349830019,
    3423522498,
    943393587,
    1208633922,
    3023538099,
]

SS2: list = [
    2712152457,
    2172913029,
    3537114822,
    3553629123,
    1347687492,
    287055117,
    2695638156,
    556016901,
    1364991309,
    1128268611,
    270014472,
    303832590,
    1364201793,
    4043062476,
    3267889866,
    1667244867,
    539502600,
    1078199364,
    538976256,
    2442927501,
    3772784832,
    3806339778,
    3234334920,
    320083719,
    2711889285,
    2206994319,
    50332419,
    1937259339,
    3015195531,
    319820547,
    3536851650,
    3807129294,
    1886400576,
    2156661900,
    859586319,
    2695374984,
    842019330,
    3520863693,
    4076091078,
    1886663748,
    3773574348,
    2442401157,
    50858763,
    1398019911,
    1348213836,
    1398283083,
    2981903757,
    16777473,
    539239428,
    270277644,
    1936732995,
    2425886856,
    269488128,
    3234598092,
    4075827906,
    3520600521,
    539765772,
    3823380423,
    1919955522,
    2206204803,
    2476219275,
    3520074177,
    2189690502,
    3251112393,
    1616912448,
    1347424320,
    2745181059,
    3823643595,
    17566989,
    2998154886,
    2459704974,
    1129058127,
    3014932359,
    1381505610,
    3267626694,
    1886926920,
    2728666758,
    303043074,
    2745970575,
    3520337349,
    1633689921,
    3284140995,
    2964599940,
    1094713665,
    1380979266,
    1903967565,
    2173439373,
    526344,
    320610063,
    2442664329,
    0,
    286791945,
    263172,
    1397756739,
    4092868551,
    3789562305,
    4059839949,
    1920218694,
    590098191,
    589571847,
    2964336768,
    2206731147,
    34344462,
    2745707403,
    2728403586,
    1651256910,
    2475692931,
    1095503181,
    1634216265,
    1887190092,
    17303817,
    34081290,
    3015458703,
    3823906767,
    4092605379,
    3250849221,
    2206467975,
    269751300,
    4076617422,
    1617175620,
    3537641166,
    573320718,
    1128794955,
    303569418,
    33818118,
    555753729,
    1667771211,
    1650730566,
    33554946,
    4059313605,
    2458915458,
    2189953674,
    789516,
    3014669187,
    1920745038,
    3503296704,
    1920481866,
    1128531783,
    2459178630,
    3789825477,
    572794374,
    2155872384,
    2712415629,
    3554418639,
    2711626113,
    808464384,
    859059975,
    2729193102,
    842282502,
    286528773,
    572531202,
    808990728,
    4042536132,
    2745444231,
    1094976837,
    1078725708,
    2172649857,
    3790088649,
    2156135556,
    2475956103,
    825505029,
    3284667339,
    3268153038,
    809253900,
    1903178049,
    286265601,
    3284404167,
    2173176201,
    1903441221,
    4093131723,
    3537377994,
    4042799304,
    2425623684,
    1364728137,
    2189427330,
    3234071748,
    4093394895,
    1095240009,
    825768201,
    1667508039,
    3233808576,
    3284930511,
    3553892295,
    2964863112,
    51121935,
    2190216846,
    1111491138,
    589308675,
    2442137985,
    1617701964,
    3554155467,
    2695111812,
    808727556,
    4059050433,
    1078462536,
    3267363522,
    1668034383,
    826031373,
    556543245,
    1077936192,
    2998681230,
    842808846,
    2965126284,
    3250586049,
    2728929930,
    2998418058,
    1112280654,
    1364464965,
    859323147,
    3504086220,
    1617438792,
    1937522511,
    2426150028,
    3503823048,
    1112017482,
    1381242438,
    1936996167,
    2694848640,
    3790351821,
    1111754310,
    2981377413,
    589835019,
    1633953093,
    4076354250,
    3823117251,
    2981640585,
    2981114241,
    2476482447,
    1381768782,
    4059576777,
    3806602950,
    2997891714,
    825241857,
    3806866122,
    1634479437,
    1398546255,
    3773048004,
    4042272960,
    3251375565,
    2156398728,
    303306246,
    842545674,
    1347950664,
    3503559876,
    1650467394,
    556280073,
    50595591,
    858796803,
    3773311176,
    320346891,
    17040645,
    1903704393,
    2425360512,
    1650993738,
    573057546,
    2459441802,
]

SS3: list = [
    137377848,
    3370182696,
    220277805,
    2258805798,
    3485715471,
    3469925406,
    2209591347,
    2293282872,
    2409868335,
    1080057888,
    1162957845,
    3351495687,
    1145062404,
    1331915823,
    1264805931,
    1263753243,
    3284385795,
    1113743394,
    53686323,
    2243015733,
    153167913,
    2158010400,
    3269648418,
    2275648551,
    3285438483,
    2173800465,
    17895441,
    100795398,
    202382364,
    2360392764,
    103953462,
    1262700555,
    3487820847,
    2290124808,
    1281387564,
    2292230184,
    118690839,
    3300967428,
    101848086,
    3304125492,
    3267543042,
    1161905157,
    3252805665,
    3335705622,
    255015999,
    221330493,
    2390920206,
    2291177496,
    136325160,
    1312967694,
    3337810998,
    238173246,
    2241963045,
    3388078137,
    218172429,
    3486768159,
    3369130008,
    186853419,
    1180853286,
    1249015866,
    119743527,
    253963311,
    3253858353,
    1114796082,
    1111638018,
    3302020116,
    1094795265,
    3233857536,
    1131638835,
    1197696039,
    2359340076,
    2340653067,
    3354653751,
    2376182829,
    2155905024,
    252910623,
    3401762826,
    203435052,
    2325915690,
    70267956,
    3268595730,
    184748043,
    3470978094,
    3387025449,
    1297177629,
    2224067604,
    135272472,
    3371235384,
    1196643351,
    2393025582,
    134219784,
    3317810181,
    51580947,
    3452029965,
    2256700422,
    2310125625,
    3488873535,
    1299283005,
    3250700289,
    20000817,
    3320968245,
    2323810314,
    1247963178,
    2175905841,
    3251752977,
    2105376,
    3352548375,
    33685506,
    35790882,
    67109892,
    1214277672,
    1097953329,
    117638151,
    3419658267,
    2375130141,
    2308020249,
    1096900641,
    2394078270,
    3336758310,
    1230067737,
    3453082653,
    1095847953,
    2156957712,
    3436239900,
    2324863002,
    2208538659,
    2342758443,
    3234910224,
    2172747777,
    251857935,
    1195590663,
    168957978,
    3286491171,
    3437292588,
    2374077453,
    2410921023,
    2257753110,
    1265858619,
    1280334876,
    2191695906,
    2174853153,
    1130586147,
    52633635,
    1296124941,
    3368077320,
    2391972894,
    2358287388,
    171063354,
    201329676,
    237120558,
    2326968378,
    1315073070,
    2408815647,
    1246910490,
    3270701106,
    2190643218,
    3287543859,
    1229015049,
    1215330360,
    3435187212,
    85005333,
    3421763643,
    1081110576,
    1165063221,
    1332968511,
    87110709,
    1052688,
    50528259,
    1147167780,
    1298230317,
    3334652934,
    1148220468,
    3318862869,
    2226172980,
    3403868202,
    151062537,
    1181905974,
    152115225,
    3472030782,
    1077952512,
    34738194,
    3235962912,
    2377235517,
    83952645,
    3404920890,
    16842753,
    3237015600,
    170010666,
    1314020382,
    2309072937,
    1179800598,
    1128480771,
    2239857669,
    68162580,
    2306967561,
    2341705755,
    2159063088,
    3319915557,
    1212172296,
    1232173113,
    2274595863,
    3438345276,
    236067870,
    2189590530,
    18948129,
    2357234700,
    185800731,
    1330863135,
    1198748727,
    1146115092,
    2192748594,
    219225117,
    86058021,
    1329810447,
    0,
    1178747910,
    3454135341,
    1213224984,
    1112690706,
    3420710955,
    1316125758,
    3402815514,
    3384920073,
    3455188029,
    3158064,
    2240910357,
    1164010533,
    204487740,
    2259858486,
    3303072804,
    2343811131,
    1282440252,
    235015182,
    1079005200,
    154220601,
    102900774,
    36843570,
    2223014916,
    1231120425,
    2207485971,
    120796215,
    3353601063,
    69215268,
    2225120292,
    3418605579,
    1129533459,
    167905290,
    2273543175,
    3385972761,
    1279282188,
    2206433283,
    2407762959,
    3468872718,
    187906107,
    1245857802,
    2276701239,
]

L_ENDIAN = 0


async def get_dword(buf: str, off: bytes) -> int:
    return struct.unpack(">L", buf[off : off + 4])[0]


async def get_b0(a: int) -> int:
    return a & 255


async def get_b1(a: int) -> int:
    return a >> 8 & 255


async def get_b2(a: int) -> int:
    return a >> 16 & 255


async def get_b3(a: int) -> int:
    return a >> 24 & 255


async def rol(data: int, shift: int, size: int = 32) -> int:
    shift %= size
    remains = data >> size - shift
    body = (data << shift) - (remains << size)
    return body + remains


async def ror(data: int, shift: int, size=32) -> int:
    shift %= size
    body = data >> shift
    remains = (data << size - shift) - (body << size)
    return body + remains


async def endian_change(data: int) -> int:
    rol1 = await rol(data, 8, 32) & 16711935
    rol2 = await rol(data, 24, 32) & 4278255360
    return rol1 | rol2


class SEED:
    def __init__(self):
        self.KC0 = 2654435769
        self.KC1 = 1013904243
        self.KC2 = 2027808486
        self.KC3 = 4055616972
        self.KC4 = 3816266649
        self.KC5 = 3337566003
        self.KC6 = 2380164711
        self.KC7 = 465362127
        self.KC8 = 930724254
        self.KC9 = 1861448508
        self.KC10 = 3722897016
        self.KC11 = 3150826737
        self.KC12 = 2006686179
        self.KC13 = 4013372358
        self.KC14 = 3731777421
        self.KC15 = 3168587547

    async def seed_encrypt(self, src: int, round_key: str) -> bytes:
        L0 = []
        L1 = []
        R0 = []
        R1 = []
        if L_ENDIAN == 1:
            L0.append(await endian_change(await get_dword(src, 0)))
            L1.append(await endian_change(await get_dword(src, 4)))
            R0.append(await endian_change(await get_dword(src, 8)))
            R1.append(await endian_change(await get_dword(src, 12)))
        else:
            L0.append(await get_dword(src, 0))
            L1.append(await get_dword(src, 4))
            R0.append(await get_dword(src, 8))
            R1.append(await get_dword(src, 12))
        K = round_key
        await self.seed_round(L0, L1, R0, R1, K, 0)
        await self.seed_round(R0, R1, L0, L1, K, 2)
        await self.seed_round(L0, L1, R0, R1, K, 4)
        await self.seed_round(R0, R1, L0, L1, K, 6)
        await self.seed_round(L0, L1, R0, R1, K, 8)
        await self.seed_round(R0, R1, L0, L1, K, 10)
        await self.seed_round(L0, L1, R0, R1, K, 12)
        await self.seed_round(R0, R1, L0, L1, K, 14)
        await self.seed_round(L0, L1, R0, R1, K, 16)
        await self.seed_round(R0, R1, L0, L1, K, 18)
        await self.seed_round(L0, L1, R0, R1, K, 20)
        await self.seed_round(R0, R1, L0, L1, K, 22)
        await self.seed_round(L0, L1, R0, R1, K, 24)
        await self.seed_round(R0, R1, L0, L1, K, 26)
        await self.seed_round(L0, L1, R0, R1, K, 28)
        await self.seed_round(R0, R1, L0, L1, K, 30)
        if L_ENDIAN == 1:
            return struct.pack(
                ">LLLL",
                await endian_change(R0[0]),
                await endian_change(R1[0]),
                await endian_change(L0[0]),
                await endian_change(L1[0]),
            )
        else:
            return struct.pack(">LLLL", R0[0], R1[0], L0[0], L1[0])

    @staticmethod
    async def seed_round(
        self, L0: list, L1: list, R0: list, R1: list, K: list, off: int
    ) -> None:
        T0 = R0[0] ^ K[off + 0]
        T1 = R1[0] ^ K[off + 1]
        T1 ^= T0
        T1 = (
            SS0[await get_b0(T1)]
            ^ SS1[await get_b1(T1)]
            ^ SS2[await get_b2(T1)]
            ^ SS3[await get_b3(T1)]
        )
        T0 += T1
        T0 &= 4294967295
        T0 = (
            SS0[await get_b0(T0)]
            ^ SS1[await get_b1(T0)]
            ^ SS2[await get_b2(T0)]
            ^ SS3[await get_b3(T0)]
        )
        T1 += T0
        T1 &= 4294967295
        T1 = (
            SS0[await get_b0(T1)]
            ^ SS1[await get_b1(T1)]
            ^ SS2[await get_b2(T1)]
            ^ SS3[await get_b3(T1)]
        )
        T0 += T1
        T0 &= 4294967295
        L0[0] ^= T0
        L1[0] ^= T1

    async def seed_round_key(self, user_key) -> Any:
        if len(user_key) < 16:
            user_key += "\x00" * (16 - len(user_key))
        A = []
        B = []
        C = []
        D = []
        if L_ENDIAN == 1:
            A.append(await endian_change(await get_dword(user_key, 0)))
            B.append(await endian_change(await get_dword(user_key, 4)))
            C.append(await endian_change(await get_dword(user_key, 8)))
            D.append(await endian_change(await get_dword(user_key, 12)))
        else:
            A.append(await get_dword(user_key, 0))
            B.append(await get_dword(user_key, 4))
            C.append(await get_dword(user_key, 8))
            D.append(await get_dword(user_key, 12))
        RoundKey = []
        for i in range(32):
            RoundKey.append(0)

        K = RoundKey
        await self.round_key_update0(K, 0, A, B, C, D, self.KC0)
        await self.round_key_update1(K, 2, A, B, C, D, self.KC1)
        await self.round_key_update0(K, 4, A, B, C, D, self.KC2)
        await self.round_key_update1(K, 6, A, B, C, D, self.KC3)
        await self.round_key_update0(K, 8, A, B, C, D, self.KC4)
        await self.round_key_update1(K, 10, A, B, C, D, self.KC5)
        await self.round_key_update0(K, 12, A, B, C, D, self.KC6)
        await self.round_key_update1(K, 14, A, B, C, D, self.KC7)
        await self.round_key_update0(K, 16, A, B, C, D, self.KC8)
        await self.round_key_update1(K, 18, A, B, C, D, self.KC9)
        await self.round_key_update0(K, 20, A, B, C, D, self.KC10)
        await self.round_key_update1(K, 22, A, B, C, D, self.KC11)
        await self.round_key_update0(K, 24, A, B, C, D, self.KC12)
        await self.round_key_update1(K, 26, A, B, C, D, self.KC13)
        await self.round_key_update0(K, 28, A, B, C, D, self.KC14)
        T0 = A[0] + C[0] - self.KC15
        T1 = B[0] - D[0] + self.KC15
        K[30] = (
            SS0[await get_b0(T0)]
            ^ SS1[await get_b1(T0)]
            ^ SS2[await get_b2(T0)]
            ^ SS3[await get_b3(T0)]
        )
        K[31] = (
            SS0[await get_b0(T1)]
            ^ SS1[await get_b1(T1)]
            ^ SS2[await get_b2(T1)]
            ^ SS3[await get_b3(T1)]
        )
        for i in range(32):
            RoundKey[i] &= 4294967295

        return RoundKey

    @staticmethod
    async def round_key_update0(
        self, K: list, off: int, A: list, B: list, C: list, D: list, KC: int
    ) -> None:
        T0 = A[0] + C[0] - KC & 4294967295
        T1 = B[0] + KC - D[0] & 4294967295
        K[off + 0] = (
            SS0[await get_b0(T0)]
            ^ SS1[await get_b1(T0)]
            ^ SS2[await get_b2(T0)]
            ^ SS3[await get_b3(T0)]
        )
        K[off + 1] = (
            SS0[await get_b0(T1)]
            ^ SS1[await get_b1(T1)]
            ^ SS2[await get_b2(T1)]
            ^ SS3[await get_b3(T1)]
        )
        T0 = A[0]
        A[0] = (A[0] >> 8 ^ (B[0] & 255) << 24) & 4294967295
        B[0] = (B[0] >> 8 ^ (T0 & 255) << 24) & 4294967295

    @staticmethod
    async def round_key_update1(
        self, K: list, off: int, A: list, B: list, C: list, D: list, KC: int
    ) -> None:
        T0 = A[0] + C[0] - KC & 4294967295
        T1 = B[0] + KC - D[0] & 4294967295
        K[off + 0] = (
            SS0[await get_b0(T0)]
            ^ SS1[await get_b1(T0)]
            ^ SS2[await get_b2(T0)]
            ^ SS3[await get_b3(T0)]
        )
        K[off + 1] = (
            SS0[await get_b0(T1)]
            ^ SS1[await get_b1(T1)]
            ^ SS2[await get_b2(T1)]
            ^ SS3[await get_b3(T1)]
        )
        T0 = C[0]
        C[0] = (C[0] << 8 ^ D[0] >> 24) & 4294967295
        D[0] = (D[0] << 8 ^ T0 >> 24) & 4294967295

    async def my_cbc_encrypt(self, in_data, k, iv) -> bytes:
        xo_red = []
        for i in range(0, 16):
            xo_red.append(iv[i] ^ in_data[i])

        enc = await self.seed_encrypt(bytes(xo_red), k)
        return enc