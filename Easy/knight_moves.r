test.cases <- c("g2", "a1", "d6", "e5", "b1")

vec <- c("a1", "b1", "c1", "d1", "e1", "f1", "g1", "h1",
			"a2", "b2", "c2", "d2", "e2", "f2", "g2", "h2",
			"a3", "b3", "c3", "d3", "e3", "f3", "g3", "h3",
			"a4", "b4", "c4", "d4", "e4", "f4", "g4", "h4",
			"a5", "b5", "c5", "d5", "e5", "f5", "g5", "h5",
			"a6", "b6", "c6", "d6", "e6", "f6", "g6", "h6",
			"a7", "b7", "c7", "d7", "e7", "f7", "g7", "h7",
			"a8", "b8", "c8", "d8", "e8", "f8", "g8", "h8")
M <- matrix(vec, 8, 8, byrow = TRUE)
M <- cbind(M, rep(NA, 8))
M <- cbind(M, rep(NA, 8))
M <- cbind(rep(NA, 8), M)
M <- cbind(rep(NA, 8), M)
M <- rbind(M, rep(NA, 12))
M <- rbind(M, rep(NA, 12))
M <- rbind(rep(NA, 12), M)
M <- rbind(rep(NA, 12), M)
			
#args <- commandArgs(trailingOnly=TRUE)
#test.cases <- strsplit(readLines(args[[1]], warn=FALSE), '\n')
cat(sapply(test.cases, function(test) {
	if (length(test) > 0) {
		rows <- which(M == test, arr.ind = TRUE)[1]
		cols <- which(M == test, arr.ind = TRUE)[2]
		steps <- c(M[rows-2, cols-1], M[rows-2, cols+1], M[rows+2, cols-1], M[rows+2, cols+1],
					M[rows-1, cols-2], M[rows-1, cols+2], M[rows+1, cols-2], M[rows+1, cols+2])
		steps <- sort(steps[!is.na(steps)])
		paste(steps, sep = " ", collapse = " ")
	}
}), sep = "\n")