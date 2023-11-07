# Tasks

# Active

- [ ] finish basic format intepreter covering formats from: https://github.com/dyne/file-extension-list


# Priority

- [ ] identify the file formats I need to be able to identify right now

## Backlog

- [ ] get list of all file formats
    - https://www.wikiwand.com/en/List_of_filename_extensions
    - https://www.wikiwand.com/en/List_of_file_formats
    - https://github.com/dyne/file-extension-list
    - https://gist.github.com/securifera/e7eed730cbe1ce43d0c29d7cd2d582f4
    - * noticed ics missing incidentally while scrolling, ie: lists prolly aren't complete
- [ ] identify the file formats that are the most common
- [ ] analyze/test the coverage level by unique file ids and proportional format distribution
    - [ ] add version coverage graphs to docs
    - [ ] get many sample files and create statistical profiles/models for edgecases
        - * ie: train/test sklearn models on file metadata, text/char/binary data, etc
        - * note: backlogged as this would only be needed in edgecases (say where a json format is used without the extension)
        - [ ] add truepos/falsepos/trueneg/falseneg, f1, prec, recall, auc, etc to aforementioned coverage metrics
- [ ] create mkdocs website
- [ ] compare python vs. maturin/rust python accelerated speed



