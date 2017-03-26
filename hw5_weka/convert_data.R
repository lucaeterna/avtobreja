setwd('/home/lux/Documents/АвтОбрЕЯ/4course/weka/')

data <- read.csv('oborot_features.csv', stringsAsFactors = FALSE)
data$prevtag <- as.factor(data$prevtag)
data$nexttag <- as.factor(data$nexttag)
data$class <- as.factor(data$class)

library('foreign')


write.arff(data, 'oborot_str.arff', relation='oborot_str')
