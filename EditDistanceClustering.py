

# EditDistance

# X is numpy matrix format.

def normal_leven(str1, str2):
    len_str1 = len(str1) + 1
    len_str2 = len(str2) + 1
    # create the matrix
    matrix = [0 for n in range(len_str1 * len_str2)]
    #1st row
    for i in range(len_str1):
        matrix[i] = i
    # 1st column
    for j in range(0, len(matrix), len_str1):
        if j % len_str1 == 0:
            matrix[j] = j // len_str1
    # iterations
    for i in range(1, len_str1):
        for j in range(1, len_str2):
            if str1[i-1] == str2[j-1]:
                cost = 0
            else:
                cost = 1
            matrix[j*len_str1+i] = min(matrix[(j-1)*len_str1+i]+1,
                    matrix[j*len_str1+(i-1)]+1,
                    matrix[(j-1)*len_str1+(i-1)] + cost)
    return matrix[-1]  # print the last value
	
	
#DIY distanceFucntion (re-calculate the weights) 
def distfunc(x1,x2):
    #assume we have 4 variables for clustering, you can change by your own needs
    return 0.8*normal_leven(x1[0],x2[0])+0.7*normal_leven(x1[1],x2[1])+1.2*normal_leven(x1[2],x2[2])+2*normal_leven(x1[3],x2[3])
	
	
def randCent(matrix,k):
    #random choice K centroids:
    choice         = list(np.random.randint(len(matrix), size=k))
    centroids      = matrix[choice]
    return centroids
    
def KModes_changed(matrix, k, random_state=0,distMeas=distfunc, createCent=randCent,max_iters=10):
    m = np.shape(matrix)[0]
    print('-------------------start--------------------')
    for iters in range(max_iters):
        np.random.seed(random_state+iters)
        clusterAssment = np.mat(np.zeros((m,2))) #create mat to assign data points to a centroid
    #The first column stores index and the second column stores distance
        centroids = createCent(matrix, k)
        print('this is the {0}iterations，K centroids starting complete......'.format(iters+1))
        count=1
        clusterChanged = True
        lastcentroids = centroids.copy()
        while clusterChanged:
            clusterChanged = False
            for i in range(len(matrix)):  #for each data point assign it to the closest centroid
                minDist  = np.inf
                minIndex = -1
                for j in range(k):
                    distJI = distMeas(centroids[j,:],matrix[i,:])
                    if distJI < minDist:
                        minDist = distJI; minIndex = j
                if clusterAssment[i,0] != minIndex:
                    clusterChanged = True
                clusterAssment[i,:] = minIndex,minDist
            
            for cent in range(k):#recalculate centroids
                ptsInClust = matrix[np.nonzero(clusterAssment[:,0].A==cent)[0]]#get all the point in this cluster
                centroids[cent,:] = mode(ptsInClust).mode #assign centroid to mean 
            dist = sum(clusterAssment[:,1])
            
            print('Doing {0} iterations ,cost:{1}'.format(count,dist)) 
            count+=1
        #计算总dist
        print('Complete! The random_state is {0}'.format(random_state+iters))
        print('---------------------------------------------------')
        
    print('-------------------Good job !--------------------') 
    return centroids, clusterAssment
	
	

                
				
            
 
        
	
