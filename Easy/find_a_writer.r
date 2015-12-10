test.cases <- c("osSE5Gu0Vi8WRq93UvkYZCjaOKeNJfTyH6tzDQbxFm4M1ndXIPh27wBA rLclpg| 3 35 27 62 51 27 46 57 26 10 46 63 57 45 15 43 53",
				"3Kucdq9bfCEgZGF2nwx8UpzQJyHiOm0hoaYP6ST1WM7Nks5XjrR4IltBeDLV vA| 2 26 33 55 34 50 33 61 44 28 46 32 28 30 3 50 34 61 40 7 1 31")

#args <- commandArgs(trailingOnly=TRUE)
#test.cases <- strsplit(readLines(args[[1]], warn=FALSE), '\n')
cat(sapply(test.cases, function(test) {
	if (length(test) > 0) {
		parts <- strsplit(test, split = "| ", fixed = TRUE)[[1]]
		T <- strsplit(parts[1], split = "")[[1]]
		code <- as.numeric(strsplit(parts[2], split = " ")[[1]])
		Writer <- T[code]
		paste(Writer, sep = "", collapse = "")
	}
}), sep = "\n")