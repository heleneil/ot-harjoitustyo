# MyNotes app

In the app users can create notes and edit them. To make notes the user must log into their account.

[Latest release](https://github.com/heleneil/ot-harjoitustyo/releases/tag/viikko7)

## Python version

The app is programmed and tested using Python version ```3.10```.

## Documentation
- [Instructions](https://github.com/heleneil/ot-harjoitustyo/blob/master/documentation/instructions.md)
- [Software requirements specification](https://github.com/heleneil/ot-harjoitustyo/blob/master/documentation/SRS.md)
- [Worklog](https://github.com/heleneil/ot-harjoitustyo/blob/master/documentation/worklog.md)
- [Architecture](https://github.com/heleneil/ot-harjoitustyo/blob/master/documentation/architecture.md)
- [Testing](https://github.com/heleneil/ot-harjoitustyo/blob/master/documentation/testing.md)

## Installing and running the program
1. Install dependencies:

```poetry install```

2. Run program:

```poetry run invoke start```

## Commands

###### Running the program

```poetry run invoke start```

###### Running tests

```poetry run invoke test```

###### Coverage report

```poetry run invoke coverage```

###### Pylint

```poetry run invoke pylint```

