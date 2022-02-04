# omni-coveragereporter-python - Go Reporting

Go reports are quite unique in their structure and these are notes on what I've found so far.

## Run command examples

### 1. Test

```shell
go test
```

### 2. Coverage

```shell
go test --cover
```

### 3. Coverage with .out file

```shell
go test -coverprofile=coverage.out
```

### 4. Coverage with .html file

```shell
go test -coverprofile=coverage.out && go tool cover -html=coverage.out 
```

## Report structure

##### Contents of `coverage.out` example

```shell
mode: set
${absolute_path}/images-go/points/image-utils.go:15.74,19.17 4 1
${absolute_path}/images-go/points/image-utils.go:32.2,32.30 1 1
${absolute_path}/images-go/points/image-utils.go:20.9,21.46 1 1
${absolute_path}/images-go/points/image-utils.go:23.9,24.46 1 1
${absolute_path}/images-go/points/image-utils.go:26.9,27.46 1 1
${absolute_path}/images-go/points/image-utils.go:29.9,30.46 1 1
```
> absolute_path - This is the absolute path to the project

What's important to look at is the numbers on the right side.

To put it in a format-wise self-explanatory way it could be represented like this:

```text
mode: set
<PATH_TO_FILE>:<LINE_NUMBER_NOT_CONSIDERED>.<COVERAGE_PERCENTAGE>,<LINE_NUMBER_CANDIDATE_TO_COVERAGE>.<BLOCK_COVERAGE_PERCENTAGE> <NR_LINES_CANDIDATE_TO_COVERAGE_INCLUSIVE_LINE_CANDIDATE_DIRECTION_UPWARD> <NUMBER_OF_HITS>
...
```

This is a fairly complicated format and in order to read it, this is what I'm doing in this plugin:

1. Ignore all percentages - It doesn't look like any of the reporting frameworks will need them specifically and we can and should calculate them separately
2. All non-considered lines should fall back to their non-cover-able value (frequently just null or omission of the line number for coverage)
3. The number of hits should be given directly at the specified line number (0 and >0 values alike in the same way)
4. Per line hit, add the rest of the line coverage upwards until N-1.

