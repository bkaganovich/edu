<!-- /notes/linux-fs/important-sys-files.md -->

<br>

`Last updated: Tue 29 Nov 2022 08:58 IST`

<h1 id="important-system-files">Important Linux System Files</h1>

## `/etc/passwd`

```bash
1. username:
2. encrypted password (x means stored in shadow):
3. user ID:
4. default group ID:
5. user info (optional):
6. home dir:
7. login shell
```

## `/etc/shadow`

```bash
1. username:
2. $hash type$encrypted password:
3. date last password change:
4. min required days between password changes:
5. number days in advance to display password expiration message:
6. number of days after password expiration to disable the account:
7. account expiration date:
8. reserve field:
```

## `/etc/hosts`

```bash
127.0.0.1   localhost
```