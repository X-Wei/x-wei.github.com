title: (DeepLearning MOOC) Lesson 4: Deep Models for Text and Sequences     
Date: 2016-06-07           
Slug: dlMOOC_L4          
Tags: deep learning    
  
problems with text:   
  
1. often very rare word is important, e.g. *retinopathy*  
2. ambiguity: e.g. *cat* and *kitty*  
  
→ need a lot of labeled data ⇒ not realistic.   
⇒ **unsupervised learning**  
  
similar words appear in similar context.   
embedding: map words to small vectors  
![](../images/dlMOOC_L4/pasted_image.png)  
measure the closeness by cosine distance:   
![](../images/dlMOOC_L4/pasted_image003.png)  
  
word2vec  
--------  
initial: random vector  
→ train model to predict nearby word.   
![](../images/dlMOOC_L4/pasted_image001.png)  
![](../images/dlMOOC_L4/pasted_image004.png)  
pb: too many words in dictionary → softmax too slow  
⇒ random sample the non-target words   
![](../images/dlMOOC_L4/pasted_image005.png)  
  
![](../images/dlMOOC_L4/pasted_image006.png)  
  
  
tSNE  
----  
dimension reduction (not PCA) that preserves the neighborhood structure (close vector → close in 2d as well).   
![](../images/dlMOOC_L4/pasted_image002.png)  
  
  
RNN  
---  
treat varaible length sequences of words.   
use the current word (Xi) and the last prediction as input.   
![](../images/dlMOOC_L4/pasted_image007.png)  
  
backprop for RNN  
----------------  
apply highly correlated derivatives to W → not good for SGD.   
![](../images/dlMOOC_L4/pasted_image008.png)  
  
pb if we use highly correlated updates: grad either explod or it disappear quickly.   
  
![](../images/dlMOOC_L4/pasted_image009.png)  
  
fix grad-exploding: *clip*  
![](../images/dlMOOC_L4/pasted_image010.png)  
  
grad-vanishing: memory loss in RNN  
⇒ LSTM  
  
LSTM  
----  
in RNN: replace the NN by a LSTM cell  
![](../images/dlMOOC_L4/pasted_image011.png)  
  
![](../images/dlMOOC_L4/pasted_image013.png)  
represent the system with memory by a diagram with logical gates:   
  
![](../images/dlMOOC_L4/pasted_image014.png)  
change the decision variables to continous:  
![](../images/dlMOOC_L4/pasted_image012.png)  
a logistic regression in each gate: controls when to remember and when to forget things.   
![](../images/dlMOOC_L4/pasted_image015.png)  
<http://blog.csdn.net/dark_scope/article/details/47056361>  
![](../images/dlMOOC_L4/pasted_image024.png)  
![](../images/dlMOOC_L4/pasted_image023.png)  
  
  
regularization for LSTM:  
  
* L2 regularization: OK  
* dropout: OK when used for input/output (X and Y), but NOT use to the recurrent in/out.  
  
  
beam search  
-----------  
beam search is for *generating* sequences by RNN.   
  
Greedy approach: at each step, *sample* from the predicted distribution of the RNN.   
![](../images/dlMOOC_L4/pasted_image017.png)  
smarter approach:   
predict more steps and pick the seq with largest proba.   
![](../images/dlMOOC_L4/pasted_image018.png)  
pb with this: the number of possible seq grows exponentially   
⇒ just keep the few most promising seqs → "**Beam search"**  
![](../images/dlMOOC_L4/pasted_image016.png)  
  
seq to seq  
----------  
RNN: model to map vaiable length seq to fix-length vectors.   
![](../images/dlMOOC_L4/pasted_image021.png)  
Beam search: sequence generation (map fix-length vectors to seq)  
![](../images/dlMOOC_L4/pasted_image019.png)  
  
concat them together: seq to seq system  
![](../images/dlMOOC_L4/pasted_image022.png)  
  
e.g.   
translation, speech recognation, image captionning  
