from invoke import task

@task
def start(ctx):
    ctx.run("python3 src/views.py")


def test(ctx):
    ctx.run("pyhton3 src/tests/login_view_test.py")
