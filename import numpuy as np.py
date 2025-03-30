import numpuy as np
def gradient_descent(x,y):
 m_cuur=b_curr=0
 iteration=1000
 n=len(x)
 learnin_rate=0.001
 for i in range(iteration):
        y_predicted=m_curr*x+b_curr
        md=-(2/n)*sum(x*(y-y_predcted))
        bd=-(2/n)*sum(y-y_predicted)
        m_curr=m_curr-learnin_rate*md
        b_curr=b_curr-learning_rate*bd
        print("m {},b {},cost {},iteration {}".format(m_curr,b_curr,i))
x=np.array([1,2,3,4,5])
y=np.array([5,7,9,11,13])

gradient_decent(x,y)
