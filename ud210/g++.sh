docker run --rm --user $(id -u):$(id -g) -v "$PWD":/usr/src/myapp -w /usr/src/myapp gcc g++ "$@"
