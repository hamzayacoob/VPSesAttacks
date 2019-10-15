#This attack takes in the path of the wav file
#The time interval representation of the wav file (use scipy.io.wavfile.read)
#The window size of the attack
#The sample rate of the file
def TDIAttack(path, inputArray, windowSize, fs):
    n = int(len(inputArray)/windowSize)

    #Breaks array into buckets of elements
    #Each bucket has 'windowSize' amount of elements
    def createBuckets(arr, n):
        length = len(arr)
        return [ arr[i*length // n: (i+1)*length // n] 
                 for i in range(n) ]

    #Load audio file
    arr = np.copy(inputArray)
    
    #Store split array into variable
    splitArray = createBuckets(arr,n)

    l = list()

    for x in splitArray[:n]:
        #print(np.fliplr([x])[0])
        l.extend(np.fliplr([x])[0])
    
    #Stores the modified array and casts it as int
    data2 = np.asanyarray(l)
    #Ensures the file is of the right type otherwise errors occur
    data2= np.asarray(data2,dtype=np.int16)
    
    #How to store the new location of the wav file
    new_audio_path = path[0:-4]+''+str(fs)+'_TDI'+str(windowSize)+'.wav'
    
    return new_audio_path, data2