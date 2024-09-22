#Check dimention of the dataset
dim(State_Crime2012)

#View the dataset (V is capital)
View(State_Crime2012)

#Calculate the summery statistics
summary(State_Crime2012)

#report table with Table1: summery statistics.....
#gole is to reduce number of variables

#remove A1 category heading using r 
#removing the state header name, help in showing the state name on the graph
crime2012 <- data.frame(State_Crime2012, row.names = "State")

#Shows first 6 rows of data
head(crime2012)

#Shows first 6 rows of data
head(State_Crime2012)

dim(State_Crime2012)
dim(crime2012)

install.packages("stats")
library(stats)

# Perform Principal Component Analysis PCS
PCA <- princomp(crime2012, cor = TRUE)

summary(PCA)

# Variables no = PCA no
#Proportion of Variance check %
#take upto 80%

#check PC link to variable 

#correlation matrix, check highest correlation +ve and -ve
PCA$loadings

#PCA good for quantitative 

#For visualisation
install.packages("factoextra")
library("factoextra")

#Scree Plot with Elbow
fviz_eig(PCA)

fviz_pca_ind(PCA, col.ind = "cos2", # color by quality of representation 
             gradient.cols = c("blue","yellow","red"),
             repel = TRUE #avoids text overlapping
             )
#Present Principle component Scores
PCA$scores

#Scaling is reqired for clustering

crime12 <- scale(crime2012)
head(crime12)

#K-Means
#change the ceneters to increase the clusturing groups
km <- kmeans(crime12, centers = 2)
km

#find optimal number of clusters

fviz_nbclust(crime12, kmeans)

#Illustration of the clusters
fviz_cluster(km, crime12)

# Hierarchical clusturing using Ward's method
hc <- hclust(d = dist(crime12, method = "euclidean"),method = "ward.D")
hc

#plot the dendrogram
dendrogram <- as.dendrogram(hc)
plot(dendrogram) 

# Boarder around 2 clusters
rect.hclust(hc, k = 2, border = 1:5)

#color branches function

dendrogram_G <- color_branches(dendrogram, h = 5)
plot(dendrogram_G) 

install.packages("dendextend")
library("dendextend")

#Time Series Project, data over time 
# work with 1 Univariant

