test.cases <- c("XX.YY,XXX.Y,X..YY,XX..Y",
				"XXX.YYYY,X...Y..Y,XX..YYYY,X.....YY,XX....YY",
				"XX...YY,X....YY,XX..YYY,X..YYYY",
				"XXYY,X..Y,XX.Y")

#args <- commandArgs(trailingOnly=TRUE)
#test.cases <- strsplit(readLines(args[[1]], warn=FALSE), '\n')
cat(sapply(test.cases, function(test) {
	if (length(test) > 0) {
		rows <- strsplit(test, ",")[[1]]
		Mini <- 10
		for (r in rows){
			r <- strsplit(r, split = "")[[1]]
			x <- max((which(r == "X")))
			y <- min((which(r == "Y")))
			d <- y - x - 1
			if (d < Mini){
				Mini <- d
			}
		}
		Mini
	}
}), sep = "\n")