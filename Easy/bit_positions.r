test.cases <- c("86,2,3", "125,1,2")

dec_to_bits <- function(n){
	bits <- c()
	while (n > 0){
		m <- n %% 2
		n <- floor(n / 2)
		bits <- c(bits, as.character(m))
	}
	rev(bits)
}

#args <- commandArgs(trailingOnly=TRUE)
#test.cases <- strsplit(readLines(args[[1]], warn=FALSE), '\n')
cat(sapply(test.cases, function(test) {
	if (length(test) > 0) {
		test <- strsplit(test, split = ",")
		dec <- as.integer(test[[1]][1])
		pos1 <- as.integer(test[[1]][2])
		pos2 <- as.integer(test[[1]][3])
		binary <- rev(dec_to_bits(dec))
		if (binary[pos1] == binary[pos2]){
			"true"
		}else{
			"false"
		}
	}
}), sep = "\n")