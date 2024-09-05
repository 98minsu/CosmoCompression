# Welcome to CosmoCompression

This is a repository of implementation examples for the dimensionality reduction methods discussed in Dimensionality Reduction Techniques for Statistical Inference in Cosmology (arXiv:2409.02102)

# Contents
(All data vectors provided in this repository for demonstration purposes are weak lensing second moment data vectors generated from N-body simulations)
- MOPED.npz contains simulated data vectors required to compute fiducial covariance matrices and parameter derivatives.
- samples.npz contains parameter samples ($S_8, \Omega_m, w_0, \eta_{\rm IA}, A_{\rm IA}, \Omega_b, n_s, h$, shear callibration, and redshift callibration; 16 parameters total) and corresponding simulated data vectors.
- notebook.ipnyb contains commented examples of implementations of PCA, PCA-f, MOPED, e-MOPED, CCA, and NN-MSE with Optuna hyperparameter tuning as discussed in arXiv:2409.02102.
- _0.db is the sqlite database maintained by Optuna during hyperparameter tuning.
- _optuna_0.npy is a part of the compressed data vector using NN-MSE after hyperparameter tuning.

# More on notebook.ipnyb

The 6 main compression methods compared and commented on in the paper are demonstrated here. However, the SBI is not carried out and left as an excercise to the reader. Code to produce Figure 9 of arXiv:2409.02102 is provided to examine the correlation matrix of the compressed data vectors, and their cross-correlation to the parameters. From this plot one can make an informed estimate of which method will be the most effective. Effective compression for SBI will produce  compressed data vector components that are uncorrelated to each other and highly correlated to the parameters of interest in constraining.

PCA and PCA-f the eigenvalue plots demonstrate which components are actually useful with PCA and the fact that PCA-f components are all noise dominated. With MOPED and e-MOPED we examine the claim that MOPED conserves Fisher information and diagonalizes the fiducial covariance matrix. With CCA, a plot of the mutual information between the compressed data vector component and the 16 parameters shows which components are the most important. NN-MSE requires hyperparameter tuning for the inference of each of the 16 parameters, and the example given is only for the first parameter ($S_8$). A plot compares the real and predicted $S_8$ values from the data vectors, and shows that neural networks are decent at estimating $S_8$ from the weak lensing second moment data vectors.

# Requirements 

- Generally
  - matplotlib
- Linear Methods
  - numpy, scipy
- NN-MSE
  - tensorflow, optuna



Author: Minsu Park
