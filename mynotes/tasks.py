from invoke import task


@task
def start(ctx):
    ctx.run("python3 src/build.py")


@task
def test(ctx):
    ctx.run("python3 src/run_tests.py")


@task
def pylint(ctx):
    ctx.run("pylint src")


@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src")
    ctx.run("coverage html")
