# Jeff

CLI tool for generating `LICENSE` files, based on user input.


![Jeff in action!](http://i.imgur.com/UrhjbWM.gifv)


#### Installation:

```bash
$ pip install jeff
```


#### Basic usage:

```bash
$ jeff mit # Outputs mit license content, with user credentials.
```


#### Advanced usage:

Argument name   | usage         | Default value                                 | Description
---             | ---           | ---                                           | ---
`name`          | -n, --name    | [`getpass.getuser()`](http://goo.gl/feOHre)   | Specifies License owner's name.
`year`          | -y, --year    | [`date.today().year`](http://goo.gl/47kuL3)   | Specifies License's year.
`email`         | -e, --email   | `''`                                          | Specifies License owner's email.
`project name`  | -p, --project | `''`                                          | Specifies Project's name.


```bash
$ jeff mit -n"John Doe" # Outputs mit license content, with name "John Doe".
```

```bash
$ jeff mit -y2017 # Outputs mit license content, with year 2017.
```

```bash
$ jeff mit -ejohn.doe@example.com # Outputs mit license content, with email "john.doe@example.com".
```

```bash
$ jeff mit -p "CatJS" # Outputs mit license content, with project's name "CatJS".
```


## License

[MIT License](https://opensource.org/licenses/MIT) © Oskar Cieslik
