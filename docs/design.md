
- if loc
    - check ext
    - if success, return
    - else
        - if val, load
        - resolve bin
- if uri
    - check ext
    - if success, return
    - else
        - if val, fetch
        - resolve bin
- if raw (text)
- if bin
    - try decode text
    - if works
        - resolve text
    - else
        - filter for other formats
            - * via unique checks is too slow
            - ? use ML, or other approach
