from invoke import task


@task
def mer(c, name):
    with open(f"mer/{name}.py") as file:
        exec(file.read())
