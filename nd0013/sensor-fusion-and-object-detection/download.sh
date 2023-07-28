#!/bin/sh

rm -rf home/{dataset,results}

wget -O home/dataset --content-disposition "https://www.dropbox.com/sh/q37x44t6yb20eqz/AABNGZ7MvNTJQVlFJ9tGFyHGa?dl=0"

wget -O home/results --content-disposition "https://www.dropbox.com/sh/tb9xk9bqthmd7s2/AAAYbj-2wOA-veI1AfA8eVd1a?dl=0"
