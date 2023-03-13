# Prerequisites
1. install python3
   1. brew install python3
2. install package 
   1. pip install -r requirement.txt

# How to use
### Parameter
1. X
   1. X coordinate to click on monitor
2. Y 
   1. Y coordinate to click on monitor
3. `times`
   1. how many times you want to click. 
   2. if times is 10, script total click 10 times.
4. `sleep`
   1. how long you wait after previous click.
   2. if sleep is 10, script click after 10 seconds after previous click.

### Run
1. add alias to your `~/.zshrc` or `~/.bash_profile`
```text
alias auto-click="python3 {$PATH}/useful_cli/main.py auto-click"
```
   - Replace `PATH` to your project root.

2. run script
```shell
$ auto-click 500 500 --sleep 60 --times 10
```