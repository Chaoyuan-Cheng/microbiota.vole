library(car)
setwd("C:\\Users\\40506\\OneDrive\\OneDrive_SYNC\\CODES\\0R")
f = read.csv("E:\\16SrRNA\\1our_data\\0布氏田鼠\\GLM_data-ASV.标准化2.csv")

f$diet = as.factor(f$diet)


#######################
# spearman

sp.fit = glm(spearman~GD
                   +diet
                   +contact
                   +shannon_mean
                   +sample_size
                   ,data = f,family = gaussian())

# CV
cv.fit = glm(CV_mean~GD
                   +diet
                   +contact
                   +shannon_mean
                   +sample_size
                   ,data = f,family = gaussian())
#

summary(sp.fit)
summary(cv.fit)

########################
# multimodel inference and model averaging
library(MuMIn)

options(na.action="na.fail") # the default argument is not proper here


dd <- dredge(
  sp.fit,      # model
  beta="none",      # standardize the estimates or not 
  evaluate=TRUE,    # evaluate and rank the models
  rank="AIC",

  )
print(dd, abbrev.names = TRUE)
write.csv(dd,"123.csv")

# Model averaging
avg <- model.avg(dd)

summary(avg)

confint(avg)

