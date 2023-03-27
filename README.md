
# Labo6Python

In this repo there's code for a ping-based network monitoring tool that allows you to check the status of your servers. Pings are performed at a specified interval if so desired.
With this tool, you can easily check whether your servers are online and keep track of their status.

## Features

- Perform ping checks for servers based on their hostname
- Add, delete, or list servers through an interactive terminal interface
- Operate the system via command-line interface using `sys.argv`
- Keep track of data and checks performed in a JSON file
- Force ping check and/or schedule ping check on specified interval
- Two modes available: management mode and check mode
- Generate an HTML page that reports on the state of the servers using a template file 

## Usage

```{bash}
python main.py https://www.example.com
```
Om direct een website toe te voegen aan de lijst

```{bash}
python main.py --manage 
python main.py --m
```
Om in management modus te geraken

```{bash}
python main.py --check
python main.py --c
```
Om forced check uit te voeren
