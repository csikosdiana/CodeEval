test.cases <- c("3.1415926", "1.41421356", "01-01-1970", "2.7182818284", "4 8 15 16 23 42")

big_digits <- c("-**----*--***--***---*---****--**--****--**---**--",
			"*--*--**-----*----*-*--*-*----*-------*-*--*-*--*-",
			"*--*---*---**---**--****-***--***----*---**---***-",
			"*--*---*--*-------*----*----*-*--*--*---*--*----*-",
			"-**---***-****-***-----*-***---**---*----**---**--",
			"--------------------------------------------------")
#args <- commandArgs(trailingOnly=TRUE)
#test.cases <- strsplit(readLines(args[[1]], warn=FALSE), '\n')
cat(sapply(test.cases, function(test) {
	if (length(test) > 0) {
		nums <- gsub("[^0-9]", "", test)
		nums <- strsplit(nums, split = "")
		Result <- c()
		i = 1
		while (i < 7){
			Line <- c()
			for (n in nums[[1]]){
				n <- as.integer(n)
				if (n == 0){
					l <- substr(big_digits[i], 1, 5)
				}else{
					l <- substr(big_digits[i], n*5 + 1, n*5 + 5)
				}
			Line <- c(Line, l)
			}
			i <- i + 1
			Line <- paste(Line, sep = "", collapse = "")
			Result <- c(Result, Line)
		}
		Result <- paste(Result, sep = "\n")
	}
}), sep = "\n")