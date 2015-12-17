test.cases <- c("4 3 3 5 7",
				"3 20 30 40")

#args <- commandArgs(trailingOnly=TRUE)
#test.cases <- strsplit(readLines(args[[1]], warn=FALSE), '\n')
cat(sapply(test.cases, function(test) {
	if (length(test) > 0) {
		test <- strsplit(test, " ")[[1]]
		h <- as.numeric(test[1])
		houses <- as.numeric(test[2:length(test)])
		H <- floor(mean(houses))
		min_dist <- sum(abs(houses - H))
		
		k <- H
		repeat {
			k <- k + 1
			distance <- sum(abs(houses - k))
			if (distance < min_dist) {
				H <- k
				min_dist <- distance
			} else {
				break
			}
		}
		
		k <- H
		repeat {
			k <- k - 1
			distance <- sum(abs(houses - k))
			if (distance < min_dist) {
				H <- k
				min_dist <- distance
			} else {
				break
			}
		}
		min_dist
	}
}), sep = "\n")