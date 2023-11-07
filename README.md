# python-universal-format-identifier

## References

- [dyne/file-extension-list](https://github.com/dyne/file-extension-list)

## Requirements

- It should be possible to provide a path to a local file resource, or a URL/URI for the path, however - to the extent the path/(url/uri) are used, the file should not actually be read by the package, it should only infer what type it is from the resource name. IE: The resolver should not make any network requests, nor load data from disk.
    - Note: This requirement is introduced by the package(s) this package is built to serve as a dependency for.
    - Note: It may be possible to parameterize this in the future, but that would go on the backlog right now.
- In the case of binary/text data, an incomplete file should suffice.
    - This should be useful in situations where the file one is checking the format of is from the web, but is very large, so one only reads in the first few kilobytes of data.

## Usage


```python
from pufi import resolve
```

<!--
## Requirements

- The user should be able to pass in either raw text, or a path to a file with rawtext, and receive back a string telling them the format of the file.
 -->
