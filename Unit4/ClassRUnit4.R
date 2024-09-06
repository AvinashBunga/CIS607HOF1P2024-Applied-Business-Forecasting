
#Delete DNS values in the dataset
Deca <- Decathlon[!grepl("DNS", Decathlon$m1500),]

#Delete NS values in the dataset
Deca <- Deca[!grepl("NM", Deca$PV),]

#Check no of rows and columns in the data "Decathlon"
dim(Decathlon)

#Check no of rows and columns in the data "Deca"
dim(Deca)

#View the data set "Deca"
View(Deca)

#Convert Char to String in full data
Deca1 <- as.data.frame(sapply(Deca, as.numeric))

#Check structure of Full Data
str(Deca1)

#Scaling data is important to make sure all the numeric values are in the same range

Deca2 <- scale(Deca1[, 5:14])

View(Deca2)

# Summary before scaling the data
summary(Deca1[, 4:14])

#Determin Number Of Factors

library("psych")
#Scree plot for scaled data "Deca2"
scree(Deca2)

#Extract and Rorate Factors
fa <- factanal(Deca2, factors = 4)
fa$loadings

#Visualize the Factor Model
loads <- fa$loadings
fa.diagram(loads)

#Cor to check which to select 
#do research of corelating to understand how to select data

#Grapging Factor 1 vs Factor 2

loads1 <- fa$loadings[,1:2]
                      
plot(loads1, type = "n")

text(loads1, labels=names(Decathlon[, 5:14]))


#Project Forcasting 
#Data time and veriable
#ex weather, temp each hour 
# univatire TS 
#Time,Var
#Time can like each min each hour each year 
#Gold price every day, 
#Stock price every min
#Project Praposal, 2 page, problem being solved, explain the dataset 
#Find dataset
# No kaggle dataset 

