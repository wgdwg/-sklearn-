# -sklearn库的使用
在使用sklearn库之前，我们先看一下这个库的结构，该库经常用于监督学习和无监督学习，sklearn共分为6大部分，分别用于完成分类任务，回归任务，聚类任务，降维任务，模型选择以及数据的预处理。
库的算法主要有四类：分类，回归，聚类，降维。其中：
常用的回归：线性、决策树、SVM、KNN ；集成回归：随机森林、Adaboost、GradientBoosting、Bagging、ExtraTrees
常用的分类：线性、决策树、SVM、KNN，朴素贝叶斯；集成分类：随机森林、Adaboost、GradientBoosting、Bagging、ExtraTrees
常用聚类：k均值（K-means）、层次聚类（Hierarchical clustering）、DBSCAN
常用降维：LinearDiscriminantAnalysis、PCA
我们利用机器学习库sklearn中训练好的模型去计算参数w,b，然后带入求出损失函数，使得损失函数最小，拟合的更好。
