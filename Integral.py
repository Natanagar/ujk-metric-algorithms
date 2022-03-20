import numpy as np
import sys

dataAmount = 1000;

f = open('dataOutput.txt','w')
for i in range(dataAmount):
    p = 1
    f.write('p−value: ' + str(p) + '\n')
    dimension = np.random.randint(low=1, high = 11)
    f.write('Dimension: ' + str(dimension ) + '\n')
    highX = 1000
    low_lim = highX * np.random.random_sample();
    print(low_lim)
    upper_lim = (highX - low_lim) * np.random.random_sample() + low_lim
    print(upper_lim)
    f.write( 'Xinterval: [' + str(low_lim ) + ',' + str(upper_lim ) + ']\ n')
    numPoints = np.random.randint(low=1, high = 1001)
    f.write('Sample Size: ' + str(numPoints) + '\n ' )
    APoints = np.random.randint(low=1, high = 1001)
    f.write('Set A:{ ')
    if dimension == 1:
        for i in range(APoints - 1):
            f.write(str((upper_lim - low_lim) * np.random.sample() + low_lim) + ', ')
            f.write(str((upper_lim - low_lim) * np.random.sample() + low_lim));
    else:
        for i in range(APoints):
            f.write('(')
            for j in range(dimension - 1 ):
                f.write(str((upper_lim - low_lim) * np.random.sample() + low_lim) + ', ');
                f.write(str((upper_lim - low_lim) * np.random.sample() + low_lim) + ')');
                if i != APoints - 1:
                        f.write(', ')
    f.write("} \n" )
    f.write( 'Set B: { ')
    BPoints = np.random.randint( low = 1, high=1001)
    if dimension == 1:
        for i in range(BPoints - 1):
            f.write(str((upper_lim - low_lim) * np.random.sample() + low_lim) + ", ")
            f.write(str((upper_lim - low_lim) * np.random.sample() + low_lim) + ")")
            if i != BPoints - 1:
                f.write(", ")
    f.write("} \n")
    confidence  = 0.05
    f.write("Confidence level: " + str(confidence) + "\n")
    f.write("\n")
f.close()


