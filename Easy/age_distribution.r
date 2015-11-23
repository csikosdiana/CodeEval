test.cases <- c("0", "19")

age_desc <- function(age){
	if ((age >= 0) & (age <= 2)){
		"Still in Mama's arms"
	}
	else if((age == 3) | (age == 4)) {
		"Preschool Maniac"
	}
	else if((age >= 5) & (age <= 11)) {
		"Elementary school"
	}
	else if((age >= 12) & (age <= 14)) {
		"Middle school"
	}
	else if((age >= 15) & (age <= 18)) {
		"High school"
	}
	else if((age >= 19) & (age <= 22)) {
		"College"
	}
	else if((age >= 23) & (age <= 65)) {
		"Working for the man"
	}
	else if((age >= 66) & (age <= 100)) {
		"The Golden Years"
	}
	else {
		"This program is for humans"
	}
}

#args <- commandArgs(trailingOnly=TRUE)
#test.cases <- strsplit(readLines(args[[1]], warn=FALSE), '\n')
cat(sapply(test.cases, function(test) {
	if (length(test) > 0) {
		AGE <- as.integer(test)
		age_desc(AGE)
	}
}), sep = "\n")