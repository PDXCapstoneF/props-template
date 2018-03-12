# props-template
Translates a config and templated `.props` into a normal Java `.props` file.

## Get started

1. Get [`pipenv`].
1. `pipenv install`
1. `pipenv check`
1. `pipenv shell`

## Example

```
$ cat example/template.props example/mapping.json
com.apple.someprops = value
com.apple.foo = $foo
com.apple.biz = $biz
com.apple.untouched = $$untouched
{
	"foo": "bar",
	"biz": "baz"
}
$ python main.py example/template.props example/mapping.json
#Sun Mar 11 17:31:07 PDT 2018
com.apple.someprops=value
com.apple.foo=bar
com.apple.biz=baz
com.apple.untouched=$untouched
```
