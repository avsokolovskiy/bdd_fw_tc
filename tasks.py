from invoke import task


@task
def run(context, browser="", tags="", resh="", resw=""):
    behave_cmd = "behave"
    if browser != "":
        behave_cmd += f' -D browser={browser}'
    if tags != "":
        behave_cmd += f' --tags={tags}'
    if resh != "":
        behave_cmd += f' -D resolution_h={resh}'
    if resw != "":
        behave_cmd += f' -D resolution_w={resw}'
    print(f'cmd : {behave_cmd}')
    context.run(behave_cmd)

@task
def run_with_allure(context, browser="", tags="", resh="", resw=""):
    behave_cmd = "behave -f allure_behave.formatter:AllureFormatter -o artifacts -f pretty"
    if browser != "":
        behave_cmd += f' -D browser={browser}'
    if tags != "":
        behave_cmd += f' --tags={tags}'
    if resh != "":
        behave_cmd += f' -D resolution_h={resh}'
    if resw != "":
        behave_cmd += f' -D resolution_w={resw}'
    print(f'cmd : {behave_cmd}')
    context.run(behave_cmd)