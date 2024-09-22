x=5
x
x^2
x**2
sqrt(4) #square root funtion 
x<-10 # <- is also considered as "="
x
x*2
y<-x*2 # Assigned value to y
y
z<-"Hi" # Assigned value to z
z
rm(y) # rm to remove the assigned value
y
x==10 # Logical Operation, checks if value is correct
x!=10 # Logical Operation, checks if value is correct != (Not Equal)
x<=10 # Logical Operation, checks if value is correct
x>=10 # Logical Operation, checks if value is correct
Salary <- c(50,100,64,81,43) # Assigning value to Salary
Salary
New_salary <- Salary+(Salary*0.01) # Assigning value to New_salary
New_salary
length(Salary)
length(New_salary)
Gender<-c("M","F","F","M","F")
Gender
new_data<-data.frame(Salary,Gender)
dim(new_data)
new_data[1,] #1st row and column
new_data[,1] #
new_data[1,1]
new_data[c(1,5),] # values of row 1 and 5
new_data[,c(2)] 
data5<-new_data[c(1,2,3),] # created new data file using new_data
