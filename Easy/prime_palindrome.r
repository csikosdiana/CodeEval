
is.palindrome <- function(p) {
	p <- as.character(p)
	p_rev <- paste(rev(substring(p,1:nchar(p) ,1:nchar(p))), collapse="")
	if (p == p_rev) {
		return(TRUE)
	} else {
		return(FALSE)
	}
}

is.prime <- function(n) {
	if (n <= 1) {
		return(FALSE)
	}
	if (n == 2) {
		return(TRUE)
	}
	for (i in 2:ceiling(n/2)) {
		if (n %% i == 0) {
			return(FALSE)
		}
	}
	return(TRUE)
}

k <- 999
repeat {
	palindrome <- is.palindrome(k)
	if (palindrome == TRUE) {
		prime <- is.prime(k)
		if (prime == TRUE){
			cat(k)
			break
		}
	}
	k <- k - 1
}
