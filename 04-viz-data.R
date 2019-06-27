rm(list=ls())
data = read.csv('./data/jPOST-species-info.csv')

tb_jPOST = data.frame(rev(sort(table(data$Species.Name))))
colnames(tb_jPOST)[1] <- 'Species'

write.csv(
    tb_jPOST,
    './data/jPOST-data-statistics-24-06-19.csv',
    row.names = FALSE)
    
library(ggplot2)
p = ggplot(tb_jPOST[1:10,], aes(x = Species, y = Freq)) +
    geom_bar(stat='identity') +
    ylab('# jPOST projects') + 
    ggtitle('Top 10 species protemics data in jPOST database') +
    theme(axis.text.x = element_text(angle=60,vjust=1,hjust=1))
    
png('./figures/Figure-xx.png',width=900,height=1000,res=200)
p
dev.off()