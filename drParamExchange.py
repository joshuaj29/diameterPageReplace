#! python3
# TCT_2_Diam - takes TCT diameters and inserts them into kyocera diameter pages

import re



def main():
    # Path files for existing diameter tables
    # Old diameter tables
    btpoly = ('path to file/BTPOLY.txt')
    btpolyhc = ('path to file/BTPOLYHC.txt')
    fr4 = ('path to file/FR4.txt')
    fr4hc = ('path to file/FR4HC.txt')
    fr4mc = ('path to file/FR4MC.txt')
    #n13 = ('path to file/N13.txt')
    #n13hc = ('path to file/N13HC.txt')
    rogers = ('path to file/ROGERS.txt')
    rogershc = ('path to file/ROGERSHC.txt')
    teflon = ('path to file/TEFLON.txt')

    # New diameter tables
    ht500 = ('path to file/24730 TCS HT500 20210430.txt')
    ht750 = ('path to file/24730 TCS HT750 20210430.txt')
    ht1000 = ('path to file/24730 TCS HT1000 20210430.txt')
    ht1500 = ('path to file/24730 TCS HT1500 20210430.txt')
    poly300 = ('path to file/24730 TCS POLY300 20210630.txt')
    poly500 = ('path to file/24730 TCS POLY500 20210430.txt')
    poly1000 = ('path to file/24730 TCS POLY1000 20210430.txt')
    teflon300 = ('path to file/24730 TEFLON300 20210728.txt')
    teflon400 = ('path to file/24730 TCS TEFLON400 20210430.txt')
    teflon750 = ('path to file/24730 TCS TEFLON750 20210430.txt')
    slots = ('path to file/22380 UCY SLOT 20K-160K 20220322.txt')


    # TCT diameters to be added to new file
    TCTd = ['0.0059', '0.0071', '0.0079', '0.0098', '0.0118', '0.0138', '0.0157',
            '0.0177', '0.0197', '0.0210', '0.0225', '0.0236', '0.0240', '0.0250',
            '0.0256', '0.0260', '0.0310', '0.0315', '0.0350', '0.0354', '0.0360',
            '0.0390', '0.0394', '0.0410', '0.0413', '0.0420', '0.0453', '0.0469',
            '0.0492', '0.0625', '0.0785', '0.0787', '0.1015', '0.1040', '0.1043',
            '0.1200', '0.1201', '0.1260', '0.1280', '0.1285', '0.1437', '0.1440',
            '0.1949', '0.2067', '0.2461', '0.0180', '0.0320', '0.0465', '0.0512',
            '0.0669', '0.0781', '0.0145', '0.0200', '0.1299', '0.0430', '0.0433',
            '0.0380', '0.0091', '0.0400', '0.1358', '0.1360', '0.0550', '0.0551',
            '0.0591', '0.0595', '0.1870', '0.1875', '0.0472', '0.2205', '0.0748',
            '0.0374', '0.0945', '0.1378', '0.1405', '0.0236w1', '0.0280w1', '0.0595w1',
            '0.0689w1', '0.0760w1']


    # create new diameter pages using newParams function
    newParams(ht500, fr4hc, 'HT500.txt', TCTd, slots)
    newParams(ht750, fr4mc, 'HT750.txt', TCTd, slots)
    newParams(ht1000 ,fr4, 'HT1000 (FR4).txt', TCTd, slots)
    newParams(ht1000, fr4hc, 'HT1000 (FR4HC).txt', TCTd, slots)
    newParams(ht1000, fr4mc, 'HT1000 (FR4MC).txt', TCTd, slots)
    newParams(ht1500, fr4, 'HT1500.txt', TCTd, slots)
    newParams(poly300, btpolyhc, 'POLY300.txt', TCTd, slots)
    newParams(poly500, btpoly, 'POLY500.txt', TCTd, slots)
    newParams(poly1000, btpoly, 'POLY1000.txt', TCTd, slots)
    newParams(teflon300, teflon, 'TEFLON300 (TEFLON).txt', TCTd, slots)
    newParams(teflon300, rogershc, 'TEFLON300 (ROGERSHC).txt', TCTd, slots)
    newParams(teflon750, rogers, 'TEFLON750.txt', TCTd, slots)






class newParams:
    def __init__(self, tctDpage, kyoDpage, newFileName, TCTd, slots):
        TCTd = sorted(TCTd)
        self.reTools = re.compile('^(?:(C\d\.\d+|\d\.\d+)|(F\d+)|(S\d+(?:\.?))|(B\d+)|(H\d+)|(Z\d?(?:\.|)\d+)|(w\d)){1,7}')
        FaS = self.feedsNSpeeds(tctDpage, self.reTools, slots, TCTd)
        oldFaS = self.oldFeedsNSpeeds(kyoDpage, self.reTools)
        self.diamSwap(FaS, oldFaS)
        self.write2File(newFileName, oldFaS)


    def feedsNSpeeds(self, tctDpage, reTools, slots, TCTd):
        FaS = {}
        for line in TCTd:
            try:
                tGroups = reTools.search(line).groups()
            except AttributeError:
                continue
            if tGroups[6] == None:
                with open(tctDpage, 'r') as tctTXT:
                    for i in tctTXT:
                        try:
                            tctGroups = reTools.search(i).groups()
                        except AttributeError:
                            continue
                        if tGroups[0] == tctGroups[0][1:]:
                            diam = tGroups[0]
                            pmeter = i
                            
                            FaS.setdefault(diam, {})
                            FaS[diam] = str(pmeter)
                            break
                        else:
                            continue

            elif tGroups[6] == 'w1':
                with open(slots, 'r') as slotTXT:
                    for i in slotTXT:
                        try:
                            tctGroups = reTools.search(i).groups()
                        except AttributeError:
                            continue
                        if tGroups[0] == tctGroups[0][1:]:
                            diam = tGroups[0] + tGroups[6]
                            pmeter = i
                            
                            FaS.setdefault(diam, {})
                            FaS[diam] = str(pmeter)
                        else:
                            continue
        return FaS




    def oldFeedsNSpeeds(self, kyoDpage, reTools):
        oldFaS = {}
        with open(kyoDpage, 'r') as kyoTXT:
            for line in kyoTXT:
                try:
                    kGroups = reTools.search(line).groups()
                except AttributeError:
                    continue

                oldPmeter = line
                if kGroups[6] == None:
                    oldDiam = kGroups[0][1:]
                elif kGroups[6] == 'w1':
                    oldDiam = kGroups[0][1:] + kGroups[6]

                oldFaS.setdefault(oldDiam, {})
                oldFaS[oldDiam] = str(oldPmeter)
        return oldFaS





    def diamSwap(self, FaS, oldFaS):
        for diameter in oldFaS:
            for i in FaS:
                if diameter == i:
                    oldFaS[diameter] = FaS[diameter]
                    break
        return oldFaS




    def write2File(self, newFileName, oldFaS):
        with open(newFileName, 'w') as newFile:
            for line in oldFaS:
                newFile.write(oldFaS[line])




    
    
    



if __name__ == "__main__":
    main()
