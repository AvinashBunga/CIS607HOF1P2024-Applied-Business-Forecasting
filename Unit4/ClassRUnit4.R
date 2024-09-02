
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