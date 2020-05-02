def get_no(arr):
    i = 0
    count = 0
    total_sum = sum(arr)
    left_sum = arr[0]
    while i < (len(arr)):
        left_sum += arr[i]
        right_sum = total_sum - left_sum
        print left_sum , " : ", right_sum
        if left_sum > right_sum:
            count += 1
        i += 1
    return count


def is_pallindrom(word):
    return word == word[::-1]

def threePalindromicSubstrings(word):
    # Write your code here
    i = 0
    j = 2
    pallindrom_words = []
    while j < (len(word)+1):
        print i, j
        if is_pallindrom(word[i:j]) and len(pallindrom_words) != 3:
            pallindrom_words.append(word[i:j])
            print word[i:j]
            i=j
            j+=1
        j+=1
    if len(pallindrom_words) == 3:
        return pallindrom_words
    else:
        return "Impossible"

if __name__ == '__main__':
    # l = [1000,5321,5255,-7067,-1790,9725,8358,668,-3371,9573,-8682,-7849,-8023,9946,2450,-6512,5375,-7713,-2082,5328,8461,8739,6326,4895,8509,-5599,-421,-9414,5022,1753,7706,2355,-7893,-2051,7232,-6019,-5940,-9061,-8187,4417,4087,-3342,2327,3772,606,-3797,5907,2003,3015,-7490,-2776,3502,-3913,3391,-1594,-419,135,-1560,3638,-8483,4944,-5089,5300,5976,-1078,-7000,5151,-6896,6488,-9320,-8581,9916,582,4007,-2350,7144,-4593,-369,-759,9488,-6386,1909,-3577,2160,-564,7905,8819,6349,8405,793,-2929,-6153,-4676,5329,-6003,353,-5075,-6647,-8777,5500,-2482,5033,9609,-1742,4981,1919,-1118,-2347,-6649,-3941,6259,7392,-3287,584,-4572,8663,-6925,-9376,-7231,-2548,9770,-4847,-3563,662,-2626,-6994,-8998,3093,-1045,-1329,-4193,-5954,8775,-5663,-6331,8557,2048,-404,-27,-1464,3543,-9576,-758,4491,8227,7565,-3822,-5257,2990,-5514,8026,190,-357,-2378,2642,6530,-9874,9258,-7612,6495,-6677,-811,-3503,-8040,-9925,-1992,-2002,5856,-7222,4345,6020,-5218,366,-4611,-7789,-6905,8588,6895,-767,-5957,4672,-2530,-9506,-3570,-9148,3792,-526,-2621,-3732,6781,3293,4733,-3013,-1052,-6916,2852,-4779,-3379,2755,-1603,383,-6106,-4881,-9082,3212,6420,-7984,-837,-5058,-8660,644,514,-775,7275,2795,-8433,-4386,-3233,-9546,8836,2971,-8661,-8928,-7560,2776,3035,4018,-1373,-1209,-2158,-4613,6307,8235,3007,938,3348,5820,-846,9128,-1491,7806,-1867,-9136,-3723,-4370,-2497,1522,5972,8932,-4807,-1424,4618,6030,-161,-6636,8339,1939,-7747,-8105,5670,-1263,523,-688,7070,-6445,-3696,-1157,-3754,4361,975,6646,151,-8804,-2169,9342,1218,-2084,6933,6091,448,7789,4291,7578,8915,-2797,-6933,5682,-3705,2511,-5706,1570,-5689,-2058,-3361,6986,-82,1912,1677,-3898,-2868,-4756,2695,-7426,6487,1397,-3270,-6474,3009,709,-6841,9310,5961,-8936,8162,3289,6700,5041,-9629,-493,-2340,524,1907,-426,-3355,7659,2814,-4333,-6652,-8606,-953,3097,1657,9411,-1212,9619,7607,-2082,-8847,2048,4170,-974,2057,3504,-8303,-9727,3811,1943,-7317,9893,-183,-6061,-5655,2184,-2825,-9918,-2441,-8937,512,9270,4420,2801,-9226,-8460,-8958,-5987,-4665,2228,-8445,-1241,6567,6117,-4091,6597,7881,7294,8106,5014,9543,8619,-3945,-4971,2538,7919,4404,1343,-9079,3349,-341,-9806,5040,6717,9618,1818,1344,-9460,-1527,-764,283,-3730,-1729,7456,6406,5625,9072,2844,-2690,1811,5287,-9735,9658,-5011,2043,-8910,-6639,-7882,2942,-6530,1230,1972,-522,-8936,1233,77,-1102,5681,-32,-4456,263,8402,-1563,-6652,302,-9736,-9884,9464,-2928,-9148,1515,-8361,6652,9219,5924,7141,4738,-4205,-7173,4384,8263,-852,1720,-8896,2650,9615,-4957,9224,-5456,-2198,-562,2408,3997,4761,-4264,8882,7689,-8749,-2906,8252,3245,-7679,-7585,-3578,-8582,-1714,-4173,-9218,-8096,3357,2765,6761,-5888,-6478,-8111,-5471,-2783,-9748,-851,-6986,1257,9185,-1766,1252,-7807,-1830,-5674,-8778,-3341,5654,7174,-6029,4614,4010,1379,7335,-1233,-5996,-6900,2025,-2594,-2622,9240,4170,-8055,-3331,-5182,2563,1955,4799,6366,904,3790,8488,1836,-88,6303,-8734,5834,-2029,7874,-2804,-9392,-3079,-6177,3529,9922,-9455,5737,-256,-6535,7499,-5568,8444,4278,-2446,4210,-6917,4280,-7682,-3076,5327,-5371,-8540,-6010,0,9368,-4082,1398,3640,7017,1352,-8154,-2971,-5976,8580,-8396,-2994,-6607,-6335,728,-1337,-8084,5589,-9509,-1965,-3729,-5702,-9863,2412,4301,-7727,7153,-1992,3656,8790,4577,7390,6783,2523,9723,6831,-4308,3035,8146,4585,5457,-8456,-553,-1717,1633,-9564,-4128,-1956,5645,-3026,1190,-251,-7954,-6198,-2738,6,723,6786,3548,2254,6807,-6648,9113,8918,-6154,5773,994,-6365,-9777,4538,-6412,-4296,8668,-9917,7893,-3619,5807,8311,-2021,1318,-2833,2213,-2659,-3007,-780,2488,-6083,-8440,-3895,3810,2922,1945,-3811,5941,-5109,5111,-9410,8330,5590,9029,-1537,-5156,-5224,-5913,-5454,-1979,1029,3546,5272,138,9499,108,-3449,7436,5625,-9359,-5162,3217,-681,9037,9586,9210,-7527,5981,386,5193,7282,2150,8491,-7838,7522,-4929,-8709,-451,-2869,-3642,7347,-9,7392,-4512,8281,5024,4154,431,-4481,-5897,4937,4552,4440,-3853,4255,-5522,-9716,-5210,-4285,7825,-1825,-9857,788,-67,1601,-1042,-3834,-6501,8353,-9724,9679,9683,6118,-7584,9859,1554,-6771,3061,6149,-829,-5051,5189,-2692,2393,-746,4688,-1343,5645,8993,8051,9028,-7434,5027,-677,2601,-5416,-2502,-4967,6164,1592,1733,7241,-3802,2709,401,7393,-6007,-4187,4789,6881,-8855,8945,9124,1808,-2471,9411,-9730,-4612,4894,-3536,-9303,-1619,8890,3634,4337,9610,-3674,5013,-2544,-290,151,-5604,5402,-5050,3350,5194,-1208,254,-8505,1308,-6956,-4113,-1061,-8100,-8066,2376,-1153,-2625,-5643,-5825,4510,-3771,-9474,1520,-4128,-4122,-6768,-9680,9412,3716,5408,-3416,3290,6115,-4935,2073,6616,-6833,3717,-5876,-6717,5084,-9679,-1342,3733,-2710,3102,-8597,3554,-1007,7423,-6834,-9667,8879,4803,325,-5521,4858,-3850,-831,6189,-2261,-6027,-1047,6637,-7307,6474,9540,-5925,2541,3458,6883,1961,-7877,4926,5884,2345,3596,7604,-6403,8214,-5939,-5515,4934,8613,-369,4684,3746,-4111,-9194,-3862,-1920,-5723,4967,-9977,1234,-8473,4108,-3766,-3933,-2224,799,-8123,3120,-5030,1280,-6036,9907,-9443,-526,-8519,1566,-8725,1530,-1232,4494,5589,528,-6991,7266,8993,2399,-1015,-269,-1655,-3547,-3141,-4178,1255,-8532,1628,5239,7604,4436,-3910,-4518,-4799,-5504,-7627,-2189,6412,5547,-4075,-4094,2669,-2426,-9428,2243,5844,402,-2286,-6100,-7746,9129,2150,-6347,6623,1321,-2324,-5480,-2996,-4079,7588,3998,8776,-6117,5330,-1776,2671,2419,6843,2273,-6035,2851,4455,2017,8589,6986,9536,6111,-2855,-318,-338,9801,-4188,-7365,-9728,-3029,-4844,-9114,8941,-5604,-1959,8646,-6144,-9165,-4298,-259,-9993,-7052,-3389,-9647,-8532,-8097,-7569,-5928,4015,4643,-8474,-5532,-6407,1597,3046,627,3044,-4409,-2860,1616,-9293,-5484,-6541,-536]
    # print   get_no(l)
    s = 'madamciviclevel'
    # print s[12]
    print len(s)
    print threePalindromicSubstrings(s)
