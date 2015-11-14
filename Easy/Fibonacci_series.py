def fib(n):
	f_0 = 0
	f_i = 1
	i = 1
	while i < n:
		i = i + 1
		f_j = f_i
		f_k = f_i + f_0
		f_0 = f_j
		f_i = f_k
	print f_i

fib(18)

#PYTHON 2.7.3
#import sys
#test_cases = open(sys.argv[1], 'r')
#data = test_cases.readlines()
#for test in data:
#    if len(test) > 0:
#        if int(test) == 0:
#            print 0
#        else:
#            f_0, f_1 = 0, 1
#            for i in range(int(test) - 1):
#                f_0, f_1 = f_1, f_0 + f_1
#            print f_1

#R 3.1.2
#args <- commandArgs(trailingOnly=TRUE)
#test.cases <- strsplit(readLines(args[[1]], warn=FALSE), '\n')
#for (test in test.cases) {
#    if (length(test) > 0) {
#        if (test == 0){
#            print(0)
#        } else{
#		test <- as.integer(test)
#        f_0 <- 0
#        f_1 <- 1
#        for (i in 1:(test-1)) {
#            f_k <- f_1
#            f_1 <- f_0 + f_1
#            f_0 <- f_k
#        }
#    }
#    print(f_1)
#}
#}

Fibonacci <- function(n){
	F <- NULL
	if (n == 0){
		F <- 0
	} else if(n == 1){
		F <- 1
	} else{
		F <- Fibonacci(n-1) + Fibonacci(n-2)
	}
	return(F)
}
args <- commandArgs(trailingOnly=TRUE)
data <- file(args[[1]], "r")
repeat {
	l <- readLines(data, n = 1, warn=FALSE)
	if (length(l) == 0){
		break
	}
	test <- as.numeric(l)
	cat(Fibonacci(test), "\n")
}

close(data)



test.cases <- strsplit(readLines(args[[1]], warn=FALSE), '\n')
for (test in test.cases) {
    if (length(test) > 0) {
		test <- as.numeric(test)
		cat(Fibonacci(test), "\n")
	}
}

#fib <- file(args[[1]], "r") 
#while(length(l <- readLines(fib, n = 1, warn = FALSE)) > 0) {
#	cat(Fibonacci(as.numeric(l)),"\n")
#}
#close(fib)