# comment.char = "" hast to be set due to # char in C# 
tlc = read.table("language_correlation.csv", sep=",", header=TRUE, comment.char = "")
# histogram with 1 break for each record
hist(tlc$correlation,breaks=nrow(tlc),xlab='Language Correlation')
