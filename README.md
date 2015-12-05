# Jeff

CLI tool for generating `LICENSE` files, based on user input.


#### Installation:

```bash
$ pip install jeff
```


#### Basic usage:


```bash
$ jeff mit # Outputs mit license content, with user credentials.
```

#### Advanced usage:

Argument name   | usage         | Default value                         | Description
---             | ---           | ---                                   | ---
`name`          | -n, --name    | [`getpass.getuser()`](goo.gl/feOHre)  | Specifies License owner's name.
`year`          | -y, --year    | [`date.today().year`](goo.gl/47kuL3)  | Specifies License's year.
`email`         | -e, --email   | `''`                                  | Specifies License owner's email.
`project name`  | -p, --project | `''`                                  | Specifies Project's name.

## License

[MIT License](https://opensource.org/licenses/MIT) © Oskar Cieslik
