test.cases <- c("1", "7", "22")

happy <- function(x, visited){
			visited <<- c()
			n <- as.numeric(strsplit(as.character(x), "")[[1]])
			n <- sum(n^2)
			if (n == 1){
				TRUE
			}
			else if (n %in% visited) {
				FALSE
			} else {
				visited <- c(visited, n)
				happy(n, visited)
			}
}

#args <- commandArgs(trailingOnly=TRUE)
#test.cases <- strsplit(readLines(args[[1]], warn=FALSE), '\n')
cat(sapply(test.cases, function(test) {
	if (length(test) > 0) {
		num <- as.numeric(test)
		visited <- c()
		if (happy(num, visited)) {
			1
		} else {
			0
		}
	}
}), sep = "\n")