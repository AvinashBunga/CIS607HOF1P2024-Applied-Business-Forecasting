View(mtcars)
plot(mtcars$mpg,mtcars$wt)
plot(mtcars$wt,mtcars$mpg, xlab = "Weight", ylab = "MPG")

cor(mtcars$wt, mtcars$mpg)
# person is default

cor(mtcars$wt, mtcars$mpg, method = "pearson")

cor(mtcars$wt, mtcars$mpg, method = "kendall")

cor(mtcars$wt, mtcars$mpg, method = "spearman")

cor(mtcars$wt, mtcars$mpg, method = "kendall")

cor(mtcars$wt, mtcars$mpg, method = "k")

cor(mtcars$wt, mtcars$mpg, method = "spearman")

cor(mtcars$wt, mtcars$mpg, method = "s")

hist(mtcars$mpg)

hist(mtcars$wt)
# To check Normal or Not
qqnorm(mtcars$mpg)

qqnorm(mtcars$wt)

qqline(mtcars$mpg)
# Normality Not Met move to "spearman"
qqline(mtcars$wt)

install.packages("psych")

table1 <- table(mtcars$vs, mtcars$am)

phi(table1)
# Week corelation between vs and am

#Scatter plot, 4 variables 
pairs(~ mpg + wt + cyl + hp, data = mtcars)

cor(mtcars[, c("mpg", "wt", "hp", "cyl")])

cor(mtcars[c("mpg", "wt", "hp", "cyl")])

cor(mtcars[,c("mpg", "wt", "hp", "cyl")])

names(mtcars)

lm(mpg ~ cyl+disp+hp+drat+wt+qsec+vs+am+gear+carb, data = mtcars)

Full_model <- lm(mpg ~ cyl+disp+hp+drat+wt+qsec+vs+am+gear+carb, data = mtcars)

summary(Full_model)

