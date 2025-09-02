import numpy as np

# 1. Define sigmoid activation (In case you have tried different activation function code that here instead of sigmoid)
def sigmoid(z):
    # implement sigmoid
    return 1/(1+np.exp(-z))

def softmax(z):
    exp_z = np.exp(z - np.max(z, axis=1, keepdims=True))  # stability trick
    return exp_z / np.sum(exp_z, axis=1, keepdims=True)

# 2. Input (Student Profile)
X = np.array([[8,90, 85],[2,10,20]])   # Fill with your chosen 3 parameters [e.g. - study_hours, attendance, quiz_score]

# 3. Initialize weights and biases (Set your own weights and biases!)
# Hidden layer
W1 = np.eye(3)
b1 = np.array([0.5,0.25,0.25])

# Output layer (2 neurons: Pass, Fail)
W2 = np.array([[0.6,0.2,0.2],[0.4,0.3,0.3]])
b2 = np.array([0.5,0.5])

# 4. Forward Propagation
# Input → Hidden
Z1 = np.dot(X,W1.T)+b1  # dot product + bias
A1 = sigmoid(Z1)  # apply activation magic

# Hidden → Output  (Try thinking this on your own)
Z2 =np.dot(A1,W2.T)+b2
A2 =softmax(Z2)

#if A2>0.5:
#    A2='PASS'
#else:
#    A2='FAIL'
#5. Final Prediction
#print("Oracle prediction (Pass, Fail):", A2)

pred_labels = np.where(A2[:,0] > A2[:,1], "PASS", "FAIL")
print("Final Oracle verdict:", pred_labels)

#TRY VERIFYING THE RESULTS WITH YOUR WEIGHTS AND BIASES THAT YOU HAVE TRIED ON PEN PAPER!!