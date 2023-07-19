import matplotlib.image
import cv2
import numpy as np
from sklearn.linear_model import RANSACRegressor
#import scipy

#def f(x,a,b):
#    return x*a+b

def getrawdata(videofilename):
    """
    Gets the location (in the horizontal direction) of the seed in each frame.
    
    Returns:
       raw -- the maximums of all the columns (smoothed) after difference operations etc.
       positions -- the raw position of the seed (two columns: first column: frame index; second column: position in pixels
       speed -- pixels per frame (fitted using RANSAC linear regression (avoids outliers).
    """
    checkplots = []
    cap = cv2.VideoCapture(videofilename)
    frame = None
    results = []
    count = 0
    raw = []
    for it in range(100000):
        oldframe = frame
        ret, frame = cap.read()
        if not ret: break
        frame = np.mean(frame.astype(float),2)
        if it%100==0: checkplots.append(frame.copy())
        if it>0:
            diff = (frame-oldframe)
            smoothdiff=(diff[:,3:]+diff[:,2:-1]+diff[:,1:-2]+diff[:,:-3])/4
            maxes = np.max(smoothdiff,0)
            raw.append(maxes)
    raw = np.array(raw)
    raw = raw[100:-100,:] #remove first and last 100 frames
    raw = (raw.T/np.mean(raw,1)).T
    idx = np.arange(len(raw))
    threshold = np.max(raw)/2#np.percentile(raw,99.9)
    positions = [[i,np.mean(np.where(r))] for i,r in enumerate(raw.T>threshold)]
    positions = np.array(positions)
    positions = positions[~np.isnan(positions[:,1]),:]
    
    #this version will be affected by outliers...
    #mean,cov = scipy.optimize.curve_fit(f, positions[:,0], positions[:,1])
    
    #using RANSAC
    #X = np.c_[np.ones_like(positions[:,0:1]),positions[:,0:1]]
    reg = RANSACRegressor(random_state=0).fit(positions[:,0:1], positions[:,1])   
    #from sklearn import linear_model
    #lr = linear_model.LinearRegression()
    #lr.fit(X, positions[:,1])
    #lr.coef_,reg.estimator_.coef_
    
    #bagging
    #gradients = []
    #for fitresample in range(1000):
    #    choice = np.random.choice(len(positions),10,True)
    #    grad,offset = np.polyfit(positions[choice,0], positions[choice,1],1)
    #    gradients.append(grad)
    #plt.hist(gradients,100);
    #np.median(gradients)

    #save check plot    
    
    startframe = reg.estimator_.intercept_
    speed = 1/reg.estimator_.coef_[0]
    
    try:
        a = 200+100*((startframe+(1/speed)*1920)//100)
        b = 100*(startframe//100)+200

        pic = []
        for f in np.arange(a,b,100):
            sli = int(speed*(f-100-startframe))
            print(sli,checkplots[int(f/100)][:,sli-30:sli+30].shape)
            pic.append(checkplots[int(f/100)][:,sli-30:sli+30])
        im = np.concatenate(pic,axis=1)
        matplotlib.image.imsave(videofilename+'.png', im)        
    except:
        print("Failed to generate check plot")
    #plt.imshow(im)


    
    return raw, positions, speed, startframe+100, (startframe+(1/speed)*1920)+100
