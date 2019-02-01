# EditDistanceClustering

This repository provides a new clustering method based on Edit Distance and Kmeans algorithms. This algotithm is suitable for those variables which are string format and literally correlated. For example, 

customerA has features: {area: '华东区'}
customerB has features: {area: '西华北'}
customerC has features: {area: '华南区'}

P.S.: '华东区', '西华北' and '华南区' are area in China. 

Edit Distance can be presented as :


D(i,j) = i    if j=0 ;
D(i,j) = j    if i=0 ;
D(i,j) = min(D(i-1, j) +1, D(i,j-1)+1,  D(i-1,j-1)+[A[i]!=B[j])  otherwise ;
       

Therefore the distance(D) betweeh A and C is 1; D(A,B) = 3 D(A,C) =3. We can map the original area of customer into certain words such that they have a clear literal distance which is also correlated with their geographical location.

Based on this intuition, the algorithm run as follow processing:

(i)   random chooce K centroids.
(ii)  calculate Edit Distance between all data points and centroids assign them into the nearest centroids.
(iii) rebuild the centroilds based on the mode of group.
(iv)  repeate (ii) and (iii) until doesn't move or max_iters, calculate the overall cost.
(v)   repeate (i) to (v) serveral times, use the lowest-cost exmperiment as our clustering result.

Becieds, you can give a customerized weighted for distance function if the importance of the variables is not the same.

