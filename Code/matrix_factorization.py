def matrix_factorization(R, P, Q, K, steps=1000, alpha=0.0002, beta=0.01):
    Q = Q.T
    e = 0
    iterate = 0
    target =100
    for step in xrange(steps):
       sumrating = 0
       for i in xrange(len(R)):
           for j in xrange(len(R[i])):
                if R[i][j] > 0:
                    eij = R[i][j] - np.dot(P[i,:],Q[:,j])
                    sumrating = sumrating + 1
                    for k in xrange(K):
                        P[i][k] = P[i][k] + alpha * (2 * eij * Q[k][j] - beta * P[i][k])
                        Q[k][j] = Q[k][j] + alpha * (2 * eij * P[i][k] - beta * Q[k][j])
       eR = np.dot(P,Q)
       e = 0
       for i in xrange(len(R)):
           for j in xrange(len(R[i])):
               if R[i][j] > 0:
                   e = e + pow(R[i][j] - np.dot(P[i,:],Q[:,j]), 2)

       e = pow(e/sumrating,0.5)

    return P, Q.T
