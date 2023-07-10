###α多样性计算
#清除所有变量

rm(list=ls())
#加载vegan包
library(vegan)
library(stringr)

#读入物种数据
idf = read.csv("E:\\16SrRNA\\3multi\\project_id.csv",header = T,sep = ",")
idlist = idf$"id"

# 循环部分
for (i in idlist){
otu<-read.csv(str_glue('E:\\16SrRNA\\3multi\\ASV_used\\{i}_feature.used.tsv'),header = TRUE,row.names = 1,check.names=F,sep = "\t")

#Shannon 指数
Shannon<-diversity(otu, index = "shannon", MARGIN = 2, base = exp(1))
#Simpson 指数
Simpson<-diversity(otu, index = "simpson", MARGIN = 2, base = exp(1))
#Richness 指数
Richness <- specnumber(otu,MARGIN = 2)

#合并
index<-as.data.frame(cbind(Shannon,Simpson,Richness))

#转置物种数据
totu<-t(otu)
totu<-ceiling(as.data.frame(t(otu)))

#多样性指数
obs_chao1_ace<-t(estimateR(totu))
obs_chao1_ace<-obs_chao1_ace[rownames(index),]
index$Chao1<-obs_chao1_ace[,2]
index$Ace<-obs_chao1_ace[,4]
index$Sobs<-obs_chao1_ace[,1]
index$Pielou <- Shannon / log(Richness, 2)
index$Goods_coverage <- 1 - colSums(otu == 1) / colSums(otu)

#合并、导出数据

write.table(cbind(sample=c(rownames(index)),index),str_glue('E:\\16SrRNA\\3multi\\diversity\\{i}_diversity.csv'),row.names = F,sep = ',',quote = F)

}
