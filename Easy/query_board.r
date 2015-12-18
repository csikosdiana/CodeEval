test.cases <- c("SetCol 32 20",
				"SetRow 15 7",
				"SetRow 16 31",
				"QueryCol 32",
				"SetCol 2 14",
				"QueryRow 10",
				"SetCol 14 0",
				"QueryRow 15",
				"SetRow 10 1",
				"QueryCol 2")

board <- matrix(0, 256, 256)
#args <- commandArgs(trailingOnly=TRUE)
#test.cases <- strsplit(readLines(args[[1]], warn=FALSE), '\n')
for (test in test.cases) {
	if (length(test) > 0) {
		tasks <- strsplit(test, " ")[[1]]
		ord <- tasks[1]
		if (ord == "SetRow") {
			i <- as.numeric(tasks[2]) + 1
			x <- as.numeric(tasks[3])
			board[i,] <- x
		}
		else if (ord == "SetCol") {
			j <- as.numeric(tasks[2]) + 1
			x <- as.numeric(tasks[3])
			board[,j] <- x
		}
		else if (ord == "QueryRow") {
			i <- as.numeric(tasks[2]) + 1
			cat(sum(board[i,]), "\n")
		} else {
			j <- as.numeric(tasks[2]) + 1
			cat(sum(board[,j]), "\n")
		}
	}
}