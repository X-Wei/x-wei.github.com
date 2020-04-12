Title: [XCS224N] Lecture 4 – Backpropagation
Date: 2020-03-21
Slug:  xcs224n-lecture4
Tags: deep learning
Series: XCS224N: NLP with deep learning

More Matrix Gradients
---------------------

![](../images/xcs224n-lecture4/pasted_image.png)

![](../images/xcs224n-lecture4/pasted_image001.png)

![](../images/xcs224n-lecture4/pasted_image002.png)
 ⇒ 
![](../images/xcs224n-lecture4/pasted_image003.png)

![](../images/xcs224n-lecture4/pasted_image004.png)

Deriving Gradients wrt Words
----------------------------

![](../images/xcs224n-lecture4/pasted_image005.png)

**pitfall** in tetraining word vectors: 
if some word is not in training data, but other synonyms are present ⇒ only the synonyms word vectors are moved

![](../images/xcs224n-lecture4/pasted_image006.png)

takeaway: 

![](../images/xcs224n-lecture4/pasted_image007.png)

Backpropagation
---------------
backprop:

* apply (generalized) chain rule
* re-use shared stuff

### computation graph

![](../images/xcs224n-lecture4/pasted_image009.png)

⇒ Go backwards along edges, pass along **gradients**

![](../images/xcs224n-lecture4/pasted_image010.png)

receive upstream grad => compute downstream grad

![](../images/xcs224n-lecture4/pasted_image012.png)

for node with multiple inputs:

![](../images/xcs224n-lecture4/pasted_image027.png)

![](../images/xcs224n-lecture4/pasted_image014.png)

More on Backpropagation
-----------------------

![](../images/xcs224n-lecture4/pasted_image015.png)

**intuition:**

* plus( `+` ) *distributes* upstream grad

  ![](../images/xcs224n-lecture4/pasted_image016.png)

* `max`*routes* upstream grad

  ![](../images/xcs224n-lecture4/pasted_image017.png)

* multiply( `*` ) *switches* the upstream grad

  ![](../images/xcs224n-lecture4/pasted_image018.png)

efficency: compute shared part once

![](../images/xcs224n-lecture4/pasted_image019.png)

### Backprop in general computation graph

comput-graph is a DAG  ⇒ topological sort

* **Fprop**: visit nodes in topological
* **Bprop**: in reverse topological order

![](../images/xcs224n-lecture4/pasted_image020.png)

![](../images/xcs224n-lecture4/pasted_image022.png)

Complexity = **O(n)**
Automatic Differentiation: symbolic computation on the symbolic expression of Fprop.
Moden DL framework: must provide the Fprop/Bprop formular for each node.

Backprop Implementations
------------------------

![](../images/xcs224n-lecture4/pasted_image023.png)

for each gate, impl the forward/backward API:

![](../images/xcs224n-lecture4/pasted_image025.png)

**Numeric Gradient**
For checking if the forward/backward impl is correct
e.g.check

![](../images/xcs224n-lecture4/pasted_image026.png)

(note: use *two-sided* gradient checks)

Regularization
--------------
Regularization term added to loss func to prevent overfitting:

![](../images/xcs224n-lecture4/pasted_image028.png)

![](../images/xcs224n-lecture4/pasted_image029.png)

Vectorization/tensorization
---------------------------
avoid forloops, use matrix multiplication instead.

![](../images/xcs224n-lecture4/pasted_image030.png)

Nonlinearities
--------------

![](../images/xcs224n-lecture4/pasted_image031.png)

tanh is recaled and shifted of sigmoid:
`tanh(x) = 2 * sigmoid(2x) - 1` 

new world activation func:

![](../images/xcs224n-lecture4/pasted_image032.png)

Parameter Initialization
------------------------
Initialize the weights to *small, random* values ⇒ **break the symmetry.**

* Init bias to 0
* Init all other weights to Uniform(-r, r).
* **Xavier initialization**: *variance inverse-proportional to sum of prev&next layer size*

  ![](../images/xcs224n-lecture4/pasted_image033.png)

Optimizers and Learning Rates
-----------------------------
Usually simple SGD works fine, but needs to tune the learningrate (*lr*).
**adaptive optimizers**: *per-parameter* learning rate.

![](../images/xcs224n-lecture4/pasted_image034.png)

**learning rate:** 

* try with powers of 10
* learningrate-decay: 

  ![](../images/xcs224n-lecture4/pasted_image035.png)

  (*epoch* = full pass over the training data)
