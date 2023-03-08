#! python3
# TCT_2_Diam - takes TCT diameters and inserts them into kyocera diameter pages


# Path files for existing diameter tables
# Kyocera diameter tables
btpoly = ('C:/Users/joshuaj/Documents/Drilling/Engineering/Old_Cut_Data/B_valueChange/BTPOLY.txt')
btpolyhc = ('C:/Users/joshuaj/Documents/Drilling/Engineering/Old_Cut_Data/B_valueChange/BTPOLYHC.txt')
fr4 = ('C:/Users/joshuaj/Documents/Drilling/Engineering/Old_Cut_Data/B_valueChange/FR4.txt')
fr4hc = ('C:/Users/joshuaj/Documents/Drilling/Engineering/Old_Cut_Data/B_valueChange/FR4HC.txt')
fr4mc = ('C:/Users/joshuaj/Documents/Drilling/Engineering/Old_Cut_Data/B_valueChange/FR4MC.txt')
n13 = ('C:/Users/joshuaj/Documents/Drilling/Engineering/Old_Cut_Data/B_valueChange/N13.txt')
n13hc = ('C:/Users/joshuaj/Documents/Drilling/Engineering/Old_Cut_Data/B_valueChange/N13HC.txt')
rogers = ('C:/Users/joshuaj/Documents/Drilling/Engineering/Old_Cut_Data/B_valueChange/ROGERS.txt')
rogershc = ('C:/Users/joshuaj/Documents/Drilling/Engineering/Old_Cut_Data/B_valueChange/ROGERSHC.txt')
teflon = ('C:/Users/joshuaj/Documents/Drilling/Engineering/Old_Cut_Data/B_valueChange/TEFLON.txt')

# TCT diameter tables
ht500 = ('C:/Users/joshuaj/Documents/Drilling/Engineering/TCT Drill Parameters/24730 TCS HT500 20210430.txt')
ht750 = ('C:/Users/joshuaj/Documents/Drilling/Engineering/TCT Drill Parameters/24730 TCS HT750 20210430.txt')
ht1000 = ('C:/Users/joshuaj/Documents/Drilling/Engineering/TCT Drill Parameters/24730 TCS HT1000 20210430.txt')
ht1500 = ('C:/Users/joshuaj/Documents/Drilling/Engineering/TCT Drill Parameters/24730 TCS HT1500 20210430.txt')
poly300 = ('C:/Users/joshuaj/Documents/Drilling/Engineering/TCT Drill Parameters/24730 TCS POLY300 20210630.txt')
poly500 = ('C:/Users/joshuaj/Documents/Drilling/Engineering/TCT Drill Parameters/24730 TCS POLY500 20210430.txt')
poly1000 = ('C:/Users/joshuaj/Documents/Drilling/Engineering/TCT Drill Parameters/24730 TCS POLY1000 20210430.txt')
teflon300 = ('C:/Users/joshuaj/Documents/Drilling/Engineering/TCT Drill Parameters/24730 TEFLON300 20210728.txt')
teflon400 = ('C:/Users/joshuaj/Documents/Drilling/Engineering/TCT Drill Parameters/24730 TCS TEFLON400 20210430.txt')
teflon750 = ('C:/Users/joshuaj/Documents/Drilling/Engineering/TCT Drill Parameters/24730 TCS TEFLON750 20210430.txt')


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
        '0.0591', '0.0595', '0.1870', '0.1875', '0.0472', '0.2205', '0.0748']
            

def newParams(tctDpage, kyoDpage, newFileName):
    FaS = {}
    tctTXT = open(tctDpage, 'r')
    kyoTXT = open(kyoDpage, 'r')
    
    for line in tctTXT:
        for i in TCTd:
            if line[1:7] == i:
                diam = line[1:7]
                pmeter = line
                
                FaS.setdefault(diam, {})
                FaS[diam] = str(pmeter)
        
    
    oldFaS = {}
    
    for line in kyoTXT:
        for i in TCTd:
            if line[-3:-1] == 'w1':
                oldDiam = line[1:7] + line[-3:-1]
                oldPmeter = line
                
            else:
                
                oldDiam = line[1:7]
                oldPmeter = line
                
            oldFaS.setdefault(oldDiam, {})
            oldFaS[oldDiam] = str(oldPmeter)
            
            
    for diameter in oldFaS:
        for i in TCTd:
            if diameter == i:
                oldFaS[diameter] = FaS[diameter]
    
    
    newFile = open(newFileName, 'w')
    for line in oldFaS:
        newFile.write(oldFaS[line])
    
    
    tctTXT.close()
    kyoTXT.close()
    newFile.close()
    
    
# create new diameter pages using newParams function
newParams(ht500, fr4hc, 'HT500.txt')
newParams(ht750, fr4mc, 'HT750.txt')
newParams(ht1000 ,fr4, 'HT1000 (FR4).txt')
newParams(ht1000, fr4hc, 'HT1000 (FR4HC).txt')
newParams(ht1000, fr4mc, 'HT1000 (FR4MC).txt')
newParams(ht1500, fr4, 'HT1500.txt')
newParams(poly300, btpolyhc, 'POLY300.txt')
newParams(poly500, btpoly, 'POLY500.txt')
newParams(poly1000, btpoly, 'POLY1000.txt')
newParams(teflon300, teflon, 'TEFLON300 (TEFLON).txt')
newParams(teflon300, rogershc, 'TEFLON300 (ROGERSHC).txt')
newParams(teflon750, rogers, 'TEFLON750.txt')


