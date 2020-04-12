Title: [XCS224N] Lecture 3 – Neural Networks
Date: 2020-03-21
Slug:  xcs224n-lecture3
Tags: deep learning
Series: XCS224N: NLP with deep learning

This week: neural net fundamentals

Classification Setup and Notation
---------------------------------
training data:

![](../images/xcs224n-lecture3/pasted_image.png)

### softmax classifier

(linear classifier — hyperplane): 

![](../images/xcs224n-lecture3/pasted_image001.png)

ith row of the param W: weight vector for class i to compute logits: 

![](../images/xcs224n-lecture3/pasted_image002.png)

prediction = softmax of f_y:

![](../images/xcs224n-lecture3/pasted_image003.png)

### cross-entropy

goal: for (x, y), maximize p(y|x)
⇒ loss for (x, y) = -log p(y|x)

![](../images/xcs224n-lecture3/pasted_image004.png)

![](../images/xcs224n-lecture3/pasted_image005.png)

in our case, the truth distribution is `one-hot` , i.e.p = [0, 0, ... , 1, ... 0]
⇒ cross entropy H = - sum{log q(y|x), for all x, y}

loss for all training data = averaging the losses:

![](../images/xcs224n-lecture3/pasted_image006.png)

where the logits vector `f` is:

![](../images/xcs224n-lecture3/pasted_image007.png)

Neural Network Classifier
-------------------------
softmax or SVM or other linear models are not powerful enough
⇒ NN to learn nonlinear decision boundaries

![](../images/xcs224n-lecture3/pasted_image008.png)

in NLP:
learn both *model parameters* ( `W` ) and *representations* (wordvecs `x` )

![](../images/xcs224n-lecture3/pasted_image010.png)

artificial neuron: `y=f(Wx)` , where f is nonlinear activation func.

![](../images/xcs224n-lecture3/pasted_image011.png)

when f = sigmoid = `1/(1+exp(-x))` , the neuron is binary logistic regression unit.

A neural network = running *several logistic regressions* at the same time

![](../images/xcs224n-lecture3/pasted_image013.png)

matrix notation: 

![](../images/xcs224n-lecture3/pasted_image014.png)

Without non-linearities *f()*, deep neural networks can’t do anything more than a linear transform.

Named Entity Recognition (NER)
------------------------------
task: find and classify names in text

![](../images/xcs224n-lecture3/pasted_image015.png)

*BIO encoding*: 

![](../images/xcs224n-lecture3/pasted_image016.png)

Binary Word Window Classification
---------------------------------
Classify a word in its *context* window of neighboring words.
simple idea: concat all context words

![](../images/xcs224n-lecture3/pasted_image017.png)

Binary classification with unnormalized scores(2008&2011): 
build *true window* and *corrupted windows*.

![](../images/xcs224n-lecture3/pasted_image020.png)

feed-forward computation:

![](../images/xcs224n-lecture3/pasted_image021.png)

intuition: middle layer learns *non-linear interactions* between words:
example: only if “*museums*” is first vector should it matter that “*in*” is in the second position.

max-margin loss: let true window score be larger (by at leaset delta=1)than the corrupted window score.

![](../images/xcs224n-lecture3/pasted_image022.png)

__QUESTION: why we can use SGD when continuous?__

SGD:

![](../images/xcs224n-lecture3/pasted_image023.png)

Computing Gradients by Hand
---------------------------
multivariable derivatives / matrix calculus

* *when f is from Rn → R1, ***Gradient**=vector of partial derivatives 

![](../images/xcs224n-lecture3/pasted_image024.png)

* *when f is from Rn → Rm, ***Jacobian** is an *m x n* matrix of partial derivatives 

![](../images/xcs224n-lecture3/pasted_image025.png)

**chain rule**: multiply the Jacobians

![](../images/xcs224n-lecture3/pasted_image026.png)

⇒ the nonlinear (activation) function **h** is *element-wise*, Jacobian of **h** is *diagonal:*

![](../images/xcs224n-lecture3/pasted_image028.png)

⇒ other Jacobians:

![](../images/xcs224n-lecture3/pasted_image029.png)

![](../images/xcs224n-lecture3/pasted_image030.png)

Gradients in Neural Network
---------------------------
notation:

![](../images/xcs224n-lecture3/pasted_image033.png)

⇒ Apply the chain rule with Jacobian/grad formulars from last section:

![](../images/xcs224n-lecture3/pasted_image031.png)

![](../images/xcs224n-lecture3/pasted_image032.png)

![](../images/xcs224n-lecture3/pasted_image034.png)

⇒ extract the common part, call it **local error signal**:

![](../images/xcs224n-lecture3/pasted_image035.png)

⇒

![](../images/xcs224n-lecture3/pasted_image036.png)
