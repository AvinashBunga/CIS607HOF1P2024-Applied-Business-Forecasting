
load("/Users/avinash/Desktop/CIS/CIS607/Unit6/titanic.rdata")

# Assigning name to the data
Titanic1 <- titanic.raw

# First Few Rows of data
head(Titanic1)

Titanic1


#gives frequency table 
summary(Titanic1)

#Random Sample
sample <- sample(nrow(Titanic1), size = 0.9*nrow(Titanic1), replace = FALSE)
train <- Titanic1[sample, ]
test <- Titanic1[-sample, ]

head(train)
tail(train)

head(test)
tail(test)

summary(test)
summary(train)

length(sample)
#number of observations
dim(test)
dim(train)

install.packages("rpart")
library("rpart")

Tree_model1 <- rpart(Survived ~ Sex, data = train)
Tree_model1

table(train$Survived)

install.packages("rpart.plot")
library("rpart.plot")

rpart.plot(Tree_model1, extra = 104)

summary(Tree_model1)

Tree_model12 <- rpart(Survived ~ ., data = train)
Tree_model12

#Tree_model12 <- rpart(Survived ~ Class + Sex + Age, data = train)
#Tree_model12

rpart.plot(Tree_model12, extra = 104)

summary(Tree_model12)

#Accoring to thew result sex is the most important part
#Variable importance
#Sex Class   Age 
#73    23     5 

#How to evaluate our model
prediction <- predict(Tree_model12, test, type = 'class')
Table2 <- table(test$Survived, prediction)
Table2

Table2 <- table(test$Survived, prediction)
Table2

conf.matrix <- prop.table(Table2)
conf.matrix

rownames(conf.matrix) <- c("Died", "Survived")
colnames(conf.matrix) <- c("Predicted Died", "Predicted Survived")
conf.matrix


# Calculate model accuracy
Accuracy <- sum(diag(Table2)) / sum(Table2)
Accuracy

#Check ARIMA model for project
#histogram
#summary min max (Table)