# K-Means-Clustering
## 簡介
* k-means是**一種「聚類」的非監督式學習演算法**，根據**相似性原則**，將具有較高相似度的數據對象劃分至同一類
* k-means以**數據間的距離作為相似性則的度量標準**，越小，則數據的相似性越高，越有可能被分在同一類。
* 衡量「距離」方法有很多種，如以下三類，而k-means最常使用「Euclidean Distance」：
  * Minkowski Distance  
  
       <img src="https://render.githubusercontent.com/render/math?math=d =\root n \of {\sum_{i=1}^{p}|x_i%2Dy_i|^ n}">  
  
  * Euclidean Distance (公式一n=2)
  
       <img src="https://render.githubusercontent.com/render/math?math=d =\sqrt {\sum_{i=1}^{p}|x_i%2Dy_i|^ 2}"> 
  
  * CityBlock Distance (公式一n=1)
  
       <img src="https://render.githubusercontent.com/render/math?math=d = \sum_{i=1}^{p}|x_i%2Dy_i|"> 
  
* 算法中的k代表類別數，means代表同類內數據的均值（均值用來表示該類的群心），因此，k-means又稱為k-均值算法。

* 聚類與分類最大的區別在於：
  * 「聚類為非監督式學習」，即待處理數據對像沒有任何先驗知識
  
  * 「分類為監督式學習」，即存在有先驗知識的訓練數據集。

## 演算法步驟
  1. 首先输入 k 值，即希望透過聚類( clusting )來分成 k 組 
  
  2. 從數據集中"隨機"選取 k 個數據點當作初始質心( 群心 ) 
  
  3. 計算每個點到聚類中心的距離，將每個點聚類到離該點最近的聚類中心。
  
  4. 重新計算每個聚類中所有點的坐標平均值，並將其作為新的聚類中心

  5. 反覆執行(2)、(3)，直到聚類中心點不再變化或變化很小為止。
        
## 優缺點分析
 :heart:  優點
 1. 簡單易實現
 
 2. 類別密集，效果更佳
 
 3. 對大數據集有較高的效率並且是可伸縮性的
 
 4. 時間複雜度近於線性 - O(n×k×t) ，其中n代表數據集中對象的數量，t代表著算法迭代的次數，k代表著類別的數目
 
 :black_heart:  缺點
 1.  K 值的選定是非常難以估計的。很多時候，事先並不知道給定的數據集應該分成多少個類別才最合適
 
 2. **初始聚類中心的選擇對聚類結果有較大的影響**，一旦初始值選擇的不好，可能**無法得到有效的聚類結果**
 
 3. 當數據量非常大時，演算法的時間開銷是非常大的。所以需要對算法的時間複雜度進行分析、改進，提高算法應用範圍
 
## 演算法改進
## 使用範例圖
![](https://i.imgur.com/qXIXrpY.png)
