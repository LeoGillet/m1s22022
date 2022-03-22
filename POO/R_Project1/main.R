df <- read.table("18.txt")

hist(df[,1], breaks=100) # Gaussian distribution
hist(df[,2], breaks=100) # Uniform distribution