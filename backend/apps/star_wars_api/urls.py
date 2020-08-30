def url_join(base_url: str, *args: str, append_slash: bool = False) -> str:
    """Join base_url and args items into one URL.

    Append slash at the end of url if `append_slash` is truthy.
    """
    url = '/'.join(
        str(path).strip('/')
        for path in (base_url, *args)
    )
    return '{0}/'.format(url) if append_slash else url
