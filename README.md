## [childrenofliber.com](https://childrenofliber.com)

Implementation of the `childrenofliber.com` website, as described in [SCP-3455](https://scpwiki.com/scp-3455). Available under the MIT License.

### What is this?

I mean, you should just read SCP-3455. But in the article, it makes mention of a website which is (in the special time period) used for news and events related to the month of Liberary, and outside of it, is a simple countdown until the next occurrence. Since Liberary isn't real (or so we think!!), this site always displays the latter.

## Development

```
ruff check
ruff format
mypy app.py
```

### Execution

For development:

```
flask run
```

For production:

```
waitress-serve --port 3455 app:app
```

See also the Dockerfile for convenient deployment.
